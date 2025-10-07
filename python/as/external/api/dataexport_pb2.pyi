from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from handyrusty import hr_pb2 as _hr_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DataExportRequest(_message.Message):
    __slots__ = ("org_id", "ns_id")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    NS_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: int
    ns_id: int
    def __init__(self, org_id: _Optional[int] = ..., ns_id: _Optional[int] = ...) -> None: ...

class StreamResponse(_message.Message):
    __slots__ = ("current", "total", "chunk")
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    current: int
    total: int
    chunk: bytes
    def __init__(self, current: _Optional[int] = ..., total: _Optional[int] = ..., chunk: _Optional[bytes] = ...) -> None: ...
