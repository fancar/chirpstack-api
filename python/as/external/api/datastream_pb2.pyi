from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DataStreamRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DataStreamResponse(_message.Message):
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
