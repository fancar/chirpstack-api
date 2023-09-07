# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/as_pb/external/api/networkServer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5chirpstack-api/as_pb/external/api/networkServer.proto\x12\x03\x61pi\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xe7\x03\n\rNetworkServer\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06server\x18\x03 \x01(\t\x12\x0f\n\x07\x63\x61_cert\x18\x04 \x01(\t\x12\x10\n\x08tls_cert\x18\x05 \x01(\t\x12\x0f\n\x07tls_key\x18\x06 \x01(\t\x12\x35\n\x17routing_profile_ca_cert\x18\x07 \x01(\tR\x14routingProfileCACert\x12\x37\n\x18routing_profile_tls_cert\x18\x08 \x01(\tR\x15routingProfileTLSCert\x12\x35\n\x17routing_profile_tls_key\x18\t \x01(\tR\x14routingProfileTLSKey\x12!\n\x19gateway_discovery_enabled\x18\n \x01(\x08\x12\"\n\x1agateway_discovery_interval\x18\x0b \x01(\r\x12\x43\n\x1egateway_discovery_tx_frequency\x18\x0c \x01(\rR\x1bgatewayDiscoveryTXFrequency\x12\x30\n\x14gateway_discovery_dr\x18\r \x01(\rR\x12gatewayDiscoveryDR\x12\x13\n\x0b\x64\x65scription\x18\x0e \x01(\t\"\xa1\x01\n\x15NetworkServerListItem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06server\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"H\n\x1a\x43reateNetworkServerRequest\x12*\n\x0enetwork_server\x18\x01 \x01(\x0b\x32\x12.api.NetworkServer\")\n\x1b\x43reateNetworkServerResponse\x12\n\n\x02id\x18\x01 \x01(\x03\"%\n\x17GetNetworkServerRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"\xc7\x01\n\x18GetNetworkServerResponse\x12*\n\x0enetwork_server\x18\x01 \x01(\x0b\x32\x12.api.NetworkServer\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x0e\n\x06region\x18\x05 \x01(\t\"H\n\x1aUpdateNetworkServerRequest\x12*\n\x0enetwork_server\x18\x01 \x01(\x0b\x32\x12.api.NetworkServer\"(\n\x1a\x44\x65leteNetworkServerRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"\x82\x01\n\x18ListNetworkServerRequest\x12\r\n\x05limit\x18\x01 \x01(\x03\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\'\n\x0forganization_id\x18\x03 \x01(\x03R\x0eorganizationID\x12\x0f\n\x07orderBy\x18\x04 \x01(\t\x12\r\n\x05order\x18\x05 \x01(\t\"\\\n\x19ListNetworkServerResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\x03\x12*\n\x06result\x18\x02 \x03(\x0b\x32\x1a.api.NetworkServerListItem\"4\n\x17GetADRAlgorithmsRequest\x12\x19\n\x11network_server_id\x18\x01 \x01(\x03\"E\n\x18GetADRAlgorithmsResponse\x12)\n\x0e\x61\x64r_algorithms\x18\x01 \x03(\x0b\x32\x11.api.ADRAlgorithm\"(\n\x0c\x41\x44RAlgorithm\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t2\xc1\x05\n\x14NetworkServerService\x12l\n\x06\x43reate\x12\x1f.api.CreateNetworkServerRequest\x1a .api.CreateNetworkServerResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x14/api/network-servers:\x01*\x12\x65\n\x03Get\x12\x1c.api.GetNetworkServerRequest\x1a\x1d.api.GetNetworkServerResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/api/network-servers/{id}\x12v\n\x06Update\x12\x1f.api.UpdateNetworkServerRequest\x1a\x16.google.protobuf.Empty\"3\x82\xd3\xe4\x93\x02-\x1a(/api/network-servers/{network_server.id}:\x01*\x12\x64\n\x06\x44\x65lete\x12\x1f.api.DeleteNetworkServerRequest\x1a\x16.google.protobuf.Empty\"!\x82\xd3\xe4\x93\x02\x1b*\x19/api/network-servers/{id}\x12\x63\n\x04List\x12\x1d.api.ListNetworkServerRequest\x1a\x1e.api.ListNetworkServerResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/api/network-servers\x12\x90\x01\n\x10GetADRAlgorithms\x12\x1c.api.GetADRAlgorithmsRequest\x1a\x1d.api.GetADRAlgorithmsResponse\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/api/network-servers/{network_server_id}/adr-algorithmsBr\n!io.chirpstack.api.as.external.apiB\x12NetworkServerProtoP\x01Z7github.com/brocaar/chirpstack-api/go/v3/as/external/apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.as_pb.external.api.networkServer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!io.chirpstack.api.as.external.apiB\022NetworkServerProtoP\001Z7github.com/brocaar/chirpstack-api/go/v3/as/external/api'
  _NETWORKSERVERSERVICE.methods_by_name['Create']._options = None
  _NETWORKSERVERSERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\031\"\024/api/network-servers:\001*'
  _NETWORKSERVERSERVICE.methods_by_name['Get']._options = None
  _NETWORKSERVERSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\033\022\031/api/network-servers/{id}'
  _NETWORKSERVERSERVICE.methods_by_name['Update']._options = None
  _NETWORKSERVERSERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002-\032(/api/network-servers/{network_server.id}:\001*'
  _NETWORKSERVERSERVICE.methods_by_name['Delete']._options = None
  _NETWORKSERVERSERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002\033*\031/api/network-servers/{id}'
  _NETWORKSERVERSERVICE.methods_by_name['List']._options = None
  _NETWORKSERVERSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\026\022\024/api/network-servers'
  _NETWORKSERVERSERVICE.methods_by_name['GetADRAlgorithms']._options = None
  _NETWORKSERVERSERVICE.methods_by_name['GetADRAlgorithms']._serialized_options = b'\202\323\344\223\0029\0227/api/network-servers/{network_server_id}/adr-algorithms'
  _globals['_NETWORKSERVER']._serialized_start=155
  _globals['_NETWORKSERVER']._serialized_end=642
  _globals['_NETWORKSERVERLISTITEM']._serialized_start=645
  _globals['_NETWORKSERVERLISTITEM']._serialized_end=806
  _globals['_CREATENETWORKSERVERREQUEST']._serialized_start=808
  _globals['_CREATENETWORKSERVERREQUEST']._serialized_end=880
  _globals['_CREATENETWORKSERVERRESPONSE']._serialized_start=882
  _globals['_CREATENETWORKSERVERRESPONSE']._serialized_end=923
  _globals['_GETNETWORKSERVERREQUEST']._serialized_start=925
  _globals['_GETNETWORKSERVERREQUEST']._serialized_end=962
  _globals['_GETNETWORKSERVERRESPONSE']._serialized_start=965
  _globals['_GETNETWORKSERVERRESPONSE']._serialized_end=1164
  _globals['_UPDATENETWORKSERVERREQUEST']._serialized_start=1166
  _globals['_UPDATENETWORKSERVERREQUEST']._serialized_end=1238
  _globals['_DELETENETWORKSERVERREQUEST']._serialized_start=1240
  _globals['_DELETENETWORKSERVERREQUEST']._serialized_end=1280
  _globals['_LISTNETWORKSERVERREQUEST']._serialized_start=1283
  _globals['_LISTNETWORKSERVERREQUEST']._serialized_end=1413
  _globals['_LISTNETWORKSERVERRESPONSE']._serialized_start=1415
  _globals['_LISTNETWORKSERVERRESPONSE']._serialized_end=1507
  _globals['_GETADRALGORITHMSREQUEST']._serialized_start=1509
  _globals['_GETADRALGORITHMSREQUEST']._serialized_end=1561
  _globals['_GETADRALGORITHMSRESPONSE']._serialized_start=1563
  _globals['_GETADRALGORITHMSRESPONSE']._serialized_end=1632
  _globals['_ADRALGORITHM']._serialized_start=1634
  _globals['_ADRALGORITHM']._serialized_end=1674
  _globals['_NETWORKSERVERSERVICE']._serialized_start=1677
  _globals['_NETWORKSERVERSERVICE']._serialized_end=2382
# @@protoc_insertion_point(module_scope)
