import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MulticastGroupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLASS_C: _ClassVar[MulticastGroupType]
    CLASS_B: _ClassVar[MulticastGroupType]
CLASS_C: MulticastGroupType
CLASS_B: MulticastGroupType

class MulticastGroup(_message.Message):
    __slots__ = ("id", "name", "mc_addr", "mc_nwk_s_key", "mc_app_s_key", "f_cnt", "group_type", "dr", "frequency", "ping_slot_period", "service_profile_id", "organization_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MC_ADDR_FIELD_NUMBER: _ClassVar[int]
    MC_NWK_S_KEY_FIELD_NUMBER: _ClassVar[int]
    MC_APP_S_KEY_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    DR_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    PING_SLOT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    mc_addr: str
    mc_nwk_s_key: str
    mc_app_s_key: str
    f_cnt: int
    group_type: MulticastGroupType
    dr: int
    frequency: int
    ping_slot_period: int
    service_profile_id: str
    organization_id: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., mc_addr: _Optional[str] = ..., mc_nwk_s_key: _Optional[str] = ..., mc_app_s_key: _Optional[str] = ..., f_cnt: _Optional[int] = ..., group_type: _Optional[_Union[MulticastGroupType, str]] = ..., dr: _Optional[int] = ..., frequency: _Optional[int] = ..., ping_slot_period: _Optional[int] = ..., service_profile_id: _Optional[str] = ..., organization_id: _Optional[int] = ...) -> None: ...

class MulticastGroupListItem(_message.Message):
    __slots__ = ("id", "name", "service_profile_id", "service_profile_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    service_profile_id: str
    service_profile_name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., service_profile_id: _Optional[str] = ..., service_profile_name: _Optional[str] = ...) -> None: ...

class CreateMulticastGroupRequest(_message.Message):
    __slots__ = ("multicast_group",)
    MULTICAST_GROUP_FIELD_NUMBER: _ClassVar[int]
    multicast_group: MulticastGroup
    def __init__(self, multicast_group: _Optional[_Union[MulticastGroup, _Mapping]] = ...) -> None: ...

class CreateMulticastGroupResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetMulticastGroupRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetMulticastGroupResponse(_message.Message):
    __slots__ = ("multicast_group", "created_at", "updated_at")
    MULTICAST_GROUP_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    multicast_group: MulticastGroup
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, multicast_group: _Optional[_Union[MulticastGroup, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpdateMulticastGroupRequest(_message.Message):
    __slots__ = ("multicast_group",)
    MULTICAST_GROUP_FIELD_NUMBER: _ClassVar[int]
    multicast_group: MulticastGroup
    def __init__(self, multicast_group: _Optional[_Union[MulticastGroup, _Mapping]] = ...) -> None: ...

class DeleteMulticastGroupRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AddDeviceToMulticastGroupRequest(_message.Message):
    __slots__ = ("multicast_group_id", "dev_eui")
    MULTICAST_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    multicast_group_id: str
    dev_eui: str
    def __init__(self, multicast_group_id: _Optional[str] = ..., dev_eui: _Optional[str] = ...) -> None: ...

class RemoveDeviceFromMulticastGroupRequest(_message.Message):
    __slots__ = ("multicast_group_id", "dev_eui")
    MULTICAST_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    multicast_group_id: str
    dev_eui: str
    def __init__(self, multicast_group_id: _Optional[str] = ..., dev_eui: _Optional[str] = ...) -> None: ...

class ListMulticastGroupRequest(_message.Message):
    __slots__ = ("limit", "offset", "organization_id", "dev_eui", "search", "service_profile_id")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    organization_id: int
    dev_eui: str
    search: str
    service_profile_id: str
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., organization_id: _Optional[int] = ..., dev_eui: _Optional[str] = ..., search: _Optional[str] = ..., service_profile_id: _Optional[str] = ...) -> None: ...

class ListMulticastGroupResponse(_message.Message):
    __slots__ = ("total_count", "result")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    result: _containers.RepeatedCompositeFieldContainer[MulticastGroupListItem]
    def __init__(self, total_count: _Optional[int] = ..., result: _Optional[_Iterable[_Union[MulticastGroupListItem, _Mapping]]] = ...) -> None: ...

class MulticastQueueItem(_message.Message):
    __slots__ = ("multicast_group_id", "f_cnt", "f_port", "data")
    MULTICAST_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    multicast_group_id: str
    f_cnt: int
    f_port: int
    data: bytes
    def __init__(self, multicast_group_id: _Optional[str] = ..., f_cnt: _Optional[int] = ..., f_port: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class EnqueueMulticastQueueItemRequest(_message.Message):
    __slots__ = ("multicast_queue_item",)
    MULTICAST_QUEUE_ITEM_FIELD_NUMBER: _ClassVar[int]
    multicast_queue_item: MulticastQueueItem
    def __init__(self, multicast_queue_item: _Optional[_Union[MulticastQueueItem, _Mapping]] = ...) -> None: ...

class EnqueueMulticastQueueItemResponse(_message.Message):
    __slots__ = ("f_cnt",)
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    f_cnt: int
    def __init__(self, f_cnt: _Optional[int] = ...) -> None: ...

class FlushMulticastGroupQueueItemsRequest(_message.Message):
    __slots__ = ("multicast_group_id",)
    MULTICAST_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    multicast_group_id: str
    def __init__(self, multicast_group_id: _Optional[str] = ...) -> None: ...

class ListMulticastGroupQueueItemsRequest(_message.Message):
    __slots__ = ("multicast_group_id",)
    MULTICAST_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    multicast_group_id: str
    def __init__(self, multicast_group_id: _Optional[str] = ...) -> None: ...

class ListMulticastGroupQueueItemsResponse(_message.Message):
    __slots__ = ("multicast_queue_items",)
    MULTICAST_QUEUE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    multicast_queue_items: _containers.RepeatedCompositeFieldContainer[MulticastQueueItem]
    def __init__(self, multicast_queue_items: _Optional[_Iterable[_Union[MulticastQueueItem, _Mapping]]] = ...) -> None: ...
