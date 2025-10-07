import datetime

from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from common import common_pb2 as _common_pb2
from ns import profiles_pb2 as _profiles_pb2
from gw import gw_pb2 as _gw_pb2
from ns import ns_pb2 as _ns_pb2
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

class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GENERIC: _ClassVar[ErrorType]
    OTAA: _ClassVar[ErrorType]
    DATA_UP_FCNT_RESET: _ClassVar[ErrorType]
    DATA_UP_MIC: _ClassVar[ErrorType]
    DEVICE_QUEUE_ITEM_SIZE: _ClassVar[ErrorType]
    DEVICE_QUEUE_ITEM_FCNT: _ClassVar[ErrorType]
    DATA_UP_FCNT_RETRANSMISSION: _ClassVar[ErrorType]
    DATA_DOWN_GATEWAY: _ClassVar[ErrorType]
RX1: RXWindow
RX2: RXWindow
GENERIC: ErrorType
OTAA: ErrorType
DATA_UP_FCNT_RESET: ErrorType
DATA_UP_MIC: ErrorType
DEVICE_QUEUE_ITEM_SIZE: ErrorType
DEVICE_QUEUE_ITEM_FCNT: ErrorType
DATA_UP_FCNT_RETRANSMISSION: ErrorType
DATA_DOWN_GATEWAY: ErrorType

class UpdateSPonDeviceRequest(_message.Message):
    __slots__ = ("id", "sp_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    SP_ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    sp_id: bytes
    def __init__(self, id: _Optional[bytes] = ..., sp_id: _Optional[bytes] = ...) -> None: ...

class GetServiceProfileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class GetServiceProfileResponse(_message.Message):
    __slots__ = ("as_data",)
    AS_DATA_FIELD_NUMBER: _ClassVar[int]
    as_data: ServiceProfileItem
    def __init__(self, as_data: _Optional[_Union[ServiceProfileItem, _Mapping]] = ...) -> None: ...

class CreateServiceProfileRequest(_message.Message):
    __slots__ = ("as_data", "ns_data")
    AS_DATA_FIELD_NUMBER: _ClassVar[int]
    NS_DATA_FIELD_NUMBER: _ClassVar[int]
    as_data: ServiceProfileItem
    ns_data: _profiles_pb2.ServiceProfile
    def __init__(self, as_data: _Optional[_Union[ServiceProfileItem, _Mapping]] = ..., ns_data: _Optional[_Union[_profiles_pb2.ServiceProfile, _Mapping]] = ...) -> None: ...

class CreateServiceProfileResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class ServiceProfileItem(_message.Message):
    __slots__ = ("network_server_id", "organization_id", "name", "description", "device_count_limit", "created_at", "updated_at")
    NETWORK_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COUNT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    network_server_id: int
    organization_id: int
    name: str
    description: str
    device_count_limit: int
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, network_server_id: _Optional[int] = ..., organization_id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., device_count_limit: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GatewayMetaData(_message.Message):
    __slots__ = ("gw_id", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    GW_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    gw_id: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, gw_id: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetGWMetaDataResponse(_message.Message):
    __slots__ = ("metadata_list",)
    METADATA_LIST_FIELD_NUMBER: _ClassVar[int]
    metadata_list: _containers.RepeatedCompositeFieldContainer[GatewayMetaData]
    def __init__(self, metadata_list: _Optional[_Iterable[_Union[GatewayMetaData, _Mapping]]] = ...) -> None: ...

class GetDictionaryRequest(_message.Message):
    __slots__ = ("dic_type",)
    DIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    dic_type: str
    def __init__(self, dic_type: _Optional[str] = ...) -> None: ...

class GetDictionaryResponse(_message.Message):
    __slots__ = ("dic_type", "list")
    DIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    dic_type: str
    list: _containers.RepeatedCompositeFieldContainer[Dictionary]
    def __init__(self, dic_type: _Optional[str] = ..., list: _Optional[_Iterable[_Union[Dictionary, _Mapping]]] = ...) -> None: ...

class Dictionary(_message.Message):
    __slots__ = ("code", "dic_type", "label", "is_actual")
    CODE_FIELD_NUMBER: _ClassVar[int]
    DIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    IS_ACTUAL_FIELD_NUMBER: _ClassVar[int]
    code: int
    dic_type: str
    label: str
    is_actual: bool
    def __init__(self, code: _Optional[int] = ..., dic_type: _Optional[str] = ..., label: _Optional[str] = ..., is_actual: _Optional[bool] = ...) -> None: ...

class GetOrgByDevEUIRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    def __init__(self, dev_eui: _Optional[str] = ...) -> None: ...

class NewAppSKeyRequest(_message.Message):
    __slots__ = ("dev_eui", "dev_addr", "aes_key_envelope")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    AES_KEY_ENVELOPE_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    dev_addr: bytes
    aes_key_envelope: _common_pb2.KeyEnvelope
    def __init__(self, dev_eui: _Optional[bytes] = ..., dev_addr: _Optional[bytes] = ..., aes_key_envelope: _Optional[_Union[_common_pb2.KeyEnvelope, _Mapping]] = ...) -> None: ...

class GetOrgIDByGwIDRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetDeviceAppSKeyResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    def __init__(self, value: _Optional[bytes] = ...) -> None: ...

class GetDeviceKeysResponse(_message.Message):
    __slots__ = ("nwk_key", "app_key")
    NWK_KEY_FIELD_NUMBER: _ClassVar[int]
    APP_KEY_FIELD_NUMBER: _ClassVar[int]
    nwk_key: bytes
    app_key: bytes
    def __init__(self, nwk_key: _Optional[bytes] = ..., app_key: _Optional[bytes] = ...) -> None: ...

class GetOrgByDevEUIResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ListOrganizationRequest(_message.Message):
    __slots__ = ("limit", "offset", "search")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    search: str
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., search: _Optional[str] = ...) -> None: ...

class ListOrganizationResponse(_message.Message):
    __slots__ = ("total_count", "result")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    result: _containers.RepeatedCompositeFieldContainer[OrganizationListItem]
    def __init__(self, total_count: _Optional[int] = ..., result: _Optional[_Iterable[_Union[OrganizationListItem, _Mapping]]] = ...) -> None: ...

class OrganizationListItem(_message.Message):
    __slots__ = ("id", "name", "display_name", "can_have_gateways", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CAN_HAVE_GATEWAYS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    display_name: str
    can_have_gateways: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., can_have_gateways: _Optional[bool] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetDevicesSummaryRequest(_message.Message):
    __slots__ = ("organization_id",)
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: int
    def __init__(self, organization_id: _Optional[int] = ...) -> None: ...

class GetDevicesSummaryResponse(_message.Message):
    __slots__ = ("active_count", "inactive_count", "dr_count", "never_seen_count")
    class DrCountEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ACTIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DR_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEVER_SEEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    active_count: int
    inactive_count: int
    dr_count: _containers.ScalarMap[int, int]
    never_seen_count: int
    def __init__(self, active_count: _Optional[int] = ..., inactive_count: _Optional[int] = ..., dr_count: _Optional[_Mapping[int, int]] = ..., never_seen_count: _Optional[int] = ...) -> None: ...

class GetGatewaysSummaryRequest(_message.Message):
    __slots__ = ("organization_id",)
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: int
    def __init__(self, organization_id: _Optional[int] = ...) -> None: ...

class GetGatewaysSummaryResponse(_message.Message):
    __slots__ = ("active_count", "inactive_count", "never_seen_count")
    ACTIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEVER_SEEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    active_count: int
    inactive_count: int
    never_seen_count: int
    def __init__(self, active_count: _Optional[int] = ..., inactive_count: _Optional[int] = ..., never_seen_count: _Optional[int] = ...) -> None: ...

class DeviceActivationContext(_message.Message):
    __slots__ = ("dev_addr", "app_s_key")
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    APP_S_KEY_FIELD_NUMBER: _ClassVar[int]
    dev_addr: bytes
    app_s_key: _common_pb2.KeyEnvelope
    def __init__(self, dev_addr: _Optional[bytes] = ..., app_s_key: _Optional[_Union[_common_pb2.KeyEnvelope, _Mapping]] = ...) -> None: ...

class HandleUplinkDataRequest(_message.Message):
    __slots__ = ("dev_eui", "join_eui", "f_cnt", "f_port", "adr", "dr", "tx_info", "rx_info", "data", "device_activation_context", "confirmed_uplink", "late", "mic", "time", "limit", "per", "snr", "rssi")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    JOIN_EUI_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    ADR_FIELD_NUMBER: _ClassVar[int]
    DR_FIELD_NUMBER: _ClassVar[int]
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    RX_INFO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ACTIVATION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_UPLINK_FIELD_NUMBER: _ClassVar[int]
    LATE_FIELD_NUMBER: _ClassVar[int]
    MIC_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PER_FIELD_NUMBER: _ClassVar[int]
    SNR_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    join_eui: bytes
    f_cnt: int
    f_port: int
    adr: bool
    dr: int
    tx_info: _gw_pb2.UplinkTXInfo
    rx_info: _containers.RepeatedCompositeFieldContainer[_gw_pb2.UplinkRXInfo]
    data: bytes
    device_activation_context: DeviceActivationContext
    confirmed_uplink: bool
    late: bool
    mic: bytes
    time: _timestamp_pb2.Timestamp
    limit: _ns_pb2.RateLimit
    per: float
    snr: float
    rssi: float
    def __init__(self, dev_eui: _Optional[bytes] = ..., join_eui: _Optional[bytes] = ..., f_cnt: _Optional[int] = ..., f_port: _Optional[int] = ..., adr: _Optional[bool] = ..., dr: _Optional[int] = ..., tx_info: _Optional[_Union[_gw_pb2.UplinkTXInfo, _Mapping]] = ..., rx_info: _Optional[_Iterable[_Union[_gw_pb2.UplinkRXInfo, _Mapping]]] = ..., data: _Optional[bytes] = ..., device_activation_context: _Optional[_Union[DeviceActivationContext, _Mapping]] = ..., confirmed_uplink: _Optional[bool] = ..., late: _Optional[bool] = ..., mic: _Optional[bytes] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., limit: _Optional[_Union[_ns_pb2.RateLimit, str]] = ..., per: _Optional[float] = ..., snr: _Optional[float] = ..., rssi: _Optional[float] = ..., **kwargs) -> None: ...

class HandleProprietaryUplinkRequest(_message.Message):
    __slots__ = ("mac_payload", "mic", "tx_info", "rx_info")
    MAC_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    MIC_FIELD_NUMBER: _ClassVar[int]
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    RX_INFO_FIELD_NUMBER: _ClassVar[int]
    mac_payload: bytes
    mic: bytes
    tx_info: _gw_pb2.UplinkTXInfo
    rx_info: _containers.RepeatedCompositeFieldContainer[_gw_pb2.UplinkRXInfo]
    def __init__(self, mac_payload: _Optional[bytes] = ..., mic: _Optional[bytes] = ..., tx_info: _Optional[_Union[_gw_pb2.UplinkTXInfo, _Mapping]] = ..., rx_info: _Optional[_Iterable[_Union[_gw_pb2.UplinkRXInfo, _Mapping]]] = ...) -> None: ...

class HandleErrorRequest(_message.Message):
    __slots__ = ("dev_eui", "type", "error", "f_cnt", "message_id")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    type: ErrorType
    error: str
    f_cnt: int
    message_id: str
    def __init__(self, dev_eui: _Optional[bytes] = ..., type: _Optional[_Union[ErrorType, str]] = ..., error: _Optional[str] = ..., f_cnt: _Optional[int] = ..., message_id: _Optional[str] = ...) -> None: ...

class HandleDownlinkACKRequest(_message.Message):
    __slots__ = ("dev_eui", "f_cnt", "acknowledged", "message_id")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    f_cnt: int
    acknowledged: bool
    message_id: str
    def __init__(self, dev_eui: _Optional[bytes] = ..., f_cnt: _Optional[int] = ..., acknowledged: _Optional[bool] = ..., message_id: _Optional[str] = ...) -> None: ...

class SetDeviceStatusRequest(_message.Message):
    __slots__ = ("dev_eui", "battery", "margin", "external_power_source", "battery_level_unavailable", "battery_level")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    MARGIN_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_POWER_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BATTERY_LEVEL_UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    BATTERY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    battery: int
    margin: int
    external_power_source: bool
    battery_level_unavailable: bool
    battery_level: float
    def __init__(self, dev_eui: _Optional[bytes] = ..., battery: _Optional[int] = ..., margin: _Optional[int] = ..., external_power_source: _Optional[bool] = ..., battery_level_unavailable: _Optional[bool] = ..., battery_level: _Optional[float] = ...) -> None: ...

class SetDeviceLocationRequest(_message.Message):
    __slots__ = ("dev_eui", "location", "uplink_ids")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    UPLINK_IDS_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    location: _common_pb2.Location
    uplink_ids: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, dev_eui: _Optional[bytes] = ..., location: _Optional[_Union[_common_pb2.Location, _Mapping]] = ..., uplink_ids: _Optional[_Iterable[bytes]] = ...) -> None: ...

class HandleGatewayStatsRequest(_message.Message):
    __slots__ = ("gateway_id", "stats_id", "time", "location", "rx_packets_received", "rx_packets_received_ok", "tx_packets_received", "tx_packets_emitted", "metadata", "tx_packets_per_frequency", "rx_packets_per_frequency", "tx_packets_per_dr", "rx_packets_per_dr", "tx_packets_per_status", "radio")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class TxPacketsPerFrequencyEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class RxPacketsPerFrequencyEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class TxPacketsPerDrEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class RxPacketsPerDrEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class TxPacketsPerStatusEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    STATS_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    RX_PACKETS_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    RX_PACKETS_RECEIVED_OK_FIELD_NUMBER: _ClassVar[int]
    TX_PACKETS_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    TX_PACKETS_EMITTED_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TX_PACKETS_PER_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    RX_PACKETS_PER_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    TX_PACKETS_PER_DR_FIELD_NUMBER: _ClassVar[int]
    RX_PACKETS_PER_DR_FIELD_NUMBER: _ClassVar[int]
    TX_PACKETS_PER_STATUS_FIELD_NUMBER: _ClassVar[int]
    RADIO_FIELD_NUMBER: _ClassVar[int]
    gateway_id: bytes
    stats_id: bytes
    time: _timestamp_pb2.Timestamp
    location: _common_pb2.Location
    rx_packets_received: int
    rx_packets_received_ok: int
    tx_packets_received: int
    tx_packets_emitted: int
    metadata: _containers.ScalarMap[str, str]
    tx_packets_per_frequency: _containers.ScalarMap[int, int]
    rx_packets_per_frequency: _containers.ScalarMap[int, int]
    tx_packets_per_dr: _containers.ScalarMap[int, int]
    rx_packets_per_dr: _containers.ScalarMap[int, int]
    tx_packets_per_status: _containers.ScalarMap[str, int]
    radio: str
    def __init__(self, gateway_id: _Optional[bytes] = ..., stats_id: _Optional[bytes] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., location: _Optional[_Union[_common_pb2.Location, _Mapping]] = ..., rx_packets_received: _Optional[int] = ..., rx_packets_received_ok: _Optional[int] = ..., tx_packets_received: _Optional[int] = ..., tx_packets_emitted: _Optional[int] = ..., metadata: _Optional[_Mapping[str, str]] = ..., tx_packets_per_frequency: _Optional[_Mapping[int, int]] = ..., rx_packets_per_frequency: _Optional[_Mapping[int, int]] = ..., tx_packets_per_dr: _Optional[_Mapping[int, int]] = ..., rx_packets_per_dr: _Optional[_Mapping[int, int]] = ..., tx_packets_per_status: _Optional[_Mapping[str, int]] = ..., radio: _Optional[str] = ...) -> None: ...

class HandleTxAckRequest(_message.Message):
    __slots__ = ("dev_eui", "f_cnt", "gateway_id", "tx_info", "message_id")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    f_cnt: int
    gateway_id: bytes
    tx_info: _gw_pb2.DownlinkTXInfo
    message_id: str
    def __init__(self, dev_eui: _Optional[bytes] = ..., f_cnt: _Optional[int] = ..., gateway_id: _Optional[bytes] = ..., tx_info: _Optional[_Union[_gw_pb2.DownlinkTXInfo, _Mapping]] = ..., message_id: _Optional[str] = ...) -> None: ...

class ReEncryptDeviceQueueItemsRequest(_message.Message):
    __slots__ = ("dev_eui", "dev_addr", "f_cnt_start", "items")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    F_CNT_START_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    dev_addr: bytes
    f_cnt_start: int
    items: _containers.RepeatedCompositeFieldContainer[ReEncryptDeviceQueueItem]
    def __init__(self, dev_eui: _Optional[bytes] = ..., dev_addr: _Optional[bytes] = ..., f_cnt_start: _Optional[int] = ..., items: _Optional[_Iterable[_Union[ReEncryptDeviceQueueItem, _Mapping]]] = ...) -> None: ...

class ReEncryptDeviceQueueItemsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ReEncryptedDeviceQueueItem]
    def __init__(self, items: _Optional[_Iterable[_Union[ReEncryptedDeviceQueueItem, _Mapping]]] = ...) -> None: ...

class ReEncryptDeviceQueueItem(_message.Message):
    __slots__ = ("frm_payload", "f_cnt", "f_port", "confirmed")
    FRM_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    frm_payload: bytes
    f_cnt: int
    f_port: int
    confirmed: bool
    def __init__(self, frm_payload: _Optional[bytes] = ..., f_cnt: _Optional[int] = ..., f_port: _Optional[int] = ..., confirmed: _Optional[bool] = ...) -> None: ...

class ReEncryptedDeviceQueueItem(_message.Message):
    __slots__ = ("frm_payload", "f_cnt", "f_port", "confirmed", "non_encr_pl")
    FRM_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    NON_ENCR_PL_FIELD_NUMBER: _ClassVar[int]
    frm_payload: bytes
    f_cnt: int
    f_port: int
    confirmed: bool
    non_encr_pl: bytes
    def __init__(self, frm_payload: _Optional[bytes] = ..., f_cnt: _Optional[int] = ..., f_port: _Optional[int] = ..., confirmed: _Optional[bool] = ..., non_encr_pl: _Optional[bytes] = ...) -> None: ...

class GatewayTaskResponseData(_message.Message):
    __slots__ = ("gateway_id", "exec_id", "cmd", "stderr", "error", "description", "name")
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    EXEC_ID_FIELD_NUMBER: _ClassVar[int]
    CMD_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    gateway_id: bytes
    exec_id: bytes
    cmd: str
    stderr: bytes
    error: str
    description: str
    name: str
    def __init__(self, gateway_id: _Optional[bytes] = ..., exec_id: _Optional[bytes] = ..., cmd: _Optional[str] = ..., stderr: _Optional[bytes] = ..., error: _Optional[str] = ..., description: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GatewayTaskResult(_message.Message):
    __slots__ = ("metadata", "chunk")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    metadata: GatewayTaskResponseData
    chunk: bytes
    def __init__(self, metadata: _Optional[_Union[GatewayTaskResponseData, _Mapping]] = ..., chunk: _Optional[bytes] = ...) -> None: ...

class CheckJwtRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class CheckJwtResponse(_message.Message):
    __slots__ = ("is_active", "is_admin")
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    is_active: bool
    is_admin: bool
    def __init__(self, is_active: _Optional[bool] = ..., is_admin: _Optional[bool] = ...) -> None: ...
