import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from common import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GatewayProfile(_message.Message):
    __slots__ = ("id", "name", "network_server_id", "channels", "extra_channels", "design", "description", "gps", "secure", "downlink_tx_power")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    DESIGN_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GPS_FIELD_NUMBER: _ClassVar[int]
    SECURE_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_TX_POWER_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    network_server_id: int
    channels: _containers.RepeatedScalarFieldContainer[int]
    extra_channels: _containers.RepeatedCompositeFieldContainer[GatewayProfileExtraChannel]
    design: str
    description: str
    gps: bool
    secure: bool
    downlink_tx_power: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., network_server_id: _Optional[int] = ..., channels: _Optional[_Iterable[int]] = ..., extra_channels: _Optional[_Iterable[_Union[GatewayProfileExtraChannel, _Mapping]]] = ..., design: _Optional[str] = ..., description: _Optional[str] = ..., gps: _Optional[bool] = ..., secure: _Optional[bool] = ..., downlink_tx_power: _Optional[int] = ...) -> None: ...

class GatewayProfileListItem(_message.Message):
    __slots__ = ("id", "name", "network_server_id", "network_server_name", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    network_server_id: int
    network_server_name: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., network_server_id: _Optional[int] = ..., network_server_name: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GatewayProfileExtraChannel(_message.Message):
    __slots__ = ("modulation", "frequency", "bandwidth", "bitrate", "spreading_factors")
    MODULATION_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    BITRATE_FIELD_NUMBER: _ClassVar[int]
    SPREADING_FACTORS_FIELD_NUMBER: _ClassVar[int]
    modulation: _common_pb2.Modulation
    frequency: int
    bandwidth: int
    bitrate: int
    spreading_factors: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, modulation: _Optional[_Union[_common_pb2.Modulation, str]] = ..., frequency: _Optional[int] = ..., bandwidth: _Optional[int] = ..., bitrate: _Optional[int] = ..., spreading_factors: _Optional[_Iterable[int]] = ...) -> None: ...

class CreateGatewayProfileRequest(_message.Message):
    __slots__ = ("gateway_profile",)
    GATEWAY_PROFILE_FIELD_NUMBER: _ClassVar[int]
    gateway_profile: GatewayProfile
    def __init__(self, gateway_profile: _Optional[_Union[GatewayProfile, _Mapping]] = ...) -> None: ...

class CreateGatewayProfileResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetGatewayProfileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetGatewayProfileResponse(_message.Message):
    __slots__ = ("gateway_profile", "created_at", "updated_at")
    GATEWAY_PROFILE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    gateway_profile: GatewayProfile
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, gateway_profile: _Optional[_Union[GatewayProfile, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpdateGatewayProfileRequest(_message.Message):
    __slots__ = ("gateway_profile",)
    GATEWAY_PROFILE_FIELD_NUMBER: _ClassVar[int]
    gateway_profile: GatewayProfile
    def __init__(self, gateway_profile: _Optional[_Union[GatewayProfile, _Mapping]] = ...) -> None: ...

class DeleteGatewayProfileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListGatewayProfilesRequest(_message.Message):
    __slots__ = ("limit", "offset", "network_server_id", "orderBy", "order")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    ORDERBY_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    network_server_id: int
    orderBy: str
    order: str
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., network_server_id: _Optional[int] = ..., orderBy: _Optional[str] = ..., order: _Optional[str] = ...) -> None: ...

class ListGatewayProfilesResponse(_message.Message):
    __slots__ = ("total_count", "result")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    result: _containers.RepeatedCompositeFieldContainer[GatewayProfileListItem]
    def __init__(self, total_count: _Optional[int] = ..., result: _Optional[_Iterable[_Union[GatewayProfileListItem, _Mapping]]] = ...) -> None: ...

class CountGatewaysResponse(_message.Message):
    __slots__ = ("data",)
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.ScalarMap[str, int]
    def __init__(self, data: _Optional[_Mapping[str, int]] = ...) -> None: ...
