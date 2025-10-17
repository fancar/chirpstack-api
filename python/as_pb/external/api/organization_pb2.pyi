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

class Organization(_message.Message):
    __slots__ = ("id", "name", "display_name", "can_have_gateways", "max_gateway_count", "max_device_count", "gw_only")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CAN_HAVE_GATEWAYS_FIELD_NUMBER: _ClassVar[int]
    MAX_GATEWAY_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_DEVICE_COUNT_FIELD_NUMBER: _ClassVar[int]
    GW_ONLY_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    display_name: str
    can_have_gateways: bool
    max_gateway_count: int
    max_device_count: int
    gw_only: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., can_have_gateways: _Optional[bool] = ..., max_gateway_count: _Optional[int] = ..., max_device_count: _Optional[int] = ..., gw_only: _Optional[bool] = ...) -> None: ...

class OrganizationListItem(_message.Message):
    __slots__ = ("id", "name", "display_name", "can_have_gateways", "created_at", "updated_at", "device_count", "gateway_count")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CAN_HAVE_GATEWAYS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COUNT_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_COUNT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    display_name: str
    can_have_gateways: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    device_count: int
    gateway_count: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., can_have_gateways: _Optional[bool] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., device_count: _Optional[int] = ..., gateway_count: _Optional[int] = ...) -> None: ...

class GetOrganizationRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetOrganizationResponse(_message.Message):
    __slots__ = ("organization", "created_at", "updated_at")
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    organization: Organization
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, organization: _Optional[_Union[Organization, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateOrganizationRequest(_message.Message):
    __slots__ = ("organization",)
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    organization: Organization
    def __init__(self, organization: _Optional[_Union[Organization, _Mapping]] = ...) -> None: ...

class CreateOrganizationResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class UpdateOrganizationRequest(_message.Message):
    __slots__ = ("organization",)
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    organization: Organization
    def __init__(self, organization: _Optional[_Union[Organization, _Mapping]] = ...) -> None: ...

class DeleteOrganizationRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ListOrganizationRequest(_message.Message):
    __slots__ = ("limit", "offset", "search", "orderBy", "order", "user_id")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    ORDERBY_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    search: str
    orderBy: str
    order: str
    user_id: int
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ..., search: _Optional[str] = ..., orderBy: _Optional[str] = ..., order: _Optional[str] = ..., user_id: _Optional[int] = ...) -> None: ...

class ListOrganizationResponse(_message.Message):
    __slots__ = ("total_count", "result")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    result: _containers.RepeatedCompositeFieldContainer[OrganizationListItem]
    def __init__(self, total_count: _Optional[int] = ..., result: _Optional[_Iterable[_Union[OrganizationListItem, _Mapping]]] = ...) -> None: ...

class OrganizationUser(_message.Message):
    __slots__ = ("organization_id", "user_id", "is_admin", "is_device_admin", "is_gateway_admin", "email", "is_active", "note", "name", "surname", "company", "position", "phone", "org_cnt")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    IS_DEVICE_ADMIN_FIELD_NUMBER: _ClassVar[int]
    IS_GATEWAY_ADMIN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SURNAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    ORG_CNT_FIELD_NUMBER: _ClassVar[int]
    organization_id: int
    user_id: int
    is_admin: bool
    is_device_admin: bool
    is_gateway_admin: bool
    email: str
    is_active: bool
    note: str
    name: str
    surname: str
    company: str
    position: str
    phone: str
    org_cnt: int
    def __init__(self, organization_id: _Optional[int] = ..., user_id: _Optional[int] = ..., is_admin: _Optional[bool] = ..., is_device_admin: _Optional[bool] = ..., is_gateway_admin: _Optional[bool] = ..., email: _Optional[str] = ..., is_active: _Optional[bool] = ..., note: _Optional[str] = ..., name: _Optional[str] = ..., surname: _Optional[str] = ..., company: _Optional[str] = ..., position: _Optional[str] = ..., phone: _Optional[str] = ..., org_cnt: _Optional[int] = ...) -> None: ...

class OrganizationUserListItem(_message.Message):
    __slots__ = ("user_id", "email", "is_admin", "is_device_admin", "is_gateway_admin", "created_at", "updated_at", "is_active", "name", "surname", "company", "position", "phone", "org_cnt")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    IS_DEVICE_ADMIN_FIELD_NUMBER: _ClassVar[int]
    IS_GATEWAY_ADMIN_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SURNAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    ORG_CNT_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    email: str
    is_admin: bool
    is_device_admin: bool
    is_gateway_admin: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    is_active: bool
    name: str
    surname: str
    company: str
    position: str
    phone: str
    org_cnt: int
    def __init__(self, user_id: _Optional[int] = ..., email: _Optional[str] = ..., is_admin: _Optional[bool] = ..., is_device_admin: _Optional[bool] = ..., is_gateway_admin: _Optional[bool] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., is_active: _Optional[bool] = ..., name: _Optional[str] = ..., surname: _Optional[str] = ..., company: _Optional[str] = ..., position: _Optional[str] = ..., phone: _Optional[str] = ..., org_cnt: _Optional[int] = ...) -> None: ...

class AddOrganizationUserRequest(_message.Message):
    __slots__ = ("organization_user",)
    ORGANIZATION_USER_FIELD_NUMBER: _ClassVar[int]
    organization_user: OrganizationUser
    def __init__(self, organization_user: _Optional[_Union[OrganizationUser, _Mapping]] = ...) -> None: ...

class UpdateOrganizationUserRequest(_message.Message):
    __slots__ = ("organization_user",)
    ORGANIZATION_USER_FIELD_NUMBER: _ClassVar[int]
    organization_user: OrganizationUser
    def __init__(self, organization_user: _Optional[_Union[OrganizationUser, _Mapping]] = ...) -> None: ...

class DeleteOrganizationUserRequest(_message.Message):
    __slots__ = ("organization_id", "user_id")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: int
    user_id: int
    def __init__(self, organization_id: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class ListOrganizationUsersRequest(_message.Message):
    __slots__ = ("organization_id", "limit", "offset", "orderBy", "order", "search")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDERBY_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    organization_id: int
    limit: int
    offset: int
    orderBy: str
    order: str
    search: str
    def __init__(self, organization_id: _Optional[int] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ..., orderBy: _Optional[str] = ..., order: _Optional[str] = ..., search: _Optional[str] = ...) -> None: ...

class ListOrganizationUsersResponse(_message.Message):
    __slots__ = ("total_count", "result")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    result: _containers.RepeatedCompositeFieldContainer[OrganizationUserListItem]
    def __init__(self, total_count: _Optional[int] = ..., result: _Optional[_Iterable[_Union[OrganizationUserListItem, _Mapping]]] = ...) -> None: ...

class GetOrganizationUserRequest(_message.Message):
    __slots__ = ("organization_id", "user_id")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: int
    user_id: int
    def __init__(self, organization_id: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class GetOrganizationUserResponse(_message.Message):
    __slots__ = ("organization_user", "created_at", "updated_at")
    ORGANIZATION_USER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    organization_user: OrganizationUser
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, organization_user: _Optional[_Union[OrganizationUser, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
