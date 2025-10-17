import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from common import common_pb2 as _common_pb2
import importlib
_frameLog_pb2 = importlib.import_module('as.external.api.frameLog_pb2')
from handyrusty import hr_pb2 as _hr_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Gateway(_message.Message):
    __slots__ = ("id", "name", "description", "location", "organization_id", "discovery_enabled", "network_server_id", "gateway_profile_id", "boards", "tags", "metadata", "address", "serno", "active", "phone", "op_status_code", "op_status_label", "network_server_name")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    BOARDS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SERNO_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    OP_STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    OP_STATUS_LABEL_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    location: _common_pb2.Location
    organization_id: int
    discovery_enabled: bool
    network_server_id: int
    gateway_profile_id: str
    boards: _containers.RepeatedCompositeFieldContainer[GatewayBoard]
    tags: _containers.ScalarMap[str, str]
    metadata: _containers.ScalarMap[str, str]
    address: str
    serno: str
    active: bool
    phone: str
    op_status_code: int
    op_status_label: str
    network_server_name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., location: _Optional[_Union[_common_pb2.Location, _Mapping]] = ..., organization_id: _Optional[int] = ..., discovery_enabled: _Optional[bool] = ..., network_server_id: _Optional[int] = ..., gateway_profile_id: _Optional[str] = ..., boards: _Optional[_Iterable[_Union[GatewayBoard, _Mapping]]] = ..., tags: _Optional[_Mapping[str, str]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., address: _Optional[str] = ..., serno: _Optional[str] = ..., active: _Optional[bool] = ..., phone: _Optional[str] = ..., op_status_code: _Optional[int] = ..., op_status_label: _Optional[str] = ..., network_server_name: _Optional[str] = ...) -> None: ...

class GatewayBoard(_message.Message):
    __slots__ = ("fpga_id", "fine_timestamp_key")
    FPGA_ID_FIELD_NUMBER: _ClassVar[int]
    FINE_TIMESTAMP_KEY_FIELD_NUMBER: _ClassVar[int]
    fpga_id: str
    fine_timestamp_key: str
    def __init__(self, fpga_id: _Optional[str] = ..., fine_timestamp_key: _Optional[str] = ...) -> None: ...

class CreateGatewayRequest(_message.Message):
    __slots__ = ("gateway",)
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    gateway: Gateway
    def __init__(self, gateway: _Optional[_Union[Gateway, _Mapping]] = ...) -> None: ...

class GetGatewayRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetGatewayResponse(_message.Message):
    __slots__ = ("gateway", "created_at", "updated_at", "first_seen_at", "last_seen_at", "GPS_seen_at")
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    GPS_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    gateway: Gateway
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    first_seen_at: _timestamp_pb2.Timestamp
    last_seen_at: _timestamp_pb2.Timestamp
    GPS_seen_at: _timestamp_pb2.Timestamp
    def __init__(self, gateway: _Optional[_Union[Gateway, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., first_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., GPS_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetGatewayStatusResponse(_message.Message):
    __slots__ = ("id", "active", "last_seen_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    active: bool
    last_seen_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., active: _Optional[bool] = ..., last_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DeleteGatewayRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GenerateGatewayClientCertificateRequest(_message.Message):
    __slots__ = ("gateway_id",)
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    gateway_id: str
    def __init__(self, gateway_id: _Optional[str] = ...) -> None: ...

class GenerateGatewayClientCertificateResponse(_message.Message):
    __slots__ = ("tls_cert", "tls_key", "ca_cert", "expires_at")
    TLS_CERT_FIELD_NUMBER: _ClassVar[int]
    TLS_KEY_FIELD_NUMBER: _ClassVar[int]
    CA_CERT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    tls_cert: str
    tls_key: str
    ca_cert: str
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, tls_cert: _Optional[str] = ..., tls_key: _Optional[str] = ..., ca_cert: _Optional[str] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListGatewayRequest(_message.Message):
    __slots__ = ("limit", "offset", "organization_id", "search", "orderBy", "order")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    ORDERBY_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    organization_id: int
    search: str
    orderBy: str
    order: str
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., organization_id: _Optional[int] = ..., search: _Optional[str] = ..., orderBy: _Optional[str] = ..., order: _Optional[str] = ...) -> None: ...

class GatewayListItem(_message.Message):
    __slots__ = ("id", "name", "description", "created_at", "updated_at", "first_seen_at", "last_seen_at", "organization_id", "network_server_id", "location", "network_server_name", "radio", "active", "op_status_label", "op_status_code", "gateway_profile_id", "gateway_profile_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    RADIO_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OP_STATUS_LABEL_FIELD_NUMBER: _ClassVar[int]
    OP_STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    first_seen_at: _timestamp_pb2.Timestamp
    last_seen_at: _timestamp_pb2.Timestamp
    organization_id: int
    network_server_id: int
    location: _common_pb2.Location
    network_server_name: str
    radio: str
    active: bool
    op_status_label: str
    op_status_code: int
    gateway_profile_id: str
    gateway_profile_name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., first_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., organization_id: _Optional[int] = ..., network_server_id: _Optional[int] = ..., location: _Optional[_Union[_common_pb2.Location, _Mapping]] = ..., network_server_name: _Optional[str] = ..., radio: _Optional[str] = ..., active: _Optional[bool] = ..., op_status_label: _Optional[str] = ..., op_status_code: _Optional[int] = ..., gateway_profile_id: _Optional[str] = ..., gateway_profile_name: _Optional[str] = ...) -> None: ...

class GatewayMonItem(_message.Message):
    __slots__ = ("id", "name", "last_seen_at", "radio", "cpu", "ram", "disk", "uptime", "ntp_status", "active", "op_status_label", "rx_count", "tx_count", "disk1", "disk1_name", "disk2", "disk2_name", "lte_type", "lte_level")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    RADIO_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    RAM_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    NTP_STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OP_STATUS_LABEL_FIELD_NUMBER: _ClassVar[int]
    RX_COUNT_FIELD_NUMBER: _ClassVar[int]
    TX_COUNT_FIELD_NUMBER: _ClassVar[int]
    DISK1_FIELD_NUMBER: _ClassVar[int]
    DISK1_NAME_FIELD_NUMBER: _ClassVar[int]
    DISK2_FIELD_NUMBER: _ClassVar[int]
    DISK2_NAME_FIELD_NUMBER: _ClassVar[int]
    LTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LTE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    last_seen_at: _timestamp_pb2.Timestamp
    radio: str
    cpu: str
    ram: str
    disk: str
    uptime: str
    ntp_status: str
    active: bool
    op_status_label: str
    rx_count: int
    tx_count: int
    disk1: str
    disk1_name: str
    disk2: str
    disk2_name: str
    lte_type: str
    lte_level: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., last_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., radio: _Optional[str] = ..., cpu: _Optional[str] = ..., ram: _Optional[str] = ..., disk: _Optional[str] = ..., uptime: _Optional[str] = ..., ntp_status: _Optional[str] = ..., active: _Optional[bool] = ..., op_status_label: _Optional[str] = ..., rx_count: _Optional[int] = ..., tx_count: _Optional[int] = ..., disk1: _Optional[str] = ..., disk1_name: _Optional[str] = ..., disk2: _Optional[str] = ..., disk2_name: _Optional[str] = ..., lte_type: _Optional[str] = ..., lte_level: _Optional[str] = ...) -> None: ...

class ListGatewayResponse(_message.Message):
    __slots__ = ("total_count", "result")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    result: _containers.RepeatedCompositeFieldContainer[GatewayListItem]
    def __init__(self, total_count: _Optional[int] = ..., result: _Optional[_Iterable[_Union[GatewayListItem, _Mapping]]] = ...) -> None: ...

class ListMonResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedCompositeFieldContainer[GatewayMonItem]
    def __init__(self, result: _Optional[_Iterable[_Union[GatewayMonItem, _Mapping]]] = ...) -> None: ...

class UpdateGatewayRequest(_message.Message):
    __slots__ = ("gateway",)
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    gateway: Gateway
    def __init__(self, gateway: _Optional[_Union[Gateway, _Mapping]] = ...) -> None: ...

class GatewayStats(_message.Message):
    __slots__ = ("timestamp", "rx_packets_received", "rx_packets_received_ok", "tx_packets_received", "tx_packets_emitted", "tx_packets_per_frequency", "rx_packets_per_frequency", "tx_packets_per_dr", "rx_packets_per_dr", "tx_packets_per_status")
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
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RX_PACKETS_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    RX_PACKETS_RECEIVED_OK_FIELD_NUMBER: _ClassVar[int]
    TX_PACKETS_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    TX_PACKETS_EMITTED_FIELD_NUMBER: _ClassVar[int]
    TX_PACKETS_PER_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    RX_PACKETS_PER_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    TX_PACKETS_PER_DR_FIELD_NUMBER: _ClassVar[int]
    RX_PACKETS_PER_DR_FIELD_NUMBER: _ClassVar[int]
    TX_PACKETS_PER_STATUS_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    rx_packets_received: int
    rx_packets_received_ok: int
    tx_packets_received: int
    tx_packets_emitted: int
    tx_packets_per_frequency: _containers.ScalarMap[int, int]
    rx_packets_per_frequency: _containers.ScalarMap[int, int]
    tx_packets_per_dr: _containers.ScalarMap[int, int]
    rx_packets_per_dr: _containers.ScalarMap[int, int]
    tx_packets_per_status: _containers.ScalarMap[str, int]
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., rx_packets_received: _Optional[int] = ..., rx_packets_received_ok: _Optional[int] = ..., tx_packets_received: _Optional[int] = ..., tx_packets_emitted: _Optional[int] = ..., tx_packets_per_frequency: _Optional[_Mapping[int, int]] = ..., rx_packets_per_frequency: _Optional[_Mapping[int, int]] = ..., tx_packets_per_dr: _Optional[_Mapping[int, int]] = ..., rx_packets_per_dr: _Optional[_Mapping[int, int]] = ..., tx_packets_per_status: _Optional[_Mapping[str, int]] = ...) -> None: ...

class GetGatewayStatsRequest(_message.Message):
    __slots__ = ("gateway_id", "interval", "start_timestamp", "end_timestamp")
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    gateway_id: str
    interval: str
    start_timestamp: _timestamp_pb2.Timestamp
    end_timestamp: _timestamp_pb2.Timestamp
    def __init__(self, gateway_id: _Optional[str] = ..., interval: _Optional[str] = ..., start_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetGatewayStatsResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedCompositeFieldContainer[GatewayStats]
    def __init__(self, result: _Optional[_Iterable[_Union[GatewayStats, _Mapping]]] = ...) -> None: ...

class PingRX(_message.Message):
    __slots__ = ("gateway_id", "rssi", "lora_snr", "latitude", "longitude", "altitude")
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    LORA_SNR_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    gateway_id: str
    rssi: int
    lora_snr: float
    latitude: float
    longitude: float
    altitude: float
    def __init__(self, gateway_id: _Optional[str] = ..., rssi: _Optional[int] = ..., lora_snr: _Optional[float] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[float] = ...) -> None: ...

class GetLastPingRequest(_message.Message):
    __slots__ = ("gateway_id",)
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    gateway_id: str
    def __init__(self, gateway_id: _Optional[str] = ...) -> None: ...

class GetLastPingResponse(_message.Message):
    __slots__ = ("created_at", "frequency", "dr", "ping_rx")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    DR_FIELD_NUMBER: _ClassVar[int]
    PING_RX_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    frequency: int
    dr: int
    ping_rx: _containers.RepeatedCompositeFieldContainer[PingRX]
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., frequency: _Optional[int] = ..., dr: _Optional[int] = ..., ping_rx: _Optional[_Iterable[_Union[PingRX, _Mapping]]] = ...) -> None: ...

class StreamGatewayFrameLogsRequest(_message.Message):
    __slots__ = ("gateway_id",)
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    gateway_id: str
    def __init__(self, gateway_id: _Optional[str] = ...) -> None: ...

class StreamGatewayFrameLogsResponse(_message.Message):
    __slots__ = ("uplink_frame", "downlink_frame")
    UPLINK_FRAME_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_FRAME_FIELD_NUMBER: _ClassVar[int]
    uplink_frame: _frameLog_pb2.UplinkFrameLog
    downlink_frame: _frameLog_pb2.DownlinkFrameLog
    def __init__(self, uplink_frame: _Optional[_Union[_frameLog_pb2.UplinkFrameLog, _Mapping]] = ..., downlink_frame: _Optional[_Union[_frameLog_pb2.DownlinkFrameLog, _Mapping]] = ...) -> None: ...

class GwTaskResults(_message.Message):
    __slots__ = ("id", "exec_id", "updated_at", "cmd", "stderr", "error", "description", "stdout_len", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    EXEC_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CMD_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STDOUT_LEN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    exec_id: str
    updated_at: _timestamp_pb2.Timestamp
    cmd: str
    stderr: bytes
    error: str
    description: str
    stdout_len: int
    name: str
    def __init__(self, id: _Optional[int] = ..., exec_id: _Optional[str] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., cmd: _Optional[str] = ..., stderr: _Optional[bytes] = ..., error: _Optional[str] = ..., description: _Optional[str] = ..., stdout_len: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class GetTaskResultsResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[GwTaskResults]
    def __init__(self, results: _Optional[_Iterable[_Union[GwTaskResults, _Mapping]]] = ...) -> None: ...
