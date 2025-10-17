import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from common import common_pb2 as _common_pb2
from gw import gw_pb2 as _gw_pb2
from ns import profiles_pb2 as _profiles_pb2
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

class RateLimit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Unlimited: _ClassVar[RateLimit]
    Dropped: _ClassVar[RateLimit]
    Marked: _ClassVar[RateLimit]

class AggregationInterval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SECOND: _ClassVar[AggregationInterval]
    MINUTE: _ClassVar[AggregationInterval]
    HOUR: _ClassVar[AggregationInterval]
    DAY: _ClassVar[AggregationInterval]
    WEEK: _ClassVar[AggregationInterval]
    MONTH: _ClassVar[AggregationInterval]
    QUARTER: _ClassVar[AggregationInterval]
    YEAR: _ClassVar[AggregationInterval]

class MulticastGroupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLASS_C: _ClassVar[MulticastGroupType]
    CLASS_B: _ClassVar[MulticastGroupType]
RX1: RXWindow
RX2: RXWindow
Unlimited: RateLimit
Dropped: RateLimit
Marked: RateLimit
SECOND: AggregationInterval
MINUTE: AggregationInterval
HOUR: AggregationInterval
DAY: AggregationInterval
WEEK: AggregationInterval
MONTH: AggregationInterval
QUARTER: AggregationInterval
YEAR: AggregationInterval
CLASS_C: MulticastGroupType
CLASS_B: MulticastGroupType

class CreateServiceProfileRequest(_message.Message):
    __slots__ = ("service_profile",)
    SERVICE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    service_profile: _profiles_pb2.ServiceProfile
    def __init__(self, service_profile: _Optional[_Union[_profiles_pb2.ServiceProfile, _Mapping]] = ...) -> None: ...

class CreateServiceProfileResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class GetServiceProfileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class GetServiceProfileResponse(_message.Message):
    __slots__ = ("service_profile", "created_at", "updated_at")
    SERVICE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    service_profile: _profiles_pb2.ServiceProfile
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, service_profile: _Optional[_Union[_profiles_pb2.ServiceProfile, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpdateServiceProfileRequest(_message.Message):
    __slots__ = ("service_profile",)
    SERVICE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    service_profile: _profiles_pb2.ServiceProfile
    def __init__(self, service_profile: _Optional[_Union[_profiles_pb2.ServiceProfile, _Mapping]] = ...) -> None: ...

class DeleteServiceProfileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class CreateRoutingProfileRequest(_message.Message):
    __slots__ = ("routing_profile",)
    ROUTING_PROFILE_FIELD_NUMBER: _ClassVar[int]
    routing_profile: _profiles_pb2.RoutingProfile
    def __init__(self, routing_profile: _Optional[_Union[_profiles_pb2.RoutingProfile, _Mapping]] = ...) -> None: ...

class CreateRoutingProfileResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class GetRoutingProfileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class GetRoutingProfileResponse(_message.Message):
    __slots__ = ("routing_profile", "created_at", "updated_at")
    ROUTING_PROFILE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    routing_profile: _profiles_pb2.RoutingProfile
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, routing_profile: _Optional[_Union[_profiles_pb2.RoutingProfile, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpdateRoutingProfileRequest(_message.Message):
    __slots__ = ("routing_profile",)
    ROUTING_PROFILE_FIELD_NUMBER: _ClassVar[int]
    routing_profile: _profiles_pb2.RoutingProfile
    def __init__(self, routing_profile: _Optional[_Union[_profiles_pb2.RoutingProfile, _Mapping]] = ...) -> None: ...

class DeleteRoutingProfileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class CreateDeviceProfileRequest(_message.Message):
    __slots__ = ("device_profile",)
    DEVICE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    device_profile: _profiles_pb2.DeviceProfile
    def __init__(self, device_profile: _Optional[_Union[_profiles_pb2.DeviceProfile, _Mapping]] = ...) -> None: ...

class CreateDeviceProfileResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class GetDeviceProfileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class GetDeviceProfileResponse(_message.Message):
    __slots__ = ("device_profile", "created_at", "updated_at")
    DEVICE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    device_profile: _profiles_pb2.DeviceProfile
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, device_profile: _Optional[_Union[_profiles_pb2.DeviceProfile, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpdateDeviceProfileRequest(_message.Message):
    __slots__ = ("device_profile",)
    DEVICE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    device_profile: _profiles_pb2.DeviceProfile
    def __init__(self, device_profile: _Optional[_Union[_profiles_pb2.DeviceProfile, _Mapping]] = ...) -> None: ...

class DeleteDeviceProfileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class Device(_message.Message):
    __slots__ = ("dev_eui", "device_profile_id", "service_profile_id", "routing_profile_id", "skip_f_cnt_check", "reference_altitude", "is_disabled", "keep_queue")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_F_CNT_CHECK_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    IS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    KEEP_QUEUE_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    device_profile_id: bytes
    service_profile_id: bytes
    routing_profile_id: bytes
    skip_f_cnt_check: bool
    reference_altitude: float
    is_disabled: bool
    keep_queue: bool
    def __init__(self, dev_eui: _Optional[bytes] = ..., device_profile_id: _Optional[bytes] = ..., service_profile_id: _Optional[bytes] = ..., routing_profile_id: _Optional[bytes] = ..., skip_f_cnt_check: _Optional[bool] = ..., reference_altitude: _Optional[float] = ..., is_disabled: _Optional[bool] = ..., keep_queue: _Optional[bool] = ...) -> None: ...

class CreateDeviceRequest(_message.Message):
    __slots__ = ("device",)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: Device
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ...) -> None: ...

class GetDeviceRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    def __init__(self, dev_eui: _Optional[bytes] = ...) -> None: ...

class GetDeviceResponse(_message.Message):
    __slots__ = ("device", "created_at", "updated_at")
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    device: Device
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetDeviceForExportResponse(_message.Message):
    __slots__ = ("dev_eui", "supports_class_b", "supports_class_c", "MAC_version", "is_disabled", "supports_join", "nwk_s_enc_key")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_CLASS_B_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_CLASS_C_FIELD_NUMBER: _ClassVar[int]
    MAC_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_JOIN_FIELD_NUMBER: _ClassVar[int]
    NWK_S_ENC_KEY_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    supports_class_b: bool
    supports_class_c: bool
    MAC_version: str
    is_disabled: bool
    supports_join: bool
    nwk_s_enc_key: str
    def __init__(self, dev_eui: _Optional[bytes] = ..., supports_class_b: _Optional[bool] = ..., supports_class_c: _Optional[bool] = ..., MAC_version: _Optional[str] = ..., is_disabled: _Optional[bool] = ..., supports_join: _Optional[bool] = ..., nwk_s_enc_key: _Optional[str] = ...) -> None: ...

class UpdateDeviceRequest(_message.Message):
    __slots__ = ("device",)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: Device
    def __init__(self, device: _Optional[_Union[Device, _Mapping]] = ...) -> None: ...

class DeleteDeviceRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    def __init__(self, dev_eui: _Optional[bytes] = ...) -> None: ...

class DeviceActivation(_message.Message):
    __slots__ = ("dev_eui", "dev_addr", "s_nwk_s_int_key", "f_nwk_s_int_key", "nwk_s_enc_key", "f_cnt_up", "n_f_cnt_down", "a_f_cnt_down", "skip_f_cnt_check", "RX1DROffset", "RX2DR", "RX2Frequency", "TXPowerIndex", "DR", "ADR", "nb_trans", "enabled_uplink_channels", "extra_uplink_channels", "app_s_key")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    S_NWK_S_INT_KEY_FIELD_NUMBER: _ClassVar[int]
    F_NWK_S_INT_KEY_FIELD_NUMBER: _ClassVar[int]
    NWK_S_ENC_KEY_FIELD_NUMBER: _ClassVar[int]
    F_CNT_UP_FIELD_NUMBER: _ClassVar[int]
    N_F_CNT_DOWN_FIELD_NUMBER: _ClassVar[int]
    A_F_CNT_DOWN_FIELD_NUMBER: _ClassVar[int]
    SKIP_F_CNT_CHECK_FIELD_NUMBER: _ClassVar[int]
    RX1DROFFSET_FIELD_NUMBER: _ClassVar[int]
    RX2DR_FIELD_NUMBER: _ClassVar[int]
    RX2FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    TXPOWERINDEX_FIELD_NUMBER: _ClassVar[int]
    DR_FIELD_NUMBER: _ClassVar[int]
    ADR_FIELD_NUMBER: _ClassVar[int]
    NB_TRANS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_UPLINK_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_UPLINK_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    APP_S_KEY_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    dev_addr: bytes
    s_nwk_s_int_key: bytes
    f_nwk_s_int_key: bytes
    nwk_s_enc_key: bytes
    f_cnt_up: int
    n_f_cnt_down: int
    a_f_cnt_down: int
    skip_f_cnt_check: bool
    RX1DROffset: int
    RX2DR: int
    RX2Frequency: int
    TXPowerIndex: int
    DR: int
    ADR: bool
    nb_trans: int
    enabled_uplink_channels: _containers.RepeatedScalarFieldContainer[int]
    extra_uplink_channels: _containers.RepeatedCompositeFieldContainer[ExtraChannels]
    app_s_key: bytes
    def __init__(self, dev_eui: _Optional[bytes] = ..., dev_addr: _Optional[bytes] = ..., s_nwk_s_int_key: _Optional[bytes] = ..., f_nwk_s_int_key: _Optional[bytes] = ..., nwk_s_enc_key: _Optional[bytes] = ..., f_cnt_up: _Optional[int] = ..., n_f_cnt_down: _Optional[int] = ..., a_f_cnt_down: _Optional[int] = ..., skip_f_cnt_check: _Optional[bool] = ..., RX1DROffset: _Optional[int] = ..., RX2DR: _Optional[int] = ..., RX2Frequency: _Optional[int] = ..., TXPowerIndex: _Optional[int] = ..., DR: _Optional[int] = ..., ADR: _Optional[bool] = ..., nb_trans: _Optional[int] = ..., enabled_uplink_channels: _Optional[_Iterable[int]] = ..., extra_uplink_channels: _Optional[_Iterable[_Union[ExtraChannels, _Mapping]]] = ..., app_s_key: _Optional[bytes] = ...) -> None: ...

class ExtraChannels(_message.Message):
    __slots__ = ("index", "frequency", "minDR", "maxDR")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    MINDR_FIELD_NUMBER: _ClassVar[int]
    MAXDR_FIELD_NUMBER: _ClassVar[int]
    index: int
    frequency: int
    minDR: int
    maxDR: int
    def __init__(self, index: _Optional[int] = ..., frequency: _Optional[int] = ..., minDR: _Optional[int] = ..., maxDR: _Optional[int] = ...) -> None: ...

class ActivateDeviceRequest(_message.Message):
    __slots__ = ("device_activation",)
    DEVICE_ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    device_activation: DeviceActivation
    def __init__(self, device_activation: _Optional[_Union[DeviceActivation, _Mapping]] = ...) -> None: ...

class DeactivateDeviceRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    def __init__(self, dev_eui: _Optional[bytes] = ...) -> None: ...

class GetDeviceActivationRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    def __init__(self, dev_eui: _Optional[bytes] = ...) -> None: ...

class GetDeviceActivationResponse(_message.Message):
    __slots__ = ("device_activation",)
    DEVICE_ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    device_activation: DeviceActivation
    def __init__(self, device_activation: _Optional[_Union[DeviceActivation, _Mapping]] = ...) -> None: ...

class GetRandomDevAddrResponse(_message.Message):
    __slots__ = ("dev_addr",)
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    dev_addr: bytes
    def __init__(self, dev_addr: _Optional[bytes] = ...) -> None: ...

class CreateMACCommandQueueItemRequest(_message.Message):
    __slots__ = ("dev_eui", "cid", "commands")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    CID_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    cid: int
    commands: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, dev_eui: _Optional[bytes] = ..., cid: _Optional[int] = ..., commands: _Optional[_Iterable[bytes]] = ...) -> None: ...

class SendProprietaryPayloadRequest(_message.Message):
    __slots__ = ("mac_payload", "mic", "gateway_macs", "polarization_inversion", "frequency", "dr")
    MAC_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    MIC_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_MACS_FIELD_NUMBER: _ClassVar[int]
    POLARIZATION_INVERSION_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    DR_FIELD_NUMBER: _ClassVar[int]
    mac_payload: bytes
    mic: bytes
    gateway_macs: _containers.RepeatedScalarFieldContainer[bytes]
    polarization_inversion: bool
    frequency: int
    dr: int
    def __init__(self, mac_payload: _Optional[bytes] = ..., mic: _Optional[bytes] = ..., gateway_macs: _Optional[_Iterable[bytes]] = ..., polarization_inversion: _Optional[bool] = ..., frequency: _Optional[int] = ..., dr: _Optional[int] = ...) -> None: ...

class Gateway(_message.Message):
    __slots__ = ("id", "location", "gateway_profile_id", "boards", "routing_profile_id", "service_profile_id", "suspended")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    BOARDS_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    location: _common_pb2.Location
    gateway_profile_id: bytes
    boards: _containers.RepeatedCompositeFieldContainer[GatewayBoard]
    routing_profile_id: bytes
    service_profile_id: bytes
    suspended: bool
    def __init__(self, id: _Optional[bytes] = ..., location: _Optional[_Union[_common_pb2.Location, _Mapping]] = ..., gateway_profile_id: _Optional[bytes] = ..., boards: _Optional[_Iterable[_Union[GatewayBoard, _Mapping]]] = ..., routing_profile_id: _Optional[bytes] = ..., service_profile_id: _Optional[bytes] = ..., suspended: _Optional[bool] = ...) -> None: ...

class GatewayMeta(_message.Message):
    __slots__ = ("id", "routing_profile_id", "gateway_profile_id", "service_profile_id", "is_private", "suspended", "boards", "location", "first_seen_at", "last_uplink_at", "last_stats_at", "gps_seen_at", "meta_data", "stats_duration")
    class MetaDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVATE_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    BOARDS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPLINK_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_STATS_AT_FIELD_NUMBER: _ClassVar[int]
    GPS_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    STATS_DURATION_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    routing_profile_id: bytes
    gateway_profile_id: bytes
    service_profile_id: bytes
    is_private: bool
    suspended: bool
    boards: _containers.RepeatedCompositeFieldContainer[GatewayBoard]
    location: _common_pb2.Location
    first_seen_at: _timestamp_pb2.Timestamp
    last_uplink_at: _timestamp_pb2.Timestamp
    last_stats_at: _timestamp_pb2.Timestamp
    gps_seen_at: _timestamp_pb2.Timestamp
    meta_data: _containers.ScalarMap[str, str]
    stats_duration: int
    def __init__(self, id: _Optional[bytes] = ..., routing_profile_id: _Optional[bytes] = ..., gateway_profile_id: _Optional[bytes] = ..., service_profile_id: _Optional[bytes] = ..., is_private: _Optional[bool] = ..., suspended: _Optional[bool] = ..., boards: _Optional[_Iterable[_Union[GatewayBoard, _Mapping]]] = ..., location: _Optional[_Union[_common_pb2.Location, _Mapping]] = ..., first_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_uplink_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_stats_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., gps_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., meta_data: _Optional[_Mapping[str, str]] = ..., stats_duration: _Optional[int] = ...) -> None: ...

class GatewayBoard(_message.Message):
    __slots__ = ("fpga_id", "fine_timestamp_key")
    FPGA_ID_FIELD_NUMBER: _ClassVar[int]
    FINE_TIMESTAMP_KEY_FIELD_NUMBER: _ClassVar[int]
    fpga_id: bytes
    fine_timestamp_key: bytes
    def __init__(self, fpga_id: _Optional[bytes] = ..., fine_timestamp_key: _Optional[bytes] = ...) -> None: ...

class CreateGatewayRequest(_message.Message):
    __slots__ = ("gateway",)
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    gateway: Gateway
    def __init__(self, gateway: _Optional[_Union[Gateway, _Mapping]] = ...) -> None: ...

class GetGatewayRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class GetGatewayMetaResponse(_message.Message):
    __slots__ = ("gateway_meta",)
    GATEWAY_META_FIELD_NUMBER: _ClassVar[int]
    gateway_meta: GatewayMeta
    def __init__(self, gateway_meta: _Optional[_Union[GatewayMeta, _Mapping]] = ...) -> None: ...

class GetGatewayResponse(_message.Message):
    __slots__ = ("created_at", "updated_at", "gateway", "meta")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    gateway: Gateway
    meta: GatewayMeta
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., gateway: _Optional[_Union[Gateway, _Mapping]] = ..., meta: _Optional[_Union[GatewayMeta, _Mapping]] = ...) -> None: ...

class UpdateGatewayRequest(_message.Message):
    __slots__ = ("gateway",)
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    gateway: Gateway
    def __init__(self, gateway: _Optional[_Union[Gateway, _Mapping]] = ...) -> None: ...

class DeleteGatewayRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class GenerateGatewayClientCertificateRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class GenerateGatewayClientCertificateResponse(_message.Message):
    __slots__ = ("tls_cert", "tls_key", "ca_cert", "expires_at")
    TLS_CERT_FIELD_NUMBER: _ClassVar[int]
    TLS_KEY_FIELD_NUMBER: _ClassVar[int]
    CA_CERT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    tls_cert: bytes
    tls_key: bytes
    ca_cert: bytes
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, tls_cert: _Optional[bytes] = ..., tls_key: _Optional[bytes] = ..., ca_cert: _Optional[bytes] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GatewayStats(_message.Message):
    __slots__ = ("timestamp", "rx_packets_received", "rx_packets_received_ok", "tx_packets_received", "tx_packets_emitted")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RX_PACKETS_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    RX_PACKETS_RECEIVED_OK_FIELD_NUMBER: _ClassVar[int]
    TX_PACKETS_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    TX_PACKETS_EMITTED_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    rx_packets_received: int
    rx_packets_received_ok: int
    tx_packets_received: int
    tx_packets_emitted: int
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., rx_packets_received: _Optional[int] = ..., rx_packets_received_ok: _Optional[int] = ..., tx_packets_received: _Optional[int] = ..., tx_packets_emitted: _Optional[int] = ...) -> None: ...

class GetGatewayStatsRequest(_message.Message):
    __slots__ = ("gateway_id", "interval", "start_timestamp", "end_timestamp")
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    gateway_id: bytes
    interval: AggregationInterval
    start_timestamp: _timestamp_pb2.Timestamp
    end_timestamp: _timestamp_pb2.Timestamp
    def __init__(self, gateway_id: _Optional[bytes] = ..., interval: _Optional[_Union[AggregationInterval, str]] = ..., start_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetGatewayStatsResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedCompositeFieldContainer[GatewayStats]
    def __init__(self, result: _Optional[_Iterable[_Union[GatewayStats, _Mapping]]] = ...) -> None: ...

class DeviceQueueItem(_message.Message):
    __slots__ = ("dev_eui", "frm_payload", "f_cnt", "f_port", "confirmed", "dev_addr", "ttl", "message_id", "non_encr_pl", "created_at", "timeout_after")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    FRM_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    NON_ENCR_PL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_AFTER_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    frm_payload: bytes
    f_cnt: int
    f_port: int
    confirmed: bool
    dev_addr: bytes
    ttl: int
    message_id: str
    non_encr_pl: bytes
    created_at: _timestamp_pb2.Timestamp
    timeout_after: _timestamp_pb2.Timestamp
    def __init__(self, dev_eui: _Optional[bytes] = ..., frm_payload: _Optional[bytes] = ..., f_cnt: _Optional[int] = ..., f_port: _Optional[int] = ..., confirmed: _Optional[bool] = ..., dev_addr: _Optional[bytes] = ..., ttl: _Optional[int] = ..., message_id: _Optional[str] = ..., non_encr_pl: _Optional[bytes] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., timeout_after: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateDeviceQueueItemRequest(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: DeviceQueueItem
    def __init__(self, item: _Optional[_Union[DeviceQueueItem, _Mapping]] = ...) -> None: ...

class FlushDeviceQueueForDevEUIRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    def __init__(self, dev_eui: _Optional[bytes] = ...) -> None: ...

class GetDeviceQueueItemsForDevEUIRequest(_message.Message):
    __slots__ = ("dev_eui", "count_only")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    COUNT_ONLY_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    count_only: bool
    def __init__(self, dev_eui: _Optional[bytes] = ..., count_only: _Optional[bool] = ...) -> None: ...

class GetDeviceQueueItemsForDevEUIResponse(_message.Message):
    __slots__ = ("items", "total_count")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DeviceQueueItem]
    total_count: int
    def __init__(self, items: _Optional[_Iterable[_Union[DeviceQueueItem, _Mapping]]] = ..., total_count: _Optional[int] = ...) -> None: ...

class GetNextDownlinkFCntForDevEUIRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    def __init__(self, dev_eui: _Optional[bytes] = ...) -> None: ...

class GetNextDownlinkFCntForDevEUIResponse(_message.Message):
    __slots__ = ("f_cnt",)
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    f_cnt: int
    def __init__(self, f_cnt: _Optional[int] = ...) -> None: ...

class FCntInResponse(_message.Message):
    __slots__ = ("f_cnt",)
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    f_cnt: int
    def __init__(self, f_cnt: _Optional[int] = ...) -> None: ...

class UplinkFrameLog(_message.Message):
    __slots__ = ("phy_payload", "tx_info", "rx_info", "m_type", "dev_addr", "dev_eui", "published_at")
    PHY_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    RX_INFO_FIELD_NUMBER: _ClassVar[int]
    M_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    phy_payload: bytes
    tx_info: _gw_pb2.UplinkTXInfo
    rx_info: _containers.RepeatedCompositeFieldContainer[_gw_pb2.UplinkRXInfo]
    m_type: _common_pb2.MType
    dev_addr: bytes
    dev_eui: bytes
    published_at: _timestamp_pb2.Timestamp
    def __init__(self, phy_payload: _Optional[bytes] = ..., tx_info: _Optional[_Union[_gw_pb2.UplinkTXInfo, _Mapping]] = ..., rx_info: _Optional[_Iterable[_Union[_gw_pb2.UplinkRXInfo, _Mapping]]] = ..., m_type: _Optional[_Union[_common_pb2.MType, str]] = ..., dev_addr: _Optional[bytes] = ..., dev_eui: _Optional[bytes] = ..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DownlinkFrameLog(_message.Message):
    __slots__ = ("phy_payload", "tx_info", "token", "downlink_id", "gateway_id", "m_type", "dev_addr", "dev_eui", "published_at", "limit", "frm_payload")
    PHY_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_ID_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    M_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    FRM_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    phy_payload: bytes
    tx_info: _gw_pb2.DownlinkTXInfo
    token: int
    downlink_id: bytes
    gateway_id: bytes
    m_type: _common_pb2.MType
    dev_addr: bytes
    dev_eui: bytes
    published_at: _timestamp_pb2.Timestamp
    limit: RateLimit
    frm_payload: bytes
    def __init__(self, phy_payload: _Optional[bytes] = ..., tx_info: _Optional[_Union[_gw_pb2.DownlinkTXInfo, _Mapping]] = ..., token: _Optional[int] = ..., downlink_id: _Optional[bytes] = ..., gateway_id: _Optional[bytes] = ..., m_type: _Optional[_Union[_common_pb2.MType, str]] = ..., dev_addr: _Optional[bytes] = ..., dev_eui: _Optional[bytes] = ..., published_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., limit: _Optional[_Union[RateLimit, str]] = ..., frm_payload: _Optional[bytes] = ...) -> None: ...

class DeviceActivationContext(_message.Message):
    __slots__ = ("dev_addr", "app_s_key")
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    APP_S_KEY_FIELD_NUMBER: _ClassVar[int]
    dev_addr: bytes
    app_s_key: _common_pb2.KeyEnvelope
    def __init__(self, dev_addr: _Optional[bytes] = ..., app_s_key: _Optional[_Union[_common_pb2.KeyEnvelope, _Mapping]] = ...) -> None: ...

class StreamUplink(_message.Message):
    __slots__ = ("dev_eui", "join_eui", "f_cnt", "f_port", "adr", "dr", "tx_info", "rx_info", "data", "device_activation_context", "confirmed_uplink", "late", "mic", "time", "limit", "per", "snr", "rssi", "phy_payload", "device_session", "ctx_id", "unencrypted_data", "orgid", "gw_orgid", "dev_addr")
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
    PHY_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SESSION_FIELD_NUMBER: _ClassVar[int]
    CTX_ID_FIELD_NUMBER: _ClassVar[int]
    UNENCRYPTED_DATA_FIELD_NUMBER: _ClassVar[int]
    ORGID_FIELD_NUMBER: _ClassVar[int]
    GW_ORGID_FIELD_NUMBER: _ClassVar[int]
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
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
    limit: RateLimit
    per: float
    snr: float
    rssi: float
    phy_payload: bytes
    device_session: DeviceSession
    ctx_id: str
    unencrypted_data: bytes
    orgid: int
    gw_orgid: int
    dev_addr: bytes
    def __init__(self, dev_eui: _Optional[bytes] = ..., join_eui: _Optional[bytes] = ..., f_cnt: _Optional[int] = ..., f_port: _Optional[int] = ..., adr: _Optional[bool] = ..., dr: _Optional[int] = ..., tx_info: _Optional[_Union[_gw_pb2.UplinkTXInfo, _Mapping]] = ..., rx_info: _Optional[_Iterable[_Union[_gw_pb2.UplinkRXInfo, _Mapping]]] = ..., data: _Optional[bytes] = ..., device_activation_context: _Optional[_Union[DeviceActivationContext, _Mapping]] = ..., confirmed_uplink: _Optional[bool] = ..., late: _Optional[bool] = ..., mic: _Optional[bytes] = ..., time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., limit: _Optional[_Union[RateLimit, str]] = ..., per: _Optional[float] = ..., snr: _Optional[float] = ..., rssi: _Optional[float] = ..., phy_payload: _Optional[bytes] = ..., device_session: _Optional[_Union[DeviceSession, _Mapping]] = ..., ctx_id: _Optional[str] = ..., unencrypted_data: _Optional[bytes] = ..., orgid: _Optional[int] = ..., gw_orgid: _Optional[int] = ..., dev_addr: _Optional[bytes] = ..., **kwargs) -> None: ...

class StreamDownlink(_message.Message):
    __slots__ = ("phy_payload", "tx_info", "downlink_id", "gateway_id", "device_session", "limit", "frm_payload", "encrypted")
    PHY_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_ID_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SESSION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    FRM_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    phy_payload: bytes
    tx_info: _gw_pb2.DownlinkTXInfo
    downlink_id: bytes
    gateway_id: bytes
    device_session: DeviceSession
    limit: RateLimit
    frm_payload: bytes
    encrypted: bool
    def __init__(self, phy_payload: _Optional[bytes] = ..., tx_info: _Optional[_Union[_gw_pb2.DownlinkTXInfo, _Mapping]] = ..., downlink_id: _Optional[bytes] = ..., gateway_id: _Optional[bytes] = ..., device_session: _Optional[_Union[DeviceSession, _Mapping]] = ..., limit: _Optional[_Union[RateLimit, str]] = ..., frm_payload: _Optional[bytes] = ..., encrypted: _Optional[bool] = ...) -> None: ...

class RXFrameForHandyRusty(_message.Message):
    __slots__ = ("phy_payload", "tx_info", "rx_info", "late", "device_session", "ctx_id", "limit")
    PHY_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    RX_INFO_FIELD_NUMBER: _ClassVar[int]
    LATE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SESSION_FIELD_NUMBER: _ClassVar[int]
    CTX_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    phy_payload: bytes
    tx_info: _gw_pb2.UplinkTXInfo
    rx_info: _containers.RepeatedCompositeFieldContainer[_gw_pb2.UplinkRXInfo]
    late: bool
    device_session: DeviceSession
    ctx_id: str
    limit: RateLimit
    def __init__(self, phy_payload: _Optional[bytes] = ..., tx_info: _Optional[_Union[_gw_pb2.UplinkTXInfo, _Mapping]] = ..., rx_info: _Optional[_Iterable[_Union[_gw_pb2.UplinkRXInfo, _Mapping]]] = ..., late: _Optional[bool] = ..., device_session: _Optional[_Union[DeviceSession, _Mapping]] = ..., ctx_id: _Optional[str] = ..., limit: _Optional[_Union[RateLimit, str]] = ..., **kwargs) -> None: ...

class TXFrameForHandyRusty(_message.Message):
    __slots__ = ("phy_payload", "tx_info", "token", "downlink_id", "gateway_id", "device_session", "limit", "frm_payload")
    PHY_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_ID_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SESSION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    FRM_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    phy_payload: bytes
    tx_info: _gw_pb2.DownlinkTXInfo
    token: int
    downlink_id: bytes
    gateway_id: bytes
    device_session: DeviceSession
    limit: RateLimit
    frm_payload: bytes
    def __init__(self, phy_payload: _Optional[bytes] = ..., tx_info: _Optional[_Union[_gw_pb2.DownlinkTXInfo, _Mapping]] = ..., token: _Optional[int] = ..., downlink_id: _Optional[bytes] = ..., gateway_id: _Optional[bytes] = ..., device_session: _Optional[_Union[DeviceSession, _Mapping]] = ..., limit: _Optional[_Union[RateLimit, str]] = ..., frm_payload: _Optional[bytes] = ...) -> None: ...

class DeviceSession(_message.Message):
    __slots__ = ("FCntUp", "NFCntDown", "AFCntDown", "ConfFCnt", "KEK_label", "AES_key", "per")
    FCNTUP_FIELD_NUMBER: _ClassVar[int]
    NFCNTDOWN_FIELD_NUMBER: _ClassVar[int]
    AFCNTDOWN_FIELD_NUMBER: _ClassVar[int]
    CONFFCNT_FIELD_NUMBER: _ClassVar[int]
    KEK_LABEL_FIELD_NUMBER: _ClassVar[int]
    AES_KEY_FIELD_NUMBER: _ClassVar[int]
    PER_FIELD_NUMBER: _ClassVar[int]
    FCntUp: int
    NFCntDown: int
    AFCntDown: int
    ConfFCnt: int
    KEK_label: str
    AES_key: bytes
    per: float
    def __init__(self, FCntUp: _Optional[int] = ..., NFCntDown: _Optional[int] = ..., AFCntDown: _Optional[int] = ..., ConfFCnt: _Optional[int] = ..., KEK_label: _Optional[str] = ..., AES_key: _Optional[bytes] = ..., per: _Optional[float] = ...) -> None: ...

class StreamFrameLogsForGatewayRequest(_message.Message):
    __slots__ = ("gateway_id",)
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    gateway_id: bytes
    def __init__(self, gateway_id: _Optional[bytes] = ...) -> None: ...

class StreamFrameLogsForGatewayResponse(_message.Message):
    __slots__ = ("uplink_frame_set", "downlink_frame")
    UPLINK_FRAME_SET_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_FRAME_FIELD_NUMBER: _ClassVar[int]
    uplink_frame_set: UplinkFrameLog
    downlink_frame: DownlinkFrameLog
    def __init__(self, uplink_frame_set: _Optional[_Union[UplinkFrameLog, _Mapping]] = ..., downlink_frame: _Optional[_Union[DownlinkFrameLog, _Mapping]] = ...) -> None: ...

class StreamFrameLogsForDeviceRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    def __init__(self, dev_eui: _Optional[bytes] = ...) -> None: ...

class StreamFrameLogsForDeviceResponse(_message.Message):
    __slots__ = ("uplink_frame_set", "downlink_frame")
    UPLINK_FRAME_SET_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_FRAME_FIELD_NUMBER: _ClassVar[int]
    uplink_frame_set: UplinkFrameLog
    downlink_frame: DownlinkFrameLog
    def __init__(self, uplink_frame_set: _Optional[_Union[UplinkFrameLog, _Mapping]] = ..., downlink_frame: _Optional[_Union[DownlinkFrameLog, _Mapping]] = ...) -> None: ...

class GetVersionResponse(_message.Message):
    __slots__ = ("version", "region")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    version: str
    region: _common_pb2.Region
    def __init__(self, version: _Optional[str] = ..., region: _Optional[_Union[_common_pb2.Region, str]] = ...) -> None: ...

class GatewayProfile(_message.Message):
    __slots__ = ("id", "channels", "extra_channels", "stats_interval", "downlink_tx_power")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    STATS_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_TX_POWER_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    channels: _containers.RepeatedScalarFieldContainer[int]
    extra_channels: _containers.RepeatedCompositeFieldContainer[GatewayProfileExtraChannel]
    stats_interval: _duration_pb2.Duration
    downlink_tx_power: int
    def __init__(self, id: _Optional[bytes] = ..., channels: _Optional[_Iterable[int]] = ..., extra_channels: _Optional[_Iterable[_Union[GatewayProfileExtraChannel, _Mapping]]] = ..., stats_interval: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., downlink_tx_power: _Optional[int] = ...) -> None: ...

class GatewayProfileExtraChannel(_message.Message):
    __slots__ = ("modulation", "frequency", "bandwidth", "bitrate", "spreading_factors")
    MODULATION_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    BITRATE_FIELD_NUMBER: _ClassVar[int]
    SPREADING_FACTORS_FIELD_NUMBER: _ClassVar[int]
    modulation: _common_pb2.Modulation
    frequency: int
    bandwidth: int
    bitrate: int
    spreading_factors: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, modulation: _Optional[_Union[_common_pb2.Modulation, str]] = ..., frequency: _Optional[int] = ..., bandwidth: _Optional[int] = ..., bitrate: _Optional[int] = ..., spreading_factors: _Optional[_Iterable[int]] = ...) -> None: ...

class CreateGatewayProfileRequest(_message.Message):
    __slots__ = ("gateway_profile",)
    GATEWAY_PROFILE_FIELD_NUMBER: _ClassVar[int]
    gateway_profile: GatewayProfile
    def __init__(self, gateway_profile: _Optional[_Union[GatewayProfile, _Mapping]] = ...) -> None: ...

class CreateGatewayProfileResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class GetGatewayProfileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class GetGatewayProfileResponse(_message.Message):
    __slots__ = ("gateway_profile", "created_at", "updated_at")
    GATEWAY_PROFILE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    gateway_profile: GatewayProfile
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, gateway_profile: _Optional[_Union[GatewayProfile, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpdateGatewayProfileRequest(_message.Message):
    __slots__ = ("gateway_profile",)
    GATEWAY_PROFILE_FIELD_NUMBER: _ClassVar[int]
    gateway_profile: GatewayProfile
    def __init__(self, gateway_profile: _Optional[_Union[GatewayProfile, _Mapping]] = ...) -> None: ...

class DeleteGatewayProfileRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class MulticastGroup(_message.Message):
    __slots__ = ("id", "mc_addr", "mc_nwk_s_key", "f_cnt", "group_type", "dr", "frequency", "ping_slot_period", "service_profile_id", "routing_profile_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    MC_ADDR_FIELD_NUMBER: _ClassVar[int]
    MC_NWK_S_KEY_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    DR_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    PING_SLOT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    mc_addr: bytes
    mc_nwk_s_key: bytes
    f_cnt: int
    group_type: MulticastGroupType
    dr: int
    frequency: int
    ping_slot_period: int
    service_profile_id: bytes
    routing_profile_id: bytes
    def __init__(self, id: _Optional[bytes] = ..., mc_addr: _Optional[bytes] = ..., mc_nwk_s_key: _Optional[bytes] = ..., f_cnt: _Optional[int] = ..., group_type: _Optional[_Union[MulticastGroupType, str]] = ..., dr: _Optional[int] = ..., frequency: _Optional[int] = ..., ping_slot_period: _Optional[int] = ..., service_profile_id: _Optional[bytes] = ..., routing_profile_id: _Optional[bytes] = ...) -> None: ...

class CreateMulticastGroupRequest(_message.Message):
    __slots__ = ("multicast_group",)
    MULTICAST_GROUP_FIELD_NUMBER: _ClassVar[int]
    multicast_group: MulticastGroup
    def __init__(self, multicast_group: _Optional[_Union[MulticastGroup, _Mapping]] = ...) -> None: ...

class CreateMulticastGroupResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class GetMulticastGroupRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class GetMulticastGroupResponse(_message.Message):
    __slots__ = ("multicast_group", "created_at", "updated_at")
    MULTICAST_GROUP_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    multicast_group: MulticastGroup
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, multicast_group: _Optional[_Union[MulticastGroup, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpdateMulticastGroupRequest(_message.Message):
    __slots__ = ("multicast_group",)
    MULTICAST_GROUP_FIELD_NUMBER: _ClassVar[int]
    multicast_group: MulticastGroup
    def __init__(self, multicast_group: _Optional[_Union[MulticastGroup, _Mapping]] = ...) -> None: ...

class DeleteMulticastGroupRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class AddDeviceToMulticastGroupRequest(_message.Message):
    __slots__ = ("dev_eui", "multicast_group_id")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    MULTICAST_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    multicast_group_id: bytes
    def __init__(self, dev_eui: _Optional[bytes] = ..., multicast_group_id: _Optional[bytes] = ...) -> None: ...

class RemoveDeviceFromMulticastGroupRequest(_message.Message):
    __slots__ = ("dev_eui", "multicast_group_id")
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    MULTICAST_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    multicast_group_id: bytes
    def __init__(self, dev_eui: _Optional[bytes] = ..., multicast_group_id: _Optional[bytes] = ...) -> None: ...

class MulticastQueueItem(_message.Message):
    __slots__ = ("multicast_group_id", "f_cnt", "f_port", "frm_payload")
    MULTICAST_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    FRM_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    multicast_group_id: bytes
    f_cnt: int
    f_port: int
    frm_payload: bytes
    def __init__(self, multicast_group_id: _Optional[bytes] = ..., f_cnt: _Optional[int] = ..., f_port: _Optional[int] = ..., frm_payload: _Optional[bytes] = ...) -> None: ...

class EnqueueMulticastQueueItemRequest(_message.Message):
    __slots__ = ("multicast_queue_item",)
    MULTICAST_QUEUE_ITEM_FIELD_NUMBER: _ClassVar[int]
    multicast_queue_item: MulticastQueueItem
    def __init__(self, multicast_queue_item: _Optional[_Union[MulticastQueueItem, _Mapping]] = ...) -> None: ...

class FlushMulticastQueueForMulticastGroupRequest(_message.Message):
    __slots__ = ("multicast_group_id",)
    MULTICAST_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    multicast_group_id: bytes
    def __init__(self, multicast_group_id: _Optional[bytes] = ...) -> None: ...

class GetMulticastQueueItemsForMulticastGroupRequest(_message.Message):
    __slots__ = ("multicast_group_id",)
    MULTICAST_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    multicast_group_id: bytes
    def __init__(self, multicast_group_id: _Optional[bytes] = ...) -> None: ...

class GetMulticastQueueItemsForMulticastGroupResponse(_message.Message):
    __slots__ = ("multicast_queue_items",)
    MULTICAST_QUEUE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    multicast_queue_items: _containers.RepeatedCompositeFieldContainer[MulticastQueueItem]
    def __init__(self, multicast_queue_items: _Optional[_Iterable[_Union[MulticastQueueItem, _Mapping]]] = ...) -> None: ...

class GetADRAlgorithmsResponse(_message.Message):
    __slots__ = ("adr_algorithms",)
    ADR_ALGORITHMS_FIELD_NUMBER: _ClassVar[int]
    adr_algorithms: _containers.RepeatedCompositeFieldContainer[ADRAlgorithm]
    def __init__(self, adr_algorithms: _Optional[_Iterable[_Union[ADRAlgorithm, _Mapping]]] = ...) -> None: ...

class ADRAlgorithm(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ClearDeviceNoncesRequest(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    def __init__(self, dev_eui: _Optional[bytes] = ...) -> None: ...

class CountGatewaysResponse(_message.Message):
    __slots__ = ("data",)
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.ScalarMap[str, int]
    def __init__(self, data: _Optional[_Mapping[str, int]] = ...) -> None: ...
