import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceQueueItem(_message.Message):
    __slots__ = ("dev_eui", "confirmed", "f_cnt", "f_port", "data", "json_object", "ttl", "message_id", "owner", "created_at", "timeout_after", "application_id")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    JSON_OBJECT_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_AFTER_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    confirmed: bool
    f_cnt: int
    f_port: int
    data: bytes
    json_object: str
    ttl: int
    message_id: str
    owner: str
    created_at: _timestamp_pb2.Timestamp
    timeout_after: _timestamp_pb2.Timestamp
    application_id: int
    def __init__(self, dev_eui: _Optional[str] = ..., confirmed: _Optional[bool] = ..., f_cnt: _Optional[int] = ..., f_port: _Optional[int] = ..., data: _Optional[bytes] = ..., json_object: _Optional[str] = ..., ttl: _Optional[int] = ..., message_id: _Optional[str] = ..., owner: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., timeout_after: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., application_id: _Optional[int] = ...) -> None: ...

class DownlinkItemHex(_message.Message):
    __slots__ = ("confirmed", "f_cnt", "f_port", "data", "ttl", "message_id")
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    confirmed: bool
    f_cnt: int
    f_port: int
    data: str
    ttl: int
    message_id: str
    def __init__(self, confirmed: _Optional[bool] = ..., f_cnt: _Optional[int] = ..., f_port: _Optional[int] = ..., data: _Optional[str] = ..., ttl: _Optional[int] = ..., message_id: _Optional[str] = ...) -> None: ...

class EnqueueDeviceQueueItemHexRequest(_message.Message):
    __slots__ = ("dev_eui", "device_queue_item", "get_fcnt")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    DEVICE_QUEUE_ITEM_FIELD_NUMBER: _ClassVar[int]
    GET_FCNT_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    device_queue_item: DownlinkItemHex
    get_fcnt: bool
    def __init__(self, dev_eui: _Optional[str] = ..., device_queue_item: _Optional[_Union[DownlinkItemHex, _Mapping]] = ..., get_fcnt: _Optional[bool] = ...) -> None: ...

class EnqueueDeviceQueueItemRequest(_message.Message):
    __slots__ = ("device_queue_item", "get_fcnt")
    DEVICE_QUEUE_ITEM_FIELD_NUMBER: _ClassVar[int]
    GET_FCNT_FIELD_NUMBER: _ClassVar[int]
    device_queue_item: DeviceQueueItem
    get_fcnt: bool
    def __init__(self, device_queue_item: _Optional[_Union[DeviceQueueItem, _Mapping]] = ..., get_fcnt: _Optional[bool] = ...) -> None: ...

class EnqueueDeviceQueueItemResponse(_message.Message):
    __slots__ = ("f_cnt", "msg_id")
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    MSG_ID_FIELD_NUMBER: _ClassVar[int]
    f_cnt: int
    msg_id: str
    def __init__(self, f_cnt: _Optional[int] = ..., msg_id: _Optional[str] = ...) -> None: ...

class FlushDeviceQueueRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    def __init__(self, dev_eui: _Optional[str] = ...) -> None: ...

class ListDeviceQueueItemsRequest(_message.Message):
    __slots__ = ("dev_eui", "count_only")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    COUNT_ONLY_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    count_only: bool
    def __init__(self, dev_eui: _Optional[str] = ..., count_only: _Optional[bool] = ...) -> None: ...

class ListDeviceQueueItemsResponse(_message.Message):
    __slots__ = ("device_queue_items", "total_count")
    DEVICE_QUEUE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    device_queue_items: _containers.RepeatedCompositeFieldContainer[DeviceQueueItem]
    total_count: int
    def __init__(self, device_queue_items: _Optional[_Iterable[_Union[DeviceQueueItem, _Mapping]]] = ..., total_count: _Optional[int] = ...) -> None: ...

class EnqueueDeviceQueueActilityItemRequest(_message.Message):
    __slots__ = ("dev_eui", "confirm_downlink", "flush_downlink_queue", "payload_hex", "target_ports", "f_cnt", "ttl", "get_fcnt")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_DOWNLINK_FIELD_NUMBER: _ClassVar[int]
    FLUSH_DOWNLINK_QUEUE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_HEX_FIELD_NUMBER: _ClassVar[int]
    TARGET_PORTS_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    GET_FCNT_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    confirm_downlink: bool
    flush_downlink_queue: bool
    payload_hex: str
    target_ports: str
    f_cnt: int
    ttl: int
    get_fcnt: bool
    def __init__(self, dev_eui: _Optional[str] = ..., confirm_downlink: _Optional[bool] = ..., flush_downlink_queue: _Optional[bool] = ..., payload_hex: _Optional[str] = ..., target_ports: _Optional[str] = ..., f_cnt: _Optional[int] = ..., ttl: _Optional[int] = ..., get_fcnt: _Optional[bool] = ...) -> None: ...

class EnqueueDeviceQueueActilityItemResponse(_message.Message):
    __slots__ = ("confirm_downlink", "flush_downlink_queue", "payload_hex", "target_ports", "status", "msg_id")
    CONFIRM_DOWNLINK_FIELD_NUMBER: _ClassVar[int]
    FLUSH_DOWNLINK_QUEUE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_HEX_FIELD_NUMBER: _ClassVar[int]
    TARGET_PORTS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MSG_ID_FIELD_NUMBER: _ClassVar[int]
    confirm_downlink: bool
    flush_downlink_queue: bool
    payload_hex: str
    target_ports: str
    status: str
    msg_id: str
    def __init__(self, confirm_downlink: _Optional[bool] = ..., flush_downlink_queue: _Optional[bool] = ..., payload_hex: _Optional[str] = ..., target_ports: _Optional[str] = ..., status: _Optional[str] = ..., msg_id: _Optional[str] = ...) -> None: ...

class GetNextDownlinkFCntRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    def __init__(self, dev_eui: _Optional[str] = ...) -> None: ...

class GetNextDownlinkFCntResponse(_message.Message):
    __slots__ = ("f_cnt",)
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    f_cnt: int
    def __init__(self, f_cnt: _Optional[int] = ...) -> None: ...
