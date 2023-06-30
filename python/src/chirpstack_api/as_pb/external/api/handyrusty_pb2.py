# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/as_pb/external/api/handyrusty.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from chirpstack_api.handyrusty import hr_pb2 as chirpstack__api_dot_handyrusty_dot_hr__pb2
from chirpstack_api.gw import gw_pb2 as chirpstack__api_dot_gw_dot_gw__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2chirpstack-api/as_pb/external/api/handyrusty.proto\x12\x03\x61pi\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\"chirpstack-api/handyrusty/hr.proto\x1a\x1a\x63hirpstack-api/gw/gw.proto2\xe6\x0c\n\x11HandyRustyService\x12z\n\x10GetFrameCounters\x12\x1b.hr.GetFrameCountersRequest\x1a\x1c.hr.GetFrameCountersResponse\"+\x82\xd3\xe4\x93\x02%\" /api/handy-rusty/frames/counters:\x01*\x12n\n\rGetFrameSpeed\x12\x18.hr.GetFrameSpeedRequest\x1a\x19.hr.GetFrameSpeedResponse\"(\x82\xd3\xe4\x93\x02\"\"\x1d/api/handy-rusty/frames/speed:\x01*\x12r\n\x0b\x45xecCommand\x12\x16.hr.ExecCommandRequest\x1a\x1e.gw.GatewayCommandExecResponse\"+\x82\xd3\xe4\x93\x02%\" /api/handy-rusty/rc/exec-command:\x01*\x12\x8a\x01\n\x12GetDeviceFramesLog\x12\x1d.hr.GetDeviceFramesLogRequest\x1a\x1e.hr.GetDeviceFramesLogResponse\"5\x82\xd3\xe4\x93\x02/\"*/api/handy-rusty/frames/logs/device-frames:\x01*\x12\x99\x01\n\x18StreamDeviceFramesLogCSV\x12\x1d.hr.GetDeviceFramesLogRequest\x1a$.hr.StreamDeviceFramesLogCSVResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./api/handy-rusty/frames/logs/device-frames/csv0\x01\x12n\n\x0fGetCurrentState\x12\x16.google.protobuf.Empty\x1a\x1b.hr.GetCurrentStateResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/api/handy-rusty/current-state\x12\x8a\x01\n\x15GetIntegrationReplies\x12 .hr.GetIntegrationRepliesRequest\x1a!.hr.GetIntegrationRepliesResponse\",\x82\xd3\xe4\x93\x02&\x12$/api/handy-rusty/integration/replies\x12\x63\n\nGetGwStats\x12\x15.hr.GetGwStatsRequest\x1a\x16.hr.GetGwStatsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/api/handy-rusty/gateway/stats\x12|\n\x0eGetDeviceStats\x12\x19.hr.GetDeviceStatsRequest\x1a\x1a.hr.GetDeviceStatsResponse\"3\x82\xd3\xe4\x93\x02-\x12+/api/handy-rusty/device/stats/last-24-hours\x12\x93\x01\n\x1aGetDeviceStatsLastTwoweeks\x12\x19.hr.GetDeviceStatsRequest\x1a&.hr.GetDeviceStatsLastTwoweeksResponse\"2\x82\xd3\xe4\x93\x02,\x12*/api/handy-rusty/device/stats/last-14-days\x12\xa8\x01\n$GetDeviceStatsLastTwoweeksAggregated\x12\x19.hr.GetDeviceStatsRequest\x1a&.hr.GetDeviceStatsLastTwoweeksResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/api/handy-rusty/device/stats/last-14-days-aggregated\x12\xa6\x01\n\x18GetAveragesForDeviceList\x12#.hr.GetAveragesForDeviceListRequest\x1a$.hr.GetAveragesForDeviceListResponse\"?\x82\xd3\xe4\x93\x02\x39\"4/api/handy-rusty/device/stats/last-24-hours/for-list:\x01*B9Z7github.com/brocaar/chirpstack-api/go/v3/as/external/apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.as_pb.external.api.handyrusty_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z7github.com/brocaar/chirpstack-api/go/v3/as/external/api'
  _HANDYRUSTYSERVICE.methods_by_name['GetFrameCounters']._options = None
  _HANDYRUSTYSERVICE.methods_by_name['GetFrameCounters']._serialized_options = b'\202\323\344\223\002%\" /api/handy-rusty/frames/counters:\001*'
  _HANDYRUSTYSERVICE.methods_by_name['GetFrameSpeed']._options = None
  _HANDYRUSTYSERVICE.methods_by_name['GetFrameSpeed']._serialized_options = b'\202\323\344\223\002\"\"\035/api/handy-rusty/frames/speed:\001*'
  _HANDYRUSTYSERVICE.methods_by_name['ExecCommand']._options = None
  _HANDYRUSTYSERVICE.methods_by_name['ExecCommand']._serialized_options = b'\202\323\344\223\002%\" /api/handy-rusty/rc/exec-command:\001*'
  _HANDYRUSTYSERVICE.methods_by_name['GetDeviceFramesLog']._options = None
  _HANDYRUSTYSERVICE.methods_by_name['GetDeviceFramesLog']._serialized_options = b'\202\323\344\223\002/\"*/api/handy-rusty/frames/logs/device-frames:\001*'
  _HANDYRUSTYSERVICE.methods_by_name['StreamDeviceFramesLogCSV']._options = None
  _HANDYRUSTYSERVICE.methods_by_name['StreamDeviceFramesLogCSV']._serialized_options = b'\202\323\344\223\0020\022./api/handy-rusty/frames/logs/device-frames/csv'
  _HANDYRUSTYSERVICE.methods_by_name['GetCurrentState']._options = None
  _HANDYRUSTYSERVICE.methods_by_name['GetCurrentState']._serialized_options = b'\202\323\344\223\002 \022\036/api/handy-rusty/current-state'
  _HANDYRUSTYSERVICE.methods_by_name['GetIntegrationReplies']._options = None
  _HANDYRUSTYSERVICE.methods_by_name['GetIntegrationReplies']._serialized_options = b'\202\323\344\223\002&\022$/api/handy-rusty/integration/replies'
  _HANDYRUSTYSERVICE.methods_by_name['GetGwStats']._options = None
  _HANDYRUSTYSERVICE.methods_by_name['GetGwStats']._serialized_options = b'\202\323\344\223\002 \022\036/api/handy-rusty/gateway/stats'
  _HANDYRUSTYSERVICE.methods_by_name['GetDeviceStats']._options = None
  _HANDYRUSTYSERVICE.methods_by_name['GetDeviceStats']._serialized_options = b'\202\323\344\223\002-\022+/api/handy-rusty/device/stats/last-24-hours'
  _HANDYRUSTYSERVICE.methods_by_name['GetDeviceStatsLastTwoweeks']._options = None
  _HANDYRUSTYSERVICE.methods_by_name['GetDeviceStatsLastTwoweeks']._serialized_options = b'\202\323\344\223\002,\022*/api/handy-rusty/device/stats/last-14-days'
  _HANDYRUSTYSERVICE.methods_by_name['GetDeviceStatsLastTwoweeksAggregated']._options = None
  _HANDYRUSTYSERVICE.methods_by_name['GetDeviceStatsLastTwoweeksAggregated']._serialized_options = b'\202\323\344\223\0027\0225/api/handy-rusty/device/stats/last-14-days-aggregated'
  _HANDYRUSTYSERVICE.methods_by_name['GetAveragesForDeviceList']._options = None
  _HANDYRUSTYSERVICE.methods_by_name['GetAveragesForDeviceList']._serialized_options = b'\202\323\344\223\0029\"4/api/handy-rusty/device/stats/last-24-hours/for-list:\001*'
  _HANDYRUSTYSERVICE._serialized_start=183
  _HANDYRUSTYSERVICE._serialized_end=1821
# @@protoc_insertion_point(module_scope)