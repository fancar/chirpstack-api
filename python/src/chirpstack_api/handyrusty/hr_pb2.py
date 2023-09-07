# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/handyrusty/hr.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from chirpstack_api.common import common_pb2 as chirpstack__api_dot_common_dot_common__pb2
from chirpstack_api.gw import gw_pb2 as chirpstack__api_dot_gw_dot_gw__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"chirpstack-api/handyrusty/hr.proto\x12\x02hr\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\"chirpstack-api/common/common.proto\x1a\x1a\x63hirpstack-api/gw/gw.proto\"3\n\x1fGetAveragesForDeviceListRequest\x12\x10\n\x08\x64\x65v_list\x18\x01 \x03(\t\"r\n\x15\x41veragesForDeviceList\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\t\x12\x0f\n\x07per_avg\x18\x02 \x01(\x02\x12\x12\n\npacket_cnt\x18\x03 \x01(\r\x12\x10\n\x08snr_last\x18\x04 \x01(\x01\x12\x11\n\trssi_last\x18\x05 \x01(\x05\"M\n GetAveragesForDeviceListResponse\x12)\n\x06result\x18\x01 \x03(\x0b\x32\x19.hr.AveragesForDeviceList\"(\n\x15GetDeviceStatsRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\t\"\xd4\x02\n\x16GetDeviceStatsResponse\x12\x12\n\npacket_cnt\x18\x01 \x01(\r\x12\x0f\n\x07\x65sp_avg\x18\x02 \x01(\x02\x12\x0f\n\x07snr_avg\x18\x03 \x01(\x02\x12\x10\n\x08rssi_avg\x18\x04 \x01(\x02\x12\x0f\n\x07per_avg\x18\x05 \x01(\x02\x12\x10\n\x08\x65sp_last\x18\x06 \x01(\x01\x12\x10\n\x08snr_last\x18\x07 \x01(\x01\x12\x11\n\trssi_last\x18\x08 \x01(\x05\x12\x0f\n\x07sf_last\x18\t \x01(\r\x12+\n\x07rx_last\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07tx_last\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tjoin_last\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08per_last\x18\r \x01(\x02\"\x9e\x01\n\x0b\x44\x65viceStats\x12.\n\ncreated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06rx_cnt\x18\x02 \x01(\r\x12\x0e\n\x06tx_cnt\x18\x03 \x01(\r\x12\x0b\n\x03per\x18\x04 \x01(\x02\x12\x0b\n\x03\x65sp\x18\x05 \x01(\x02\x12\x0c\n\x04rssi\x18\x06 \x01(\x02\x12\x0b\n\x03snr\x18\x07 \x01(\x02\x12\n\n\x02sf\x18\x08 \x01(\r\"D\n\"GetDeviceStatsLastTwoweeksResponse\x12\x1e\n\x05stats\x18\x01 \x03(\x0b\x32\x0f.hr.DeviceStats\"i\n\nLogsGwItem\x12.\n\ncreated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x03\x12\x1d\n\ngateway_id\x18\x03 \x01(\tR\tgatewayID\"\xe3\x01\n\x12LogsGatewayRequest\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\'\n\x0forganization_id\x18\x03 \x01(\x03R\x0eorganizationID\x12\x0f\n\x07gw_list\x18\x04 \x03(\t\x12\x0c\n\x04\x63ode\x18\x05 \x01(\x03\x12\x33\n\x0fstart_timestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rend_timestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"J\n\x13LogsGatewayResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\x03\x12\x1e\n\x06result\x18\x02 \x03(\x0b\x32\x0e.hr.LogsGwItem\"\xf8\x01\n\x1cGetIntegrationRepliesRequest\x12\x0e\n\x06offset\x18\x01 \x01(\r\x12\r\n\x05limit\x18\x02 \x01(\r\x12\x17\n\x0forganisation_id\x18\x03 \x01(\x03\x12\x1a\n\x12routing_profile_id\x18\x04 \x01(\x03\x12\x0f\n\x07\x64\x65v_eui\x18\x05 \x01(\t\x12\x10\n\x08is_error\x18\x06 \x01(\x08\x12\r\n\x05is_ok\x18\x07 \x01(\x08\x12)\n\x05start\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03\x65nd\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"Z\n\x1dGetIntegrationRepliesResponse\x12\x13\n\x0bitems_total\x18\x01 \x01(\r\x12$\n\x06result\x18\x02 \x03(\x0b\x32\x14.hr.IntegrationReply\"\xbc\x01\n\x10IntegrationReply\x12\x17\n\x0fintegration_url\x18\x01 \x01(\t\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x12\x1f\n\x17status_code_description\x18\x03 \x01(\t\x12\x16\n\x0e\x61pplication_id\x18\x04 \x01(\x03\x12\x17\n\x07\x64\x65v_eui\x18\x05 \x01(\tR\x06\x64\x65vEUI\x12(\n\x04time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"x\n\x1cStoreIntegrationReplyRequest\x12\x17\n\x0forganisation_id\x18\x01 \x01(\x03\x12\x1a\n\x12routing_profile_id\x18\x02 \x01(\x03\x12#\n\x05reply\x18\x03 \x01(\x0b\x32\x14.hr.IntegrationReply\"5\n\x1dStoreIntegrationReplyResponse\x12\x14\n\x0cstored_count\x18\x01 \x01(\x03\"N\n\x17GetCurrentStateResponse\x12\x16\n\x0ewl_last_packet\x18\x01 \x01(\t\x12\x1b\n\x13wl_last_packet_unix\x18\x02 \x01(\x03\"w\n StreamDeviceFramesLogCSVResponse\x12\x11\n\x07\x63urrent\x18\x01 \x01(\rH\x00\x12\x0f\n\x05total\x18\x02 \x01(\rH\x00\x12\x0e\n\x04rows\x18\x03 \x01(\rH\x01\x12\x0f\n\x05\x63hunk\x18\x04 \x01(\x0cH\x01\x42\x06\n\x04sizeB\x06\n\x04\x64\x61ta\"\x89\x02\n\x19GetDeviceFramesLogRequest\x12\x0e\n\x06offset\x18\x01 \x01(\r\x12\r\n\x05limit\x18\x02 \x01(\r\x12\r\n\x05start\x18\x03 \x01(\t\x12\x0b\n\x03\x65nd\x18\x04 \x01(\t\x12;\n\x07\x66ilters\x18\x05 \x03(\x0b\x32*.hr.GetDeviceFramesLogRequest.FiltersEntry\x12\x17\n\x0forganization_id\x18\x06 \x01(\x03\x12\x1a\n\x08timezone\x18\x07 \x01(\tR\x08timeZone\x12\x0f\n\x07gw_only\x18\x08 \x01(\x08\x1a.\n\x0c\x46iltersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"S\n\x1aGetDeviceFramesLogResponse\x12\x13\n\x0bitems_total\x18\x01 \x01(\r\x12 \n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x12.hr.DeviceFrameLog\"c\n\x12\x45xecCommandRequest\x12\x12\n\ngateway_id\x18\x01 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\r\x12\x17\n\x0f\x62\x61\x63kground_task\x18\x04 \x01(\x08\"5\n\x17GetFrameCountersRequest\x12\r\n\x05start\x18\x01 \x01(\t\x12\x0b\n\x03\x65nd\x18\x02 \x01(\t\"?\n\x18GetFrameCountersResponse\x12#\n\x08\x63ounters\x18\x01 \x03(\x0b\x32\x11.hr.FrameCounters\"2\n\x14GetFrameSpeedRequest\x12\r\n\x05start\x18\x01 \x01(\t\x12\x0b\n\x03\x65nd\x18\x02 \x01(\t\"9\n\x15GetFrameSpeedResponse\x12 \n\x08\x63ounters\x18\x01 \x03(\x0b\x32\x0e.hr.FrameSpeed\"d\n\x18GetDeviceCountersRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\r\x12\r\n\x05start\x18\x02 \x01(\t\x12\x0b\n\x03\x65nd\x18\x03 \x01(\t\x12\x13\n\x0b\x61ggregation\x18\x04 \x01(\t\"Z\n\x19GetDeviceCountersResponse\x12\x17\n\x0forganization_id\x18\x01 \x01(\r\x12$\n\x08\x63ounters\x18\x02 \x03(\x0b\x32\x12.hr.DeviceCounters\"e\n\x19GetGatewayCountersRequest\x12\x17\n\x0forganization_id\x18\x01 \x01(\r\x12\r\n\x05start\x18\x02 \x01(\t\x12\x0b\n\x03\x65nd\x18\x03 \x01(\t\x12\x13\n\x0b\x61ggregation\x18\x04 \x01(\t\"[\n\x1aGetGatewayCountersResponse\x12\x17\n\x0forganization_id\x18\x01 \x01(\r\x12$\n\x08\x63ounters\x18\x02 \x03(\x0b\x32\x12.hr.DeviceCounters\"%\n\x12GetVersionResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\"\x85\x01\n\x0e\x44\x65viceCounters\x12\x17\n\x0forganization_id\x18\x01 \x01(\r\x12\x12\n\ncreated_at\x18\x02 \x01(\r\x12\x14\n\x0c\x61\x63tive_count\x18\x03 \x01(\r\x12\x16\n\x0einactive_count\x18\x04 \x01(\r\x12\x18\n\x10never_seen_count\x18\x05 \x01(\r\"\xb2\x02\n\rFrameCounters\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\x03\x12\x0e\n\x06rx_cnt\x18\x02 \x01(\r\x12\x0e\n\x06tx_cnt\x18\x03 \x01(\r\x12\x11\n\ttotal_cnt\x18\x04 \x01(\r\x12\x14\n\x0cunknown_type\x18\x05 \x01(\r\x12\x14\n\x0cjoin_request\x18\x06 \x01(\r\x12\x16\n\x0erejoin_request\x18\x07 \x01(\r\x12\x13\n\x0bjoin_accept\x18\x08 \x01(\r\x12\x1b\n\x13unconfirmed_data_up\x18\t \x01(\r\x12\x1d\n\x15unconfirmed_data_down\x18\n \x01(\r\x12\x19\n\x11\x63onfirmed_data_up\x18\x0b \x01(\r\x12\x1b\n\x13\x63onfirmed_data_down\x18\x0c \x01(\r\x12\x13\n\x0bproprietary\x18\r \x01(\r\"\"\n\nFrameSpeed\x12\t\n\x01t\x18\x01 \x01(\x03\x12\t\n\x01y\x18\x02 \x01(\r\"\xca\x03\n\x0e\x44\x65viceFrameLog\x12\x11\n\tdirection\x18\x01 \x01(\t\x12\x11\n\tdate_time\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12\r\n\x05mType\x18\x04 \x01(\t\x12\x10\n\x08\x64\x65v_addr\x18\x05 \x01(\t\x12\x0e\n\x06\x64\x65vEUI\x18\x06 \x01(\t\x12\x0e\n\x06rxRssi\x18\x07 \x01(\x05\x12\x0e\n\x06rx_snr\x18\x08 \x01(\x01\x12\x12\n\nrx_channel\x18\t \x01(\r\x12\x13\n\x0brx_rf_chain\x18\n \x01(\r\x12\n\n\x02gw\x18\x0b \x01(\t\x12\x0f\n\x07tx_info\x18\x0c \x01(\t\x12\x1b\n\x07rx_info\x18\r \x03(\x0b\x32\n.hr.RXInfo\x12\'\n\x0fphy_payloadJSON\x18\x0e \x01(\tR\x0ePhyPayloadJson\x12\x0f\n\x07\x61irtime\x18\x0f \x01(\x01\x12\x0b\n\x03\x65sp\x18\x10 \x01(\x01\x12\x0c\n\x04late\x18\x11 \x01(\r\x12\x13\n\x0b\x66rm_payload\x18\x12 \x01(\t\x12\x0e\n\x06\x46\x43ntUp\x18\x13 \x01(\r\x12\x11\n\tNFCntDown\x18\x14 \x01(\r\x12\x11\n\tAFCntDown\x18\x15 \x01(\r\x12\x10\n\x08\x43onfFCnt\x18\x16 \x01(\r\x12\x0f\n\x07sp_fact\x18\x17 \x01(\r\x12\r\n\x05limit\x18\x18 \x01(\t\"\x9e\x03\n\x06RXInfo\x12\x1d\n\tGatewayID\x18\x01 \x01(\tR\ngateway_id\x12\x12\n\x04Rssi\x18\x02 \x01(\x05R\x04rssi\x12\x19\n\x07LoraSnr\x18\x03 \x01(\x01R\x08lora_snr\x12\x18\n\x07\x43hannel\x18\x04 \x01(\rR\x07\x63hannel\x12\x19\n\x07RfChain\x18\x05 \x01(\rR\x08rf_chain\x12\x14\n\x05\x42oard\x18\x06 \x01(\rR\x05\x62oard\x12\x18\n\x07\x41ntenna\x18\x07 \x01(\rR\x07\x61ntenna\x12,\n\x08Location\x18\x08 \x01(\x0b\x32\x10.common.LocationR\x08location\x12\x30\n\x11\x46ineTimestampType\x18\t \x01(\x0e\x32\x15.gw.FineTimestampType\x12#\n\x0cGpsTimestamp\x18\n \x01(\tR\rgps_timestamp\x12%\n\rFineTimestamp\x18\x0b \x01(\tR\x0e\x66ine_timestamp\x12\x18\n\x07\x43ontext\x18\x0c \x01(\tR\x07\x63ontext\x12\x1b\n\x08UplinkID\x18\r \x01(\tR\tuplink_id\"\x1f\n\x11GetGwStatsRequest\x12\n\n\x02id\x18\x01 \x01(\t\"P\n\x12GetGwStatsResponse\x12\x12\n\nradio_hour\x18\x01 \x01(\x02\x12\x11\n\tradio_day\x18\x02 \x01(\x02\x12\x13\n\x0bradio_month\x18\x03 \x01(\x02\x32\xb0\x0b\n\x11HandyRustyService\x12>\n\nGetVersion\x12\x16.google.protobuf.Empty\x1a\x16.hr.GetVersionResponse\"\x00\x12R\n\x11GetDeviceCounters\x12\x1c.hr.GetDeviceCountersRequest\x1a\x1d.hr.GetDeviceCountersResponse\"\x00\x12U\n\x12GetGatewayCounters\x12\x1d.hr.GetGatewayCountersRequest\x1a\x1e.hr.GetGatewayCountersResponse\"\x00\x12O\n\x10GetFrameCounters\x12\x1b.hr.GetFrameCountersRequest\x1a\x1c.hr.GetFrameCountersResponse\"\x00\x12\x46\n\rGetFrameSpeed\x12\x18.hr.GetFrameSpeedRequest\x1a\x19.hr.GetFrameSpeedResponse\"\x00\x12G\n\x0b\x45xecCommand\x12\x16.hr.ExecCommandRequest\x1a\x1e.gw.GatewayCommandExecResponse\"\x00\x12U\n\x12GetDeviceFramesLog\x12\x1d.hr.GetDeviceFramesLogRequest\x1a\x1e.hr.GetDeviceFramesLogResponse\"\x00\x12\x63\n\x18StreamDeviceFramesLogCSV\x12\x1d.hr.GetDeviceFramesLogRequest\x1a$.hr.StreamDeviceFramesLogCSVResponse\"\x00\x30\x01\x12H\n\x0fGetCurrentState\x12\x16.google.protobuf.Empty\x1a\x1b.hr.GetCurrentStateResponse\"\x00\x12`\n\x17StoreIntegrationReplies\x12 .hr.StoreIntegrationReplyRequest\x1a!.hr.StoreIntegrationReplyResponse\"\x00\x12^\n\x15GetIntegrationReplies\x12 .hr.GetIntegrationRepliesRequest\x1a!.hr.GetIntegrationRepliesResponse\"\x00\x12\x43\n\x0eGetGatewayLogs\x12\x16.hr.LogsGatewayRequest\x1a\x17.hr.LogsGatewayResponse\"\x00\x12=\n\nGetGwStats\x12\x15.hr.GetGwStatsRequest\x1a\x16.hr.GetGwStatsResponse\"\x00\x12I\n\x0eGetDeviceStats\x12\x19.hr.GetDeviceStatsRequest\x1a\x1a.hr.GetDeviceStatsResponse\"\x00\x12\x61\n\x1aGetDeviceStatsLastTwoweeks\x12\x19.hr.GetDeviceStatsRequest\x1a&.hr.GetDeviceStatsLastTwoweeksResponse\"\x00\x12k\n$GetDeviceStatsLastTwoweeksAggregated\x12\x19.hr.GetDeviceStatsRequest\x1a&.hr.GetDeviceStatsLastTwoweeksResponse\"\x00\x12g\n\x18GetAveragesForDeviceList\x12#.hr.GetAveragesForDeviceListRequest\x1a$.hr.GetAveragesForDeviceListResponse\"\x00\x42\x34Z2github.com/brocaar/chirpstack-api/go/v3/handyrustyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.handyrusty.hr_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/brocaar/chirpstack-api/go/v3/handyrusty'
  _GETDEVICEFRAMESLOGREQUEST_FILTERSENTRY._options = None
  _GETDEVICEFRAMESLOGREQUEST_FILTERSENTRY._serialized_options = b'8\001'
  _globals['_GETAVERAGESFORDEVICELISTREQUEST']._serialized_start=168
  _globals['_GETAVERAGESFORDEVICELISTREQUEST']._serialized_end=219
  _globals['_AVERAGESFORDEVICELIST']._serialized_start=221
  _globals['_AVERAGESFORDEVICELIST']._serialized_end=335
  _globals['_GETAVERAGESFORDEVICELISTRESPONSE']._serialized_start=337
  _globals['_GETAVERAGESFORDEVICELISTRESPONSE']._serialized_end=414
  _globals['_GETDEVICESTATSREQUEST']._serialized_start=416
  _globals['_GETDEVICESTATSREQUEST']._serialized_end=456
  _globals['_GETDEVICESTATSRESPONSE']._serialized_start=459
  _globals['_GETDEVICESTATSRESPONSE']._serialized_end=799
  _globals['_DEVICESTATS']._serialized_start=802
  _globals['_DEVICESTATS']._serialized_end=960
  _globals['_GETDEVICESTATSLASTTWOWEEKSRESPONSE']._serialized_start=962
  _globals['_GETDEVICESTATSLASTTWOWEEKSRESPONSE']._serialized_end=1030
  _globals['_LOGSGWITEM']._serialized_start=1032
  _globals['_LOGSGWITEM']._serialized_end=1137
  _globals['_LOGSGATEWAYREQUEST']._serialized_start=1140
  _globals['_LOGSGATEWAYREQUEST']._serialized_end=1367
  _globals['_LOGSGATEWAYRESPONSE']._serialized_start=1369
  _globals['_LOGSGATEWAYRESPONSE']._serialized_end=1443
  _globals['_GETINTEGRATIONREPLIESREQUEST']._serialized_start=1446
  _globals['_GETINTEGRATIONREPLIESREQUEST']._serialized_end=1694
  _globals['_GETINTEGRATIONREPLIESRESPONSE']._serialized_start=1696
  _globals['_GETINTEGRATIONREPLIESRESPONSE']._serialized_end=1786
  _globals['_INTEGRATIONREPLY']._serialized_start=1789
  _globals['_INTEGRATIONREPLY']._serialized_end=1977
  _globals['_STOREINTEGRATIONREPLYREQUEST']._serialized_start=1979
  _globals['_STOREINTEGRATIONREPLYREQUEST']._serialized_end=2099
  _globals['_STOREINTEGRATIONREPLYRESPONSE']._serialized_start=2101
  _globals['_STOREINTEGRATIONREPLYRESPONSE']._serialized_end=2154
  _globals['_GETCURRENTSTATERESPONSE']._serialized_start=2156
  _globals['_GETCURRENTSTATERESPONSE']._serialized_end=2234
  _globals['_STREAMDEVICEFRAMESLOGCSVRESPONSE']._serialized_start=2236
  _globals['_STREAMDEVICEFRAMESLOGCSVRESPONSE']._serialized_end=2355
  _globals['_GETDEVICEFRAMESLOGREQUEST']._serialized_start=2358
  _globals['_GETDEVICEFRAMESLOGREQUEST']._serialized_end=2623
  _globals['_GETDEVICEFRAMESLOGREQUEST_FILTERSENTRY']._serialized_start=2577
  _globals['_GETDEVICEFRAMESLOGREQUEST_FILTERSENTRY']._serialized_end=2623
  _globals['_GETDEVICEFRAMESLOGRESPONSE']._serialized_start=2625
  _globals['_GETDEVICEFRAMESLOGRESPONSE']._serialized_end=2708
  _globals['_EXECCOMMANDREQUEST']._serialized_start=2710
  _globals['_EXECCOMMANDREQUEST']._serialized_end=2809
  _globals['_GETFRAMECOUNTERSREQUEST']._serialized_start=2811
  _globals['_GETFRAMECOUNTERSREQUEST']._serialized_end=2864
  _globals['_GETFRAMECOUNTERSRESPONSE']._serialized_start=2866
  _globals['_GETFRAMECOUNTERSRESPONSE']._serialized_end=2929
  _globals['_GETFRAMESPEEDREQUEST']._serialized_start=2931
  _globals['_GETFRAMESPEEDREQUEST']._serialized_end=2981
  _globals['_GETFRAMESPEEDRESPONSE']._serialized_start=2983
  _globals['_GETFRAMESPEEDRESPONSE']._serialized_end=3040
  _globals['_GETDEVICECOUNTERSREQUEST']._serialized_start=3042
  _globals['_GETDEVICECOUNTERSREQUEST']._serialized_end=3142
  _globals['_GETDEVICECOUNTERSRESPONSE']._serialized_start=3144
  _globals['_GETDEVICECOUNTERSRESPONSE']._serialized_end=3234
  _globals['_GETGATEWAYCOUNTERSREQUEST']._serialized_start=3236
  _globals['_GETGATEWAYCOUNTERSREQUEST']._serialized_end=3337
  _globals['_GETGATEWAYCOUNTERSRESPONSE']._serialized_start=3339
  _globals['_GETGATEWAYCOUNTERSRESPONSE']._serialized_end=3430
  _globals['_GETVERSIONRESPONSE']._serialized_start=3432
  _globals['_GETVERSIONRESPONSE']._serialized_end=3469
  _globals['_DEVICECOUNTERS']._serialized_start=3472
  _globals['_DEVICECOUNTERS']._serialized_end=3605
  _globals['_FRAMECOUNTERS']._serialized_start=3608
  _globals['_FRAMECOUNTERS']._serialized_end=3914
  _globals['_FRAMESPEED']._serialized_start=3916
  _globals['_FRAMESPEED']._serialized_end=3950
  _globals['_DEVICEFRAMELOG']._serialized_start=3953
  _globals['_DEVICEFRAMELOG']._serialized_end=4411
  _globals['_RXINFO']._serialized_start=4414
  _globals['_RXINFO']._serialized_end=4828
  _globals['_GETGWSTATSREQUEST']._serialized_start=4830
  _globals['_GETGWSTATSREQUEST']._serialized_end=4861
  _globals['_GETGWSTATSRESPONSE']._serialized_start=4863
  _globals['_GETGWSTATSRESPONSE']._serialized_end=4943
  _globals['_HANDYRUSTYSERVICE']._serialized_start=4946
  _globals['_HANDYRUSTYSERVICE']._serialized_end=6402
# @@protoc_insertion_point(module_scope)
