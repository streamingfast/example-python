import http.client
import json
import ssl
import sys
import grpc
import os

from sf.firehose.v2 import firehose_pb2_grpc
from sf.firehose.v2.firehose_pb2 import Request
from sf.antelope.type.v1 import type_pb2
from google.protobuf.json_format import MessageToJson

AUTH_ENDPOINT = os.getenv('AUTH_ENDPOINT') or 'auth.pinax.network'
STREAM_ENDPOINT = os.getenv('ENDPOINT') or 'wax.firehose.pinax.network:443'

def token_for_api_key(apiKey):
    # Needs to be cached since this API is rate limited, the returned token is valid for 24h
    #
    # - Pinax uses https://auth.dfuse.io/v1/auth/issue
    # - StreamingFast uses https://auth.pinax.network/v1/auth/issue
    connection = http.client.HTTPSConnection(AUTH_ENDPOINT)
    connection.request(
        'POST',
        '/v1/auth/issue',
        json.dumps({"api_key": apiKey}),
        {'Content-type': 'application/json'},
    )
    response = connection.getresponse()

    if response.status != 200:
        raise Exception(
            f" Status: {response.status} reason: {response.reason}")

    token = json.loads(response.read().decode())['token']
    connection.close()

    return token


def firehose_stream():
    credentials = grpc.access_token_call_credentials(
        token_for_api_key(sys.argv[1]))
    channel = grpc.secure_channel(
        STREAM_ENDPOINT,
        credentials=grpc.composite_channel_credentials(grpc.ssl_channel_credentials(),
                                                       credentials))
    return firehose_pb2_grpc.StreamStub(channel)


def block_stats(block):
    action_count = 0
    for trx in block.unfiltered_transaction_traces:
        action_count += len(trx.action_traces)

    return len(block.unfiltered_transactions), action_count


def main():
    if len(sys.argv) <= 1:
        print("Error: Wrong number of arguments")
        print()
        print("usage: python3 main.py <apiKey> --full")
        exit(1)

    blockstream = firehose_stream()
    stream = blockstream.Blocks(Request(
        start_block_num=275_975_000,
        stop_block_num=275_975_010,

        # Show all blocks, switch to True to only show final blocks
        final_blocks_only=False,
    ))

    print_full = len(sys.argv) > 2 and sys.argv[2] == "--full"

    for response in stream:
        block = type_pb2.Block()
        succeed = response.block.Unpack(block)
        if succeed != True:
            raise Exception(
                "Invalid target type, field to unpack is of type {} but tried to unpack it into type {}".format(response.block.TypeName(), block.DESCRIPTOR.full_name))

        trx_count, action_count = block_stats(block)

        print(
            "Block #{} ({}) - {} Transactions ({} actions)".format(block.number, block.id, trx_count, action_count))
        if print_full:
            print(MessageToJson(block))


main()
