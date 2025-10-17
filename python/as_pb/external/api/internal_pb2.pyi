import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import empty_pb2 as _empty_pb2
import importlib
_user_pb2 = importlib.import_module('as.external.api.user_pb2')
from handyrusty import hr_pb2 as _hr_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMainCountersRequest(_message.Message):
    __slots__ = ("interval", "start_timestamp", "end_timestamp")
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    interval: str
    start_timestamp: _timestamp_pb2.Timestamp
    end_timestamp: _timestamp_pb2.Timestamp
    def __init__(self, interval: _Optional[str] = ..., start_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MainCounters(_message.Message):
    __slots__ = ("timestamp", "rx_count", "rx_count_sent", "rx_count_err")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RX_COUNT_FIELD_NUMBER: _ClassVar[int]
    RX_COUNT_SENT_FIELD_NUMBER: _ClassVar[int]
    RX_COUNT_ERR_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    rx_count: int
    rx_count_sent: int
    rx_count_err: int
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., rx_count: _Optional[int] = ..., rx_count_sent: _Optional[int] = ..., rx_count_err: _Optional[int] = ...) -> None: ...

class GetMainCountersResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedCompositeFieldContainer[MainCounters]
    def __init__(self, result: _Optional[_Iterable[_Union[MainCounters, _Mapping]]] = ...) -> None: ...

class GetInfoResponse(_message.Message):
    __slots__ = ("api", "app_server", "net_server", "handyrusty", "clickhouse", "app_postgres", "net_postgres", "redis")
    API_FIELD_NUMBER: _ClassVar[int]
    APP_SERVER_FIELD_NUMBER: _ClassVar[int]
    NET_SERVER_FIELD_NUMBER: _ClassVar[int]
    HANDYRUSTY_FIELD_NUMBER: _ClassVar[int]
    CLICKHOUSE_FIELD_NUMBER: _ClassVar[int]
    APP_POSTGRES_FIELD_NUMBER: _ClassVar[int]
    NET_POSTGRES_FIELD_NUMBER: _ClassVar[int]
    REDIS_FIELD_NUMBER: _ClassVar[int]
    api: str
    app_server: str
    net_server: str
    handyrusty: str
    clickhouse: str
    app_postgres: str
    net_postgres: str
    redis: str
    def __init__(self, api: _Optional[str] = ..., app_server: _Optional[str] = ..., net_server: _Optional[str] = ..., handyrusty: _Optional[str] = ..., clickhouse: _Optional[str] = ..., app_postgres: _Optional[str] = ..., net_postgres: _Optional[str] = ..., redis: _Optional[str] = ...) -> None: ...

class APIKey(_message.Message):
    __slots__ = ("id", "name", "is_admin", "organization_id", "description", "is_active")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    is_admin: bool
    organization_id: int
    description: str
    is_active: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., is_admin: _Optional[bool] = ..., organization_id: _Optional[int] = ..., description: _Optional[str] = ..., is_active: _Optional[bool] = ...) -> None: ...

class CreateAPIKeyRequest(_message.Message):
    __slots__ = ("api_key",)
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    api_key: APIKey
    def __init__(self, api_key: _Optional[_Union[APIKey, _Mapping]] = ...) -> None: ...

class UpdateAPIKeyRequest(_message.Message):
    __slots__ = ("api_key",)
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    api_key: APIKey
    def __init__(self, api_key: _Optional[_Union[APIKey, _Mapping]] = ...) -> None: ...

class CreateAPIKeyResponse(_message.Message):
    __slots__ = ("id", "jwt_token")
    ID_FIELD_NUMBER: _ClassVar[int]
    JWT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    jwt_token: str
    def __init__(self, id: _Optional[str] = ..., jwt_token: _Optional[str] = ...) -> None: ...

class DeleteAPIKeyRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetAPIKeyRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetAPIKeyResponse(_message.Message):
    __slots__ = ("api_key", "created_at", "updated_at")
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    api_key: APIKey
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, api_key: _Optional[_Union[APIKey, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListAPIKeysRequest(_message.Message):
    __slots__ = ("limit", "offset", "is_admin", "organization_id", "orderBy", "order", "name")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORDERBY_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    is_admin: bool
    organization_id: int
    orderBy: str
    order: str
    name: str
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., is_admin: _Optional[bool] = ..., organization_id: _Optional[int] = ..., orderBy: _Optional[str] = ..., order: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ListAPIKeysResponse(_message.Message):
    __slots__ = ("total_count", "result")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    result: _containers.RepeatedCompositeFieldContainer[APIKey]
    def __init__(self, total_count: _Optional[int] = ..., result: _Optional[_Iterable[_Union[APIKey, _Mapping]]] = ...) -> None: ...

class OrganizationLink(_message.Message):
    __slots__ = ("organization_id", "organization_name", "is_admin", "is_device_admin", "is_gateway_admin", "created_at", "updated_at", "can_have_gateways")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    IS_DEVICE_ADMIN_FIELD_NUMBER: _ClassVar[int]
    IS_GATEWAY_ADMIN_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CAN_HAVE_GATEWAYS_FIELD_NUMBER: _ClassVar[int]
    organization_id: int
    organization_name: str
    is_admin: bool
    is_device_admin: bool
    is_gateway_admin: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    can_have_gateways: bool
    def __init__(self, organization_id: _Optional[int] = ..., organization_name: _Optional[str] = ..., is_admin: _Optional[bool] = ..., is_device_admin: _Optional[bool] = ..., is_gateway_admin: _Optional[bool] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., can_have_gateways: _Optional[bool] = ...) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("jwt",)
    JWT_FIELD_NUMBER: _ClassVar[int]
    jwt: str
    def __init__(self, jwt: _Optional[str] = ...) -> None: ...

class ProfileResponse(_message.Message):
    __slots__ = ("user", "organizations")
    USER_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONS_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    organizations: _containers.RepeatedCompositeFieldContainer[OrganizationLink]
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., organizations: _Optional[_Iterable[_Union[OrganizationLink, _Mapping]]] = ...) -> None: ...

class GlobalSearchRequest(_message.Message):
    __slots__ = ("search", "limit", "offset")
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    search: str
    limit: int
    offset: int
    def __init__(self, search: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class GlobalSearchResponse(_message.Message):
    __slots__ = ("result", "total_count")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedCompositeFieldContainer[GlobalSearchResult]
    total_count: int
    def __init__(self, result: _Optional[_Iterable[_Union[GlobalSearchResult, _Mapping]]] = ..., total_count: _Optional[int] = ...) -> None: ...

class GlobalSearchResult(_message.Message):
    __slots__ = ("kind", "score", "organization_id", "organization_name", "application_id", "application_name", "device_dev_eui", "device_name", "gateway_mac", "gateway_name", "routing_profile_id", "routing_profile_name")
    KIND_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_MAC_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    kind: str
    score: float
    organization_id: int
    organization_name: str
    application_id: int
    application_name: str
    device_dev_eui: str
    device_name: str
    gateway_mac: str
    gateway_name: str
    routing_profile_id: int
    routing_profile_name: str
    def __init__(self, kind: _Optional[str] = ..., score: _Optional[float] = ..., organization_id: _Optional[int] = ..., organization_name: _Optional[str] = ..., application_id: _Optional[int] = ..., application_name: _Optional[str] = ..., device_dev_eui: _Optional[str] = ..., device_name: _Optional[str] = ..., gateway_mac: _Optional[str] = ..., gateway_name: _Optional[str] = ..., routing_profile_id: _Optional[int] = ..., routing_profile_name: _Optional[str] = ...) -> None: ...

class SettingsResponse(_message.Message):
    __slots__ = ("server_name", "branding", "openid_connect", "tools_enabled")
    SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    BRANDING_FIELD_NUMBER: _ClassVar[int]
    OPENID_CONNECT_FIELD_NUMBER: _ClassVar[int]
    TOOLS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    server_name: str
    branding: Branding
    openid_connect: OpenIDConnect
    tools_enabled: ToolsEnabled
    def __init__(self, server_name: _Optional[str] = ..., branding: _Optional[_Union[Branding, _Mapping]] = ..., openid_connect: _Optional[_Union[OpenIDConnect, _Mapping]] = ..., tools_enabled: _Optional[_Union[ToolsEnabled, _Mapping]] = ...) -> None: ...

class Branding(_message.Message):
    __slots__ = ("registration", "footer", "top_nav_color", "tabs_color", "meta_title", "meta_description", "mode")
    REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    FOOTER_FIELD_NUMBER: _ClassVar[int]
    TOP_NAV_COLOR_FIELD_NUMBER: _ClassVar[int]
    TABS_COLOR_FIELD_NUMBER: _ClassVar[int]
    META_TITLE_FIELD_NUMBER: _ClassVar[int]
    META_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    registration: str
    footer: str
    top_nav_color: str
    tabs_color: str
    meta_title: str
    meta_description: str
    mode: str
    def __init__(self, registration: _Optional[str] = ..., footer: _Optional[str] = ..., top_nav_color: _Optional[str] = ..., tabs_color: _Optional[str] = ..., meta_title: _Optional[str] = ..., meta_description: _Optional[str] = ..., mode: _Optional[str] = ...) -> None: ...

class OpenIDConnect(_message.Message):
    __slots__ = ("enabled", "login_url", "login_label", "logout_url")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOGIN_URL_FIELD_NUMBER: _ClassVar[int]
    LOGIN_LABEL_FIELD_NUMBER: _ClassVar[int]
    LOGOUT_URL_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    login_url: str
    login_label: str
    logout_url: str
    def __init__(self, enabled: _Optional[bool] = ..., login_url: _Optional[str] = ..., login_label: _Optional[str] = ..., logout_url: _Optional[str] = ...) -> None: ...

class ToolsEnabled(_message.Message):
    __slots__ = ("bs_checker", "lora_maps", "help", "CTT", "spectrum_analyzer")
    BS_CHECKER_FIELD_NUMBER: _ClassVar[int]
    LORA_MAPS_FIELD_NUMBER: _ClassVar[int]
    HELP_FIELD_NUMBER: _ClassVar[int]
    CTT_FIELD_NUMBER: _ClassVar[int]
    SPECTRUM_ANALYZER_FIELD_NUMBER: _ClassVar[int]
    bs_checker: bool
    lora_maps: bool
    help: bool
    CTT: bool
    spectrum_analyzer: bool
    def __init__(self, bs_checker: _Optional[bool] = ..., lora_maps: _Optional[bool] = ..., help: _Optional[bool] = ..., CTT: _Optional[bool] = ..., spectrum_analyzer: _Optional[bool] = ...) -> None: ...

class OpenIDConnectLoginRequest(_message.Message):
    __slots__ = ("code", "state")
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    code: str
    state: str
    def __init__(self, code: _Optional[str] = ..., state: _Optional[str] = ...) -> None: ...

class OpenIDConnectLoginResponse(_message.Message):
    __slots__ = ("jwt_token",)
    JWT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    jwt_token: str
    def __init__(self, jwt_token: _Optional[str] = ...) -> None: ...

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
