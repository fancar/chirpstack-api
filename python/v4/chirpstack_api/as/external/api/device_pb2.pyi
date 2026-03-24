import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from common import common_pb2 as _common_pb2
import importlib
_frameLog_pb2 = importlib.import_module('as.external.api.frameLog_pb2')
from ns import ns_pb2 as _ns_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Device(_message.Message):
    __slots__ = ("dev_eui", "name", "routing_profile_id", "description", "device_profile_id", "device_profile_name", "skip_f_cnt_check", "reference_altitude", "variables", "tags", "is_disabled", "service_profile_id", "location", "keep_queue")
    class VariablesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SKIP_F_CNT_CHECK_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    IS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    KEEP_QUEUE_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    name: str
    routing_profile_id: int
    description: str
    device_profile_id: str
    device_profile_name: str
    skip_f_cnt_check: bool
    reference_altitude: float
    variables: _containers.ScalarMap[str, str]
    tags: _containers.ScalarMap[str, str]
    is_disabled: bool
    service_profile_id: str
    location: _common_pb2.Location
    keep_queue: bool
    def __init__(self, dev_eui: _Optional[str] = ..., name: _Optional[str] = ..., routing_profile_id: _Optional[int] = ..., description: _Optional[str] = ..., device_profile_id: _Optional[str] = ..., device_profile_name: _Optional[str] = ..., skip_f_cnt_check: _Optional[bool] = ..., reference_altitude: _Optional[float] = ..., variables: _Optional[_Mapping[str, str]] = ..., tags: _Optional[_Mapping[str, str]] = ..., is_disabled: _Optional[bool] = ..., service_profile_id: _Optional[str] = ..., location: _Optional[_Union[_common_pb2.Location, _Mapping]] = ..., keep_queue: _Optional[bool] = ...) -> None: ...

class DeviceListItem(_message.Message):
    __slots__ = ("dev_eui", "name", "routing_profile_id", "description", "device_profile_id", "device_profile_name", "device_status_battery", "device_status_margin", "device_status_external_power_source", "device_status_battery_level_unavailable", "device_status_battery_level", "last_seen_at", "routing_profile_name", "location", "is_disabled", "service_profile_name", "service_profile_id", "per", "snr", "rssi")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_STATUS_BATTERY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_STATUS_MARGIN_FIELD_NUMBER: _ClassVar[int]
    DEVICE_STATUS_EXTERNAL_POWER_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_STATUS_BATTERY_LEVEL_UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_STATUS_BATTERY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    IS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    PER_FIELD_NUMBER: _ClassVar[int]
    SNR_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    name: str
    routing_profile_id: int
    description: str
    device_profile_id: str
    device_profile_name: str
    device_status_battery: int
    device_status_margin: int
    device_status_external_power_source: bool
    device_status_battery_level_unavailable: bool
    device_status_battery_level: float
    last_seen_at: _timestamp_pb2.Timestamp
    routing_profile_name: str
    location: _common_pb2.Location
    is_disabled: bool
    service_profile_name: str
    service_profile_id: str
    per: float
    snr: float
    rssi: float
    def __init__(self, dev_eui: _Optional[str] = ..., name: _Optional[str] = ..., routing_profile_id: _Optional[int] = ..., description: _Optional[str] = ..., device_profile_id: _Optional[str] = ..., device_profile_name: _Optional[str] = ..., device_status_battery: _Optional[int] = ..., device_status_margin: _Optional[int] = ..., device_status_external_power_source: _Optional[bool] = ..., device_status_battery_level_unavailable: _Optional[bool] = ..., device_status_battery_level: _Optional[float] = ..., last_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., routing_profile_name: _Optional[str] = ..., location: _Optional[_Union[_common_pb2.Location, _Mapping]] = ..., is_disabled: _Optional[bool] = ..., service_profile_name: _Optional[str] = ..., service_profile_id: _Optional[str] = ..., per: _Optional[float] = ..., snr: _Optional[float] = ..., rssi: _Optional[float] = ...) -> None: ...

class DeviceKeys(_message.Message):
    __slots__ = ("dev_eui", "nwk_key", "app_key", "gen_app_key")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    NWK_KEY_FIELD_NUMBER: _ClassVar[int]
    APP_KEY_FIELD_NUMBER: _ClassVar[int]
    GEN_APP_KEY_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    nwk_key: str
    app_key: str
    gen_app_key: str
    def __init__(self, dev_eui: _Optional[str] = ..., nwk_key: _Optional[str] = ..., app_key: _Optional[str] = ..., gen_app_key: _Optional[str] = ...) -> None: ...

class CreateDeviceRequest(_message.Message):
    __slots__ = ("device",)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: Device
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ...) -> None: ...

class GetDeviceRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    def __init__(self, dev_eui: _Optional[str] = ...) -> None: ...

class GetDeviceResponse(_message.Message):
    __slots__ = ("device", "created_at", "last_seen_at", "first_uplink_at", "device_status_battery", "device_status_margin", "location")
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    FIRST_UPLINK_AT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_STATUS_BATTERY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_STATUS_MARGIN_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    device: Device
    created_at: _timestamp_pb2.Timestamp
    last_seen_at: _timestamp_pb2.Timestamp
    first_uplink_at: _timestamp_pb2.Timestamp
    device_status_battery: int
    device_status_margin: int
    location: _common_pb2.Location
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., first_uplink_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., device_status_battery: _Optional[int] = ..., device_status_margin: _Optional[int] = ..., location: _Optional[_Union[_common_pb2.Location, _Mapping]] = ...) -> None: ...

class ListDeviceRequest(_message.Message):
    __slots__ = ("limit", "offset", "routing_profile_id", "search", "multicast_group_id", "service_profile_id", "tags", "orderBy", "order", "organization_id", "device_name", "dev_eui", "service_profile_name", "routing_profile_name", "device_profile_name", "devices", "device_profile_id", "device_name_exact")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    MULTICAST_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ORDERBY_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_EXACT_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    routing_profile_id: int
    search: str
    multicast_group_id: str
    service_profile_id: str
    tags: _containers.ScalarMap[str, str]
    orderBy: str
    order: str
    organization_id: int
    device_name: str
    dev_eui: str
    service_profile_name: str
    routing_profile_name: str
    device_profile_name: str
    devices: _containers.RepeatedScalarFieldContainer[str]
    device_profile_id: str
    device_name_exact: bool
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., routing_profile_id: _Optional[int] = ..., search: _Optional[str] = ..., multicast_group_id: _Optional[str] = ..., service_profile_id: _Optional[str] = ..., tags: _Optional[_Mapping[str, str]] = ..., orderBy: _Optional[str] = ..., order: _Optional[str] = ..., organization_id: _Optional[int] = ..., device_name: _Optional[str] = ..., dev_eui: _Optional[str] = ..., service_profile_name: _Optional[str] = ..., routing_profile_name: _Optional[str] = ..., device_profile_name: _Optional[str] = ..., devices: _Optional[_Iterable[str]] = ..., device_profile_id: _Optional[str] = ..., device_name_exact: _Optional[bool] = ...) -> None: ...

class ListDeviceResponse(_message.Message):
    __slots__ = ("total_count", "result")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    result: _containers.RepeatedCompositeFieldContainer[DeviceListItem]
    def __init__(self, total_count: _Optional[int] = ..., result: _Optional[_Iterable[_Union[DeviceListItem, _Mapping]]] = ...) -> None: ...

class DeleteDeviceRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    def __init__(self, dev_eui: _Optional[str] = ...) -> None: ...

class UpdateDeviceRequest(_message.Message):
    __slots__ = ("device",)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: Device
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ...) -> None: ...

class CreateDeviceKeysRequest(_message.Message):
    __slots__ = ("device_keys",)
    DEVICE_KEYS_FIELD_NUMBER: _ClassVar[int]
    device_keys: DeviceKeys
    def __init__(self, device_keys: _Optional[_Union[DeviceKeys, _Mapping]] = ...) -> None: ...

class GetDeviceKeysRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    def __init__(self, dev_eui: _Optional[str] = ...) -> None: ...

class GetDeviceKeysResponse(_message.Message):
    __slots__ = ("device_keys",)
    DEVICE_KEYS_FIELD_NUMBER: _ClassVar[int]
    device_keys: DeviceKeys
    def __init__(self, device_keys: _Optional[_Union[DeviceKeys, _Mapping]] = ...) -> None: ...

class UpdateDeviceKeysRequest(_message.Message):
    __slots__ = ("device_keys",)
    DEVICE_KEYS_FIELD_NUMBER: _ClassVar[int]
    device_keys: DeviceKeys
    def __init__(self, device_keys: _Optional[_Union[DeviceKeys, _Mapping]] = ...) -> None: ...

class DeleteDeviceKeysRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    def __init__(self, dev_eui: _Optional[str] = ...) -> None: ...

class DeviceActivation(_message.Message):
    __slots__ = ("dev_eui", "dev_addr", "app_s_key", "nwk_s_enc_key", "s_nwk_s_int_key", "f_nwk_s_int_key", "f_cnt_up", "n_f_cnt_down", "a_f_cnt_down", "RX1DROffset", "RX2DR", "RX2Frequency", "TXPowerIndex", "DR", "ADR", "nb_trans", "enabled_uplink_channels", "extra_uplink_channels")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    APP_S_KEY_FIELD_NUMBER: _ClassVar[int]
    NWK_S_ENC_KEY_FIELD_NUMBER: _ClassVar[int]
    S_NWK_S_INT_KEY_FIELD_NUMBER: _ClassVar[int]
    F_NWK_S_INT_KEY_FIELD_NUMBER: _ClassVar[int]
    F_CNT_UP_FIELD_NUMBER: _ClassVar[int]
    N_F_CNT_DOWN_FIELD_NUMBER: _ClassVar[int]
    A_F_CNT_DOWN_FIELD_NUMBER: _ClassVar[int]
    RX1DROFFSET_FIELD_NUMBER: _ClassVar[int]
    RX2DR_FIELD_NUMBER: _ClassVar[int]
    RX2FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    TXPOWERINDEX_FIELD_NUMBER: _ClassVar[int]
    DR_FIELD_NUMBER: _ClassVar[int]
    ADR_FIELD_NUMBER: _ClassVar[int]
    NB_TRANS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_UPLINK_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_UPLINK_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    dev_addr: str
    app_s_key: str
    nwk_s_enc_key: str
    s_nwk_s_int_key: str
    f_nwk_s_int_key: str
    f_cnt_up: int
    n_f_cnt_down: int
    a_f_cnt_down: int
    RX1DROffset: int
    RX2DR: int
    RX2Frequency: int
    TXPowerIndex: int
    DR: int
    ADR: bool
    nb_trans: int
    enabled_uplink_channels: _containers.RepeatedScalarFieldContainer[int]
    extra_uplink_channels: _containers.RepeatedCompositeFieldContainer[_ns_pb2.ExtraChannels]
    def __init__(self, dev_eui: _Optional[str] = ..., dev_addr: _Optional[str] = ..., app_s_key: _Optional[str] = ..., nwk_s_enc_key: _Optional[str] = ..., s_nwk_s_int_key: _Optional[str] = ..., f_nwk_s_int_key: _Optional[str] = ..., f_cnt_up: _Optional[int] = ..., n_f_cnt_down: _Optional[int] = ..., a_f_cnt_down: _Optional[int] = ..., RX1DROffset: _Optional[int] = ..., RX2DR: _Optional[int] = ..., RX2Frequency: _Optional[int] = ..., TXPowerIndex: _Optional[int] = ..., DR: _Optional[int] = ..., ADR: _Optional[bool] = ..., nb_trans: _Optional[int] = ..., enabled_uplink_channels: _Optional[_Iterable[int]] = ..., extra_uplink_channels: _Optional[_Iterable[_Union[_ns_pb2.ExtraChannels, _Mapping]]] = ...) -> None: ...

class ActivateDeviceRequest(_message.Message):
    __slots__ = ("device_activation",)
    DEVICE_ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    device_activation: DeviceActivation
    def __init__(self, device_activation: _Optional[_Union[DeviceActivation, _Mapping]] = ...) -> None: ...

class DeactivateDeviceRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    def __init__(self, dev_eui: _Optional[str] = ...) -> None: ...

class GetDeviceActivationRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    def __init__(self, dev_eui: _Optional[str] = ...) -> None: ...

class GetDeviceActivationResponse(_message.Message):
    __slots__ = ("device_activation",)
    DEVICE_ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    device_activation: DeviceActivation
    def __init__(self, device_activation: _Optional[_Union[DeviceActivation, _Mapping]] = ...) -> None: ...

class GetRandomDevAddrRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    def __init__(self, dev_eui: _Optional[str] = ...) -> None: ...

class GetRandomDevAddrResponse(_message.Message):
    __slots__ = ("dev_addr",)
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    dev_addr: str
    def __init__(self, dev_addr: _Optional[str] = ...) -> None: ...

class DeviceStats(_message.Message):
    __slots__ = ("timestamp", "rx_packets", "gw_rssi", "gw_snr", "rx_packets_per_frequency", "rx_packets_per_dr", "errors")
    class RxPacketsPerFrequencyEntry(_message.Message):
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
    class ErrorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RX_PACKETS_FIELD_NUMBER: _ClassVar[int]
    GW_RSSI_FIELD_NUMBER: _ClassVar[int]
    GW_SNR_FIELD_NUMBER: _ClassVar[int]
    RX_PACKETS_PER_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    RX_PACKETS_PER_DR_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    rx_packets: int
    gw_rssi: float
    gw_snr: float
    rx_packets_per_frequency: _containers.ScalarMap[int, int]
    rx_packets_per_dr: _containers.ScalarMap[int, int]
    errors: _containers.ScalarMap[str, int]
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., rx_packets: _Optional[int] = ..., gw_rssi: _Optional[float] = ..., gw_snr: _Optional[float] = ..., rx_packets_per_frequency: _Optional[_Mapping[int, int]] = ..., rx_packets_per_dr: _Optional[_Mapping[int, int]] = ..., errors: _Optional[_Mapping[str, int]] = ...) -> None: ...

class GetDeviceStatsRequest(_message.Message):
    __slots__ = ("dev_eui", "interval", "start_timestamp", "end_timestamp")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    interval: str
    start_timestamp: _timestamp_pb2.Timestamp
    end_timestamp: _timestamp_pb2.Timestamp
    def __init__(self, dev_eui: _Optional[str] = ..., interval: _Optional[str] = ..., start_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetDeviceStatsResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedCompositeFieldContainer[DeviceStats]
    def __init__(self, result: _Optional[_Iterable[_Union[DeviceStats, _Mapping]]] = ...) -> None: ...

class StreamDeviceFrameLogsRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    def __init__(self, dev_eui: _Optional[str] = ...) -> None: ...

class StreamDeviceFrameLogsResponse(_message.Message):
    __slots__ = ("uplink_frame", "downlink_frame")
    UPLINK_FRAME_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_FRAME_FIELD_NUMBER: _ClassVar[int]
    uplink_frame: _frameLog_pb2.UplinkFrameLog
    downlink_frame: _frameLog_pb2.DownlinkFrameLog
    def __init__(self, uplink_frame: _Optional[_Union[_frameLog_pb2.UplinkFrameLog, _Mapping]] = ..., downlink_frame: _Optional[_Union[_frameLog_pb2.DownlinkFrameLog, _Mapping]] = ...) -> None: ...

class StreamDeviceEventLogsRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    def __init__(self, dev_eui: _Optional[str] = ...) -> None: ...

class StreamDeviceEventLogsResponse(_message.Message):
    __slots__ = ("type", "payload_json", "published_at", "stream_id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_JSON_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    type: str
    payload_json: str
    published_at: _timestamp_pb2.Timestamp
    stream_id: str
    def __init__(self, type: _Optional[str] = ..., payload_json: _Optional[str] = ..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., stream_id: _Optional[str] = ...) -> None: ...

class ClearDeviceNoncesRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    def __init__(self, dev_eui: _Optional[str] = ...) -> None: ...
