from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetDictionaryRequest(_message.Message):
    __slots__ = ("dic_type", "store")
    DIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    dic_type: str
    store: str
    def __init__(self, dic_type: _Optional[str] = ..., store: _Optional[str] = ...) -> None: ...

class GetDictionaryResponse(_message.Message):
    __slots__ = ("dic_type", "dict")
    DIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    DICT_FIELD_NUMBER: _ClassVar[int]
    dic_type: str
    dict: _containers.RepeatedCompositeFieldContainer[Dictionary]
    def __init__(self, dic_type: _Optional[str] = ..., dict: _Optional[_Iterable[_Union[Dictionary, _Mapping]]] = ...) -> None: ...

class Dictionary(_message.Message):
    __slots__ = ("code", "label", "is_actual")
    CODE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    IS_ACTUAL_FIELD_NUMBER: _ClassVar[int]
    code: str
    label: str
    is_actual: bool
    def __init__(self, code: _Optional[str] = ..., label: _Optional[str] = ..., is_actual: _Optional[bool] = ...) -> None: ...
