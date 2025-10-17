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

class RoutingProfile(_message.Message):
    __slots__ = ("id", "name", "description", "organization_id", "applications", "created_at", "dev_cnt")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DEV_CNT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    organization_id: int
    applications: _containers.RepeatedScalarFieldContainer[int]
    created_at: _timestamp_pb2.Timestamp
    dev_cnt: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., organization_id: _Optional[int] = ..., applications: _Optional[_Iterable[int]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dev_cnt: _Optional[int] = ...) -> None: ...

class CreateRoutingProfileRequest(_message.Message):
    __slots__ = ("routing_profile",)
    ROUTING_PROFILE_FIELD_NUMBER: _ClassVar[int]
    routing_profile: RoutingProfile
    def __init__(self, routing_profile: _Optional[_Union[RoutingProfile, _Mapping]] = ...) -> None: ...

class CreateRoutingProfileResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetRoutingProfileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetRoutingProfileResponse(_message.Message):
    __slots__ = ("routing_profile",)
    ROUTING_PROFILE_FIELD_NUMBER: _ClassVar[int]
    routing_profile: RoutingProfile
    def __init__(self, routing_profile: _Optional[_Union[RoutingProfile, _Mapping]] = ...) -> None: ...

class UpdateRoutingProfileRequest(_message.Message):
    __slots__ = ("routing_profile",)
    ROUTING_PROFILE_FIELD_NUMBER: _ClassVar[int]
    routing_profile: RoutingProfile
    def __init__(self, routing_profile: _Optional[_Union[RoutingProfile, _Mapping]] = ...) -> None: ...

class DeleteRoutingProfileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ListRoutingProfileRequest(_message.Message):
    __slots__ = ("limit", "offset", "organization_id", "search")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    organization_id: int
    search: str
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., organization_id: _Optional[int] = ..., search: _Optional[str] = ...) -> None: ...

class ListRoutingProfileResponse(_message.Message):
    __slots__ = ("total_count", "result")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    result: _containers.RepeatedCompositeFieldContainer[RoutingProfile]
    def __init__(self, total_count: _Optional[int] = ..., result: _Optional[_Iterable[_Union[RoutingProfile, _Mapping]]] = ...) -> None: ...
