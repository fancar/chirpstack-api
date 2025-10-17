from google.protobuf import empty_pb2 as _empty_pb2
from gw import gw_pb2 as _gw_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[MType]
    JOIN_REQUEST: _ClassVar[MType]
    JOIN_ACCEPT: _ClassVar[MType]
    UNCONFIRMED_DATA_UP: _ClassVar[MType]
    UNCONFIRMED_DATA_DOWN: _ClassVar[MType]
    CONFIRMED_DATA_UP: _ClassVar[MType]
    CONFIRMED_DATA_DOWN: _ClassVar[MType]
    REJOIN_REQUEST: _ClassVar[MType]
UNKNOWN: MType
JOIN_REQUEST: MType
JOIN_ACCEPT: MType
UNCONFIRMED_DATA_UP: MType
UNCONFIRMED_DATA_DOWN: MType
CONFIRMED_DATA_UP: MType
CONFIRMED_DATA_DOWN: MType
REJOIN_REQUEST: MType

class HandleUplinkMetaDataRequest(_message.Message):
    __slots__ = ("dev_eui", "tx_info", "rx_info", "phy_payload_byte_count", "mac_command_byte_count", "application_payload_byte_count", "message_type")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    RX_INFO_FIELD_NUMBER: _ClassVar[int]
    PHY_PAYLOAD_BYTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAC_COMMAND_BYTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_PAYLOAD_BYTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    tx_info: _gw_pb2.UplinkTXInfo
    rx_info: _containers.RepeatedCompositeFieldContainer[_gw_pb2.UplinkRXInfo]
    phy_payload_byte_count: int
    mac_command_byte_count: int
    application_payload_byte_count: int
    message_type: MType
    def __init__(self, dev_eui: _Optional[bytes] = ..., tx_info: _Optional[_Union[_gw_pb2.UplinkTXInfo, _Mapping]] = ..., rx_info: _Optional[_Iterable[_Union[_gw_pb2.UplinkRXInfo, _Mapping]]] = ..., phy_payload_byte_count: _Optional[int] = ..., mac_command_byte_count: _Optional[int] = ..., application_payload_byte_count: _Optional[int] = ..., message_type: _Optional[_Union[MType, str]] = ...) -> None: ...

class HandleDownlinkMetaDataRequest(_message.Message):
    __slots__ = ("dev_eui", "multicast_group_id", "tx_info", "phy_payload_byte_count", "mac_command_byte_count", "application_payload_byte_count", "message_type", "gateway_id")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    MULTICAST_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    PHY_PAYLOAD_BYTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAC_COMMAND_BYTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_PAYLOAD_BYTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    multicast_group_id: bytes
    tx_info: _gw_pb2.DownlinkTXInfo
    phy_payload_byte_count: int
    mac_command_byte_count: int
    application_payload_byte_count: int
    message_type: MType
    gateway_id: bytes
    def __init__(self, dev_eui: _Optional[bytes] = ..., multicast_group_id: _Optional[bytes] = ..., tx_info: _Optional[_Union[_gw_pb2.DownlinkTXInfo, _Mapping]] = ..., phy_payload_byte_count: _Optional[int] = ..., mac_command_byte_count: _Optional[int] = ..., application_payload_byte_count: _Optional[int] = ..., message_type: _Optional[_Union[MType, str]] = ..., gateway_id: _Optional[bytes] = ...) -> None: ...

class HandleUplinkMACCommandRequest(_message.Message):
    __slots__ = ("dev_eui", "cid", "commands")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    CID_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    cid: int
    commands: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, dev_eui: _Optional[bytes] = ..., cid: _Optional[int] = ..., commands: _Optional[_Iterable[bytes]] = ...) -> None: ...

class HandleRejectedUplinkFrameSetRequest(_message.Message):
    __slots__ = ("frame_set",)
    FRAME_SET_FIELD_NUMBER: _ClassVar[int]
    frame_set: _gw_pb2.UplinkFrameSet
    def __init__(self, frame_set: _Optional[_Union[_gw_pb2.UplinkFrameSet, _Mapping]] = ...) -> None: ...
