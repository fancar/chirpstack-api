import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import empty_pb2 as _empty_pb2
import importlib
_profiles_pb2 = importlib.import_module('as.external.api.profiles_pb2')
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateServiceProfileRequest(_message.Message):
    __slots__ = ("service_profile",)
    SERVICE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    service_profile: _profiles_pb2.ServiceProfile
    def __init__(self, service_profile: _Optional[_Union[_profiles_pb2.ServiceProfile, _Mapping]] = ...) -> None: ...

class CreateServiceProfileResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetServiceProfileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetServiceProfileResponse(_message.Message):
    __slots__ = ("service_profile", "created_at", "updated_at", "used_devices_count", "available_devices_count")
    SERVICE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USED_DEVICES_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_DEVICES_COUNT_FIELD_NUMBER: _ClassVar[int]
    service_profile: _profiles_pb2.ServiceProfile
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    used_devices_count: int
    available_devices_count: int
    def __init__(self, service_profile: _Optional[_Union[_profiles_pb2.ServiceProfile, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., used_devices_count: _Optional[int] = ..., available_devices_count: _Optional[int] = ...) -> None: ...

class UpdateServiceProfileRequest(_message.Message):
    __slots__ = ("service_profile",)
    SERVICE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    service_profile: _profiles_pb2.ServiceProfile
    def __init__(self, service_profile: _Optional[_Union[_profiles_pb2.ServiceProfile, _Mapping]] = ...) -> None: ...

class DeleteServiceProfileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListServiceProfileRequest(_message.Message):
    __slots__ = ("limit", "offset", "organization_id", "network_server_id", "orderBy", "order")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    ORDERBY_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    organization_id: int
    network_server_id: int
    orderBy: str
    order: str
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., organization_id: _Optional[int] = ..., network_server_id: _Optional[int] = ..., orderBy: _Optional[str] = ..., order: _Optional[str] = ...) -> None: ...

class ServiceProfileListItem(_message.Message):
    __slots__ = ("id", "name", "organization_id", "network_server_id", "created_at", "updated_at", "network_server_name", "device_count_limit", "used_devices_count", "available_devices_count", "is_disabled")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COUNT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    USED_DEVICES_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_DEVICES_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    organization_id: int
    network_server_id: int
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    network_server_name: str
    device_count_limit: int
    used_devices_count: int
    available_devices_count: int
    is_disabled: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., organization_id: _Optional[int] = ..., network_server_id: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., network_server_name: _Optional[str] = ..., device_count_limit: _Optional[int] = ..., used_devices_count: _Optional[int] = ..., available_devices_count: _Optional[int] = ..., is_disabled: _Optional[bool] = ...) -> None: ...

class ListServiceProfileResponse(_message.Message):
    __slots__ = ("total_count", "result")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    result: _containers.RepeatedCompositeFieldContainer[ServiceProfileListItem]
    def __init__(self, total_count: _Optional[int] = ..., result: _Optional[_Iterable[_Union[ServiceProfileListItem, _Mapping]]] = ...) -> None: ...
