// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.29.1
// 	protoc        (unknown)
// source: as/external/api/datastream.proto

package api

import (
	_ "google.golang.org/genproto/googleapis/api/annotations"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type DataStreamRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// ID of an item requested
	Id int64 `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
}

func (x *DataStreamRequest) Reset() {
	*x = DataStreamRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_as_external_api_datastream_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DataStreamRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DataStreamRequest) ProtoMessage() {}

func (x *DataStreamRequest) ProtoReflect() protoreflect.Message {
	mi := &file_as_external_api_datastream_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DataStreamRequest.ProtoReflect.Descriptor instead.
func (*DataStreamRequest) Descriptor() ([]byte, []int) {
	return file_as_external_api_datastream_proto_rawDescGZIP(), []int{0}
}

func (x *DataStreamRequest) GetId() int64 {
	if x != nil {
		return x.Id
	}
	return 0
}

type DataStreamResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Size:
	//
	//	*DataStreamResponse_Current
	//	*DataStreamResponse_Total
	Size isDataStreamResponse_Size `protobuf_oneof:"size"`
	// Types that are assignable to Data:
	//
	//	*DataStreamResponse_Rows
	//	*DataStreamResponse_Chunk
	Data isDataStreamResponse_Data `protobuf_oneof:"data"`
}

func (x *DataStreamResponse) Reset() {
	*x = DataStreamResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_as_external_api_datastream_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DataStreamResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DataStreamResponse) ProtoMessage() {}

func (x *DataStreamResponse) ProtoReflect() protoreflect.Message {
	mi := &file_as_external_api_datastream_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DataStreamResponse.ProtoReflect.Descriptor instead.
func (*DataStreamResponse) Descriptor() ([]byte, []int) {
	return file_as_external_api_datastream_proto_rawDescGZIP(), []int{1}
}

func (m *DataStreamResponse) GetSize() isDataStreamResponse_Size {
	if m != nil {
		return m.Size
	}
	return nil
}

func (x *DataStreamResponse) GetCurrent() uint32 {
	if x, ok := x.GetSize().(*DataStreamResponse_Current); ok {
		return x.Current
	}
	return 0
}

func (x *DataStreamResponse) GetTotal() uint32 {
	if x, ok := x.GetSize().(*DataStreamResponse_Total); ok {
		return x.Total
	}
	return 0
}

func (m *DataStreamResponse) GetData() isDataStreamResponse_Data {
	if m != nil {
		return m.Data
	}
	return nil
}

func (x *DataStreamResponse) GetRows() uint32 {
	if x, ok := x.GetData().(*DataStreamResponse_Rows); ok {
		return x.Rows
	}
	return 0
}

func (x *DataStreamResponse) GetChunk() []byte {
	if x, ok := x.GetData().(*DataStreamResponse_Chunk); ok {
		return x.Chunk
	}
	return nil
}

type isDataStreamResponse_Size interface {
	isDataStreamResponse_Size()
}

type DataStreamResponse_Current struct {
	Current uint32 `protobuf:"varint,1,opt,name=current,proto3,oneof"`
}

type DataStreamResponse_Total struct {
	Total uint32 `protobuf:"varint,2,opt,name=total,proto3,oneof"`
}

func (*DataStreamResponse_Current) isDataStreamResponse_Size() {}

func (*DataStreamResponse_Total) isDataStreamResponse_Size() {}

type isDataStreamResponse_Data interface {
	isDataStreamResponse_Data()
}

type DataStreamResponse_Rows struct {
	Rows uint32 `protobuf:"varint,3,opt,name=rows,proto3,oneof"`
}

type DataStreamResponse_Chunk struct {
	Chunk []byte `protobuf:"bytes,4,opt,name=chunk,proto3,oneof"`
}

func (*DataStreamResponse_Rows) isDataStreamResponse_Data() {}

func (*DataStreamResponse_Chunk) isDataStreamResponse_Data() {}

var File_as_external_api_datastream_proto protoreflect.FileDescriptor

var file_as_external_api_datastream_proto_rawDesc = []byte{
	0x0a, 0x20, 0x61, 0x73, 0x2f, 0x65, 0x78, 0x74, 0x65, 0x72, 0x6e, 0x61, 0x6c, 0x2f, 0x61, 0x70,
	0x69, 0x2f, 0x64, 0x61, 0x74, 0x61, 0x73, 0x74, 0x72, 0x65, 0x61, 0x6d, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x12, 0x03, 0x61, 0x70, 0x69, 0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f,
	0x61, 0x70, 0x69, 0x2f, 0x61, 0x6e, 0x6e, 0x6f, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x23, 0x0a, 0x11, 0x44, 0x61, 0x74, 0x61, 0x53, 0x74, 0x72,
	0x65, 0x61, 0x6d, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x03, 0x52, 0x02, 0x69, 0x64, 0x22, 0x86, 0x01, 0x0a, 0x12, 0x44,
	0x61, 0x74, 0x61, 0x53, 0x74, 0x72, 0x65, 0x61, 0x6d, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73,
	0x65, 0x12, 0x1a, 0x0a, 0x07, 0x63, 0x75, 0x72, 0x72, 0x65, 0x6e, 0x74, 0x18, 0x01, 0x20, 0x01,
	0x28, 0x0d, 0x48, 0x00, 0x52, 0x07, 0x63, 0x75, 0x72, 0x72, 0x65, 0x6e, 0x74, 0x12, 0x16, 0x0a,
	0x05, 0x74, 0x6f, 0x74, 0x61, 0x6c, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0d, 0x48, 0x00, 0x52, 0x05,
	0x74, 0x6f, 0x74, 0x61, 0x6c, 0x12, 0x14, 0x0a, 0x04, 0x72, 0x6f, 0x77, 0x73, 0x18, 0x03, 0x20,
	0x01, 0x28, 0x0d, 0x48, 0x01, 0x52, 0x04, 0x72, 0x6f, 0x77, 0x73, 0x12, 0x16, 0x0a, 0x05, 0x63,
	0x68, 0x75, 0x6e, 0x6b, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0c, 0x48, 0x01, 0x52, 0x05, 0x63, 0x68,
	0x75, 0x6e, 0x6b, 0x42, 0x06, 0x0a, 0x04, 0x73, 0x69, 0x7a, 0x65, 0x42, 0x06, 0x0a, 0x04, 0x64,
	0x61, 0x74, 0x61, 0x32, 0x8c, 0x01, 0x0a, 0x11, 0x44, 0x61, 0x74, 0x61, 0x53, 0x74, 0x72, 0x65,
	0x61, 0x6d, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x77, 0x0a, 0x14, 0x47, 0x65, 0x74,
	0x47, 0x61, 0x74, 0x65, 0x77, 0x61, 0x79, 0x54, 0x61, 0x73, 0x6b, 0x52, 0x65, 0x73, 0x75, 0x6c,
	0x74, 0x12, 0x16, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x44, 0x61, 0x74, 0x61, 0x53, 0x74, 0x72, 0x65,
	0x61, 0x6d, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x17, 0x2e, 0x61, 0x70, 0x69, 0x2e,
	0x44, 0x61, 0x74, 0x61, 0x53, 0x74, 0x72, 0x65, 0x61, 0x6d, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e,
	0x73, 0x65, 0x22, 0x2c, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x26, 0x12, 0x24, 0x2f, 0x61, 0x70, 0x69,
	0x2f, 0x64, 0x61, 0x74, 0x61, 0x73, 0x74, 0x72, 0x65, 0x61, 0x6d, 0x2f, 0x67, 0x61, 0x74, 0x65,
	0x77, 0x61, 0x79, 0x73, 0x2f, 0x74, 0x61, 0x73, 0x6b, 0x2d, 0x72, 0x65, 0x73, 0x75, 0x6c, 0x74,
	0x30, 0x01, 0x42, 0x7f, 0x0a, 0x07, 0x63, 0x6f, 0x6d, 0x2e, 0x61, 0x70, 0x69, 0x42, 0x0f, 0x44,
	0x61, 0x74, 0x61, 0x73, 0x74, 0x72, 0x65, 0x61, 0x6d, 0x50, 0x72, 0x6f, 0x74, 0x6f, 0x50, 0x01,
	0x5a, 0x37, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x62, 0x72, 0x6f,
	0x63, 0x61, 0x61, 0x72, 0x2f, 0x63, 0x68, 0x69, 0x72, 0x70, 0x73, 0x74, 0x61, 0x63, 0x6b, 0x2d,
	0x61, 0x70, 0x69, 0x2f, 0x67, 0x6f, 0x2f, 0x76, 0x33, 0x2f, 0x61, 0x73, 0x2f, 0x65, 0x78, 0x74,
	0x65, 0x72, 0x6e, 0x61, 0x6c, 0x2f, 0x61, 0x70, 0x69, 0xa2, 0x02, 0x03, 0x41, 0x58, 0x58, 0xaa,
	0x02, 0x03, 0x41, 0x70, 0x69, 0xca, 0x02, 0x03, 0x41, 0x70, 0x69, 0xe2, 0x02, 0x0f, 0x41, 0x70,
	0x69, 0x5c, 0x47, 0x50, 0x42, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0xea, 0x02, 0x03,
	0x41, 0x70, 0x69, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_as_external_api_datastream_proto_rawDescOnce sync.Once
	file_as_external_api_datastream_proto_rawDescData = file_as_external_api_datastream_proto_rawDesc
)

func file_as_external_api_datastream_proto_rawDescGZIP() []byte {
	file_as_external_api_datastream_proto_rawDescOnce.Do(func() {
		file_as_external_api_datastream_proto_rawDescData = protoimpl.X.CompressGZIP(file_as_external_api_datastream_proto_rawDescData)
	})
	return file_as_external_api_datastream_proto_rawDescData
}

var file_as_external_api_datastream_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_as_external_api_datastream_proto_goTypes = []interface{}{
	(*DataStreamRequest)(nil),  // 0: api.DataStreamRequest
	(*DataStreamResponse)(nil), // 1: api.DataStreamResponse
}
var file_as_external_api_datastream_proto_depIdxs = []int32{
	0, // 0: api.DataStreamService.GetGatewayTaskResult:input_type -> api.DataStreamRequest
	1, // 1: api.DataStreamService.GetGatewayTaskResult:output_type -> api.DataStreamResponse
	1, // [1:2] is the sub-list for method output_type
	0, // [0:1] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_as_external_api_datastream_proto_init() }
func file_as_external_api_datastream_proto_init() {
	if File_as_external_api_datastream_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_as_external_api_datastream_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DataStreamRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_as_external_api_datastream_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DataStreamResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	file_as_external_api_datastream_proto_msgTypes[1].OneofWrappers = []interface{}{
		(*DataStreamResponse_Current)(nil),
		(*DataStreamResponse_Total)(nil),
		(*DataStreamResponse_Rows)(nil),
		(*DataStreamResponse_Chunk)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_as_external_api_datastream_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_as_external_api_datastream_proto_goTypes,
		DependencyIndexes: file_as_external_api_datastream_proto_depIdxs,
		MessageInfos:      file_as_external_api_datastream_proto_msgTypes,
	}.Build()
	File_as_external_api_datastream_proto = out.File
	file_as_external_api_datastream_proto_rawDesc = nil
	file_as_external_api_datastream_proto_goTypes = nil
	file_as_external_api_datastream_proto_depIdxs = nil
}
