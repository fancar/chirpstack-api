import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from gw import gw_pb2 as _gw_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RXWindow(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RX1: _ClassVar[RXWindow]
    RX2: _ClassVar[RXWindow]
RX1: RXWindow
RX2: RXWindow

class UplinkFrameLog(_message.Message):
    __slots__ = ("tx_info", "rx_info", "phy_payload_json", "published_at")
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    RX_INFO_FIELD_NUMBER: _ClassVar[int]
    PHY_PAYLOAD_JSON_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    tx_info: _gw_pb2.UplinkTXInfo
    rx_info: _containers.RepeatedCompositeFieldContainer[_gw_pb2.UplinkRXInfo]
    phy_payload_json: str
    published_at: _timestamp_pb2.Timestamp
    def __init__(self, tx_info: _Optional[_Union[_gw_pb2.UplinkTXInfo, _Mapping]] = ..., rx_info: _Optional[_Iterable[_Union[_gw_pb2.UplinkRXInfo, _Mapping]]] = ..., phy_payload_json: _Optional[str] = ..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DownlinkFrameLog(_message.Message):
    __slots__ = ("tx_info", "phy_payload_json", "gateway_id", "published_at")
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    PHY_PAYLOAD_JSON_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    tx_info: _gw_pb2.DownlinkTXInfo
    phy_payload_json: str
    gateway_id: str
    published_at: _timestamp_pb2.Timestamp
    def __init__(self, tx_info: _Optional[_Union[_gw_pb2.DownlinkTXInfo, _Mapping]] = ..., phy_payload_json: _Optional[str] = ..., gateway_id: _Optional[str] = ..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
