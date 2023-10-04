// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.29.1
// 	protoc        (unknown)
// source: as/external/api/dataexport.proto

package api

import (
	handyrusty "github.com/brocaar/chirpstack-api/go/v3/handyrusty"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type DataExportRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Organization ID.
	OrgId int64 `protobuf:"varint,1,opt,name=org_id,json=orgId,proto3" json:"org_id,omitempty"`
	// network_server id
	NsId int64 `protobuf:"varint,2,opt,name=ns_id,json=nsId,proto3" json:"ns_id,omitempty"`
}

func (x *DataExportRequest) Reset() {
	*x = DataExportRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_as_external_api_dataexport_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DataExportRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DataExportRequest) ProtoMessage() {}

func (x *DataExportRequest) ProtoReflect() protoreflect.Message {
	mi := &file_as_external_api_dataexport_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DataExportRequest.ProtoReflect.Descriptor instead.
func (*DataExportRequest) Descriptor() ([]byte, []int) {
	return file_as_external_api_dataexport_proto_rawDescGZIP(), []int{0}
}

func (x *DataExportRequest) GetOrgId() int64 {
	if x != nil {
		return x.OrgId
	}
	return 0
}

func (x *DataExportRequest) GetNsId() int64 {
	if x != nil {
		return x.NsId
	}
	return 0
}

type StreamResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Types that are assignable to Row:
	//
	//	*StreamResponse_Current
	//	*StreamResponse_Total
	Row   isStreamResponse_Row `protobuf_oneof:"row"`
	Chunk []byte               `protobuf:"bytes,3,opt,name=chunk,proto3" json:"chunk,omitempty"`
}

func (x *StreamResponse) Reset() {
	*x = StreamResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_as_external_api_dataexport_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *StreamResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*StreamResponse) ProtoMessage() {}

func (x *StreamResponse) ProtoReflect() protoreflect.Message {
	mi := &file_as_external_api_dataexport_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use StreamResponse.ProtoReflect.Descriptor instead.
func (*StreamResponse) Descriptor() ([]byte, []int) {
	return file_as_external_api_dataexport_proto_rawDescGZIP(), []int{1}
}

func (m *StreamResponse) GetRow() isStreamResponse_Row {
	if m != nil {
		return m.Row
	}
	return nil
}

func (x *StreamResponse) GetCurrent() uint32 {
	if x, ok := x.GetRow().(*StreamResponse_Current); ok {
		return x.Current
	}
	return 0
}

func (x *StreamResponse) GetTotal() uint32 {
	if x, ok := x.GetRow().(*StreamResponse_Total); ok {
		return x.Total
	}
	return 0
}

func (x *StreamResponse) GetChunk() []byte {
	if x != nil {
		return x.Chunk
	}
	return nil
}

type isStreamResponse_Row interface {
	isStreamResponse_Row()
}

type StreamResponse_Current struct {
	Current uint32 `protobuf:"varint,1,opt,name=current,proto3,oneof"`
}

type StreamResponse_Total struct {
	Total uint32 `protobuf:"varint,2,opt,name=total,proto3,oneof"`
}

func (*StreamResponse_Current) isStreamResponse_Row() {}

func (*StreamResponse_Total) isStreamResponse_Row() {}

var File_as_external_api_dataexport_proto protoreflect.FileDescriptor

var file_as_external_api_dataexport_proto_rawDesc = []byte{
	0x0a, 0x20, 0x61, 0x73, 0x2f, 0x65, 0x78, 0x74, 0x65, 0x72, 0x6e, 0x61, 0x6c, 0x2f, 0x61, 0x70,
	0x69, 0x2f, 0x64, 0x61, 0x74, 0x61, 0x65, 0x78, 0x70, 0x6f, 0x72, 0x74, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x12, 0x03, 0x61, 0x70, 0x69, 0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f,
	0x61, 0x70, 0x69, 0x2f, 0x61, 0x6e, 0x6e, 0x6f, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1b, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x65, 0x6d, 0x70, 0x74, 0x79, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x1a, 0x13, 0x68, 0x61, 0x6e, 0x64, 0x79, 0x72, 0x75, 0x73, 0x74, 0x79, 0x2f, 0x68,
	0x72, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x3f, 0x0a, 0x11, 0x44, 0x61, 0x74, 0x61, 0x45,
	0x78, 0x70, 0x6f, 0x72, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x15, 0x0a, 0x06,
	0x6f, 0x72, 0x67, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x03, 0x52, 0x05, 0x6f, 0x72,
	0x67, 0x49, 0x64, 0x12, 0x13, 0x0a, 0x05, 0x6e, 0x73, 0x5f, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x03, 0x52, 0x04, 0x6e, 0x73, 0x49, 0x64, 0x22, 0x61, 0x0a, 0x0e, 0x53, 0x74, 0x72, 0x65,
	0x61, 0x6d, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x1a, 0x0a, 0x07, 0x63, 0x75,
	0x72, 0x72, 0x65, 0x6e, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0d, 0x48, 0x00, 0x52, 0x07, 0x63,
	0x75, 0x72, 0x72, 0x65, 0x6e, 0x74, 0x12, 0x16, 0x0a, 0x05, 0x74, 0x6f, 0x74, 0x61, 0x6c, 0x18,
	0x02, 0x20, 0x01, 0x28, 0x0d, 0x48, 0x00, 0x52, 0x05, 0x74, 0x6f, 0x74, 0x61, 0x6c, 0x12, 0x14,
	0x0a, 0x05, 0x63, 0x68, 0x75, 0x6e, 0x6b, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0c, 0x52, 0x05, 0x63,
	0x68, 0x75, 0x6e, 0x6b, 0x42, 0x05, 0x0a, 0x03, 0x72, 0x6f, 0x77, 0x32, 0xc7, 0x03, 0x0a, 0x11,
	0x44, 0x61, 0x74, 0x61, 0x45, 0x78, 0x70, 0x6f, 0x72, 0x74, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63,
	0x65, 0x12, 0x5e, 0x0a, 0x0b, 0x47, 0x65, 0x74, 0x47, 0x61, 0x74, 0x65, 0x77, 0x61, 0x79, 0x73,
	0x12, 0x16, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x44, 0x61, 0x74, 0x61, 0x45, 0x78, 0x70, 0x6f, 0x72,
	0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x13, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x53,
	0x74, 0x72, 0x65, 0x61, 0x6d, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x20, 0x82,
	0xd3, 0xe4, 0x93, 0x02, 0x1a, 0x12, 0x18, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x64, 0x61, 0x74, 0x61,
	0x65, 0x78, 0x70, 0x6f, 0x72, 0x74, 0x2f, 0x67, 0x61, 0x74, 0x65, 0x77, 0x61, 0x79, 0x73, 0x30,
	0x01, 0x12, 0x58, 0x0a, 0x08, 0x47, 0x65, 0x74, 0x55, 0x73, 0x65, 0x72, 0x73, 0x12, 0x16, 0x2e,
	0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e,
	0x45, 0x6d, 0x70, 0x74, 0x79, 0x1a, 0x13, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x53, 0x74, 0x72, 0x65,
	0x61, 0x6d, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x1d, 0x82, 0xd3, 0xe4, 0x93,
	0x02, 0x17, 0x12, 0x15, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x64, 0x61, 0x74, 0x61, 0x65, 0x78, 0x70,
	0x6f, 0x72, 0x74, 0x2f, 0x75, 0x73, 0x65, 0x72, 0x73, 0x30, 0x01, 0x12, 0x5c, 0x0a, 0x0a, 0x47,
	0x65, 0x74, 0x44, 0x65, 0x76, 0x69, 0x63, 0x65, 0x73, 0x12, 0x16, 0x2e, 0x61, 0x70, 0x69, 0x2e,
	0x44, 0x61, 0x74, 0x61, 0x45, 0x78, 0x70, 0x6f, 0x72, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x1a, 0x13, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x53, 0x74, 0x72, 0x65, 0x61, 0x6d, 0x52, 0x65,
	0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x1f, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x19, 0x12, 0x17,
	0x2f, 0x61, 0x70, 0x69, 0x2f, 0x64, 0x61, 0x74, 0x61, 0x65, 0x78, 0x70, 0x6f, 0x72, 0x74, 0x2f,
	0x64, 0x65, 0x76, 0x69, 0x63, 0x65, 0x73, 0x30, 0x01, 0x12, 0x99, 0x01, 0x0a, 0x1a, 0x43, 0x6f,
	0x75, 0x6e, 0x74, 0x44, 0x65, 0x76, 0x69, 0x63, 0x65, 0x46, 0x72, 0x61, 0x6d, 0x65, 0x73, 0x50,
	0x65, 0x72, 0x44, 0x65, 0x76, 0x45, 0x75, 0x69, 0x12, 0x25, 0x2e, 0x68, 0x72, 0x2e, 0x43, 0x6f,
	0x75, 0x6e, 0x74, 0x44, 0x65, 0x76, 0x69, 0x63, 0x65, 0x46, 0x72, 0x61, 0x6d, 0x65, 0x73, 0x50,
	0x65, 0x72, 0x44, 0x65, 0x76, 0x45, 0x75, 0x69, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a,
	0x26, 0x2e, 0x68, 0x72, 0x2e, 0x43, 0x6f, 0x75, 0x6e, 0x74, 0x44, 0x65, 0x76, 0x69, 0x63, 0x65,
	0x46, 0x72, 0x61, 0x6d, 0x65, 0x73, 0x50, 0x65, 0x72, 0x44, 0x65, 0x76, 0x45, 0x75, 0x69, 0x52,
	0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x2c, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x26, 0x12,
	0x24, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x64, 0x61, 0x74, 0x61, 0x65, 0x78, 0x70, 0x6f, 0x72, 0x74,
	0x2f, 0x64, 0x65, 0x76, 0x69, 0x63, 0x65, 0x73, 0x2f, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x5f, 0x66,
	0x72, 0x61, 0x6d, 0x65, 0x73, 0x42, 0x7f, 0x0a, 0x07, 0x63, 0x6f, 0x6d, 0x2e, 0x61, 0x70, 0x69,
	0x42, 0x0f, 0x44, 0x61, 0x74, 0x61, 0x65, 0x78, 0x70, 0x6f, 0x72, 0x74, 0x50, 0x72, 0x6f, 0x74,
	0x6f, 0x50, 0x01, 0x5a, 0x37, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f,
	0x62, 0x72, 0x6f, 0x63, 0x61, 0x61, 0x72, 0x2f, 0x63, 0x68, 0x69, 0x72, 0x70, 0x73, 0x74, 0x61,
	0x63, 0x6b, 0x2d, 0x61, 0x70, 0x69, 0x2f, 0x67, 0x6f, 0x2f, 0x76, 0x33, 0x2f, 0x61, 0x73, 0x2f,
	0x65, 0x78, 0x74, 0x65, 0x72, 0x6e, 0x61, 0x6c, 0x2f, 0x61, 0x70, 0x69, 0xa2, 0x02, 0x03, 0x41,
	0x58, 0x58, 0xaa, 0x02, 0x03, 0x41, 0x70, 0x69, 0xca, 0x02, 0x03, 0x41, 0x70, 0x69, 0xe2, 0x02,
	0x0f, 0x41, 0x70, 0x69, 0x5c, 0x47, 0x50, 0x42, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61,
	0xea, 0x02, 0x03, 0x41, 0x70, 0x69, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_as_external_api_dataexport_proto_rawDescOnce sync.Once
	file_as_external_api_dataexport_proto_rawDescData = file_as_external_api_dataexport_proto_rawDesc
)

func file_as_external_api_dataexport_proto_rawDescGZIP() []byte {
	file_as_external_api_dataexport_proto_rawDescOnce.Do(func() {
		file_as_external_api_dataexport_proto_rawDescData = protoimpl.X.CompressGZIP(file_as_external_api_dataexport_proto_rawDescData)
	})
	return file_as_external_api_dataexport_proto_rawDescData
}

var file_as_external_api_dataexport_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_as_external_api_dataexport_proto_goTypes = []interface{}{
	(*DataExportRequest)(nil),                             // 0: api.DataExportRequest
	(*StreamResponse)(nil),                                // 1: api.StreamResponse
	(*emptypb.Empty)(nil),                                 // 2: google.protobuf.Empty
	(*handyrusty.CountDeviceFramesPerDevEuiRequest)(nil),  // 3: hr.CountDeviceFramesPerDevEuiRequest
	(*handyrusty.CountDeviceFramesPerDevEuiResponse)(nil), // 4: hr.CountDeviceFramesPerDevEuiResponse
}
var file_as_external_api_dataexport_proto_depIdxs = []int32{
	0, // 0: api.DataExportService.GetGateways:input_type -> api.DataExportRequest
	2, // 1: api.DataExportService.GetUsers:input_type -> google.protobuf.Empty
	0, // 2: api.DataExportService.GetDevices:input_type -> api.DataExportRequest
	3, // 3: api.DataExportService.CountDeviceFramesPerDevEui:input_type -> hr.CountDeviceFramesPerDevEuiRequest
	1, // 4: api.DataExportService.GetGateways:output_type -> api.StreamResponse
	1, // 5: api.DataExportService.GetUsers:output_type -> api.StreamResponse
	1, // 6: api.DataExportService.GetDevices:output_type -> api.StreamResponse
	4, // 7: api.DataExportService.CountDeviceFramesPerDevEui:output_type -> hr.CountDeviceFramesPerDevEuiResponse
	4, // [4:8] is the sub-list for method output_type
	0, // [0:4] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_as_external_api_dataexport_proto_init() }
func file_as_external_api_dataexport_proto_init() {
	if File_as_external_api_dataexport_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_as_external_api_dataexport_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DataExportRequest); i {
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
		file_as_external_api_dataexport_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*StreamResponse); i {
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
	file_as_external_api_dataexport_proto_msgTypes[1].OneofWrappers = []interface{}{
		(*StreamResponse_Current)(nil),
		(*StreamResponse_Total)(nil),
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_as_external_api_dataexport_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_as_external_api_dataexport_proto_goTypes,
		DependencyIndexes: file_as_external_api_dataexport_proto_depIdxs,
		MessageInfos:      file_as_external_api_dataexport_proto_msgTypes,
	}.Build()
	File_as_external_api_dataexport_proto = out.File
	file_as_external_api_dataexport_proto_rawDesc = nil
	file_as_external_api_dataexport_proto_goTypes = nil
	file_as_external_api_dataexport_proto_depIdxs = nil
}
