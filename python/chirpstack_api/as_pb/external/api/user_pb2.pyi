import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("id", "session_ttl", "is_admin", "is_active", "email", "note", "name", "surname", "company", "position", "phone", "login_at", "login_with_ldap")
    ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_TTL_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SURNAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    LOGIN_AT_FIELD_NUMBER: _ClassVar[int]
    LOGIN_WITH_LDAP_FIELD_NUMBER: _ClassVar[int]
    id: int
    session_ttl: int
    is_admin: bool
    is_active: bool
    email: str
    note: str
    name: str
    surname: str
    company: str
    position: str
    phone: str
    login_at: _timestamp_pb2.Timestamp
    login_with_ldap: bool
    def __init__(self, id: _Optional[int] = ..., session_ttl: _Optional[int] = ..., is_admin: _Optional[bool] = ..., is_active: _Optional[bool] = ..., email: _Optional[str] = ..., note: _Optional[str] = ..., name: _Optional[str] = ..., surname: _Optional[str] = ..., company: _Optional[str] = ..., position: _Optional[str] = ..., phone: _Optional[str] = ..., login_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., login_with_ldap: _Optional[bool] = ...) -> None: ...

class UserListItem(_message.Message):
    __slots__ = ("id", "email", "session_ttl", "is_admin", "is_active", "created_at", "updated_at", "login_at", "name", "surname", "company", "position", "phone", "org_cnt")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SESSION_TTL_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LOGIN_AT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SURNAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    ORG_CNT_FIELD_NUMBER: _ClassVar[int]
    id: int
    email: str
    session_ttl: int
    is_admin: bool
    is_active: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    login_at: _timestamp_pb2.Timestamp
    name: str
    surname: str
    company: str
    position: str
    phone: str
    org_cnt: int
    def __init__(self, id: _Optional[int] = ..., email: _Optional[str] = ..., session_ttl: _Optional[int] = ..., is_admin: _Optional[bool] = ..., is_active: _Optional[bool] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., login_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., surname: _Optional[str] = ..., company: _Optional[str] = ..., position: _Optional[str] = ..., phone: _Optional[str] = ..., org_cnt: _Optional[int] = ...) -> None: ...

class UserLogListItem(_message.Message):
    __slots__ = ("id", "created_at", "user_id", "user_name", "event", "state_prev", "state_cur", "organization_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    STATE_PREV_FIELD_NUMBER: _ClassVar[int]
    STATE_CUR_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    created_at: _timestamp_pb2.Timestamp
    user_id: int
    user_name: str
    event: str
    state_prev: str
    state_cur: str
    organization_id: int
    def __init__(self, id: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[int] = ..., user_name: _Optional[str] = ..., event: _Optional[str] = ..., state_prev: _Optional[str] = ..., state_cur: _Optional[str] = ..., organization_id: _Optional[int] = ...) -> None: ...

class UserOrganization(_message.Message):
    __slots__ = ("organization_id", "is_admin", "is_device_admin", "is_gateway_admin")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    IS_DEVICE_ADMIN_FIELD_NUMBER: _ClassVar[int]
    IS_GATEWAY_ADMIN_FIELD_NUMBER: _ClassVar[int]
    organization_id: int
    is_admin: bool
    is_device_admin: bool
    is_gateway_admin: bool
    def __init__(self, organization_id: _Optional[int] = ..., is_admin: _Optional[bool] = ..., is_device_admin: _Optional[bool] = ..., is_gateway_admin: _Optional[bool] = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ("user", "password", "organizations")
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONS_FIELD_NUMBER: _ClassVar[int]
    user: User
    password: str
    organizations: _containers.RepeatedCompositeFieldContainer[UserOrganization]
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., password: _Optional[str] = ..., organizations: _Optional[_Iterable[_Union[UserOrganization, _Mapping]]] = ...) -> None: ...

class CreateUserResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ("user", "created_at", "updated_at")
    USER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    user: User
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ListUserRequest(_message.Message):
    __slots__ = ("limit", "offset", "orderBy", "order", "search")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDERBY_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    orderBy: str
    order: str
    search: str
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., orderBy: _Optional[str] = ..., order: _Optional[str] = ..., search: _Optional[str] = ...) -> None: ...

class ListUserResponse(_message.Message):
    __slots__ = ("total_count", "result")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    result: _containers.RepeatedCompositeFieldContainer[UserListItem]
    def __init__(self, total_count: _Optional[int] = ..., result: _Optional[_Iterable[_Union[UserListItem, _Mapping]]] = ...) -> None: ...

class ListUserLogsRequest(_message.Message):
    __slots__ = ("limit", "offset", "organization_id", "search", "orderBy", "order", "date_from", "date_to")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    ORDERBY_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    DATE_FROM_FIELD_NUMBER: _ClassVar[int]
    DATE_TO_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    organization_id: int
    search: str
    orderBy: str
    order: str
    date_from: _timestamp_pb2.Timestamp
    date_to: _timestamp_pb2.Timestamp
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., organization_id: _Optional[int] = ..., search: _Optional[str] = ..., orderBy: _Optional[str] = ..., order: _Optional[str] = ..., date_from: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_to: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListUserLogsResponse(_message.Message):
    __slots__ = ("total_count", "result")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    result: _containers.RepeatedCompositeFieldContainer[UserLogListItem]
    def __init__(self, total_count: _Optional[int] = ..., result: _Optional[_Iterable[_Union[UserLogListItem, _Mapping]]] = ...) -> None: ...

class UpdateUserPasswordRequest(_message.Message):
    __slots__ = ("user_id", "password")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    password: str
    def __init__(self, user_id: _Optional[int] = ..., password: _Optional[str] = ...) -> None: ...
