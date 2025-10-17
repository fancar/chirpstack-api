from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Modulation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LORA: _ClassVar[Modulation]
    FSK: _ClassVar[Modulation]
    LR_FHSS: _ClassVar[Modulation]

class Region(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EU868: _ClassVar[Region]
    US915: _ClassVar[Region]
    CN779: _ClassVar[Region]
    EU433: _ClassVar[Region]
    AU915: _ClassVar[Region]
    CN470: _ClassVar[Region]
    AS923: _ClassVar[Region]
    AS923_2: _ClassVar[Region]
    AS923_3: _ClassVar[Region]
    AS923_4: _ClassVar[Region]
    KR920: _ClassVar[Region]
    IN865: _ClassVar[Region]
    RU864: _ClassVar[Region]
    ISM2400: _ClassVar[Region]

class MType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JoinRequest: _ClassVar[MType]
    JoinAccept: _ClassVar[MType]
    UnconfirmedDataUp: _ClassVar[MType]
    UnconfirmedDataDown: _ClassVar[MType]
    ConfirmedDataUp: _ClassVar[MType]
    ConfirmedDataDown: _ClassVar[MType]
    RejoinRequest: _ClassVar[MType]
    Proprietary: _ClassVar[MType]

class LocationSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[LocationSource]
    GPS: _ClassVar[LocationSource]
    CONFIG: _ClassVar[LocationSource]
    GEO_RESOLVER_TDOA: _ClassVar[LocationSource]
    GEO_RESOLVER_RSSI: _ClassVar[LocationSource]
    GEO_RESOLVER_GNSS: _ClassVar[LocationSource]
    GEO_RESOLVER_WIFI: _ClassVar[LocationSource]
LORA: Modulation
FSK: Modulation
LR_FHSS: Modulation
EU868: Region
US915: Region
CN779: Region
EU433: Region
AU915: Region
CN470: Region
AS923: Region
AS923_2: Region
AS923_3: Region
AS923_4: Region
KR920: Region
IN865: Region
RU864: Region
ISM2400: Region
JoinRequest: MType
JoinAccept: MType
UnconfirmedDataUp: MType
UnconfirmedDataDown: MType
ConfirmedDataUp: MType
ConfirmedDataDown: MType
RejoinRequest: MType
Proprietary: MType
UNKNOWN: LocationSource
GPS: LocationSource
CONFIG: LocationSource
GEO_RESOLVER_TDOA: LocationSource
GEO_RESOLVER_RSSI: LocationSource
GEO_RESOLVER_GNSS: LocationSource
GEO_RESOLVER_WIFI: LocationSource

class KeyEnvelope(_message.Message):
    __slots__ = ("kek_label", "aes_key")
    KEK_LABEL_FIELD_NUMBER: _ClassVar[int]
    AES_KEY_FIELD_NUMBER: _ClassVar[int]
    kek_label: str
    aes_key: bytes
    def __init__(self, kek_label: _Optional[str] = ..., aes_key: _Optional[bytes] = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ("latitude", "longitude", "altitude", "source", "accuracy")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    ACCURACY_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    altitude: float
    source: LocationSource
    accuracy: int
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[float] = ..., source: _Optional[_Union[LocationSource, str]] = ..., accuracy: _Optional[int] = ...) -> None: ...
