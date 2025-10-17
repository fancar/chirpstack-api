import datetime

from common import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from gw import gw_pb2 as _gw_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[ErrorType]
    DOWNLINK_PAYLOAD_SIZE: _ClassVar[ErrorType]
    DOWNLINK_FCNT: _ClassVar[ErrorType]
    UPLINK_CODEC: _ClassVar[ErrorType]
    DOWNLINK_CODEC: _ClassVar[ErrorType]
    OTAA: _ClassVar[ErrorType]
    UPLINK_FCNT_RESET: _ClassVar[ErrorType]
    UPLINK_MIC: _ClassVar[ErrorType]
    UPLINK_FCNT_RETRANSMISSION: _ClassVar[ErrorType]
    DOWNLINK_GATEWAY: _ClassVar[ErrorType]

class LartechDeliveryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCEPTED: _ClassVar[LartechDeliveryStatus]
    REJECTED: _ClassVar[LartechDeliveryStatus]
    ON_AIR: _ClassVar[LartechDeliveryStatus]
    LOST: _ClassVar[LartechDeliveryStatus]
    DELIVERED: _ClassVar[LartechDeliveryStatus]
    ACCESS_DENIED: _ClassVar[LartechDeliveryStatus]
    INTERNAL_ERROR: _ClassVar[LartechDeliveryStatus]
    CANCELLED: _ClassVar[LartechDeliveryStatus]
UNKNOWN: ErrorType
DOWNLINK_PAYLOAD_SIZE: ErrorType
DOWNLINK_FCNT: ErrorType
UPLINK_CODEC: ErrorType
DOWNLINK_CODEC: ErrorType
OTAA: ErrorType
UPLINK_FCNT_RESET: ErrorType
UPLINK_MIC: ErrorType
UPLINK_FCNT_RETRANSMISSION: ErrorType
DOWNLINK_GATEWAY: ErrorType
ACCEPTED: LartechDeliveryStatus
REJECTED: LartechDeliveryStatus
ON_AIR: LartechDeliveryStatus
LOST: LartechDeliveryStatus
DELIVERED: LartechDeliveryStatus
ACCESS_DENIED: LartechDeliveryStatus
INTERNAL_ERROR: LartechDeliveryStatus
CANCELLED: LartechDeliveryStatus

class UplinkEvent(_message.Message):
    __slots__ = ("ns_id", "organization_id", "application_id", "published_at", "device_name", "dev_eui", "tx_info", "adr", "dr", "f_cnt", "f_port", "data", "object_json", "tags", "confirmed", "dev_addr", "mic", "late", "time", "device_profile_id", "service_profile_id", "routing_profile_id", "applications", "bat_time", "bat_level", "rx_info")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NS_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    ADR_FIELD_NUMBER: _ClassVar[int]
    DR_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    OBJECT_JSON_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    MIC_FIELD_NUMBER: _ClassVar[int]
    LATE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    BAT_TIME_FIELD_NUMBER: _ClassVar[int]
    BAT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    RX_INFO_FIELD_NUMBER: _ClassVar[int]
    ns_id: int
    organization_id: int
    application_id: int
    published_at: _timestamp_pb2.Timestamp
    device_name: str
    dev_eui: bytes
    tx_info: _gw_pb2.UplinkTXInfo
    adr: bool
    dr: int
    f_cnt: int
    f_port: int
    data: bytes
    object_json: str
    tags: _containers.ScalarMap[str, str]
    confirmed: bool
    dev_addr: bytes
    mic: bytes
    late: bool
    time: _timestamp_pb2.Timestamp
    device_profile_id: str
    service_profile_id: str
    routing_profile_id: int
    applications: _containers.RepeatedScalarFieldContainer[int]
    bat_time: _timestamp_pb2.Timestamp
    bat_level: float
    rx_info: _containers.RepeatedCompositeFieldContainer[_gw_pb2.UplinkRXInfo]
    def __init__(self, ns_id: _Optional[int] = ..., organization_id: _Optional[int] = ..., application_id: _Optional[int] = ..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., device_name: _Optional[str] = ..., dev_eui: _Optional[bytes] = ..., tx_info: _Optional[_Union[_gw_pb2.UplinkTXInfo, _Mapping]] = ..., adr: _Optional[bool] = ..., dr: _Optional[int] = ..., f_cnt: _Optional[int] = ..., f_port: _Optional[int] = ..., data: _Optional[bytes] = ..., object_json: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ..., confirmed: _Optional[bool] = ..., dev_addr: _Optional[bytes] = ..., mic: _Optional[bytes] = ..., late: _Optional[bool] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., device_profile_id: _Optional[str] = ..., service_profile_id: _Optional[str] = ..., routing_profile_id: _Optional[int] = ..., applications: _Optional[_Iterable[int]] = ..., bat_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., bat_level: _Optional[float] = ..., rx_info: _Optional[_Iterable[_Union[_gw_pb2.UplinkRXInfo, _Mapping]]] = ..., **kwargs) -> None: ...

class JoinEvent(_message.Message):
    __slots__ = ("application_id", "application_name", "device_name", "dev_eui", "dev_addr", "rx_info", "tx_info", "dr", "tags", "published_at", "applications")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    RX_INFO_FIELD_NUMBER: _ClassVar[int]
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    DR_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    application_name: str
    device_name: str
    dev_eui: bytes
    dev_addr: bytes
    rx_info: _containers.RepeatedCompositeFieldContainer[_gw_pb2.UplinkRXInfo]
    tx_info: _gw_pb2.UplinkTXInfo
    dr: int
    tags: _containers.ScalarMap[str, str]
    published_at: _timestamp_pb2.Timestamp
    applications: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, application_id: _Optional[int] = ..., application_name: _Optional[str] = ..., device_name: _Optional[str] = ..., dev_eui: _Optional[bytes] = ..., dev_addr: _Optional[bytes] = ..., rx_info: _Optional[_Iterable[_Union[_gw_pb2.UplinkRXInfo, _Mapping]]] = ..., tx_info: _Optional[_Union[_gw_pb2.UplinkTXInfo, _Mapping]] = ..., dr: _Optional[int] = ..., tags: _Optional[_Mapping[str, str]] = ..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., applications: _Optional[_Iterable[int]] = ...) -> None: ...

class AckEvent(_message.Message):
    __slots__ = ("application_id", "application_name", "device_name", "dev_eui", "acknowledged", "f_cnt", "tags", "published_at", "message_id", "applications")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGED_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    application_name: str
    device_name: str
    dev_eui: bytes
    acknowledged: bool
    f_cnt: int
    tags: _containers.ScalarMap[str, str]
    published_at: _timestamp_pb2.Timestamp
    message_id: str
    applications: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, application_id: _Optional[int] = ..., application_name: _Optional[str] = ..., device_name: _Optional[str] = ..., dev_eui: _Optional[bytes] = ..., acknowledged: _Optional[bool] = ..., f_cnt: _Optional[int] = ..., tags: _Optional[_Mapping[str, str]] = ..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., message_id: _Optional[str] = ..., applications: _Optional[_Iterable[int]] = ...) -> None: ...

class TxAckEvent(_message.Message):
    __slots__ = ("application_id", "application_name", "device_name", "dev_eui", "f_cnt", "tags", "gateway_id", "tx_info", "published_at", "message_id", "applications")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    application_name: str
    device_name: str
    dev_eui: bytes
    f_cnt: int
    tags: _containers.ScalarMap[str, str]
    gateway_id: bytes
    tx_info: _gw_pb2.DownlinkTXInfo
    published_at: _timestamp_pb2.Timestamp
    message_id: str
    applications: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, application_id: _Optional[int] = ..., application_name: _Optional[str] = ..., device_name: _Optional[str] = ..., dev_eui: _Optional[bytes] = ..., f_cnt: _Optional[int] = ..., tags: _Optional[_Mapping[str, str]] = ..., gateway_id: _Optional[bytes] = ..., tx_info: _Optional[_Union[_gw_pb2.DownlinkTXInfo, _Mapping]] = ..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., message_id: _Optional[str] = ..., applications: _Optional[_Iterable[int]] = ...) -> None: ...

class ErrorEvent(_message.Message):
    __slots__ = ("application_id", "application_name", "device_name", "dev_eui", "type", "error", "f_cnt", "tags", "published_at", "applications", "message_id")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    application_name: str
    device_name: str
    dev_eui: bytes
    type: ErrorType
    error: str
    f_cnt: int
    tags: _containers.ScalarMap[str, str]
    published_at: _timestamp_pb2.Timestamp
    applications: _containers.RepeatedScalarFieldContainer[int]
    message_id: str
    def __init__(self, application_id: _Optional[int] = ..., application_name: _Optional[str] = ..., device_name: _Optional[str] = ..., dev_eui: _Optional[bytes] = ..., type: _Optional[_Union[ErrorType, str]] = ..., error: _Optional[str] = ..., f_cnt: _Optional[int] = ..., tags: _Optional[_Mapping[str, str]] = ..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., applications: _Optional[_Iterable[int]] = ..., message_id: _Optional[str] = ...) -> None: ...

class StatusEvent(_message.Message):
    __slots__ = ("application_id", "application_name", "device_name", "dev_eui", "margin", "external_power_source", "battery_level_unavailable", "battery_level", "tags", "published_at", "applications")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    MARGIN_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_POWER_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BATTERY_LEVEL_UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    BATTERY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    application_name: str
    device_name: str
    dev_eui: bytes
    margin: int
    external_power_source: bool
    battery_level_unavailable: bool
    battery_level: float
    tags: _containers.ScalarMap[str, str]
    published_at: _timestamp_pb2.Timestamp
    applications: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, application_id: _Optional[int] = ..., application_name: _Optional[str] = ..., device_name: _Optional[str] = ..., dev_eui: _Optional[bytes] = ..., margin: _Optional[int] = ..., external_power_source: _Optional[bool] = ..., battery_level_unavailable: _Optional[bool] = ..., battery_level: _Optional[float] = ..., tags: _Optional[_Mapping[str, str]] = ..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., applications: _Optional[_Iterable[int]] = ...) -> None: ...

class LocationEvent(_message.Message):
    __slots__ = ("application_id", "application_name", "device_name", "dev_eui", "location", "tags", "uplink_ids", "f_cnt", "published_at", "applications")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    UPLINK_IDS_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    application_name: str
    device_name: str
    dev_eui: bytes
    location: _common_pb2.Location
    tags: _containers.ScalarMap[str, str]
    uplink_ids: _containers.RepeatedScalarFieldContainer[bytes]
    f_cnt: int
    published_at: _timestamp_pb2.Timestamp
    applications: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, application_id: _Optional[int] = ..., application_name: _Optional[str] = ..., device_name: _Optional[str] = ..., dev_eui: _Optional[bytes] = ..., location: _Optional[_Union[_common_pb2.Location, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ..., uplink_ids: _Optional[_Iterable[bytes]] = ..., f_cnt: _Optional[int] = ..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., applications: _Optional[_Iterable[int]] = ...) -> None: ...

class IntegrationEvent(_message.Message):
    __slots__ = ("application_id", "application_name", "device_name", "dev_eui", "tags", "integration_name", "event_type", "object_json", "published_at", "applications")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_JSON_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    application_name: str
    device_name: str
    dev_eui: bytes
    tags: _containers.ScalarMap[str, str]
    integration_name: str
    event_type: str
    object_json: str
    published_at: _timestamp_pb2.Timestamp
    applications: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, application_id: _Optional[int] = ..., application_name: _Optional[str] = ..., device_name: _Optional[str] = ..., dev_eui: _Optional[bytes] = ..., tags: _Optional[_Mapping[str, str]] = ..., integration_name: _Optional[str] = ..., event_type: _Optional[str] = ..., object_json: _Optional[str] = ..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., applications: _Optional[_Iterable[int]] = ...) -> None: ...

class LartechUplinkEvent(_message.Message):
    __slots__ = ("messageId", "devEui", "gatewayEui", "appId", "rxTime", "frameCounter", "confirmed", "frequency", "loraModulation", "fskModulation", "snr", "rssi", "fport", "frmPayload", "owner", "stat", "rfChain", "size", "firmware", "firstMessage")
    MESSAGEID_FIELD_NUMBER: _ClassVar[int]
    DEVEUI_FIELD_NUMBER: _ClassVar[int]
    GATEWAYEUI_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    RXTIME_FIELD_NUMBER: _ClassVar[int]
    FRAMECOUNTER_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    LORAMODULATION_FIELD_NUMBER: _ClassVar[int]
    FSKMODULATION_FIELD_NUMBER: _ClassVar[int]
    SNR_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    FPORT_FIELD_NUMBER: _ClassVar[int]
    FRMPAYLOAD_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    STAT_FIELD_NUMBER: _ClassVar[int]
    RFCHAIN_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_FIELD_NUMBER: _ClassVar[int]
    FIRSTMESSAGE_FIELD_NUMBER: _ClassVar[int]
    messageId: str
    devEui: str
    gatewayEui: str
    appId: str
    rxTime: int
    frameCounter: int
    confirmed: bool
    frequency: int
    loraModulation: LoRaModulation
    fskModulation: FSKModulation
    snr: float
    rssi: float
    fport: _wrappers_pb2.Int32Value
    frmPayload: bytes
    owner: _wrappers_pb2.StringValue
    stat: _wrappers_pb2.Int32Value
    rfChain: _wrappers_pb2.Int32Value
    size: _wrappers_pb2.Int32Value
    firmware: _wrappers_pb2.StringValue
    firstMessage: _wrappers_pb2.BoolValue
    def __init__(self, messageId: _Optional[str] = ..., devEui: _Optional[str] = ..., gatewayEui: _Optional[str] = ..., appId: _Optional[str] = ..., rxTime: _Optional[int] = ..., frameCounter: _Optional[int] = ..., confirmed: _Optional[bool] = ..., frequency: _Optional[int] = ..., loraModulation: _Optional[_Union[LoRaModulation, _Mapping]] = ..., fskModulation: _Optional[_Union[FSKModulation, _Mapping]] = ..., snr: _Optional[float] = ..., rssi: _Optional[float] = ..., fport: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., frmPayload: _Optional[bytes] = ..., owner: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., stat: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., rfChain: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., size: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., firmware: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., firstMessage: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class LoRaModulation(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class FSKModulation(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class StatusRepliesMode(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DownlinkType(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class RxWindow(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class LartechDownlink(_message.Message):
    __slots__ = ("messageId", "devEui", "appId", "retries", "fport", "frmPayloads", "enableStatusReplies", "rxWindowHint", "owner", "statusRepliesModes", "alreadySentChunks", "downlinkType", "timeZoneHours")
    MESSAGEID_FIELD_NUMBER: _ClassVar[int]
    DEVEUI_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    RETRIES_FIELD_NUMBER: _ClassVar[int]
    FPORT_FIELD_NUMBER: _ClassVar[int]
    FRMPAYLOADS_FIELD_NUMBER: _ClassVar[int]
    ENABLESTATUSREPLIES_FIELD_NUMBER: _ClassVar[int]
    RXWINDOWHINT_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    STATUSREPLIESMODES_FIELD_NUMBER: _ClassVar[int]
    ALREADYSENTCHUNKS_FIELD_NUMBER: _ClassVar[int]
    DOWNLINKTYPE_FIELD_NUMBER: _ClassVar[int]
    TIMEZONEHOURS_FIELD_NUMBER: _ClassVar[int]
    messageId: str
    devEui: str
    appId: str
    retries: _wrappers_pb2.Int32Value
    fport: _wrappers_pb2.Int32Value
    frmPayloads: _containers.RepeatedScalarFieldContainer[bytes]
    enableStatusReplies: bool
    rxWindowHint: RxWindow
    owner: _wrappers_pb2.StringValue
    statusRepliesModes: _containers.RepeatedCompositeFieldContainer[StatusRepliesMode]
    alreadySentChunks: _wrappers_pb2.Int32Value
    downlinkType: DownlinkType
    timeZoneHours: _wrappers_pb2.Int32Value
    def __init__(self, messageId: _Optional[str] = ..., devEui: _Optional[str] = ..., appId: _Optional[str] = ..., retries: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., fport: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., frmPayloads: _Optional[_Iterable[bytes]] = ..., enableStatusReplies: _Optional[bool] = ..., rxWindowHint: _Optional[_Union[RxWindow, _Mapping]] = ..., owner: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., statusRepliesModes: _Optional[_Iterable[_Union[StatusRepliesMode, _Mapping]]] = ..., alreadySentChunks: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., downlinkType: _Optional[_Union[DownlinkType, _Mapping]] = ..., timeZoneHours: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class LartechDownlinkMessageStatus(_message.Message):
    __slots__ = ("messageId", "devEui", "status", "statusDescription", "appId", "owner", "sentChunks")
    MESSAGEID_FIELD_NUMBER: _ClassVar[int]
    DEVEUI_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUSDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    SENTCHUNKS_FIELD_NUMBER: _ClassVar[int]
    messageId: str
    devEui: str
    status: LartechDeliveryStatus
    statusDescription: _wrappers_pb2.StringValue
    appId: str
    owner: _wrappers_pb2.StringValue
    sentChunks: int
    def __init__(self, messageId: _Optional[str] = ..., devEui: _Optional[str] = ..., status: _Optional[_Union[LartechDeliveryStatus, str]] = ..., statusDescription: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., appId: _Optional[str] = ..., owner: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., sentChunks: _Optional[int] = ...) -> None: ...

class UplinkDefault(_message.Message):
    __slots__ = ("ns_id", "organization_id", "device_name", "dev_eui", "adr", "dr", "f_cnt", "f_port", "data", "tags", "confirmed", "dev_addr", "mic", "late", "time", "device_profile_id", "service_profile_id", "bat_time", "bat_level", "ext_power", "no_bat_lvl", "object_json", "rx_info")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NS_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    ADR_FIELD_NUMBER: _ClassVar[int]
    DR_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    MIC_FIELD_NUMBER: _ClassVar[int]
    LATE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    BAT_TIME_FIELD_NUMBER: _ClassVar[int]
    BAT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXT_POWER_FIELD_NUMBER: _ClassVar[int]
    NO_BAT_LVL_FIELD_NUMBER: _ClassVar[int]
    OBJECT_JSON_FIELD_NUMBER: _ClassVar[int]
    RX_INFO_FIELD_NUMBER: _ClassVar[int]
    ns_id: int
    organization_id: int
    device_name: str
    dev_eui: str
    adr: bool
    dr: int
    f_cnt: int
    f_port: int
    data: str
    tags: _containers.ScalarMap[str, str]
    confirmed: bool
    dev_addr: str
    mic: str
    late: bool
    time: _timestamp_pb2.Timestamp
    device_profile_id: str
    service_profile_id: str
    bat_time: _timestamp_pb2.Timestamp
    bat_level: float
    ext_power: bool
    no_bat_lvl: bool
    object_json: str
    rx_info: _containers.RepeatedCompositeFieldContainer[UplinkRXInfoDefault]
    def __init__(self, ns_id: _Optional[int] = ..., organization_id: _Optional[int] = ..., device_name: _Optional[str] = ..., dev_eui: _Optional[str] = ..., adr: _Optional[bool] = ..., dr: _Optional[int] = ..., f_cnt: _Optional[int] = ..., f_port: _Optional[int] = ..., data: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ..., confirmed: _Optional[bool] = ..., dev_addr: _Optional[str] = ..., mic: _Optional[str] = ..., late: _Optional[bool] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., device_profile_id: _Optional[str] = ..., service_profile_id: _Optional[str] = ..., bat_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., bat_level: _Optional[float] = ..., ext_power: _Optional[bool] = ..., no_bat_lvl: _Optional[bool] = ..., object_json: _Optional[str] = ..., rx_info: _Optional[_Iterable[_Union[UplinkRXInfoDefault, _Mapping]]] = ..., **kwargs) -> None: ...

class UplinkRXInfoDefault(_message.Message):
    __slots__ = ("gateway_id", "rssi", "lora_snr", "channel", "location", "fine_timestamp_type", "encrypted_fine_timestamp", "plain_fine_timestamp", "context", "uplink_id")
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    LORA_SNR_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    FINE_TIMESTAMP_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_FINE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PLAIN_FINE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    UPLINK_ID_FIELD_NUMBER: _ClassVar[int]
    gateway_id: str
    rssi: int
    lora_snr: float
    channel: int
    location: _common_pb2.Location
    fine_timestamp_type: _gw_pb2.FineTimestampType
    encrypted_fine_timestamp: _gw_pb2.EncryptedFineTimestamp
    plain_fine_timestamp: _gw_pb2.PlainFineTimestamp
    context: str
    uplink_id: str
    def __init__(self, gateway_id: _Optional[str] = ..., rssi: _Optional[int] = ..., lora_snr: _Optional[float] = ..., channel: _Optional[int] = ..., location: _Optional[_Union[_common_pb2.Location, _Mapping]] = ..., fine_timestamp_type: _Optional[_Union[_gw_pb2.FineTimestampType, str]] = ..., encrypted_fine_timestamp: _Optional[_Union[_gw_pb2.EncryptedFineTimestamp, _Mapping]] = ..., plain_fine_timestamp: _Optional[_Union[_gw_pb2.PlainFineTimestamp, _Mapping]] = ..., context: _Optional[str] = ..., uplink_id: _Optional[str] = ...) -> None: ...
