import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkServer(_message.Message):
    __slots__ = ("id", "name", "server", "ca_cert", "tls_cert", "tls_key", "routing_profile_ca_cert", "routing_profile_tls_cert", "routing_profile_tls_key", "gateway_discovery_enabled", "gateway_discovery_interval", "gateway_discovery_tx_frequency", "gateway_discovery_dr", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    CA_CERT_FIELD_NUMBER: _ClassVar[int]
    TLS_CERT_FIELD_NUMBER: _ClassVar[int]
    TLS_KEY_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PROFILE_CA_CERT_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PROFILE_TLS_CERT_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PROFILE_TLS_KEY_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_DISCOVERY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_DISCOVERY_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_DISCOVERY_TX_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_DISCOVERY_DR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    server: str
    ca_cert: str
    tls_cert: str
    tls_key: str
    routing_profile_ca_cert: str
    routing_profile_tls_cert: str
    routing_profile_tls_key: str
    gateway_discovery_enabled: bool
    gateway_discovery_interval: int
    gateway_discovery_tx_frequency: int
    gateway_discovery_dr: int
    description: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., server: _Optional[str] = ..., ca_cert: _Optional[str] = ..., tls_cert: _Optional[str] = ..., tls_key: _Optional[str] = ..., routing_profile_ca_cert: _Optional[str] = ..., routing_profile_tls_cert: _Optional[str] = ..., routing_profile_tls_key: _Optional[str] = ..., gateway_discovery_enabled: _Optional[bool] = ..., gateway_discovery_interval: _Optional[int] = ..., gateway_discovery_tx_frequency: _Optional[int] = ..., gateway_discovery_dr: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...

class NetworkServerListItem(_message.Message):
    __slots__ = ("id", "name", "server", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    server: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., server: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateNetworkServerRequest(_message.Message):
    __slots__ = ("network_server",)
    NETWORK_SERVER_FIELD_NUMBER: _ClassVar[int]
    network_server: NetworkServer
    def __init__(self, network_server: _Optional[_Union[NetworkServer, _Mapping]] = ...) -> None: ...

class CreateNetworkServerResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetNetworkServerRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetNetworkServerResponse(_message.Message):
    __slots__ = ("network_server", "created_at", "updated_at", "version", "region")
    NETWORK_SERVER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    network_server: NetworkServer
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    version: str
    region: str
    def __init__(self, network_server: _Optional[_Union[NetworkServer, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...

class UpdateNetworkServerRequest(_message.Message):
    __slots__ = ("network_server",)
    NETWORK_SERVER_FIELD_NUMBER: _ClassVar[int]
    network_server: NetworkServer
    def __init__(self, network_server: _Optional[_Union[NetworkServer, _Mapping]] = ...) -> None: ...

class DeleteNetworkServerRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ListNetworkServerRequest(_message.Message):
    __slots__ = ("limit", "offset", "organization_id", "orderBy", "order")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORDERBY_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    organization_id: int
    orderBy: str
    order: str
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., organization_id: _Optional[int] = ..., orderBy: _Optional[str] = ..., order: _Optional[str] = ...) -> None: ...

class ListNetworkServerResponse(_message.Message):
    __slots__ = ("total_count", "result")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    result: _containers.RepeatedCompositeFieldContainer[NetworkServerListItem]
    def __init__(self, total_count: _Optional[int] = ..., result: _Optional[_Iterable[_Union[NetworkServerListItem, _Mapping]]] = ...) -> None: ...

class GetADRAlgorithmsRequest(_message.Message):
    __slots__ = ("network_server_id",)
    NETWORK_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    network_server_id: int
    def __init__(self, network_server_id: _Optional[int] = ...) -> None: ...

class GetADRAlgorithmsResponse(_message.Message):
    __slots__ = ("adr_algorithms",)
    ADR_ALGORITHMS_FIELD_NUMBER: _ClassVar[int]
    adr_algorithms: _containers.RepeatedCompositeFieldContainer[ADRAlgorithm]
    def __init__(self, adr_algorithms: _Optional[_Iterable[_Union[ADRAlgorithm, _Mapping]]] = ...) -> None: ...

class ADRAlgorithm(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
