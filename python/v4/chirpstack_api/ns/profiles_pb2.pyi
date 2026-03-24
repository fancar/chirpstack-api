from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RatePolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Drop: _ClassVar[RatePolicy]
    Mark: _ClassVar[RatePolicy]

class RateUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Hour: _ClassVar[RateUnit]
    Day: _ClassVar[RateUnit]
    Week: _ClassVar[RateUnit]
    Month: _ClassVar[RateUnit]
    Year: _ClassVar[RateUnit]
Drop: RatePolicy
Mark: RatePolicy
Hour: RateUnit
Day: RateUnit
Week: RateUnit
Month: RateUnit
Year: RateUnit

class ServiceProfile(_message.Message):
    __slots__ = ("id", "ul_rate", "ul_bucket_size", "ul_rate_policy", "ul_rate_unit", "dl_rate", "dl_bucket_size", "dl_rate_policy", "dl_rate_unit", "dev_status_req_freq", "report_dev_status_battery", "report_dev_status_margin", "dr_min", "dr_max", "channel_mask", "pr_allowed", "hr_allowed", "ra_allowed", "nwk_geo_loc", "target_per", "min_gw_diversity", "gws_private", "is_disabled", "adr_algorithm_id", "min_tx_power_index", "max_tx_power_index", "max_nb_trans", "min_nb_trans", "allow_rx_confirmed", "allow_tx_unconfirmed", "allow_tx_confirmed", "dl_queue_max_size")
    ID_FIELD_NUMBER: _ClassVar[int]
    UL_RATE_FIELD_NUMBER: _ClassVar[int]
    UL_BUCKET_SIZE_FIELD_NUMBER: _ClassVar[int]
    UL_RATE_POLICY_FIELD_NUMBER: _ClassVar[int]
    UL_RATE_UNIT_FIELD_NUMBER: _ClassVar[int]
    DL_RATE_FIELD_NUMBER: _ClassVar[int]
    DL_BUCKET_SIZE_FIELD_NUMBER: _ClassVar[int]
    DL_RATE_POLICY_FIELD_NUMBER: _ClassVar[int]
    DL_RATE_UNIT_FIELD_NUMBER: _ClassVar[int]
    DEV_STATUS_REQ_FREQ_FIELD_NUMBER: _ClassVar[int]
    REPORT_DEV_STATUS_BATTERY_FIELD_NUMBER: _ClassVar[int]
    REPORT_DEV_STATUS_MARGIN_FIELD_NUMBER: _ClassVar[int]
    DR_MIN_FIELD_NUMBER: _ClassVar[int]
    DR_MAX_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_MASK_FIELD_NUMBER: _ClassVar[int]
    PR_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    HR_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    RA_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    NWK_GEO_LOC_FIELD_NUMBER: _ClassVar[int]
    TARGET_PER_FIELD_NUMBER: _ClassVar[int]
    MIN_GW_DIVERSITY_FIELD_NUMBER: _ClassVar[int]
    GWS_PRIVATE_FIELD_NUMBER: _ClassVar[int]
    IS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    ADR_ALGORITHM_ID_FIELD_NUMBER: _ClassVar[int]
    MIN_TX_POWER_INDEX_FIELD_NUMBER: _ClassVar[int]
    MAX_TX_POWER_INDEX_FIELD_NUMBER: _ClassVar[int]
    MAX_NB_TRANS_FIELD_NUMBER: _ClassVar[int]
    MIN_NB_TRANS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RX_CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_TX_UNCONFIRMED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_TX_CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    DL_QUEUE_MAX_SIZE_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    ul_rate: int
    ul_bucket_size: int
    ul_rate_policy: RatePolicy
    ul_rate_unit: RateUnit
    dl_rate: int
    dl_bucket_size: int
    dl_rate_policy: RatePolicy
    dl_rate_unit: RateUnit
    dev_status_req_freq: int
    report_dev_status_battery: bool
    report_dev_status_margin: bool
    dr_min: int
    dr_max: int
    channel_mask: bytes
    pr_allowed: bool
    hr_allowed: bool
    ra_allowed: bool
    nwk_geo_loc: bool
    target_per: int
    min_gw_diversity: int
    gws_private: bool
    is_disabled: bool
    adr_algorithm_id: str
    min_tx_power_index: int
    max_tx_power_index: int
    max_nb_trans: int
    min_nb_trans: int
    allow_rx_confirmed: bool
    allow_tx_unconfirmed: bool
    allow_tx_confirmed: bool
    dl_queue_max_size: int
    def __init__(self, id: _Optional[bytes] = ..., ul_rate: _Optional[int] = ..., ul_bucket_size: _Optional[int] = ..., ul_rate_policy: _Optional[_Union[RatePolicy, str]] = ..., ul_rate_unit: _Optional[_Union[RateUnit, str]] = ..., dl_rate: _Optional[int] = ..., dl_bucket_size: _Optional[int] = ..., dl_rate_policy: _Optional[_Union[RatePolicy, str]] = ..., dl_rate_unit: _Optional[_Union[RateUnit, str]] = ..., dev_status_req_freq: _Optional[int] = ..., report_dev_status_battery: _Optional[bool] = ..., report_dev_status_margin: _Optional[bool] = ..., dr_min: _Optional[int] = ..., dr_max: _Optional[int] = ..., channel_mask: _Optional[bytes] = ..., pr_allowed: _Optional[bool] = ..., hr_allowed: _Optional[bool] = ..., ra_allowed: _Optional[bool] = ..., nwk_geo_loc: _Optional[bool] = ..., target_per: _Optional[int] = ..., min_gw_diversity: _Optional[int] = ..., gws_private: _Optional[bool] = ..., is_disabled: _Optional[bool] = ..., adr_algorithm_id: _Optional[str] = ..., min_tx_power_index: _Optional[int] = ..., max_tx_power_index: _Optional[int] = ..., max_nb_trans: _Optional[int] = ..., min_nb_trans: _Optional[int] = ..., allow_rx_confirmed: _Optional[bool] = ..., allow_tx_unconfirmed: _Optional[bool] = ..., allow_tx_confirmed: _Optional[bool] = ..., dl_queue_max_size: _Optional[int] = ...) -> None: ...

class DeviceProfile(_message.Message):
    __slots__ = ("id", "supports_class_b", "class_b_timeout", "ping_slot_period", "ping_slot_dr", "ping_slot_freq", "supports_class_c", "class_c_timeout", "mac_version", "reg_params_revision", "rx_delay_1", "rx_dr_offset_1", "rx_datarate_2", "rx_freq_2", "factory_preset_freqs", "max_eirp", "max_duty_cycle", "supports_join", "rf_region", "supports_32bit_f_cnt", "join_accept_delay_1", "join_accept_delay_2", "f_cnt_automatic_reset", "cmd_switches", "adr_algorithm_id", "rx1_delay", "rx1_dr_offset", "rx2_datarate", "rx2_freq")
    ID_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_CLASS_B_FIELD_NUMBER: _ClassVar[int]
    CLASS_B_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    PING_SLOT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    PING_SLOT_DR_FIELD_NUMBER: _ClassVar[int]
    PING_SLOT_FREQ_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_CLASS_C_FIELD_NUMBER: _ClassVar[int]
    CLASS_C_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MAC_VERSION_FIELD_NUMBER: _ClassVar[int]
    REG_PARAMS_REVISION_FIELD_NUMBER: _ClassVar[int]
    RX_DELAY_1_FIELD_NUMBER: _ClassVar[int]
    RX_DR_OFFSET_1_FIELD_NUMBER: _ClassVar[int]
    RX_DATARATE_2_FIELD_NUMBER: _ClassVar[int]
    RX_FREQ_2_FIELD_NUMBER: _ClassVar[int]
    FACTORY_PRESET_FREQS_FIELD_NUMBER: _ClassVar[int]
    MAX_EIRP_FIELD_NUMBER: _ClassVar[int]
    MAX_DUTY_CYCLE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_JOIN_FIELD_NUMBER: _ClassVar[int]
    RF_REGION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_32BIT_F_CNT_FIELD_NUMBER: _ClassVar[int]
    JOIN_ACCEPT_DELAY_1_FIELD_NUMBER: _ClassVar[int]
    JOIN_ACCEPT_DELAY_2_FIELD_NUMBER: _ClassVar[int]
    F_CNT_AUTOMATIC_RESET_FIELD_NUMBER: _ClassVar[int]
    CMD_SWITCHES_FIELD_NUMBER: _ClassVar[int]
    ADR_ALGORITHM_ID_FIELD_NUMBER: _ClassVar[int]
    RX1_DELAY_FIELD_NUMBER: _ClassVar[int]
    RX1_DR_OFFSET_FIELD_NUMBER: _ClassVar[int]
    RX2_DATARATE_FIELD_NUMBER: _ClassVar[int]
    RX2_FREQ_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    supports_class_b: bool
    class_b_timeout: int
    ping_slot_period: int
    ping_slot_dr: int
    ping_slot_freq: int
    supports_class_c: bool
    class_c_timeout: int
    mac_version: str
    reg_params_revision: str
    rx_delay_1: int
    rx_dr_offset_1: int
    rx_datarate_2: int
    rx_freq_2: int
    factory_preset_freqs: _containers.RepeatedScalarFieldContainer[int]
    max_eirp: int
    max_duty_cycle: int
    supports_join: bool
    rf_region: str
    supports_32bit_f_cnt: bool
    join_accept_delay_1: int
    join_accept_delay_2: int
    f_cnt_automatic_reset: bool
    cmd_switches: _containers.RepeatedCompositeFieldContainer[MacCommandSwitch]
    adr_algorithm_id: str
    rx1_delay: int
    rx1_dr_offset: int
    rx2_datarate: int
    rx2_freq: int
    def __init__(self, id: _Optional[bytes] = ..., supports_class_b: _Optional[bool] = ..., class_b_timeout: _Optional[int] = ..., ping_slot_period: _Optional[int] = ..., ping_slot_dr: _Optional[int] = ..., ping_slot_freq: _Optional[int] = ..., supports_class_c: _Optional[bool] = ..., class_c_timeout: _Optional[int] = ..., mac_version: _Optional[str] = ..., reg_params_revision: _Optional[str] = ..., rx_delay_1: _Optional[int] = ..., rx_dr_offset_1: _Optional[int] = ..., rx_datarate_2: _Optional[int] = ..., rx_freq_2: _Optional[int] = ..., factory_preset_freqs: _Optional[_Iterable[int]] = ..., max_eirp: _Optional[int] = ..., max_duty_cycle: _Optional[int] = ..., supports_join: _Optional[bool] = ..., rf_region: _Optional[str] = ..., supports_32bit_f_cnt: _Optional[bool] = ..., join_accept_delay_1: _Optional[int] = ..., join_accept_delay_2: _Optional[int] = ..., f_cnt_automatic_reset: _Optional[bool] = ..., cmd_switches: _Optional[_Iterable[_Union[MacCommandSwitch, _Mapping]]] = ..., adr_algorithm_id: _Optional[str] = ..., rx1_delay: _Optional[int] = ..., rx1_dr_offset: _Optional[int] = ..., rx2_datarate: _Optional[int] = ..., rx2_freq: _Optional[int] = ...) -> None: ...

class RoutingProfile(_message.Message):
    __slots__ = ("id", "as_id", "ca_cert", "tls_cert", "tls_key")
    ID_FIELD_NUMBER: _ClassVar[int]
    AS_ID_FIELD_NUMBER: _ClassVar[int]
    CA_CERT_FIELD_NUMBER: _ClassVar[int]
    TLS_CERT_FIELD_NUMBER: _ClassVar[int]
    TLS_KEY_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    as_id: str
    ca_cert: str
    tls_cert: str
    tls_key: str
    def __init__(self, id: _Optional[bytes] = ..., as_id: _Optional[str] = ..., ca_cert: _Optional[str] = ..., tls_cert: _Optional[str] = ..., tls_key: _Optional[str] = ...) -> None: ...

class MacCommandSwitch(_message.Message):
    __slots__ = ("cid", "enabled")
    CID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    cid: int
    enabled: bool
    def __init__(self, cid: _Optional[int] = ..., enabled: _Optional[bool] = ...) -> None: ...
