# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sf/firehose/v2/firehose.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsf/firehose/v2/firehose.proto\x12\x0esf.firehose.v2\x1a\x19google/protobuf/any.proto\"\xdc\x03\n\x12SingleBlockRequest\x12S\n\x0c\x62lock_number\x18\x03 \x01(\x0b\x32..sf.firehose.v2.SingleBlockRequest.BlockNumberH\x00R\x0b\x62lockNumber\x12j\n\x15\x62lock_hash_and_number\x18\x04 \x01(\x0b\x32\x35.sf.firehose.v2.SingleBlockRequest.BlockHashAndNumberH\x00R\x12\x62lockHashAndNumber\x12\x43\n\x06\x63ursor\x18\x05 \x01(\x0b\x32).sf.firehose.v2.SingleBlockRequest.CursorH\x00R\x06\x63ursor\x12\x34\n\ntransforms\x18\x06 \x03(\x0b\x32\x14.google.protobuf.AnyR\ntransforms\x1a\x1f\n\x0b\x42lockNumber\x12\x10\n\x03num\x18\x01 \x01(\x04R\x03num\x1a:\n\x12\x42lockHashAndNumber\x12\x10\n\x03num\x18\x01 \x01(\x04R\x03num\x12\x12\n\x04hash\x18\x02 \x01(\tR\x04hash\x1a \n\x06\x43ursor\x12\x16\n\x06\x63ursor\x18\x01 \x01(\tR\x06\x63ursorB\x0b\n\treference\"A\n\x13SingleBlockResponse\x12*\n\x05\x62lock\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyR\x05\x62lock\"\xd1\x01\n\x07Request\x12&\n\x0fstart_block_num\x18\x01 \x01(\x03R\rstartBlockNum\x12\x16\n\x06\x63ursor\x18\x02 \x01(\tR\x06\x63ursor\x12$\n\x0estop_block_num\x18\x03 \x01(\x04R\x0cstopBlockNum\x12*\n\x11\x66inal_blocks_only\x18\x04 \x01(\x08R\x0f\x66inalBlocksOnly\x12\x34\n\ntransforms\x18\n \x03(\x0b\x32\x14.google.protobuf.AnyR\ntransforms\"|\n\x08Response\x12*\n\x05\x62lock\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyR\x05\x62lock\x12,\n\x04step\x18\x06 \x01(\x0e\x32\x18.sf.firehose.v2.ForkStepR\x04step\x12\x16\n\x06\x63ursor\x18\n \x01(\tR\x06\x63ursor*G\n\x08\x46orkStep\x12\x0e\n\nSTEP_UNSET\x10\x00\x12\x0c\n\x08STEP_NEW\x10\x01\x12\r\n\tSTEP_UNDO\x10\x02\x12\x0e\n\nSTEP_FINAL\x10\x03\x32G\n\x06Stream\x12=\n\x06\x42locks\x12\x17.sf.firehose.v2.Request\x1a\x18.sf.firehose.v2.Response0\x01\x32Y\n\x05\x46\x65tch\x12P\n\x05\x42lock\x12\".sf.firehose.v2.SingleBlockRequest\x1a#.sf.firehose.v2.SingleBlockResponseB9Z7github.com/streamingfast/pbgo/sf/firehose/v2;pbfirehoseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sf.firehose.v2.firehose_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/streamingfast/pbgo/sf/firehose/v2;pbfirehose'
  _globals['_FORKSTEP']._serialized_start=960
  _globals['_FORKSTEP']._serialized_end=1031
  _globals['_SINGLEBLOCKREQUEST']._serialized_start=77
  _globals['_SINGLEBLOCKREQUEST']._serialized_end=553
  _globals['_SINGLEBLOCKREQUEST_BLOCKNUMBER']._serialized_start=415
  _globals['_SINGLEBLOCKREQUEST_BLOCKNUMBER']._serialized_end=446
  _globals['_SINGLEBLOCKREQUEST_BLOCKHASHANDNUMBER']._serialized_start=448
  _globals['_SINGLEBLOCKREQUEST_BLOCKHASHANDNUMBER']._serialized_end=506
  _globals['_SINGLEBLOCKREQUEST_CURSOR']._serialized_start=508
  _globals['_SINGLEBLOCKREQUEST_CURSOR']._serialized_end=540
  _globals['_SINGLEBLOCKRESPONSE']._serialized_start=555
  _globals['_SINGLEBLOCKRESPONSE']._serialized_end=620
  _globals['_REQUEST']._serialized_start=623
  _globals['_REQUEST']._serialized_end=832
  _globals['_RESPONSE']._serialized_start=834
  _globals['_RESPONSE']._serialized_end=958
  _globals['_STREAM']._serialized_start=1033
  _globals['_STREAM']._serialized_end=1104
  _globals['_FETCH']._serialized_start=1106
  _globals['_FETCH']._serialized_end=1195
# @@protoc_insertion_point(module_scope)
