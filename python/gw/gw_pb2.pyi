import datetime

from common import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DownlinkTiming(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMMEDIATELY: _ClassVar[DownlinkTiming]
    DELAY: _ClassVar[DownlinkTiming]
    GPS_EPOCH: _ClassVar[DownlinkTiming]

class FineTimestampType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[FineTimestampType]
    ENCRYPTED: _ClassVar[FineTimestampType]
    PLAIN: _ClassVar[FineTimestampType]

class CRCStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_CRC: _ClassVar[CRCStatus]
    BAD_CRC: _ClassVar[CRCStatus]
    CRC_OK: _ClassVar[CRCStatus]

class TxAckStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IGNORED: _ClassVar[TxAckStatus]
    OK: _ClassVar[TxAckStatus]
    TOO_LATE: _ClassVar[TxAckStatus]
    TOO_EARLY: _ClassVar[TxAckStatus]
    COLLISION_PACKET: _ClassVar[TxAckStatus]
    COLLISION_BEACON: _ClassVar[TxAckStatus]
    TX_FREQ: _ClassVar[TxAckStatus]
    TX_POWER: _ClassVar[TxAckStatus]
    GPS_UNLOCKED: _ClassVar[TxAckStatus]
    QUEUE_FULL: _ClassVar[TxAckStatus]
    INTERNAL_ERROR: _ClassVar[TxAckStatus]
IMMEDIATELY: DownlinkTiming
DELAY: DownlinkTiming
GPS_EPOCH: DownlinkTiming
NONE: FineTimestampType
ENCRYPTED: FineTimestampType
PLAIN: FineTimestampType
NO_CRC: CRCStatus
BAD_CRC: CRCStatus
CRC_OK: CRCStatus
IGNORED: TxAckStatus
OK: TxAckStatus
TOO_LATE: TxAckStatus
TOO_EARLY: TxAckStatus
COLLISION_PACKET: TxAckStatus
COLLISION_BEACON: TxAckStatus
TX_FREQ: TxAckStatus
TX_POWER: TxAckStatus
GPS_UNLOCKED: TxAckStatus
QUEUE_FULL: TxAckStatus
INTERNAL_ERROR: TxAckStatus

class Modulation(_message.Message):
    __slots__ = ("lora", "fsk", "lr_fhss")
    LORA_FIELD_NUMBER: _ClassVar[int]
    FSK_FIELD_NUMBER: _ClassVar[int]
    LR_FHSS_FIELD_NUMBER: _ClassVar[int]
    lora: LoRaModulationInfo
    fsk: FSKModulationInfo
    lr_fhss: LRFHSSModulationInfo
    def __init__(self, lora: _Optional[_Union[LoRaModulationInfo, _Mapping]] = ..., fsk: _Optional[_Union[FSKModulationInfo, _Mapping]] = ..., lr_fhss: _Optional[_Union[LRFHSSModulationInfo, _Mapping]] = ...) -> None: ...

class UplinkTXInfo(_message.Message):
    __slots__ = ("frequency", "modulation", "lora_modulation_info", "fsk_modulation_info", "lr_fhss_modulation_info")
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    MODULATION_FIELD_NUMBER: _ClassVar[int]
    LORA_MODULATION_INFO_FIELD_NUMBER: _ClassVar[int]
    FSK_MODULATION_INFO_FIELD_NUMBER: _ClassVar[int]
    LR_FHSS_MODULATION_INFO_FIELD_NUMBER: _ClassVar[int]
    frequency: int
    modulation: _common_pb2.Modulation
    lora_modulation_info: LoRaModulationInfo
    fsk_modulation_info: FSKModulationInfo
    lr_fhss_modulation_info: LRFHSSModulationInfo
    def __init__(self, frequency: _Optional[int] = ..., modulation: _Optional[_Union[_common_pb2.Modulation, str]] = ..., lora_modulation_info: _Optional[_Union[LoRaModulationInfo, _Mapping]] = ..., fsk_modulation_info: _Optional[_Union[FSKModulationInfo, _Mapping]] = ..., lr_fhss_modulation_info: _Optional[_Union[LRFHSSModulationInfo, _Mapping]] = ...) -> None: ...

class LoRaModulationInfo(_message.Message):
    __slots__ = ("bandwidth", "spreading_factor", "code_rate", "polarization_inversion")
    BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    SPREADING_FACTOR_FIELD_NUMBER: _ClassVar[int]
    CODE_RATE_FIELD_NUMBER: _ClassVar[int]
    POLARIZATION_INVERSION_FIELD_NUMBER: _ClassVar[int]
    bandwidth: int
    spreading_factor: int
    code_rate: str
    polarization_inversion: bool
    def __init__(self, bandwidth: _Optional[int] = ..., spreading_factor: _Optional[int] = ..., code_rate: _Optional[str] = ..., polarization_inversion: _Optional[bool] = ...) -> None: ...

class FSKModulationInfo(_message.Message):
    __slots__ = ("frequency_deviation", "datarate")
    FREQUENCY_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    DATARATE_FIELD_NUMBER: _ClassVar[int]
    frequency_deviation: int
    datarate: int
    def __init__(self, frequency_deviation: _Optional[int] = ..., datarate: _Optional[int] = ...) -> None: ...

class LRFHSSModulationInfo(_message.Message):
    __slots__ = ("operating_channel_width", "code_rate", "grid_steps")
    OPERATING_CHANNEL_WIDTH_FIELD_NUMBER: _ClassVar[int]
    CODE_RATE_FIELD_NUMBER: _ClassVar[int]
    GRID_STEPS_FIELD_NUMBER: _ClassVar[int]
    operating_channel_width: int
    code_rate: str
    grid_steps: int
    def __init__(self, operating_channel_width: _Optional[int] = ..., code_rate: _Optional[str] = ..., grid_steps: _Optional[int] = ...) -> None: ...

class EncryptedFineTimestamp(_message.Message):
    __slots__ = ("aes_key_index", "encrypted_ns", "fpga_id")
    AES_KEY_INDEX_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_NS_FIELD_NUMBER: _ClassVar[int]
    FPGA_ID_FIELD_NUMBER: _ClassVar[int]
    aes_key_index: int
    encrypted_ns: bytes
    fpga_id: bytes
    def __init__(self, aes_key_index: _Optional[int] = ..., encrypted_ns: _Optional[bytes] = ..., fpga_id: _Optional[bytes] = ...) -> None: ...

class PlainFineTimestamp(_message.Message):
    __slots__ = ("time",)
    TIME_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    def __init__(self, time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GatewayStats(_message.Message):
    __slots__ = ("gateway_id", "ip", "time", "location", "config_version", "rx_packets_received", "rx_packets_received_ok", "tx_packets_received", "tx_packets_emitted", "meta_data", "stats_id", "tx_packets_per_frequency", "rx_packets_per_frequency", "tx_packets_per_modulation", "rx_packets_per_modulation", "tx_packets_per_status")
    class MetaDataEntry(_message.Message):
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
    class TxPacketsPerStatusEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VERSION_FIELD_NUMBER: _ClassVar[int]
    RX_PACKETS_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    RX_PACKETS_RECEIVED_OK_FIELD_NUMBER: _ClassVar[int]
    TX_PACKETS_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    TX_PACKETS_EMITTED_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    STATS_ID_FIELD_NUMBER: _ClassVar[int]
    TX_PACKETS_PER_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    RX_PACKETS_PER_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    TX_PACKETS_PER_MODULATION_FIELD_NUMBER: _ClassVar[int]
    RX_PACKETS_PER_MODULATION_FIELD_NUMBER: _ClassVar[int]
    TX_PACKETS_PER_STATUS_FIELD_NUMBER: _ClassVar[int]
    gateway_id: bytes
    ip: str
    time: _timestamp_pb2.Timestamp
    location: _common_pb2.Location
    config_version: str
    rx_packets_received: int
    rx_packets_received_ok: int
    tx_packets_received: int
    tx_packets_emitted: int
    meta_data: _containers.ScalarMap[str, str]
    stats_id: bytes
    tx_packets_per_frequency: _containers.ScalarMap[int, int]
    rx_packets_per_frequency: _containers.ScalarMap[int, int]
    tx_packets_per_modulation: _containers.RepeatedCompositeFieldContainer[PerModulationCount]
    rx_packets_per_modulation: _containers.RepeatedCompositeFieldContainer[PerModulationCount]
    tx_packets_per_status: _containers.ScalarMap[str, int]
    def __init__(self, gateway_id: _Optional[bytes] = ..., ip: _Optional[str] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., location: _Optional[_Union[_common_pb2.Location, _Mapping]] = ..., config_version: _Optional[str] = ..., rx_packets_received: _Optional[int] = ..., rx_packets_received_ok: _Optional[int] = ..., tx_packets_received: _Optional[int] = ..., tx_packets_emitted: _Optional[int] = ..., meta_data: _Optional[_Mapping[str, str]] = ..., stats_id: _Optional[bytes] = ..., tx_packets_per_frequency: _Optional[_Mapping[int, int]] = ..., rx_packets_per_frequency: _Optional[_Mapping[int, int]] = ..., tx_packets_per_modulation: _Optional[_Iterable[_Union[PerModulationCount, _Mapping]]] = ..., rx_packets_per_modulation: _Optional[_Iterable[_Union[PerModulationCount, _Mapping]]] = ..., tx_packets_per_status: _Optional[_Mapping[str, int]] = ...) -> None: ...

class PerModulationCount(_message.Message):
    __slots__ = ("modulation", "count")
    MODULATION_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    modulation: Modulation
    count: int
    def __init__(self, modulation: _Optional[_Union[Modulation, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class UplinkRXInfo(_message.Message):
    __slots__ = ("gateway_id", "time", "time_since_gps_epoch", "rssi", "lora_snr", "channel", "rf_chain", "board", "antenna", "location", "fine_timestamp_type", "encrypted_fine_timestamp", "plain_fine_timestamp", "context", "uplink_id", "crc_status")
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TIME_SINCE_GPS_EPOCH_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    LORA_SNR_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    RF_CHAIN_FIELD_NUMBER: _ClassVar[int]
    BOARD_FIELD_NUMBER: _ClassVar[int]
    ANTENNA_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    FINE_TIMESTAMP_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_FINE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PLAIN_FINE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    UPLINK_ID_FIELD_NUMBER: _ClassVar[int]
    CRC_STATUS_FIELD_NUMBER: _ClassVar[int]
    gateway_id: bytes
    time: _timestamp_pb2.Timestamp
    time_since_gps_epoch: _duration_pb2.Duration
    rssi: int
    lora_snr: float
    channel: int
    rf_chain: int
    board: int
    antenna: int
    location: _common_pb2.Location
    fine_timestamp_type: FineTimestampType
    encrypted_fine_timestamp: EncryptedFineTimestamp
    plain_fine_timestamp: PlainFineTimestamp
    context: bytes
    uplink_id: bytes
    crc_status: CRCStatus
    def __init__(self, gateway_id: _Optional[bytes] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., time_since_gps_epoch: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., rssi: _Optional[int] = ..., lora_snr: _Optional[float] = ..., channel: _Optional[int] = ..., rf_chain: _Optional[int] = ..., board: _Optional[int] = ..., antenna: _Optional[int] = ..., location: _Optional[_Union[_common_pb2.Location, _Mapping]] = ..., fine_timestamp_type: _Optional[_Union[FineTimestampType, str]] = ..., encrypted_fine_timestamp: _Optional[_Union[EncryptedFineTimestamp, _Mapping]] = ..., plain_fine_timestamp: _Optional[_Union[PlainFineTimestamp, _Mapping]] = ..., context: _Optional[bytes] = ..., uplink_id: _Optional[bytes] = ..., crc_status: _Optional[_Union[CRCStatus, str]] = ...) -> None: ...

class DownlinkTXInfo(_message.Message):
    __slots__ = ("gateway_id", "frequency", "power", "modulation", "lora_modulation_info", "fsk_modulation_info", "board", "antenna", "timing", "immediately_timing_info", "delay_timing_info", "gps_epoch_timing_info", "context")
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    MODULATION_FIELD_NUMBER: _ClassVar[int]
    LORA_MODULATION_INFO_FIELD_NUMBER: _ClassVar[int]
    FSK_MODULATION_INFO_FIELD_NUMBER: _ClassVar[int]
    BOARD_FIELD_NUMBER: _ClassVar[int]
    ANTENNA_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATELY_TIMING_INFO_FIELD_NUMBER: _ClassVar[int]
    DELAY_TIMING_INFO_FIELD_NUMBER: _ClassVar[int]
    GPS_EPOCH_TIMING_INFO_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    gateway_id: bytes
    frequency: int
    power: int
    modulation: _common_pb2.Modulation
    lora_modulation_info: LoRaModulationInfo
    fsk_modulation_info: FSKModulationInfo
    board: int
    antenna: int
    timing: DownlinkTiming
    immediately_timing_info: ImmediatelyTimingInfo
    delay_timing_info: DelayTimingInfo
    gps_epoch_timing_info: GPSEpochTimingInfo
    context: bytes
    def __init__(self, gateway_id: _Optional[bytes] = ..., frequency: _Optional[int] = ..., power: _Optional[int] = ..., modulation: _Optional[_Union[_common_pb2.Modulation, str]] = ..., lora_modulation_info: _Optional[_Union[LoRaModulationInfo, _Mapping]] = ..., fsk_modulation_info: _Optional[_Union[FSKModulationInfo, _Mapping]] = ..., board: _Optional[int] = ..., antenna: _Optional[int] = ..., timing: _Optional[_Union[DownlinkTiming, str]] = ..., immediately_timing_info: _Optional[_Union[ImmediatelyTimingInfo, _Mapping]] = ..., delay_timing_info: _Optional[_Union[DelayTimingInfo, _Mapping]] = ..., gps_epoch_timing_info: _Optional[_Union[GPSEpochTimingInfo, _Mapping]] = ..., context: _Optional[bytes] = ...) -> None: ...

class ImmediatelyTimingInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DelayTimingInfo(_message.Message):
    __slots__ = ("delay",)
    DELAY_FIELD_NUMBER: _ClassVar[int]
    delay: _duration_pb2.Duration
    def __init__(self, delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class GPSEpochTimingInfo(_message.Message):
    __slots__ = ("time_since_gps_epoch",)
    TIME_SINCE_GPS_EPOCH_FIELD_NUMBER: _ClassVar[int]
    time_since_gps_epoch: _duration_pb2.Duration
    def __init__(self, time_since_gps_epoch: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class UplinkFrame(_message.Message):
    __slots__ = ("phy_payload", "tx_info", "rx_info")
    PHY_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    RX_INFO_FIELD_NUMBER: _ClassVar[int]
    phy_payload: bytes
    tx_info: UplinkTXInfo
    rx_info: UplinkRXInfo
    def __init__(self, phy_payload: _Optional[bytes] = ..., tx_info: _Optional[_Union[UplinkTXInfo, _Mapping]] = ..., rx_info: _Optional[_Union[UplinkRXInfo, _Mapping]] = ...) -> None: ...

class UplinkFrameSet(_message.Message):
    __slots__ = ("phy_payload", "tx_info", "rx_info")
    PHY_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    RX_INFO_FIELD_NUMBER: _ClassVar[int]
    phy_payload: bytes
    tx_info: UplinkTXInfo
    rx_info: _containers.RepeatedCompositeFieldContainer[UplinkRXInfo]
    def __init__(self, phy_payload: _Optional[bytes] = ..., tx_info: _Optional[_Union[UplinkTXInfo, _Mapping]] = ..., rx_info: _Optional[_Iterable[_Union[UplinkRXInfo, _Mapping]]] = ...) -> None: ...

class DownlinkFrame(_message.Message):
    __slots__ = ("phy_payload", "tx_info", "token", "downlink_id", "items", "gateway_id")
    PHY_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    phy_payload: bytes
    tx_info: DownlinkTXInfo
    token: int
    downlink_id: bytes
    items: _containers.RepeatedCompositeFieldContainer[DownlinkFrameItem]
    gateway_id: bytes
    def __init__(self, phy_payload: _Optional[bytes] = ..., tx_info: _Optional[_Union[DownlinkTXInfo, _Mapping]] = ..., token: _Optional[int] = ..., downlink_id: _Optional[bytes] = ..., items: _Optional[_Iterable[_Union[DownlinkFrameItem, _Mapping]]] = ..., gateway_id: _Optional[bytes] = ...) -> None: ...

class DownlinkFrameItem(_message.Message):
    __slots__ = ("phy_payload", "tx_info")
    PHY_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    phy_payload: bytes
    tx_info: DownlinkTXInfo
    def __init__(self, phy_payload: _Optional[bytes] = ..., tx_info: _Optional[_Union[DownlinkTXInfo, _Mapping]] = ...) -> None: ...

class DownlinkTXAck(_message.Message):
    __slots__ = ("gateway_id", "token", "error", "downlink_id", "items")
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    gateway_id: bytes
    token: int
    error: str
    downlink_id: bytes
    items: _containers.RepeatedCompositeFieldContainer[DownlinkTXAckItem]
    def __init__(self, gateway_id: _Optional[bytes] = ..., token: _Optional[int] = ..., error: _Optional[str] = ..., downlink_id: _Optional[bytes] = ..., items: _Optional[_Iterable[_Union[DownlinkTXAckItem, _Mapping]]] = ...) -> None: ...

class DownlinkTXAckItem(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: TxAckStatus
    def __init__(self, status: _Optional[_Union[TxAckStatus, str]] = ...) -> None: ...

class GatewayConfiguration(_message.Message):
    __slots__ = ("gateway_id", "version", "channels", "stats_interval", "band")
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    STATS_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    BAND_FIELD_NUMBER: _ClassVar[int]
    gateway_id: bytes
    version: str
    channels: _containers.RepeatedCompositeFieldContainer[ChannelConfiguration]
    stats_interval: _duration_pb2.Duration
    band: str
    def __init__(self, gateway_id: _Optional[bytes] = ..., version: _Optional[str] = ..., channels: _Optional[_Iterable[_Union[ChannelConfiguration, _Mapping]]] = ..., stats_interval: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., band: _Optional[str] = ...) -> None: ...

class ChannelConfiguration(_message.Message):
    __slots__ = ("frequency", "modulation", "lora_modulation_config", "fsk_modulation_config", "board", "demodulator")
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    MODULATION_FIELD_NUMBER: _ClassVar[int]
    LORA_MODULATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FSK_MODULATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BOARD_FIELD_NUMBER: _ClassVar[int]
    DEMODULATOR_FIELD_NUMBER: _ClassVar[int]
    frequency: int
    modulation: _common_pb2.Modulation
    lora_modulation_config: LoRaModulationConfig
    fsk_modulation_config: FSKModulationConfig
    board: int
    demodulator: int
    def __init__(self, frequency: _Optional[int] = ..., modulation: _Optional[_Union[_common_pb2.Modulation, str]] = ..., lora_modulation_config: _Optional[_Union[LoRaModulationConfig, _Mapping]] = ..., fsk_modulation_config: _Optional[_Union[FSKModulationConfig, _Mapping]] = ..., board: _Optional[int] = ..., demodulator: _Optional[int] = ...) -> None: ...

class LoRaModulationConfig(_message.Message):
    __slots__ = ("bandwidth", "spreading_factors")
    BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    SPREADING_FACTORS_FIELD_NUMBER: _ClassVar[int]
    bandwidth: int
    spreading_factors: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, bandwidth: _Optional[int] = ..., spreading_factors: _Optional[_Iterable[int]] = ...) -> None: ...

class FSKModulationConfig(_message.Message):
    __slots__ = ("bandwidth", "bitrate")
    BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    BITRATE_FIELD_NUMBER: _ClassVar[int]
    bandwidth: int
    bitrate: int
    def __init__(self, bandwidth: _Optional[int] = ..., bitrate: _Optional[int] = ...) -> None: ...

class GatewayCommandExecRequest(_message.Message):
    __slots__ = ("gateway_id", "command", "ExecId", "stdin", "environment")
    class EnvironmentEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    EXECID_FIELD_NUMBER: _ClassVar[int]
    STDIN_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    gateway_id: bytes
    command: str
    ExecId: bytes
    stdin: bytes
    environment: _containers.ScalarMap[str, str]
    def __init__(self, gateway_id: _Optional[bytes] = ..., command: _Optional[str] = ..., ExecId: _Optional[bytes] = ..., stdin: _Optional[bytes] = ..., environment: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GatewayCommandExecResponse(_message.Message):
    __slots__ = ("gateway_id", "exec_id", "stdout", "stderr", "error", "name")
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    EXEC_ID_FIELD_NUMBER: _ClassVar[int]
    STDOUT_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    gateway_id: bytes
    exec_id: bytes
    stdout: bytes
    stderr: bytes
    error: str
    name: str
    def __init__(self, gateway_id: _Optional[bytes] = ..., exec_id: _Optional[bytes] = ..., stdout: _Optional[bytes] = ..., stderr: _Optional[bytes] = ..., error: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class RawPacketForwarderEvent(_message.Message):
    __slots__ = ("gateway_id", "raw_id", "payload")
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    RAW_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    gateway_id: bytes
    raw_id: bytes
    payload: bytes
    def __init__(self, gateway_id: _Optional[bytes] = ..., raw_id: _Optional[bytes] = ..., payload: _Optional[bytes] = ...) -> None: ...

class RawPacketForwarderCommand(_message.Message):
    __slots__ = ("gateway_id", "raw_id", "payload")
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    RAW_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    gateway_id: bytes
    raw_id: bytes
    payload: bytes
    def __init__(self, gateway_id: _Optional[bytes] = ..., raw_id: _Optional[bytes] = ..., payload: _Optional[bytes] = ...) -> None: ...

class ConnState(_message.Message):
    __slots__ = ("gateway_id", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OFFLINE: _ClassVar[ConnState.State]
        ONLINE: _ClassVar[ConnState.State]
    OFFLINE: ConnState.State
    ONLINE: ConnState.State
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    gateway_id: bytes
    state: ConnState.State
    def __init__(self, gateway_id: _Optional[bytes] = ..., state: _Optional[_Union[ConnState.State, str]] = ...) -> None: ...
