import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IntegrationKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HTTP: _ClassVar[IntegrationKind]
    INFLUXDB: _ClassVar[IntegrationKind]
    THINGSBOARD: _ClassVar[IntegrationKind]
    MYDEVICES: _ClassVar[IntegrationKind]
    LORACLOUD: _ClassVar[IntegrationKind]
    GCP_PUBSUB: _ClassVar[IntegrationKind]
    AWS_SNS: _ClassVar[IntegrationKind]
    AZURE_SERVICE_BUS: _ClassVar[IntegrationKind]
    PILOT_THINGS: _ClassVar[IntegrationKind]
    MQTT_GLOBAL: _ClassVar[IntegrationKind]
    KAFKA: _ClassVar[IntegrationKind]
    LARTECH: _ClassVar[IntegrationKind]
    MQTT: _ClassVar[IntegrationKind]

class Marshaler(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JSON: _ClassVar[Marshaler]
    PROTOBUF: _ClassVar[Marshaler]
    JSON_V3: _ClassVar[Marshaler]
    ACTILITY_JSON: _ClassVar[Marshaler]
    LAR_TECH: _ClassVar[Marshaler]
    JSON_SHRINKED: _ClassVar[Marshaler]

class InfluxDBPrecision(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NS: _ClassVar[InfluxDBPrecision]
    U: _ClassVar[InfluxDBPrecision]
    MS: _ClassVar[InfluxDBPrecision]
    S: _ClassVar[InfluxDBPrecision]
    M: _ClassVar[InfluxDBPrecision]
    H: _ClassVar[InfluxDBPrecision]

class InfluxDBVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INFLUXDB_1: _ClassVar[InfluxDBVersion]
    INFLUXDB_2: _ClassVar[InfluxDBVersion]
HTTP: IntegrationKind
INFLUXDB: IntegrationKind
THINGSBOARD: IntegrationKind
MYDEVICES: IntegrationKind
LORACLOUD: IntegrationKind
GCP_PUBSUB: IntegrationKind
AWS_SNS: IntegrationKind
AZURE_SERVICE_BUS: IntegrationKind
PILOT_THINGS: IntegrationKind
MQTT_GLOBAL: IntegrationKind
KAFKA: IntegrationKind
LARTECH: IntegrationKind
MQTT: IntegrationKind
JSON: Marshaler
PROTOBUF: Marshaler
JSON_V3: Marshaler
ACTILITY_JSON: Marshaler
LAR_TECH: Marshaler
JSON_SHRINKED: Marshaler
NS: InfluxDBPrecision
U: InfluxDBPrecision
MS: InfluxDBPrecision
S: InfluxDBPrecision
M: InfluxDBPrecision
H: InfluxDBPrecision
INFLUXDB_1: InfluxDBVersion
INFLUXDB_2: InfluxDBVersion

class Application(_message.Message):
    __slots__ = ("id", "name", "description", "organization_id", "payload_codec", "payload_encoder_script", "payload_decoder_script", "is_active")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_CODEC_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_ENCODER_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_DECODER_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    organization_id: int
    payload_codec: str
    payload_encoder_script: str
    payload_decoder_script: str
    is_active: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., organization_id: _Optional[int] = ..., payload_codec: _Optional[str] = ..., payload_encoder_script: _Optional[str] = ..., payload_decoder_script: _Optional[str] = ..., is_active: _Optional[bool] = ...) -> None: ...

class ApplicationListItem(_message.Message):
    __slots__ = ("id", "name", "description", "organization_id", "is_active", "dev_cnt", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DEV_CNT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    organization_id: int
    is_active: bool
    dev_cnt: int
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., organization_id: _Optional[int] = ..., is_active: _Optional[bool] = ..., dev_cnt: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateApplicationRequest(_message.Message):
    __slots__ = ("application",)
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    application: Application
    def __init__(self, application: _Optional[_Union[Application, _Mapping]] = ...) -> None: ...

class CreateApplicationResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetApplicationRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetApplicationResponse(_message.Message):
    __slots__ = ("application",)
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    application: Application
    def __init__(self, application: _Optional[_Union[Application, _Mapping]] = ...) -> None: ...

class UpdateApplicationRequest(_message.Message):
    __slots__ = ("application",)
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    application: Application
    def __init__(self, application: _Optional[_Union[Application, _Mapping]] = ...) -> None: ...

class DeleteApplicationRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ListApplicationRequest(_message.Message):
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

class ListApplicationResponse(_message.Message):
    __slots__ = ("total_count", "result")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    result: _containers.RepeatedCompositeFieldContainer[ApplicationListItem]
    def __init__(self, total_count: _Optional[int] = ..., result: _Optional[_Iterable[_Union[ApplicationListItem, _Mapping]]] = ...) -> None: ...

class HTTPIntegrationHeader(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class HTTPIntegration(_message.Message):
    __slots__ = ("application_id", "headers", "uplink_data_url", "join_notification_url", "ack_notification_url", "error_notification_url", "status_notification_url", "location_notification_url", "tx_ack_notification_url", "integration_notification_url", "marshaler", "event_endpoint_url")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    UPLINK_DATA_URL_FIELD_NUMBER: _ClassVar[int]
    JOIN_NOTIFICATION_URL_FIELD_NUMBER: _ClassVar[int]
    ACK_NOTIFICATION_URL_FIELD_NUMBER: _ClassVar[int]
    ERROR_NOTIFICATION_URL_FIELD_NUMBER: _ClassVar[int]
    STATUS_NOTIFICATION_URL_FIELD_NUMBER: _ClassVar[int]
    LOCATION_NOTIFICATION_URL_FIELD_NUMBER: _ClassVar[int]
    TX_ACK_NOTIFICATION_URL_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_NOTIFICATION_URL_FIELD_NUMBER: _ClassVar[int]
    MARSHALER_FIELD_NUMBER: _ClassVar[int]
    EVENT_ENDPOINT_URL_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    headers: _containers.RepeatedCompositeFieldContainer[HTTPIntegrationHeader]
    uplink_data_url: str
    join_notification_url: str
    ack_notification_url: str
    error_notification_url: str
    status_notification_url: str
    location_notification_url: str
    tx_ack_notification_url: str
    integration_notification_url: str
    marshaler: Marshaler
    event_endpoint_url: str
    def __init__(self, application_id: _Optional[int] = ..., headers: _Optional[_Iterable[_Union[HTTPIntegrationHeader, _Mapping]]] = ..., uplink_data_url: _Optional[str] = ..., join_notification_url: _Optional[str] = ..., ack_notification_url: _Optional[str] = ..., error_notification_url: _Optional[str] = ..., status_notification_url: _Optional[str] = ..., location_notification_url: _Optional[str] = ..., tx_ack_notification_url: _Optional[str] = ..., integration_notification_url: _Optional[str] = ..., marshaler: _Optional[_Union[Marshaler, str]] = ..., event_endpoint_url: _Optional[str] = ...) -> None: ...

class CreateHTTPIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: HTTPIntegration
    def __init__(self, integration: _Optional[_Union[HTTPIntegration, _Mapping]] = ...) -> None: ...

class GetHTTPIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class GetHTTPIntegrationResponse(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: HTTPIntegration
    def __init__(self, integration: _Optional[_Union[HTTPIntegration, _Mapping]] = ...) -> None: ...

class UpdateHTTPIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: HTTPIntegration
    def __init__(self, integration: _Optional[_Union[HTTPIntegration, _Mapping]] = ...) -> None: ...

class DeleteHTTPIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class CreateKafkaIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: KafkaIntegration
    def __init__(self, integration: _Optional[_Union[KafkaIntegration, _Mapping]] = ...) -> None: ...

class GetKafkaIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class GetKafkaIntegrationResponse(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: KafkaIntegration
    def __init__(self, integration: _Optional[_Union[KafkaIntegration, _Mapping]] = ...) -> None: ...

class UpdateKafkaIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: KafkaIntegration
    def __init__(self, integration: _Optional[_Union[KafkaIntegration, _Mapping]] = ...) -> None: ...

class DeleteKafkaIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class KafkaIntegration(_message.Message):
    __slots__ = ("application_id", "brokers", "TLS", "username", "password", "topic", "event_key_template", "mechanism", "algorithm", "marshaler", "reader", "writers", "owner")
    class Mechanism(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLAIN: _ClassVar[KafkaIntegration.Mechanism]
        SCRAM: _ClassVar[KafkaIntegration.Mechanism]
    PLAIN: KafkaIntegration.Mechanism
    SCRAM: KafkaIntegration.Mechanism
    class Algorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SHA256: _ClassVar[KafkaIntegration.Algorithm]
        SHA512: _ClassVar[KafkaIntegration.Algorithm]
    SHA256: KafkaIntegration.Algorithm
    SHA512: KafkaIntegration.Algorithm
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    BROKERS_FIELD_NUMBER: _ClassVar[int]
    TLS_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    EVENT_KEY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    MECHANISM_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    MARSHALER_FIELD_NUMBER: _ClassVar[int]
    READER_FIELD_NUMBER: _ClassVar[int]
    WRITERS_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    brokers: _containers.RepeatedScalarFieldContainer[str]
    TLS: bool
    username: str
    password: str
    topic: str
    event_key_template: str
    mechanism: KafkaIntegration.Mechanism
    algorithm: KafkaIntegration.Algorithm
    marshaler: Marshaler
    reader: KafkaReader
    writers: _containers.RepeatedCompositeFieldContainer[KafkaWriter]
    owner: str
    def __init__(self, application_id: _Optional[int] = ..., brokers: _Optional[_Iterable[str]] = ..., TLS: _Optional[bool] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., topic: _Optional[str] = ..., event_key_template: _Optional[str] = ..., mechanism: _Optional[_Union[KafkaIntegration.Mechanism, str]] = ..., algorithm: _Optional[_Union[KafkaIntegration.Algorithm, str]] = ..., marshaler: _Optional[_Union[Marshaler, str]] = ..., reader: _Optional[_Union[KafkaReader, _Mapping]] = ..., writers: _Optional[_Iterable[_Union[KafkaWriter, _Mapping]]] = ..., owner: _Optional[str] = ...) -> None: ...

class KafkaReader(_message.Message):
    __slots__ = ("enabled", "marshaler", "topic", "group_id")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MARSHALER_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    marshaler: Marshaler
    topic: str
    group_id: str
    def __init__(self, enabled: _Optional[bool] = ..., marshaler: _Optional[_Union[Marshaler, str]] = ..., topic: _Optional[str] = ..., group_id: _Optional[str] = ...) -> None: ...

class KafkaWriter(_message.Message):
    __slots__ = ("event", "enabled", "marshaler", "topic")
    EVENT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MARSHALER_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    event: str
    enabled: bool
    marshaler: Marshaler
    topic: str
    def __init__(self, event: _Optional[str] = ..., enabled: _Optional[bool] = ..., marshaler: _Optional[_Union[Marshaler, str]] = ..., topic: _Optional[str] = ...) -> None: ...

class ListIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class IntegrationListItem(_message.Message):
    __slots__ = ("kind",)
    KIND_FIELD_NUMBER: _ClassVar[int]
    kind: IntegrationKind
    def __init__(self, kind: _Optional[_Union[IntegrationKind, str]] = ...) -> None: ...

class ListIntegrationResponse(_message.Message):
    __slots__ = ("total_count", "result")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    result: _containers.RepeatedCompositeFieldContainer[IntegrationListItem]
    def __init__(self, total_count: _Optional[int] = ..., result: _Optional[_Iterable[_Union[IntegrationListItem, _Mapping]]] = ...) -> None: ...

class InfluxDBIntegration(_message.Message):
    __slots__ = ("application_id", "endpoint", "db", "username", "password", "retention_policy_name", "precision", "version", "token", "organization", "bucket")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DB_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    endpoint: str
    db: str
    username: str
    password: str
    retention_policy_name: str
    precision: InfluxDBPrecision
    version: InfluxDBVersion
    token: str
    organization: str
    bucket: str
    def __init__(self, application_id: _Optional[int] = ..., endpoint: _Optional[str] = ..., db: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., retention_policy_name: _Optional[str] = ..., precision: _Optional[_Union[InfluxDBPrecision, str]] = ..., version: _Optional[_Union[InfluxDBVersion, str]] = ..., token: _Optional[str] = ..., organization: _Optional[str] = ..., bucket: _Optional[str] = ...) -> None: ...

class CreateInfluxDBIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: InfluxDBIntegration
    def __init__(self, integration: _Optional[_Union[InfluxDBIntegration, _Mapping]] = ...) -> None: ...

class GetInfluxDBIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class GetInfluxDBIntegrationResponse(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: InfluxDBIntegration
    def __init__(self, integration: _Optional[_Union[InfluxDBIntegration, _Mapping]] = ...) -> None: ...

class UpdateInfluxDBIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: InfluxDBIntegration
    def __init__(self, integration: _Optional[_Union[InfluxDBIntegration, _Mapping]] = ...) -> None: ...

class DeleteInfluxDBIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class ThingsBoardIntegration(_message.Message):
    __slots__ = ("application_id", "server")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    server: str
    def __init__(self, application_id: _Optional[int] = ..., server: _Optional[str] = ...) -> None: ...

class CreateThingsBoardIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: ThingsBoardIntegration
    def __init__(self, integration: _Optional[_Union[ThingsBoardIntegration, _Mapping]] = ...) -> None: ...

class GetThingsBoardIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class GetThingsBoardIntegrationResponse(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: ThingsBoardIntegration
    def __init__(self, integration: _Optional[_Union[ThingsBoardIntegration, _Mapping]] = ...) -> None: ...

class UpdateThingsBoardIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: ThingsBoardIntegration
    def __init__(self, integration: _Optional[_Union[ThingsBoardIntegration, _Mapping]] = ...) -> None: ...

class DeleteThingsBoardIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class MyDevicesIntegration(_message.Message):
    __slots__ = ("application_id", "endpoint")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    endpoint: str
    def __init__(self, application_id: _Optional[int] = ..., endpoint: _Optional[str] = ...) -> None: ...

class CreateMyDevicesIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: MyDevicesIntegration
    def __init__(self, integration: _Optional[_Union[MyDevicesIntegration, _Mapping]] = ...) -> None: ...

class GetMyDevicesIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class GetMyDevicesIntegrationResponse(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: MyDevicesIntegration
    def __init__(self, integration: _Optional[_Union[MyDevicesIntegration, _Mapping]] = ...) -> None: ...

class UpdateMyDevicesIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: MyDevicesIntegration
    def __init__(self, integration: _Optional[_Union[MyDevicesIntegration, _Mapping]] = ...) -> None: ...

class DeleteMyDevicesIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class LoRaCloudIntegration(_message.Message):
    __slots__ = ("application_id", "geolocation", "geolocation_token", "geolocation_buffer_ttl", "geolocation_min_buffer_size", "geolocation_tdoa", "geolocation_rssi", "geolocation_gnss", "geolocation_gnss_payload_field", "geolocation_gnss_use_rx_time", "geolocation_wifi", "geolocation_wifi_payload_field", "das", "das_token", "das_modem_port", "das_gnss_port", "das_gnss_use_rx_time", "das_streaming_geoloc_workaround")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    GEOLOCATION_FIELD_NUMBER: _ClassVar[int]
    GEOLOCATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    GEOLOCATION_BUFFER_TTL_FIELD_NUMBER: _ClassVar[int]
    GEOLOCATION_MIN_BUFFER_SIZE_FIELD_NUMBER: _ClassVar[int]
    GEOLOCATION_TDOA_FIELD_NUMBER: _ClassVar[int]
    GEOLOCATION_RSSI_FIELD_NUMBER: _ClassVar[int]
    GEOLOCATION_GNSS_FIELD_NUMBER: _ClassVar[int]
    GEOLOCATION_GNSS_PAYLOAD_FIELD_FIELD_NUMBER: _ClassVar[int]
    GEOLOCATION_GNSS_USE_RX_TIME_FIELD_NUMBER: _ClassVar[int]
    GEOLOCATION_WIFI_FIELD_NUMBER: _ClassVar[int]
    GEOLOCATION_WIFI_PAYLOAD_FIELD_FIELD_NUMBER: _ClassVar[int]
    DAS_FIELD_NUMBER: _ClassVar[int]
    DAS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DAS_MODEM_PORT_FIELD_NUMBER: _ClassVar[int]
    DAS_GNSS_PORT_FIELD_NUMBER: _ClassVar[int]
    DAS_GNSS_USE_RX_TIME_FIELD_NUMBER: _ClassVar[int]
    DAS_STREAMING_GEOLOC_WORKAROUND_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    geolocation: bool
    geolocation_token: str
    geolocation_buffer_ttl: int
    geolocation_min_buffer_size: int
    geolocation_tdoa: bool
    geolocation_rssi: bool
    geolocation_gnss: bool
    geolocation_gnss_payload_field: str
    geolocation_gnss_use_rx_time: bool
    geolocation_wifi: bool
    geolocation_wifi_payload_field: str
    das: bool
    das_token: str
    das_modem_port: int
    das_gnss_port: int
    das_gnss_use_rx_time: bool
    das_streaming_geoloc_workaround: bool
    def __init__(self, application_id: _Optional[int] = ..., geolocation: _Optional[bool] = ..., geolocation_token: _Optional[str] = ..., geolocation_buffer_ttl: _Optional[int] = ..., geolocation_min_buffer_size: _Optional[int] = ..., geolocation_tdoa: _Optional[bool] = ..., geolocation_rssi: _Optional[bool] = ..., geolocation_gnss: _Optional[bool] = ..., geolocation_gnss_payload_field: _Optional[str] = ..., geolocation_gnss_use_rx_time: _Optional[bool] = ..., geolocation_wifi: _Optional[bool] = ..., geolocation_wifi_payload_field: _Optional[str] = ..., das: _Optional[bool] = ..., das_token: _Optional[str] = ..., das_modem_port: _Optional[int] = ..., das_gnss_port: _Optional[int] = ..., das_gnss_use_rx_time: _Optional[bool] = ..., das_streaming_geoloc_workaround: _Optional[bool] = ...) -> None: ...

class CreateLoRaCloudIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: LoRaCloudIntegration
    def __init__(self, integration: _Optional[_Union[LoRaCloudIntegration, _Mapping]] = ...) -> None: ...

class GetLoRaCloudIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class GetLoRaCloudIntegrationResponse(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: LoRaCloudIntegration
    def __init__(self, integration: _Optional[_Union[LoRaCloudIntegration, _Mapping]] = ...) -> None: ...

class UpdateLoRaCloudIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: LoRaCloudIntegration
    def __init__(self, integration: _Optional[_Union[LoRaCloudIntegration, _Mapping]] = ...) -> None: ...

class DeleteLoRaCloudIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class GCPPubSubIntegration(_message.Message):
    __slots__ = ("application_id", "marshaler", "credentials_file", "project_id", "topic_name")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    MARSHALER_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FILE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    marshaler: Marshaler
    credentials_file: str
    project_id: str
    topic_name: str
    def __init__(self, application_id: _Optional[int] = ..., marshaler: _Optional[_Union[Marshaler, str]] = ..., credentials_file: _Optional[str] = ..., project_id: _Optional[str] = ..., topic_name: _Optional[str] = ...) -> None: ...

class CreateGCPPubSubIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: GCPPubSubIntegration
    def __init__(self, integration: _Optional[_Union[GCPPubSubIntegration, _Mapping]] = ...) -> None: ...

class GetGCPPubSubIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class GetGCPPubSubIntegrationResponse(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: GCPPubSubIntegration
    def __init__(self, integration: _Optional[_Union[GCPPubSubIntegration, _Mapping]] = ...) -> None: ...

class UpdateGCPPubSubIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: GCPPubSubIntegration
    def __init__(self, integration: _Optional[_Union[GCPPubSubIntegration, _Mapping]] = ...) -> None: ...

class DeleteGCPPubSubIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class AWSSNSIntegration(_message.Message):
    __slots__ = ("application_id", "marshaler", "region", "access_key_id", "secret_access_key", "topic_arn")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    MARSHALER_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    TOPIC_ARN_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    marshaler: Marshaler
    region: str
    access_key_id: str
    secret_access_key: str
    topic_arn: str
    def __init__(self, application_id: _Optional[int] = ..., marshaler: _Optional[_Union[Marshaler, str]] = ..., region: _Optional[str] = ..., access_key_id: _Optional[str] = ..., secret_access_key: _Optional[str] = ..., topic_arn: _Optional[str] = ...) -> None: ...

class CreateAWSSNSIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: AWSSNSIntegration
    def __init__(self, integration: _Optional[_Union[AWSSNSIntegration, _Mapping]] = ...) -> None: ...

class GetAWSSNSIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class GetAWSSNSIntegrationResponse(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: AWSSNSIntegration
    def __init__(self, integration: _Optional[_Union[AWSSNSIntegration, _Mapping]] = ...) -> None: ...

class UpdateAWSSNSIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: AWSSNSIntegration
    def __init__(self, integration: _Optional[_Union[AWSSNSIntegration, _Mapping]] = ...) -> None: ...

class DeleteAWSSNSIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class AzureServiceBusIntegration(_message.Message):
    __slots__ = ("application_id", "marshaler", "connection_string", "publish_name")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    MARSHALER_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STRING_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_NAME_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    marshaler: Marshaler
    connection_string: str
    publish_name: str
    def __init__(self, application_id: _Optional[int] = ..., marshaler: _Optional[_Union[Marshaler, str]] = ..., connection_string: _Optional[str] = ..., publish_name: _Optional[str] = ...) -> None: ...

class CreateAzureServiceBusIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: AzureServiceBusIntegration
    def __init__(self, integration: _Optional[_Union[AzureServiceBusIntegration, _Mapping]] = ...) -> None: ...

class GetAzureServiceBusIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class GetAzureServiceBusIntegrationResponse(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: AzureServiceBusIntegration
    def __init__(self, integration: _Optional[_Union[AzureServiceBusIntegration, _Mapping]] = ...) -> None: ...

class UpdateAzureServiceBusIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: AzureServiceBusIntegration
    def __init__(self, integration: _Optional[_Union[AzureServiceBusIntegration, _Mapping]] = ...) -> None: ...

class DeleteAzureServiceBusIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class PilotThingsIntegration(_message.Message):
    __slots__ = ("application_id", "server", "token")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    server: str
    token: str
    def __init__(self, application_id: _Optional[int] = ..., server: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class CreatePilotThingsIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: PilotThingsIntegration
    def __init__(self, integration: _Optional[_Union[PilotThingsIntegration, _Mapping]] = ...) -> None: ...

class GetPilotThingsIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class GetPilotThingsIntegrationResponse(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: PilotThingsIntegration
    def __init__(self, integration: _Optional[_Union[PilotThingsIntegration, _Mapping]] = ...) -> None: ...

class UpdatePilotThingsIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: PilotThingsIntegration
    def __init__(self, integration: _Optional[_Union[PilotThingsIntegration, _Mapping]] = ...) -> None: ...

class DeletePilotThingsIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class GenerateMQTTIntegrationClientCertificateRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class GenerateMQTTIntegrationClientCertificateResponse(_message.Message):
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

class CreateMQTTIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: MQTTIntegration
    def __init__(self, integration: _Optional[_Union[MQTTIntegration, _Mapping]] = ...) -> None: ...

class GetMQTTIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class GetMQTTIntegrationResponse(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: MQTTIntegration
    def __init__(self, integration: _Optional[_Union[MQTTIntegration, _Mapping]] = ...) -> None: ...

class UpdateMQTTIntegrationRequest(_message.Message):
    __slots__ = ("integration",)
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: MQTTIntegration
    def __init__(self, integration: _Optional[_Union[MQTTIntegration, _Mapping]] = ...) -> None: ...

class DeleteMQTTIntegrationRequest(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    def __init__(self, application_id: _Optional[int] = ...) -> None: ...

class MQTTIntegration(_message.Message):
    __slots__ = ("application_id", "server", "username", "password", "max_reconnect_interval", "QoS", "client_id", "ca_cert", "tls_cert", "tls_key", "event_topic_template", "command_topic_template", "retain_events", "marshaler")
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    MAX_RECONNECT_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    QOS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CA_CERT_FIELD_NUMBER: _ClassVar[int]
    TLS_CERT_FIELD_NUMBER: _ClassVar[int]
    TLS_KEY_FIELD_NUMBER: _ClassVar[int]
    EVENT_TOPIC_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_TOPIC_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    RETAIN_EVENTS_FIELD_NUMBER: _ClassVar[int]
    MARSHALER_FIELD_NUMBER: _ClassVar[int]
    application_id: int
    server: str
    username: str
    password: str
    max_reconnect_interval: int
    QoS: int
    client_id: str
    ca_cert: str
    tls_cert: str
    tls_key: str
    event_topic_template: str
    command_topic_template: str
    retain_events: bool
    marshaler: Marshaler
    def __init__(self, application_id: _Optional[int] = ..., server: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., max_reconnect_interval: _Optional[int] = ..., QoS: _Optional[int] = ..., client_id: _Optional[str] = ..., ca_cert: _Optional[str] = ..., tls_cert: _Optional[str] = ..., tls_key: _Optional[str] = ..., event_topic_template: _Optional[str] = ..., command_topic_template: _Optional[str] = ..., retain_events: _Optional[bool] = ..., marshaler: _Optional[_Union[Marshaler, str]] = ...) -> None: ...
