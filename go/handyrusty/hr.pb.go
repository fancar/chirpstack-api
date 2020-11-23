// Code generated by protoc-gen-go. DO NOT EDIT.
// source: handyrusty/hr.proto

package handyrusty

import (
	context "context"
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	empty "github.com/golang/protobuf/ptypes/empty"
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

type GetDeviceCountersRequest struct {
	// organisation that handles the devices
	OrganizationId uint32 `protobuf:"varint,1,opt,name=organization_id,json=organizationId,proto3" json:"organization_id,omitempty"`
	// start from time and date
	Start string `protobuf:"bytes,2,opt,name=start,proto3" json:"start,omitempty"`
	// end time and date
	End string `protobuf:"bytes,3,opt,name=end,proto3" json:"end,omitempty"`
	// aggregation of data: HOUR,DAY,WEEK,MONTH
	Aggregation          string   `protobuf:"bytes,4,opt,name=aggregation,proto3" json:"aggregation,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *GetDeviceCountersRequest) Reset()         { *m = GetDeviceCountersRequest{} }
func (m *GetDeviceCountersRequest) String() string { return proto.CompactTextString(m) }
func (*GetDeviceCountersRequest) ProtoMessage()    {}
func (*GetDeviceCountersRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_97d7a55acfa39588, []int{0}
}

func (m *GetDeviceCountersRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_GetDeviceCountersRequest.Unmarshal(m, b)
}
func (m *GetDeviceCountersRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_GetDeviceCountersRequest.Marshal(b, m, deterministic)
}
func (m *GetDeviceCountersRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_GetDeviceCountersRequest.Merge(m, src)
}
func (m *GetDeviceCountersRequest) XXX_Size() int {
	return xxx_messageInfo_GetDeviceCountersRequest.Size(m)
}
func (m *GetDeviceCountersRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_GetDeviceCountersRequest.DiscardUnknown(m)
}

var xxx_messageInfo_GetDeviceCountersRequest proto.InternalMessageInfo

func (m *GetDeviceCountersRequest) GetOrganizationId() uint32 {
	if m != nil {
		return m.OrganizationId
	}
	return 0
}

func (m *GetDeviceCountersRequest) GetStart() string {
	if m != nil {
		return m.Start
	}
	return ""
}

func (m *GetDeviceCountersRequest) GetEnd() string {
	if m != nil {
		return m.End
	}
	return ""
}

func (m *GetDeviceCountersRequest) GetAggregation() string {
	if m != nil {
		return m.Aggregation
	}
	return ""
}

type GetDeviceCountersResponse struct {
	// id of the organisation that handles the devices
	OrganizationId       uint32            `protobuf:"varint,1,opt,name=organization_id,json=organizationId,proto3" json:"organization_id,omitempty"`
	Counters             []*DeviceCounters `protobuf:"bytes,2,rep,name=counters,proto3" json:"counters,omitempty"`
	XXX_NoUnkeyedLiteral struct{}          `json:"-"`
	XXX_unrecognized     []byte            `json:"-"`
	XXX_sizecache        int32             `json:"-"`
}

func (m *GetDeviceCountersResponse) Reset()         { *m = GetDeviceCountersResponse{} }
func (m *GetDeviceCountersResponse) String() string { return proto.CompactTextString(m) }
func (*GetDeviceCountersResponse) ProtoMessage()    {}
func (*GetDeviceCountersResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_97d7a55acfa39588, []int{1}
}

func (m *GetDeviceCountersResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_GetDeviceCountersResponse.Unmarshal(m, b)
}
func (m *GetDeviceCountersResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_GetDeviceCountersResponse.Marshal(b, m, deterministic)
}
func (m *GetDeviceCountersResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_GetDeviceCountersResponse.Merge(m, src)
}
func (m *GetDeviceCountersResponse) XXX_Size() int {
	return xxx_messageInfo_GetDeviceCountersResponse.Size(m)
}
func (m *GetDeviceCountersResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_GetDeviceCountersResponse.DiscardUnknown(m)
}

var xxx_messageInfo_GetDeviceCountersResponse proto.InternalMessageInfo

func (m *GetDeviceCountersResponse) GetOrganizationId() uint32 {
	if m != nil {
		return m.OrganizationId
	}
	return 0
}

func (m *GetDeviceCountersResponse) GetCounters() []*DeviceCounters {
	if m != nil {
		return m.Counters
	}
	return nil
}

type GetGatewayCountersRequest struct {
	// organisation that handles the devices
	OrganizationId uint32 `protobuf:"varint,1,opt,name=organization_id,json=organizationId,proto3" json:"organization_id,omitempty"`
	// start from time and date
	Start string `protobuf:"bytes,2,opt,name=start,proto3" json:"start,omitempty"`
	// end time and date
	End string `protobuf:"bytes,3,opt,name=end,proto3" json:"end,omitempty"`
	// aggregation of data: HOUR,DAY,WEEK,MONTH
	Aggregation          string   `protobuf:"bytes,4,opt,name=aggregation,proto3" json:"aggregation,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *GetGatewayCountersRequest) Reset()         { *m = GetGatewayCountersRequest{} }
func (m *GetGatewayCountersRequest) String() string { return proto.CompactTextString(m) }
func (*GetGatewayCountersRequest) ProtoMessage()    {}
func (*GetGatewayCountersRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_97d7a55acfa39588, []int{2}
}

func (m *GetGatewayCountersRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_GetGatewayCountersRequest.Unmarshal(m, b)
}
func (m *GetGatewayCountersRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_GetGatewayCountersRequest.Marshal(b, m, deterministic)
}
func (m *GetGatewayCountersRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_GetGatewayCountersRequest.Merge(m, src)
}
func (m *GetGatewayCountersRequest) XXX_Size() int {
	return xxx_messageInfo_GetGatewayCountersRequest.Size(m)
}
func (m *GetGatewayCountersRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_GetGatewayCountersRequest.DiscardUnknown(m)
}

var xxx_messageInfo_GetGatewayCountersRequest proto.InternalMessageInfo

func (m *GetGatewayCountersRequest) GetOrganizationId() uint32 {
	if m != nil {
		return m.OrganizationId
	}
	return 0
}

func (m *GetGatewayCountersRequest) GetStart() string {
	if m != nil {
		return m.Start
	}
	return ""
}

func (m *GetGatewayCountersRequest) GetEnd() string {
	if m != nil {
		return m.End
	}
	return ""
}

func (m *GetGatewayCountersRequest) GetAggregation() string {
	if m != nil {
		return m.Aggregation
	}
	return ""
}

type GetGatewayCountersResponse struct {
	// id of the organisation that handles the devices
	OrganizationId uint32 `protobuf:"varint,1,opt,name=organization_id,json=organizationId,proto3" json:"organization_id,omitempty"`
	// log of counters
	Counters             []*DeviceCounters `protobuf:"bytes,2,rep,name=counters,proto3" json:"counters,omitempty"`
	XXX_NoUnkeyedLiteral struct{}          `json:"-"`
	XXX_unrecognized     []byte            `json:"-"`
	XXX_sizecache        int32             `json:"-"`
}

func (m *GetGatewayCountersResponse) Reset()         { *m = GetGatewayCountersResponse{} }
func (m *GetGatewayCountersResponse) String() string { return proto.CompactTextString(m) }
func (*GetGatewayCountersResponse) ProtoMessage()    {}
func (*GetGatewayCountersResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_97d7a55acfa39588, []int{3}
}

func (m *GetGatewayCountersResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_GetGatewayCountersResponse.Unmarshal(m, b)
}
func (m *GetGatewayCountersResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_GetGatewayCountersResponse.Marshal(b, m, deterministic)
}
func (m *GetGatewayCountersResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_GetGatewayCountersResponse.Merge(m, src)
}
func (m *GetGatewayCountersResponse) XXX_Size() int {
	return xxx_messageInfo_GetGatewayCountersResponse.Size(m)
}
func (m *GetGatewayCountersResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_GetGatewayCountersResponse.DiscardUnknown(m)
}

var xxx_messageInfo_GetGatewayCountersResponse proto.InternalMessageInfo

func (m *GetGatewayCountersResponse) GetOrganizationId() uint32 {
	if m != nil {
		return m.OrganizationId
	}
	return 0
}

func (m *GetGatewayCountersResponse) GetCounters() []*DeviceCounters {
	if m != nil {
		return m.Counters
	}
	return nil
}

type GetVersionResponse struct {
	// ChirpStack Network Server version.
	Version              string   `protobuf:"bytes,1,opt,name=version,proto3" json:"version,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *GetVersionResponse) Reset()         { *m = GetVersionResponse{} }
func (m *GetVersionResponse) String() string { return proto.CompactTextString(m) }
func (*GetVersionResponse) ProtoMessage()    {}
func (*GetVersionResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_97d7a55acfa39588, []int{4}
}

func (m *GetVersionResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_GetVersionResponse.Unmarshal(m, b)
}
func (m *GetVersionResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_GetVersionResponse.Marshal(b, m, deterministic)
}
func (m *GetVersionResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_GetVersionResponse.Merge(m, src)
}
func (m *GetVersionResponse) XXX_Size() int {
	return xxx_messageInfo_GetVersionResponse.Size(m)
}
func (m *GetVersionResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_GetVersionResponse.DiscardUnknown(m)
}

var xxx_messageInfo_GetVersionResponse proto.InternalMessageInfo

func (m *GetVersionResponse) GetVersion() string {
	if m != nil {
		return m.Version
	}
	return ""
}

type DeviceCounters struct {
	// id of the organisation that handles the devices
	OrganizationId uint32 `protobuf:"varint,1,opt,name=organization_id,json=organizationId,proto3" json:"organization_id,omitempty"`
	// Created at unix timestamp.
	CreatedAt uint32 `protobuf:"varint,2,opt,name=created_at,json=createdAt,proto3" json:"created_at,omitempty"`
	// Active count.
	ActiveCount uint32 `protobuf:"varint,3,opt,name=active_count,json=activeCount,proto3" json:"active_count,omitempty"`
	// Inactive count.
	InactiveCount uint32 `protobuf:"varint,4,opt,name=inactive_count,json=inactiveCount,proto3" json:"inactive_count,omitempty"`
	// Never seen count.
	NeverSeenCount       uint32   `protobuf:"varint,5,opt,name=never_seen_count,json=neverSeenCount,proto3" json:"never_seen_count,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *DeviceCounters) Reset()         { *m = DeviceCounters{} }
func (m *DeviceCounters) String() string { return proto.CompactTextString(m) }
func (*DeviceCounters) ProtoMessage()    {}
func (*DeviceCounters) Descriptor() ([]byte, []int) {
	return fileDescriptor_97d7a55acfa39588, []int{5}
}

func (m *DeviceCounters) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_DeviceCounters.Unmarshal(m, b)
}
func (m *DeviceCounters) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_DeviceCounters.Marshal(b, m, deterministic)
}
func (m *DeviceCounters) XXX_Merge(src proto.Message) {
	xxx_messageInfo_DeviceCounters.Merge(m, src)
}
func (m *DeviceCounters) XXX_Size() int {
	return xxx_messageInfo_DeviceCounters.Size(m)
}
func (m *DeviceCounters) XXX_DiscardUnknown() {
	xxx_messageInfo_DeviceCounters.DiscardUnknown(m)
}

var xxx_messageInfo_DeviceCounters proto.InternalMessageInfo

func (m *DeviceCounters) GetOrganizationId() uint32 {
	if m != nil {
		return m.OrganizationId
	}
	return 0
}

func (m *DeviceCounters) GetCreatedAt() uint32 {
	if m != nil {
		return m.CreatedAt
	}
	return 0
}

func (m *DeviceCounters) GetActiveCount() uint32 {
	if m != nil {
		return m.ActiveCount
	}
	return 0
}

func (m *DeviceCounters) GetInactiveCount() uint32 {
	if m != nil {
		return m.InactiveCount
	}
	return 0
}

func (m *DeviceCounters) GetNeverSeenCount() uint32 {
	if m != nil {
		return m.NeverSeenCount
	}
	return 0
}

func init() {
	proto.RegisterType((*GetDeviceCountersRequest)(nil), "hr.GetDeviceCountersRequest")
	proto.RegisterType((*GetDeviceCountersResponse)(nil), "hr.GetDeviceCountersResponse")
	proto.RegisterType((*GetGatewayCountersRequest)(nil), "hr.GetGatewayCountersRequest")
	proto.RegisterType((*GetGatewayCountersResponse)(nil), "hr.GetGatewayCountersResponse")
	proto.RegisterType((*GetVersionResponse)(nil), "hr.GetVersionResponse")
	proto.RegisterType((*DeviceCounters)(nil), "hr.DeviceCounters")
}

func init() {
	proto.RegisterFile("handyrusty/hr.proto", fileDescriptor_97d7a55acfa39588)
}

var fileDescriptor_97d7a55acfa39588 = []byte{
	// 467 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xcc, 0x54, 0x4f, 0x6f, 0xd3, 0x4e,
	0x10, 0xad, 0x93, 0xf6, 0xf7, 0x23, 0x13, 0x12, 0xda, 0x05, 0x55, 0xc6, 0x50, 0x14, 0x2c, 0x21,
	0x72, 0x61, 0x2d, 0xa5, 0x9c, 0x91, 0xf8, 0xa7, 0xc0, 0xd5, 0x15, 0x1c, 0xb8, 0x44, 0x1b, 0x7b,
	0xb0, 0x57, 0xd0, 0x5d, 0xb3, 0x3b, 0x36, 0x0a, 0xdf, 0x01, 0x3e, 0x19, 0x9f, 0x09, 0x21, 0xef,
	0x26, 0x69, 0x1b, 0x12, 0xa9, 0x17, 0x24, 0x6e, 0xd9, 0xb7, 0x6f, 0x66, 0x5e, 0xde, 0xec, 0x33,
	0xdc, 0x2e, 0x85, 0xca, 0x17, 0xa6, 0xb6, 0xb4, 0x48, 0x4a, 0xc3, 0x2b, 0xa3, 0x49, 0xb3, 0x4e,
	0x69, 0xa2, 0x7b, 0x85, 0xd6, 0xc5, 0x67, 0x4c, 0x1c, 0x32, 0xaf, 0x3f, 0x26, 0x78, 0x5e, 0xd1,
	0xc2, 0x13, 0xe2, 0xef, 0x01, 0x84, 0x53, 0xa4, 0x57, 0xd8, 0xc8, 0x0c, 0x5f, 0xea, 0x5a, 0x11,
	0x1a, 0x9b, 0xe2, 0x97, 0x1a, 0x2d, 0xb1, 0xc7, 0x70, 0x4b, 0x9b, 0x42, 0x28, 0xf9, 0x4d, 0x90,
	0xd4, 0x6a, 0x26, 0xf3, 0x30, 0x18, 0x05, 0xe3, 0x41, 0x3a, 0xbc, 0x0c, 0xbf, 0xcd, 0xd9, 0x1d,
	0x38, 0xb0, 0x24, 0x0c, 0x85, 0x9d, 0x51, 0x30, 0xee, 0xa5, 0xfe, 0xc0, 0x0e, 0xa1, 0x8b, 0x2a,
	0x0f, 0xbb, 0x0e, 0x6b, 0x7f, 0xb2, 0x11, 0xf4, 0x45, 0x51, 0x18, 0x2c, 0x5c, 0x61, 0xb8, 0xef,
	0x6e, 0x2e, 0x43, 0x31, 0xc1, 0xdd, 0x2d, 0x72, 0x6c, 0xa5, 0x95, 0xc5, 0xeb, 0xeb, 0xe1, 0x70,
	0x23, 0x5b, 0x16, 0x87, 0x9d, 0x51, 0x77, 0xdc, 0x9f, 0x30, 0x5e, 0x1a, 0xbe, 0xd1, 0x76, 0xcd,
	0x89, 0x7f, 0x04, 0x6e, 0xec, 0x54, 0x10, 0x7e, 0x15, 0x8b, 0x7f, 0xc0, 0x86, 0x1a, 0xa2, 0x6d,
	0x7a, 0xfe, 0xb6, 0x0f, 0x1c, 0xd8, 0x14, 0xe9, 0x3d, 0x1a, 0x2b, 0xb5, 0x5a, 0x8f, 0x0b, 0xe1,
	0xff, 0xc6, 0x43, 0x6e, 0x4c, 0x2f, 0x5d, 0x1d, 0xe3, 0x9f, 0x01, 0x0c, 0xaf, 0x36, 0xbb, 0xbe,
	0xb6, 0x13, 0x80, 0xcc, 0xa0, 0x20, 0xcc, 0x67, 0xc2, 0x3b, 0x36, 0x48, 0x7b, 0x4b, 0xe4, 0x39,
	0xb1, 0x87, 0x70, 0x53, 0x64, 0x24, 0x1b, 0x9c, 0x39, 0x75, 0xce, 0xbe, 0x41, 0xda, 0xf7, 0x98,
	0x9b, 0xc6, 0x1e, 0xc1, 0x50, 0xaa, 0x2b, 0xa4, 0x7d, 0x47, 0x1a, 0xac, 0x50, 0x4f, 0x1b, 0xc3,
	0xa1, 0xc2, 0x06, 0xcd, 0xcc, 0x22, 0xaa, 0x25, 0xf1, 0xc0, 0x4b, 0x72, 0xf8, 0x19, 0xa2, 0x72,
	0xcc, 0xc9, 0xaf, 0x00, 0x8e, 0xde, 0xb4, 0x29, 0x4a, 0xdb, 0x14, 0x9d, 0xa1, 0x69, 0xff, 0x19,
	0x4b, 0xe1, 0xe8, 0x8f, 0x27, 0xc9, 0xee, 0xb7, 0x3e, 0xee, 0x0a, 0x4e, 0x74, 0xb2, 0xe3, 0xd6,
	0x1b, 0x1a, 0xef, 0xb1, 0x77, 0xce, 0xe8, 0x8d, 0xfd, 0xb2, 0x55, 0xd9, 0xf6, 0x77, 0x18, 0x3d,
	0xd8, 0x75, 0xbd, 0x6e, 0xfb, 0x0c, 0xe0, 0x62, 0x7f, 0xec, 0x98, 0xfb, 0xe4, 0xf3, 0x55, 0xf2,
	0xf9, 0xeb, 0x36, 0xf9, 0xd1, 0xf1, 0xb2, 0xcf, 0xc6, 0x9e, 0xe3, 0xbd, 0x17, 0x4f, 0x3f, 0x4c,
	0x0a, 0x49, 0x65, 0x3d, 0xe7, 0x99, 0x3e, 0x4f, 0xe6, 0x46, 0x67, 0x42, 0x98, 0x24, 0x2b, 0xa5,
	0xa9, 0x2c, 0x89, 0xec, 0xd3, 0x13, 0x51, 0xc9, 0xa4, 0xd0, 0x49, 0x73, 0x9a, 0x5c, 0x7c, 0x6d,
	0xe6, 0xff, 0xb9, 0xfe, 0xa7, 0xbf, 0x03, 0x00, 0x00, 0xff, 0xff, 0x96, 0xb0, 0xaa, 0xea, 0x82,
	0x04, 0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConnInterface

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion6

// HandyRustyServiceClient is the client API for HandyRustyService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type HandyRustyServiceClient interface {
	// GetDeviceCounters returns the summary-counters log-items for given organisation_id
	GetDeviceCounters(ctx context.Context, in *GetDeviceCountersRequest, opts ...grpc.CallOption) (*GetDeviceCountersResponse, error)
	// GetDeviceCounters returns the summary-counters log-items for given organisation_id
	GetGatewayCounters(ctx context.Context, in *GetGatewayCountersRequest, opts ...grpc.CallOption) (*GetGatewayCountersResponse, error)
	// GetVersion returns the ChirpStack Network Server version.
	GetVersion(ctx context.Context, in *empty.Empty, opts ...grpc.CallOption) (*GetVersionResponse, error)
}

type handyRustyServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewHandyRustyServiceClient(cc grpc.ClientConnInterface) HandyRustyServiceClient {
	return &handyRustyServiceClient{cc}
}

func (c *handyRustyServiceClient) GetDeviceCounters(ctx context.Context, in *GetDeviceCountersRequest, opts ...grpc.CallOption) (*GetDeviceCountersResponse, error) {
	out := new(GetDeviceCountersResponse)
	err := c.cc.Invoke(ctx, "/hr.HandyRustyService/GetDeviceCounters", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *handyRustyServiceClient) GetGatewayCounters(ctx context.Context, in *GetGatewayCountersRequest, opts ...grpc.CallOption) (*GetGatewayCountersResponse, error) {
	out := new(GetGatewayCountersResponse)
	err := c.cc.Invoke(ctx, "/hr.HandyRustyService/GetGatewayCounters", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *handyRustyServiceClient) GetVersion(ctx context.Context, in *empty.Empty, opts ...grpc.CallOption) (*GetVersionResponse, error) {
	out := new(GetVersionResponse)
	err := c.cc.Invoke(ctx, "/hr.HandyRustyService/GetVersion", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// HandyRustyServiceServer is the server API for HandyRustyService service.
type HandyRustyServiceServer interface {
	// GetDeviceCounters returns the summary-counters log-items for given organisation_id
	GetDeviceCounters(context.Context, *GetDeviceCountersRequest) (*GetDeviceCountersResponse, error)
	// GetDeviceCounters returns the summary-counters log-items for given organisation_id
	GetGatewayCounters(context.Context, *GetGatewayCountersRequest) (*GetGatewayCountersResponse, error)
	// GetVersion returns the ChirpStack Network Server version.
	GetVersion(context.Context, *empty.Empty) (*GetVersionResponse, error)
}

// UnimplementedHandyRustyServiceServer can be embedded to have forward compatible implementations.
type UnimplementedHandyRustyServiceServer struct {
}

func (*UnimplementedHandyRustyServiceServer) GetDeviceCounters(ctx context.Context, req *GetDeviceCountersRequest) (*GetDeviceCountersResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetDeviceCounters not implemented")
}
func (*UnimplementedHandyRustyServiceServer) GetGatewayCounters(ctx context.Context, req *GetGatewayCountersRequest) (*GetGatewayCountersResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetGatewayCounters not implemented")
}
func (*UnimplementedHandyRustyServiceServer) GetVersion(ctx context.Context, req *empty.Empty) (*GetVersionResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetVersion not implemented")
}

func RegisterHandyRustyServiceServer(s *grpc.Server, srv HandyRustyServiceServer) {
	s.RegisterService(&_HandyRustyService_serviceDesc, srv)
}

func _HandyRustyService_GetDeviceCounters_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetDeviceCountersRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(HandyRustyServiceServer).GetDeviceCounters(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/hr.HandyRustyService/GetDeviceCounters",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(HandyRustyServiceServer).GetDeviceCounters(ctx, req.(*GetDeviceCountersRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _HandyRustyService_GetGatewayCounters_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetGatewayCountersRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(HandyRustyServiceServer).GetGatewayCounters(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/hr.HandyRustyService/GetGatewayCounters",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(HandyRustyServiceServer).GetGatewayCounters(ctx, req.(*GetGatewayCountersRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _HandyRustyService_GetVersion_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(empty.Empty)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(HandyRustyServiceServer).GetVersion(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/hr.HandyRustyService/GetVersion",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(HandyRustyServiceServer).GetVersion(ctx, req.(*empty.Empty))
	}
	return interceptor(ctx, in, info, handler)
}

var _HandyRustyService_serviceDesc = grpc.ServiceDesc{
	ServiceName: "hr.HandyRustyService",
	HandlerType: (*HandyRustyServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetDeviceCounters",
			Handler:    _HandyRustyService_GetDeviceCounters_Handler,
		},
		{
			MethodName: "GetGatewayCounters",
			Handler:    _HandyRustyService_GetGatewayCounters_Handler,
		},
		{
			MethodName: "GetVersion",
			Handler:    _HandyRustyService_GetVersion_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "handyrusty/hr.proto",
}
