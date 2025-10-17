from gw import gw_pb2 as _gw_pb2
from common import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResolveResult(_message.Message):
    __slots__ = ("location",)
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: _common_pb2.Location
    def __init__(self, location: _Optional[_Union[_common_pb2.Location, _Mapping]] = ...) -> None: ...

class FrameRXInfo(_message.Message):
    __slots__ = ("rx_info",)
    RX_INFO_FIELD_NUMBER: _ClassVar[int]
    rx_info: _containers.RepeatedCompositeFieldContainer[_gw_pb2.UplinkRXInfo]
    def __init__(self, rx_info: _Optional[_Iterable[_Union[_gw_pb2.UplinkRXInfo, _Mapping]]] = ...) -> None: ...

class ResolveTDOARequest(_message.Message):
    __slots__ = ("dev_eui", "frame_rx_info", "device_reference_altitude")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    FRAME_RX_INFO_FIELD_NUMBER: _ClassVar[int]
    DEVICE_REFERENCE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    frame_rx_info: FrameRXInfo
    device_reference_altitude: float
    def __init__(self, dev_eui: _Optional[bytes] = ..., frame_rx_info: _Optional[_Union[FrameRXInfo, _Mapping]] = ..., device_reference_altitude: _Optional[float] = ...) -> None: ...

class ResolveMultiFrameTDOARequest(_message.Message):
    __slots__ = ("dev_eui", "frame_rx_info_set", "device_reference_altitude")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    FRAME_RX_INFO_SET_FIELD_NUMBER: _ClassVar[int]
    DEVICE_REFERENCE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    frame_rx_info_set: _containers.RepeatedCompositeFieldContainer[FrameRXInfo]
    device_reference_altitude: float
    def __init__(self, dev_eui: _Optional[bytes] = ..., frame_rx_info_set: _Optional[_Iterable[_Union[FrameRXInfo, _Mapping]]] = ..., device_reference_altitude: _Optional[float] = ...) -> None: ...

class ResolveTDOAResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: ResolveResult
    def __init__(self, result: _Optional[_Union[ResolveResult, _Mapping]] = ...) -> None: ...

class ResolveMultiFrameTDOAResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: ResolveResult
    def __init__(self, result: _Optional[_Union[ResolveResult, _Mapping]] = ...) -> None: ...
