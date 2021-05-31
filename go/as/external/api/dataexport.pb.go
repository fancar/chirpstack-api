// Code generated by protoc-gen-go. DO NOT EDIT.
// source: as/external/api/dataexport.proto

package api

import (
	context "context"
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type DataExportRequest struct {
	// Organization ID.
	OrgId                int64    `protobuf:"varint,1,opt,name=org_id,json=orgId,proto3" json:"org_id,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *DataExportRequest) Reset()         { *m = DataExportRequest{} }
func (m *DataExportRequest) String() string { return proto.CompactTextString(m) }
func (*DataExportRequest) ProtoMessage()    {}
func (*DataExportRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_e59c4be113f4b214, []int{0}
}

func (m *DataExportRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_DataExportRequest.Unmarshal(m, b)
}
func (m *DataExportRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_DataExportRequest.Marshal(b, m, deterministic)
}
func (m *DataExportRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_DataExportRequest.Merge(m, src)
}
func (m *DataExportRequest) XXX_Size() int {
	return xxx_messageInfo_DataExportRequest.Size(m)
}
func (m *DataExportRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_DataExportRequest.DiscardUnknown(m)
}

var xxx_messageInfo_DataExportRequest proto.InternalMessageInfo

func (m *DataExportRequest) GetOrgId() int64 {
	if m != nil {
		return m.OrgId
	}
	return 0
}

type StreamResponse struct {
	// Types that are valid to be assigned to Size:
	//	*StreamResponse_Current
	//	*StreamResponse_Total
	Size isStreamResponse_Size `protobuf_oneof:"size"`
	// Types that are valid to be assigned to Data:
	//	*StreamResponse_Rows
	//	*StreamResponse_Chunk
	Data                 isStreamResponse_Data `protobuf_oneof:"data"`
	XXX_NoUnkeyedLiteral struct{}              `json:"-"`
	XXX_unrecognized     []byte                `json:"-"`
	XXX_sizecache        int32                 `json:"-"`
}

func (m *StreamResponse) Reset()         { *m = StreamResponse{} }
func (m *StreamResponse) String() string { return proto.CompactTextString(m) }
func (*StreamResponse) ProtoMessage()    {}
func (*StreamResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_e59c4be113f4b214, []int{1}
}

func (m *StreamResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_StreamResponse.Unmarshal(m, b)
}
func (m *StreamResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_StreamResponse.Marshal(b, m, deterministic)
}
func (m *StreamResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_StreamResponse.Merge(m, src)
}
func (m *StreamResponse) XXX_Size() int {
	return xxx_messageInfo_StreamResponse.Size(m)
}
func (m *StreamResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_StreamResponse.DiscardUnknown(m)
}

var xxx_messageInfo_StreamResponse proto.InternalMessageInfo

type isStreamResponse_Size interface {
	isStreamResponse_Size()
}

type StreamResponse_Current struct {
	Current uint32 `protobuf:"varint,1,opt,name=current,proto3,oneof"`
}

type StreamResponse_Total struct {
	Total uint32 `protobuf:"varint,2,opt,name=total,proto3,oneof"`
}

func (*StreamResponse_Current) isStreamResponse_Size() {}

func (*StreamResponse_Total) isStreamResponse_Size() {}

func (m *StreamResponse) GetSize() isStreamResponse_Size {
	if m != nil {
		return m.Size
	}
	return nil
}

func (m *StreamResponse) GetCurrent() uint32 {
	if x, ok := m.GetSize().(*StreamResponse_Current); ok {
		return x.Current
	}
	return 0
}

func (m *StreamResponse) GetTotal() uint32 {
	if x, ok := m.GetSize().(*StreamResponse_Total); ok {
		return x.Total
	}
	return 0
}

type isStreamResponse_Data interface {
	isStreamResponse_Data()
}

type StreamResponse_Rows struct {
	Rows uint32 `protobuf:"varint,3,opt,name=rows,proto3,oneof"`
}

type StreamResponse_Chunk struct {
	Chunk []byte `protobuf:"bytes,4,opt,name=chunk,proto3,oneof"`
}

func (*StreamResponse_Rows) isStreamResponse_Data() {}

func (*StreamResponse_Chunk) isStreamResponse_Data() {}

func (m *StreamResponse) GetData() isStreamResponse_Data {
	if m != nil {
		return m.Data
	}
	return nil
}

func (m *StreamResponse) GetRows() uint32 {
	if x, ok := m.GetData().(*StreamResponse_Rows); ok {
		return x.Rows
	}
	return 0
}

func (m *StreamResponse) GetChunk() []byte {
	if x, ok := m.GetData().(*StreamResponse_Chunk); ok {
		return x.Chunk
	}
	return nil
}

// XXX_OneofWrappers is for the internal use of the proto package.
func (*StreamResponse) XXX_OneofWrappers() []interface{} {
	return []interface{}{
		(*StreamResponse_Current)(nil),
		(*StreamResponse_Total)(nil),
		(*StreamResponse_Rows)(nil),
		(*StreamResponse_Chunk)(nil),
	}
}

func init() {
	proto.RegisterType((*DataExportRequest)(nil), "api.DataExportRequest")
	proto.RegisterType((*StreamResponse)(nil), "api.StreamResponse")
}

func init() {
	proto.RegisterFile("as/external/api/dataexport.proto", fileDescriptor_e59c4be113f4b214)
}

var fileDescriptor_e59c4be113f4b214 = []byte{
	// 369 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x94, 0x92, 0xcf, 0xaa, 0xd3, 0x40,
	0x14, 0xc6, 0x9d, 0xfe, 0x53, 0xc6, 0x3f, 0xe0, 0x68, 0xdb, 0x18, 0x14, 0x43, 0x57, 0x45, 0x30,
	0x53, 0xec, 0x42, 0xdc, 0x96, 0x4a, 0xea, 0x36, 0x45, 0x10, 0x11, 0xe5, 0x34, 0x39, 0xa4, 0x43,
	0xdb, 0x4c, 0x9c, 0x39, 0x69, 0xab, 0xcb, 0xbe, 0x82, 0x8f, 0xe1, 0xe3, 0xf8, 0x0a, 0x3e, 0xc8,
	0x25, 0x93, 0x5e, 0xb8, 0x37, 0x77, 0xd5, 0xd5, 0xf0, 0x7d, 0xf3, 0x9d, 0x1f, 0xf3, 0x0d, 0x87,
	0x07, 0x60, 0x25, 0x1e, 0x09, 0x4d, 0x0e, 0x5b, 0x09, 0x85, 0x92, 0x29, 0x10, 0xe0, 0xb1, 0xd0,
	0x86, 0xc2, 0xc2, 0x68, 0xd2, 0xa2, 0x0d, 0x85, 0xf2, 0x5f, 0x66, 0x5a, 0x67, 0x5b, 0x74, 0x09,
	0xc8, 0x73, 0x4d, 0x40, 0x4a, 0xe7, 0xb6, 0x8e, 0x8c, 0xde, 0xf0, 0xa7, 0x73, 0x20, 0xf8, 0xe8,
	0xc6, 0x62, 0xfc, 0x59, 0xa2, 0x25, 0xd1, 0xe7, 0x3d, 0x6d, 0xb2, 0x1f, 0x2a, 0xf5, 0x58, 0xc0,
	0xc6, 0xed, 0xb8, 0xab, 0x4d, 0xf6, 0x29, 0x1d, 0x9d, 0x18, 0x7f, 0xb2, 0x24, 0x83, 0xb0, 0x8b,
	0xd1, 0x16, 0x3a, 0xb7, 0x28, 0x7c, 0x7e, 0x3f, 0x29, 0x8d, 0xc1, 0x9c, 0x5c, 0xf4, 0xf1, 0xe2,
	0x5e, 0x7c, 0x6d, 0x88, 0x01, 0xef, 0x92, 0x26, 0xd8, 0x7a, 0xad, 0xf3, 0x4d, 0x2d, 0xc5, 0x73,
	0xde, 0x31, 0xfa, 0x60, 0xbd, 0xb6, 0xb3, 0x59, 0xec, 0x54, 0x95, 0x4e, 0xd6, 0x65, 0xbe, 0xf1,
	0x3a, 0x01, 0x1b, 0x3f, 0x5a, 0xb0, 0xb8, 0x96, 0xb3, 0x1e, 0xef, 0x58, 0xf5, 0x1b, 0xab, 0xb3,
	0xea, 0xf7, 0xee, 0x6f, 0xeb, 0xe6, 0x8b, 0x97, 0x68, 0xf6, 0x2a, 0x41, 0xf1, 0x9d, 0x3f, 0x8c,
	0x90, 0x22, 0x20, 0x3c, 0xc0, 0x2f, 0x2b, 0x06, 0x21, 0x14, 0x2a, 0xbc, 0x53, 0xcc, 0x7f, 0xe6,
	0xfc, 0xdb, 0x1d, 0x46, 0xc1, 0xe9, 0xdf, 0xff, 0x3f, 0x2d, 0x5f, 0x78, 0x8d, 0x4f, 0x94, 0xd9,
	0x19, 0x37, 0x61, 0xe2, 0x0b, 0x7f, 0x10, 0x21, 0x7d, 0xb6, 0x68, 0x2e, 0x84, 0xbf, 0x72, 0xf0,
	0xa1, 0xe8, 0x37, 0xe1, 0x65, 0xc5, 0x9a, 0x30, 0xf1, 0x8d, 0xf3, 0x08, 0x69, 0x8e, 0x55, 0x8d,
	0x0b, 0xd9, 0xaf, 0x1d, 0xfb, 0x85, 0x18, 0x36, 0xd9, 0x69, 0x4d, 0x9b, 0xb0, 0xd9, 0x87, 0xaf,
	0xef, 0x33, 0x45, 0xeb, 0x72, 0x15, 0x26, 0x7a, 0x27, 0x57, 0x46, 0x27, 0x00, 0x46, 0x26, 0x6b,
	0x65, 0x0a, 0x4b, 0x90, 0x6c, 0xde, 0x56, 0x93, 0x99, 0x96, 0xfb, 0xa9, 0x6c, 0x6c, 0xd3, 0xaa,
	0xe7, 0x16, 0x64, 0x7a, 0x15, 0x00, 0x00, 0xff, 0xff, 0xc7, 0x97, 0x61, 0xf3, 0x67, 0x02, 0x00,
	0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConnInterface

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion6

// DataExportServiceClient is the client API for DataExportService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type DataExportServiceClient interface {
	// GetGateways Export gateways
	GetGateways(ctx context.Context, in *DataExportRequest, opts ...grpc.CallOption) (DataExportService_GetGatewaysClient, error)
	// GetUsers Export users
	GetUsers(ctx context.Context, in *DataExportRequest, opts ...grpc.CallOption) (DataExportService_GetUsersClient, error)
	// GetDevices Export devices
	GetDevices(ctx context.Context, in *DataExportRequest, opts ...grpc.CallOption) (DataExportService_GetDevicesClient, error)
}

type dataExportServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewDataExportServiceClient(cc grpc.ClientConnInterface) DataExportServiceClient {
	return &dataExportServiceClient{cc}
}

func (c *dataExportServiceClient) GetGateways(ctx context.Context, in *DataExportRequest, opts ...grpc.CallOption) (DataExportService_GetGatewaysClient, error) {
	stream, err := c.cc.NewStream(ctx, &_DataExportService_serviceDesc.Streams[0], "/api.DataExportService/GetGateways", opts...)
	if err != nil {
		return nil, err
	}
	x := &dataExportServiceGetGatewaysClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type DataExportService_GetGatewaysClient interface {
	Recv() (*StreamResponse, error)
	grpc.ClientStream
}

type dataExportServiceGetGatewaysClient struct {
	grpc.ClientStream
}

func (x *dataExportServiceGetGatewaysClient) Recv() (*StreamResponse, error) {
	m := new(StreamResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *dataExportServiceClient) GetUsers(ctx context.Context, in *DataExportRequest, opts ...grpc.CallOption) (DataExportService_GetUsersClient, error) {
	stream, err := c.cc.NewStream(ctx, &_DataExportService_serviceDesc.Streams[1], "/api.DataExportService/GetUsers", opts...)
	if err != nil {
		return nil, err
	}
	x := &dataExportServiceGetUsersClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type DataExportService_GetUsersClient interface {
	Recv() (*StreamResponse, error)
	grpc.ClientStream
}

type dataExportServiceGetUsersClient struct {
	grpc.ClientStream
}

func (x *dataExportServiceGetUsersClient) Recv() (*StreamResponse, error) {
	m := new(StreamResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *dataExportServiceClient) GetDevices(ctx context.Context, in *DataExportRequest, opts ...grpc.CallOption) (DataExportService_GetDevicesClient, error) {
	stream, err := c.cc.NewStream(ctx, &_DataExportService_serviceDesc.Streams[2], "/api.DataExportService/GetDevices", opts...)
	if err != nil {
		return nil, err
	}
	x := &dataExportServiceGetDevicesClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type DataExportService_GetDevicesClient interface {
	Recv() (*StreamResponse, error)
	grpc.ClientStream
}

type dataExportServiceGetDevicesClient struct {
	grpc.ClientStream
}

func (x *dataExportServiceGetDevicesClient) Recv() (*StreamResponse, error) {
	m := new(StreamResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

// DataExportServiceServer is the server API for DataExportService service.
type DataExportServiceServer interface {
	// GetGateways Export gateways
	GetGateways(*DataExportRequest, DataExportService_GetGatewaysServer) error
	// GetUsers Export users
	GetUsers(*DataExportRequest, DataExportService_GetUsersServer) error
	// GetDevices Export devices
	GetDevices(*DataExportRequest, DataExportService_GetDevicesServer) error
}

// UnimplementedDataExportServiceServer can be embedded to have forward compatible implementations.
type UnimplementedDataExportServiceServer struct {
}

func (*UnimplementedDataExportServiceServer) GetGateways(req *DataExportRequest, srv DataExportService_GetGatewaysServer) error {
	return status.Errorf(codes.Unimplemented, "method GetGateways not implemented")
}
func (*UnimplementedDataExportServiceServer) GetUsers(req *DataExportRequest, srv DataExportService_GetUsersServer) error {
	return status.Errorf(codes.Unimplemented, "method GetUsers not implemented")
}
func (*UnimplementedDataExportServiceServer) GetDevices(req *DataExportRequest, srv DataExportService_GetDevicesServer) error {
	return status.Errorf(codes.Unimplemented, "method GetDevices not implemented")
}

func RegisterDataExportServiceServer(s *grpc.Server, srv DataExportServiceServer) {
	s.RegisterService(&_DataExportService_serviceDesc, srv)
}

func _DataExportService_GetGateways_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(DataExportRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(DataExportServiceServer).GetGateways(m, &dataExportServiceGetGatewaysServer{stream})
}

type DataExportService_GetGatewaysServer interface {
	Send(*StreamResponse) error
	grpc.ServerStream
}

type dataExportServiceGetGatewaysServer struct {
	grpc.ServerStream
}

func (x *dataExportServiceGetGatewaysServer) Send(m *StreamResponse) error {
	return x.ServerStream.SendMsg(m)
}

func _DataExportService_GetUsers_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(DataExportRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(DataExportServiceServer).GetUsers(m, &dataExportServiceGetUsersServer{stream})
}

type DataExportService_GetUsersServer interface {
	Send(*StreamResponse) error
	grpc.ServerStream
}

type dataExportServiceGetUsersServer struct {
	grpc.ServerStream
}

func (x *dataExportServiceGetUsersServer) Send(m *StreamResponse) error {
	return x.ServerStream.SendMsg(m)
}

func _DataExportService_GetDevices_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(DataExportRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(DataExportServiceServer).GetDevices(m, &dataExportServiceGetDevicesServer{stream})
}

type DataExportService_GetDevicesServer interface {
	Send(*StreamResponse) error
	grpc.ServerStream
}

type dataExportServiceGetDevicesServer struct {
	grpc.ServerStream
}

func (x *dataExportServiceGetDevicesServer) Send(m *StreamResponse) error {
	return x.ServerStream.SendMsg(m)
}

var _DataExportService_serviceDesc = grpc.ServiceDesc{
	ServiceName: "api.DataExportService",
	HandlerType: (*DataExportServiceServer)(nil),
	Methods:     []grpc.MethodDesc{},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "GetGateways",
			Handler:       _DataExportService_GetGateways_Handler,
			ServerStreams: true,
		},
		{
			StreamName:    "GetUsers",
			Handler:       _DataExportService_GetUsers_Handler,
			ServerStreams: true,
		},
		{
			StreamName:    "GetDevices",
			Handler:       _DataExportService_GetDevices_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "as/external/api/dataexport.proto",
}
