# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from sf.ethereum.trxstream.v1 import trxstream_pb2 as sf_dot_ethereum_dot_trxstream_dot_v1_dot_trxstream__pb2


class TransactionStreamStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Transactions = channel.unary_stream(
                '/sf.ethereum.trxstream.v1.TransactionStream/Transactions',
                request_serializer=sf_dot_ethereum_dot_trxstream_dot_v1_dot_trxstream__pb2.TransactionRequest.SerializeToString,
                response_deserializer=sf_dot_ethereum_dot_trxstream_dot_v1_dot_trxstream__pb2.Transaction.FromString,
                )


class TransactionStreamServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Transactions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransactionStreamServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Transactions': grpc.unary_stream_rpc_method_handler(
                    servicer.Transactions,
                    request_deserializer=sf_dot_ethereum_dot_trxstream_dot_v1_dot_trxstream__pb2.TransactionRequest.FromString,
                    response_serializer=sf_dot_ethereum_dot_trxstream_dot_v1_dot_trxstream__pb2.Transaction.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sf.ethereum.trxstream.v1.TransactionStream', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TransactionStream(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Transactions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/sf.ethereum.trxstream.v1.TransactionStream/Transactions',
            sf_dot_ethereum_dot_trxstream_dot_v1_dot_trxstream__pb2.TransactionRequest.SerializeToString,
            sf_dot_ethereum_dot_trxstream_dot_v1_dot_trxstream__pb2.Transaction.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)