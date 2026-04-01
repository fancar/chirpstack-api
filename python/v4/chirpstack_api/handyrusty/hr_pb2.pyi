import datetime

from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from common import common_pb2 as _common_pb2
from gw import gw_pb2 as _gw_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetAveragesForDeviceListRequest(_message.Message):
    __slots__ = ("dev_list",)
    DEV_LIST_FIELD_NUMBER: _ClassVar[int]
    dev_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, dev_list: _Optional[_Iterable[str]] = ...) -> None: ...

class AveragesForDeviceList(_message.Message):
    __slots__ = ("dev_eui", "per_avg", "packet_cnt", "snr_last", "rssi_last")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    PER_AVG_FIELD_NUMBER: _ClassVar[int]
    PACKET_CNT_FIELD_NUMBER: _ClassVar[int]
    SNR_LAST_FIELD_NUMBER: _ClassVar[int]
    RSSI_LAST_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    per_avg: float
    packet_cnt: int
    snr_last: float
    rssi_last: int
    def __init__(self, dev_eui: _Optional[str] = ..., per_avg: _Optional[float] = ..., packet_cnt: _Optional[int] = ..., snr_last: _Optional[float] = ..., rssi_last: _Optional[int] = ...) -> None: ...

class GetAveragesForDeviceListResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedCompositeFieldContainer[AveragesForDeviceList]
    def __init__(self, result: _Optional[_Iterable[_Union[AveragesForDeviceList, _Mapping]]] = ...) -> None: ...

class GetDeviceStatsRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    def __init__(self, dev_eui: _Optional[str] = ...) -> None: ...

class GetDeviceStatsResponse(_message.Message):
    __slots__ = ("packet_cnt", "esp_avg", "snr_avg", "rssi_avg", "per_avg", "esp_last", "snr_last", "rssi_last", "sf_last", "rx_last", "tx_last", "join_last", "per_last")
    PACKET_CNT_FIELD_NUMBER: _ClassVar[int]
    ESP_AVG_FIELD_NUMBER: _ClassVar[int]
    SNR_AVG_FIELD_NUMBER: _ClassVar[int]
    RSSI_AVG_FIELD_NUMBER: _ClassVar[int]
    PER_AVG_FIELD_NUMBER: _ClassVar[int]
    ESP_LAST_FIELD_NUMBER: _ClassVar[int]
    SNR_LAST_FIELD_NUMBER: _ClassVar[int]
    RSSI_LAST_FIELD_NUMBER: _ClassVar[int]
    SF_LAST_FIELD_NUMBER: _ClassVar[int]
    RX_LAST_FIELD_NUMBER: _ClassVar[int]
    TX_LAST_FIELD_NUMBER: _ClassVar[int]
    JOIN_LAST_FIELD_NUMBER: _ClassVar[int]
    PER_LAST_FIELD_NUMBER: _ClassVar[int]
    packet_cnt: int
    esp_avg: float
    snr_avg: float
    rssi_avg: float
    per_avg: float
    esp_last: float
    snr_last: float
    rssi_last: int
    sf_last: int
    rx_last: _timestamp_pb2.Timestamp
    tx_last: _timestamp_pb2.Timestamp
    join_last: _timestamp_pb2.Timestamp
    per_last: float
    def __init__(self, packet_cnt: _Optional[int] = ..., esp_avg: _Optional[float] = ..., snr_avg: _Optional[float] = ..., rssi_avg: _Optional[float] = ..., per_avg: _Optional[float] = ..., esp_last: _Optional[float] = ..., snr_last: _Optional[float] = ..., rssi_last: _Optional[int] = ..., sf_last: _Optional[int] = ..., rx_last: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tx_last: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., join_last: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., per_last: _Optional[float] = ...) -> None: ...

class DeviceStats(_message.Message):
    __slots__ = ("created_at", "rx_cnt", "tx_cnt", "per", "esp", "rssi", "snr", "sf")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    RX_CNT_FIELD_NUMBER: _ClassVar[int]
    TX_CNT_FIELD_NUMBER: _ClassVar[int]
    PER_FIELD_NUMBER: _ClassVar[int]
    ESP_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    SNR_FIELD_NUMBER: _ClassVar[int]
    SF_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    rx_cnt: int
    tx_cnt: int
    per: float
    esp: float
    rssi: float
    snr: float
    sf: int
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., rx_cnt: _Optional[int] = ..., tx_cnt: _Optional[int] = ..., per: _Optional[float] = ..., esp: _Optional[float] = ..., rssi: _Optional[float] = ..., snr: _Optional[float] = ..., sf: _Optional[int] = ...) -> None: ...

class GetDeviceStatsLastTwoweeksResponse(_message.Message):
    __slots__ = ("stats",)
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[DeviceStats]
    def __init__(self, stats: _Optional[_Iterable[_Union[DeviceStats, _Mapping]]] = ...) -> None: ...

class LogsGwItem(_message.Message):
    __slots__ = ("created_at", "code", "gateway_id")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    code: int
    gateway_id: str
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., code: _Optional[int] = ..., gateway_id: _Optional[str] = ...) -> None: ...

class LogsGatewayRequest(_message.Message):
    __slots__ = ("limit", "offset", "organization_id", "gw_list", "code", "start_timestamp", "end_timestamp")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    GW_LIST_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    organization_id: int
    gw_list: _containers.RepeatedScalarFieldContainer[str]
    code: int
    start_timestamp: _timestamp_pb2.Timestamp
    end_timestamp: _timestamp_pb2.Timestamp
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., organization_id: _Optional[int] = ..., gw_list: _Optional[_Iterable[str]] = ..., code: _Optional[int] = ..., start_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class LogsGatewayResponse(_message.Message):
    __slots__ = ("total_count", "result")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    result: _containers.RepeatedCompositeFieldContainer[LogsGwItem]
    def __init__(self, total_count: _Optional[int] = ..., result: _Optional[_Iterable[_Union[LogsGwItem, _Mapping]]] = ...) -> None: ...

class GetIntegrationRepliesRequest(_message.Message):
    __slots__ = ("offset", "limit", "organisation_id", "routing_profile_id", "dev_eui", "is_error", "is_ok", "start", "end")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    ORGANISATION_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    IS_ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_OK_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    offset: int
    limit: int
    organisation_id: int
    routing_profile_id: int
    dev_eui: str
    is_error: bool
    is_ok: bool
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    def __init__(self, offset: _Optional[int] = ..., limit: _Optional[int] = ..., organisation_id: _Optional[int] = ..., routing_profile_id: _Optional[int] = ..., dev_eui: _Optional[str] = ..., is_error: _Optional[bool] = ..., is_ok: _Optional[bool] = ..., start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetIntegrationRepliesResponse(_message.Message):
    __slots__ = ("items_total", "result")
    ITEMS_TOTAL_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    items_total: int
    result: _containers.RepeatedCompositeFieldContainer[IntegrationReply]
    def __init__(self, items_total: _Optional[int] = ..., result: _Optional[_Iterable[_Union[IntegrationReply, _Mapping]]] = ...) -> None: ...

class IntegrationReply(_message.Message):
    __slots__ = ("integration_url", "status_code", "status_code_description", "application_id", "dev_eui", "time")
    INTEGRATION_URL_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    integration_url: str
    status_code: int
    status_code_description: str
    application_id: int
    dev_eui: str
    time: _timestamp_pb2.Timestamp
    def __init__(self, integration_url: _Optional[str] = ..., status_code: _Optional[int] = ..., status_code_description: _Optional[str] = ..., application_id: _Optional[int] = ..., dev_eui: _Optional[str] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StoreIntegrationReplyRequest(_message.Message):
    __slots__ = ("organisation_id", "routing_profile_id", "reply")
    ORGANISATION_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    organisation_id: int
    routing_profile_id: int
    reply: IntegrationReply
    def __init__(self, organisation_id: _Optional[int] = ..., routing_profile_id: _Optional[int] = ..., reply: _Optional[_Union[IntegrationReply, _Mapping]] = ...) -> None: ...

class StoreIntegrationReplyResponse(_message.Message):
    __slots__ = ("stored_count",)
    STORED_COUNT_FIELD_NUMBER: _ClassVar[int]
    stored_count: int
    def __init__(self, stored_count: _Optional[int] = ...) -> None: ...

class GetCurrentStateResponse(_message.Message):
    __slots__ = ("wl_last_packet", "wl_last_packet_unix")
    WL_LAST_PACKET_FIELD_NUMBER: _ClassVar[int]
    WL_LAST_PACKET_UNIX_FIELD_NUMBER: _ClassVar[int]
    wl_last_packet: str
    wl_last_packet_unix: int
    def __init__(self, wl_last_packet: _Optional[str] = ..., wl_last_packet_unix: _Optional[int] = ...) -> None: ...

class StreamDeviceFramesCSVResponse(_message.Message):
    __slots__ = ("current", "total", "rows", "chunk")
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    current: int
    total: int
    rows: int
    chunk: bytes
    def __init__(self, current: _Optional[int] = ..., total: _Optional[int] = ..., rows: _Optional[int] = ..., chunk: _Optional[bytes] = ...) -> None: ...

class GetDeviceFramesRequest(_message.Message):
    __slots__ = ("offset", "limit", "start", "end", "filters", "organization_id", "timezone", "gw_only", "get_total", "in_filters", "order", "reverse")
    class FiltersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class InFiltersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ListOfString
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ListOfString, _Mapping]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    GW_ONLY_FIELD_NUMBER: _ClassVar[int]
    GET_TOTAL_FIELD_NUMBER: _ClassVar[int]
    IN_FILTERS_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    offset: int
    limit: int
    start: str
    end: str
    filters: _containers.ScalarMap[str, str]
    organization_id: int
    timezone: str
    gw_only: bool
    get_total: bool
    in_filters: _containers.MessageMap[str, ListOfString]
    order: str
    reverse: bool
    def __init__(self, offset: _Optional[int] = ..., limit: _Optional[int] = ..., start: _Optional[str] = ..., end: _Optional[str] = ..., filters: _Optional[_Mapping[str, str]] = ..., organization_id: _Optional[int] = ..., timezone: _Optional[str] = ..., gw_only: _Optional[bool] = ..., get_total: _Optional[bool] = ..., in_filters: _Optional[_Mapping[str, ListOfString]] = ..., order: _Optional[str] = ..., reverse: _Optional[bool] = ...) -> None: ...

class ListOfString(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class GetDeviceFramesResponse(_message.Message):
    __slots__ = ("items_total", "data")
    ITEMS_TOTAL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    items_total: int
    data: _containers.RepeatedCompositeFieldContainer[DeviceFrameLog]
    def __init__(self, items_total: _Optional[int] = ..., data: _Optional[_Iterable[_Union[DeviceFrameLog, _Mapping]]] = ...) -> None: ...

class ExecCommandRequest(_message.Message):
    __slots__ = ("gateway_id", "command", "timeout", "background_task")
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_TASK_FIELD_NUMBER: _ClassVar[int]
    gateway_id: str
    command: str
    timeout: int
    background_task: bool
    def __init__(self, gateway_id: _Optional[str] = ..., command: _Optional[str] = ..., timeout: _Optional[int] = ..., background_task: _Optional[bool] = ...) -> None: ...

class GetFrameCountersRequest(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: str
    end: str
    def __init__(self, start: _Optional[str] = ..., end: _Optional[str] = ...) -> None: ...

class GetFrameCountersResponse(_message.Message):
    __slots__ = ("counters",)
    COUNTERS_FIELD_NUMBER: _ClassVar[int]
    counters: _containers.RepeatedCompositeFieldContainer[FrameCounters]
    def __init__(self, counters: _Optional[_Iterable[_Union[FrameCounters, _Mapping]]] = ...) -> None: ...

class GetFrameSpeedRequest(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: str
    end: str
    def __init__(self, start: _Optional[str] = ..., end: _Optional[str] = ...) -> None: ...

class GetFrameSpeedResponse(_message.Message):
    __slots__ = ("counters",)
    COUNTERS_FIELD_NUMBER: _ClassVar[int]
    counters: _containers.RepeatedCompositeFieldContainer[FrameSpeed]
    def __init__(self, counters: _Optional[_Iterable[_Union[FrameSpeed, _Mapping]]] = ...) -> None: ...

class GetDeviceCountersRequest(_message.Message):
    __slots__ = ("organization_id", "start", "end", "aggregation")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    organization_id: int
    start: str
    end: str
    aggregation: str
    def __init__(self, organization_id: _Optional[int] = ..., start: _Optional[str] = ..., end: _Optional[str] = ..., aggregation: _Optional[str] = ...) -> None: ...

class GetDeviceCountersResponse(_message.Message):
    __slots__ = ("organization_id", "counters")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTERS_FIELD_NUMBER: _ClassVar[int]
    organization_id: int
    counters: _containers.RepeatedCompositeFieldContainer[DeviceCounters]
    def __init__(self, organization_id: _Optional[int] = ..., counters: _Optional[_Iterable[_Union[DeviceCounters, _Mapping]]] = ...) -> None: ...

class GetGatewayCountersRequest(_message.Message):
    __slots__ = ("organization_id", "start", "end", "aggregation")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    organization_id: int
    start: str
    end: str
    aggregation: str
    def __init__(self, organization_id: _Optional[int] = ..., start: _Optional[str] = ..., end: _Optional[str] = ..., aggregation: _Optional[str] = ...) -> None: ...

class GetGatewayCountersResponse(_message.Message):
    __slots__ = ("organization_id", "counters")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTERS_FIELD_NUMBER: _ClassVar[int]
    organization_id: int
    counters: _containers.RepeatedCompositeFieldContainer[DeviceCounters]
    def __init__(self, organization_id: _Optional[int] = ..., counters: _Optional[_Iterable[_Union[DeviceCounters, _Mapping]]] = ...) -> None: ...

class GetVersionResponse(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...

class DeviceCounters(_message.Message):
    __slots__ = ("organization_id", "created_at", "active_count", "inactive_count", "never_seen_count")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEVER_SEEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    organization_id: int
    created_at: int
    active_count: int
    inactive_count: int
    never_seen_count: int
    def __init__(self, organization_id: _Optional[int] = ..., created_at: _Optional[int] = ..., active_count: _Optional[int] = ..., inactive_count: _Optional[int] = ..., never_seen_count: _Optional[int] = ...) -> None: ...

class FrameCounters(_message.Message):
    __slots__ = ("date", "rx_cnt", "tx_cnt", "total_cnt", "unknown_type", "join_request", "rejoin_request", "join_accept", "unconfirmed_data_up", "unconfirmed_data_down", "confirmed_data_up", "confirmed_data_down", "proprietary")
    DATE_FIELD_NUMBER: _ClassVar[int]
    RX_CNT_FIELD_NUMBER: _ClassVar[int]
    TX_CNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CNT_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_TYPE_FIELD_NUMBER: _ClassVar[int]
    JOIN_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REJOIN_REQUEST_FIELD_NUMBER: _ClassVar[int]
    JOIN_ACCEPT_FIELD_NUMBER: _ClassVar[int]
    UNCONFIRMED_DATA_UP_FIELD_NUMBER: _ClassVar[int]
    UNCONFIRMED_DATA_DOWN_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_DATA_UP_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_DATA_DOWN_FIELD_NUMBER: _ClassVar[int]
    PROPRIETARY_FIELD_NUMBER: _ClassVar[int]
    date: int
    rx_cnt: int
    tx_cnt: int
    total_cnt: int
    unknown_type: int
    join_request: int
    rejoin_request: int
    join_accept: int
    unconfirmed_data_up: int
    unconfirmed_data_down: int
    confirmed_data_up: int
    confirmed_data_down: int
    proprietary: int
    def __init__(self, date: _Optional[int] = ..., rx_cnt: _Optional[int] = ..., tx_cnt: _Optional[int] = ..., total_cnt: _Optional[int] = ..., unknown_type: _Optional[int] = ..., join_request: _Optional[int] = ..., rejoin_request: _Optional[int] = ..., join_accept: _Optional[int] = ..., unconfirmed_data_up: _Optional[int] = ..., unconfirmed_data_down: _Optional[int] = ..., confirmed_data_up: _Optional[int] = ..., confirmed_data_down: _Optional[int] = ..., proprietary: _Optional[int] = ...) -> None: ...

class FrameSpeed(_message.Message):
    __slots__ = ("t", "y")
    T_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    t: int
    y: int
    def __init__(self, t: _Optional[int] = ..., y: _Optional[int] = ...) -> None: ...

class DeviceFrameLog(_message.Message):
    __slots__ = ("direction", "date_time", "date", "mType", "dev_addr", "devEUI", "rxRssi", "rx_snr", "rx_channel", "rx_rf_chain", "gw", "tx_info", "rx_info", "phy_payloadJSON", "airtime", "esp", "late", "frm_payload", "FCntUp", "NFCntDown", "AFCntDown", "ConfFCnt", "sp_fact", "limit")
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    MTYPE_FIELD_NUMBER: _ClassVar[int]
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    DEVEUI_FIELD_NUMBER: _ClassVar[int]
    RXRSSI_FIELD_NUMBER: _ClassVar[int]
    RX_SNR_FIELD_NUMBER: _ClassVar[int]
    RX_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    RX_RF_CHAIN_FIELD_NUMBER: _ClassVar[int]
    GW_FIELD_NUMBER: _ClassVar[int]
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    RX_INFO_FIELD_NUMBER: _ClassVar[int]
    PHY_PAYLOADJSON_FIELD_NUMBER: _ClassVar[int]
    AIRTIME_FIELD_NUMBER: _ClassVar[int]
    ESP_FIELD_NUMBER: _ClassVar[int]
    LATE_FIELD_NUMBER: _ClassVar[int]
    FRM_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    FCNTUP_FIELD_NUMBER: _ClassVar[int]
    NFCNTDOWN_FIELD_NUMBER: _ClassVar[int]
    AFCNTDOWN_FIELD_NUMBER: _ClassVar[int]
    CONFFCNT_FIELD_NUMBER: _ClassVar[int]
    SP_FACT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    direction: str
    date_time: str
    date: str
    mType: str
    dev_addr: str
    devEUI: str
    rxRssi: int
    rx_snr: float
    rx_channel: int
    rx_rf_chain: int
    gw: str
    tx_info: str
    rx_info: _containers.RepeatedCompositeFieldContainer[RXInfo]
    phy_payloadJSON: str
    airtime: float
    esp: float
    late: int
    frm_payload: str
    FCntUp: int
    NFCntDown: int
    AFCntDown: int
    ConfFCnt: int
    sp_fact: int
    limit: str
    def __init__(self, direction: _Optional[str] = ..., date_time: _Optional[str] = ..., date: _Optional[str] = ..., mType: _Optional[str] = ..., dev_addr: _Optional[str] = ..., devEUI: _Optional[str] = ..., rxRssi: _Optional[int] = ..., rx_snr: _Optional[float] = ..., rx_channel: _Optional[int] = ..., rx_rf_chain: _Optional[int] = ..., gw: _Optional[str] = ..., tx_info: _Optional[str] = ..., rx_info: _Optional[_Iterable[_Union[RXInfo, _Mapping]]] = ..., phy_payloadJSON: _Optional[str] = ..., airtime: _Optional[float] = ..., esp: _Optional[float] = ..., late: _Optional[int] = ..., frm_payload: _Optional[str] = ..., FCntUp: _Optional[int] = ..., NFCntDown: _Optional[int] = ..., AFCntDown: _Optional[int] = ..., ConfFCnt: _Optional[int] = ..., sp_fact: _Optional[int] = ..., limit: _Optional[str] = ..., **kwargs) -> None: ...

class RXInfo(_message.Message):
    __slots__ = ("GatewayID", "Rssi", "LoraSnr", "Channel", "RfChain", "Board", "Antenna", "Location", "FineTimestampType", "GpsTimestamp", "FineTimestamp", "Context", "UplinkID")
    GATEWAYID_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    LORASNR_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    RFCHAIN_FIELD_NUMBER: _ClassVar[int]
    BOARD_FIELD_NUMBER: _ClassVar[int]
    ANTENNA_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    FINETIMESTAMPTYPE_FIELD_NUMBER: _ClassVar[int]
    GPSTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FINETIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    UPLINKID_FIELD_NUMBER: _ClassVar[int]
    GatewayID: str
    Rssi: int
    LoraSnr: float
    Channel: int
    RfChain: int
    Board: int
    Antenna: int
    Location: _common_pb2.Location
    FineTimestampType: _gw_pb2.FineTimestampType
    GpsTimestamp: str
    FineTimestamp: str
    Context: str
    UplinkID: str
    def __init__(self, GatewayID: _Optional[str] = ..., Rssi: _Optional[int] = ..., LoraSnr: _Optional[float] = ..., Channel: _Optional[int] = ..., RfChain: _Optional[int] = ..., Board: _Optional[int] = ..., Antenna: _Optional[int] = ..., Location: _Optional[_Union[_common_pb2.Location, _Mapping]] = ..., FineTimestampType: _Optional[_Union[_gw_pb2.FineTimestampType, str]] = ..., GpsTimestamp: _Optional[str] = ..., FineTimestamp: _Optional[str] = ..., Context: _Optional[str] = ..., UplinkID: _Optional[str] = ...) -> None: ...

class GetGwStatsRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetGwStatsResponse(_message.Message):
    __slots__ = ("radio_hour", "radio_day", "radio_month")
    RADIO_HOUR_FIELD_NUMBER: _ClassVar[int]
    RADIO_DAY_FIELD_NUMBER: _ClassVar[int]
    RADIO_MONTH_FIELD_NUMBER: _ClassVar[int]
    radio_hour: float
    radio_day: float
    radio_month: float
    def __init__(self, radio_hour: _Optional[float] = ..., radio_day: _Optional[float] = ..., radio_month: _Optional[float] = ...) -> None: ...

class CountDeviceFramesPerDevEuiRequest(_message.Message):
    __slots__ = ("organization_id", "devices", "start", "end")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    organization_id: int
    devices: _containers.RepeatedScalarFieldContainer[str]
    start: str
    end: str
    def __init__(self, organization_id: _Optional[int] = ..., devices: _Optional[_Iterable[str]] = ..., start: _Optional[str] = ..., end: _Optional[str] = ...) -> None: ...

class CountDeviceFramesPerDevEuiResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedCompositeFieldContainer[PerDeviceFramesCounters]
    def __init__(self, result: _Optional[_Iterable[_Union[PerDeviceFramesCounters, _Mapping]]] = ...) -> None: ...

class PerDeviceFramesCounters(_message.Message):
    __slots__ = ("dev_eui", "join_req_cnt", "ul_cnt", "dl_cnt")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    JOIN_REQ_CNT_FIELD_NUMBER: _ClassVar[int]
    UL_CNT_FIELD_NUMBER: _ClassVar[int]
    DL_CNT_FIELD_NUMBER: _ClassVar[int]
    dev_eui: str
    join_req_cnt: int
    ul_cnt: int
    dl_cnt: int
    def __init__(self, dev_eui: _Optional[str] = ..., join_req_cnt: _Optional[int] = ..., ul_cnt: _Optional[int] = ..., dl_cnt: _Optional[int] = ...) -> None: ...
