// Code generated by protoc-gen-go. DO NOT EDIT.
// source: as/external/api/deviceQueue.proto

package api

import (
	context "context"
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	empty "github.com/golang/protobuf/ptypes/empty"
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

type DeviceQueueItem struct {
	// Device EUI (HEX encoded).
	DevEui string `protobuf:"bytes,1,opt,name=dev_eui,json=devEUI,proto3" json:"dev_eui,omitempty"`
	// Set this to true when an acknowledgement from the device is required.
	// Please note that this must not be used to guarantee a delivery.
	Confirmed bool `protobuf:"varint,2,opt,name=confirmed,proto3" json:"confirmed,omitempty"`
	// Downlink frame-counter.
	// This will be automatically set on enquue.
	FCnt uint32 `protobuf:"varint,6,opt,name=f_cnt,json=fCnt,proto3" json:"f_cnt,omitempty"`
	// FPort used (must be > 0)
	FPort uint32 `protobuf:"varint,3,opt,name=f_port,json=fPort,proto3" json:"f_port,omitempty"`
	// Base64 encoded data.
	// Or use the json_object field when an application codec has been configured.
	Data []byte `protobuf:"bytes,4,opt,name=data,proto3" json:"data,omitempty"`
	// JSON object (string).
	// Only use this when an application codec has been configured that can convert
	// this object into binary form.
	JsonObject           string   `protobuf:"bytes,5,opt,name=json_object,json=jsonObject,proto3" json:"json_object,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *DeviceQueueItem) Reset()         { *m = DeviceQueueItem{} }
func (m *DeviceQueueItem) String() string { return proto.CompactTextString(m) }
func (*DeviceQueueItem) ProtoMessage()    {}
func (*DeviceQueueItem) Descriptor() ([]byte, []int) {
	return fileDescriptor_6bc7c26115164240, []int{0}
}

func (m *DeviceQueueItem) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_DeviceQueueItem.Unmarshal(m, b)
}
func (m *DeviceQueueItem) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_DeviceQueueItem.Marshal(b, m, deterministic)
}
func (m *DeviceQueueItem) XXX_Merge(src proto.Message) {
	xxx_messageInfo_DeviceQueueItem.Merge(m, src)
}
func (m *DeviceQueueItem) XXX_Size() int {
	return xxx_messageInfo_DeviceQueueItem.Size(m)
}
func (m *DeviceQueueItem) XXX_DiscardUnknown() {
	xxx_messageInfo_DeviceQueueItem.DiscardUnknown(m)
}

var xxx_messageInfo_DeviceQueueItem proto.InternalMessageInfo

func (m *DeviceQueueItem) GetDevEui() string {
	if m != nil {
		return m.DevEui
	}
	return ""
}

func (m *DeviceQueueItem) GetConfirmed() bool {
	if m != nil {
		return m.Confirmed
	}
	return false
}

func (m *DeviceQueueItem) GetFCnt() uint32 {
	if m != nil {
		return m.FCnt
	}
	return 0
}

func (m *DeviceQueueItem) GetFPort() uint32 {
	if m != nil {
		return m.FPort
	}
	return 0
}

func (m *DeviceQueueItem) GetData() []byte {
	if m != nil {
		return m.Data
	}
	return nil
}

func (m *DeviceQueueItem) GetJsonObject() string {
	if m != nil {
		return m.JsonObject
	}
	return ""
}

type EnqueueDeviceQueueItemRequest struct {
	// Queue-item object to enqueue.
	DeviceQueueItem      *DeviceQueueItem `protobuf:"bytes,1,opt,name=device_queue_item,json=deviceQueueItem,proto3" json:"device_queue_item,omitempty"`
	XXX_NoUnkeyedLiteral struct{}         `json:"-"`
	XXX_unrecognized     []byte           `json:"-"`
	XXX_sizecache        int32            `json:"-"`
}

func (m *EnqueueDeviceQueueItemRequest) Reset()         { *m = EnqueueDeviceQueueItemRequest{} }
func (m *EnqueueDeviceQueueItemRequest) String() string { return proto.CompactTextString(m) }
func (*EnqueueDeviceQueueItemRequest) ProtoMessage()    {}
func (*EnqueueDeviceQueueItemRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_6bc7c26115164240, []int{1}
}

func (m *EnqueueDeviceQueueItemRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_EnqueueDeviceQueueItemRequest.Unmarshal(m, b)
}
func (m *EnqueueDeviceQueueItemRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_EnqueueDeviceQueueItemRequest.Marshal(b, m, deterministic)
}
func (m *EnqueueDeviceQueueItemRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_EnqueueDeviceQueueItemRequest.Merge(m, src)
}
func (m *EnqueueDeviceQueueItemRequest) XXX_Size() int {
	return xxx_messageInfo_EnqueueDeviceQueueItemRequest.Size(m)
}
func (m *EnqueueDeviceQueueItemRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_EnqueueDeviceQueueItemRequest.DiscardUnknown(m)
}

var xxx_messageInfo_EnqueueDeviceQueueItemRequest proto.InternalMessageInfo

func (m *EnqueueDeviceQueueItemRequest) GetDeviceQueueItem() *DeviceQueueItem {
	if m != nil {
		return m.DeviceQueueItem
	}
	return nil
}

type EnqueueDeviceQueueItemResponse struct {
	// Frame-counter for the enqueued payload.
	FCnt                 uint32   `protobuf:"varint,1,opt,name=f_cnt,json=fCnt,proto3" json:"f_cnt,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *EnqueueDeviceQueueItemResponse) Reset()         { *m = EnqueueDeviceQueueItemResponse{} }
func (m *EnqueueDeviceQueueItemResponse) String() string { return proto.CompactTextString(m) }
func (*EnqueueDeviceQueueItemResponse) ProtoMessage()    {}
func (*EnqueueDeviceQueueItemResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_6bc7c26115164240, []int{2}
}

func (m *EnqueueDeviceQueueItemResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_EnqueueDeviceQueueItemResponse.Unmarshal(m, b)
}
func (m *EnqueueDeviceQueueItemResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_EnqueueDeviceQueueItemResponse.Marshal(b, m, deterministic)
}
func (m *EnqueueDeviceQueueItemResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_EnqueueDeviceQueueItemResponse.Merge(m, src)
}
func (m *EnqueueDeviceQueueItemResponse) XXX_Size() int {
	return xxx_messageInfo_EnqueueDeviceQueueItemResponse.Size(m)
}
func (m *EnqueueDeviceQueueItemResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_EnqueueDeviceQueueItemResponse.DiscardUnknown(m)
}

var xxx_messageInfo_EnqueueDeviceQueueItemResponse proto.InternalMessageInfo

func (m *EnqueueDeviceQueueItemResponse) GetFCnt() uint32 {
	if m != nil {
		return m.FCnt
	}
	return 0
}

type FlushDeviceQueueRequest struct {
	// Device EUI (HEX encoded).
	DevEui               string   `protobuf:"bytes,1,opt,name=dev_eui,json=devEUI,proto3" json:"dev_eui,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *FlushDeviceQueueRequest) Reset()         { *m = FlushDeviceQueueRequest{} }
func (m *FlushDeviceQueueRequest) String() string { return proto.CompactTextString(m) }
func (*FlushDeviceQueueRequest) ProtoMessage()    {}
func (*FlushDeviceQueueRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_6bc7c26115164240, []int{3}
}

func (m *FlushDeviceQueueRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_FlushDeviceQueueRequest.Unmarshal(m, b)
}
func (m *FlushDeviceQueueRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_FlushDeviceQueueRequest.Marshal(b, m, deterministic)
}
func (m *FlushDeviceQueueRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_FlushDeviceQueueRequest.Merge(m, src)
}
func (m *FlushDeviceQueueRequest) XXX_Size() int {
	return xxx_messageInfo_FlushDeviceQueueRequest.Size(m)
}
func (m *FlushDeviceQueueRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_FlushDeviceQueueRequest.DiscardUnknown(m)
}

var xxx_messageInfo_FlushDeviceQueueRequest proto.InternalMessageInfo

func (m *FlushDeviceQueueRequest) GetDevEui() string {
	if m != nil {
		return m.DevEui
	}
	return ""
}

type ListDeviceQueueItemsRequest struct {
	// Device EUI (HEX encoded).
	DevEui string `protobuf:"bytes,1,opt,name=dev_eui,json=devEUI,proto3" json:"dev_eui,omitempty"`
	// Return only the count, not the result-set.
	CountOnly            bool     `protobuf:"varint,2,opt,name=count_only,json=countOnly,proto3" json:"count_only,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ListDeviceQueueItemsRequest) Reset()         { *m = ListDeviceQueueItemsRequest{} }
func (m *ListDeviceQueueItemsRequest) String() string { return proto.CompactTextString(m) }
func (*ListDeviceQueueItemsRequest) ProtoMessage()    {}
func (*ListDeviceQueueItemsRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_6bc7c26115164240, []int{4}
}

func (m *ListDeviceQueueItemsRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ListDeviceQueueItemsRequest.Unmarshal(m, b)
}
func (m *ListDeviceQueueItemsRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ListDeviceQueueItemsRequest.Marshal(b, m, deterministic)
}
func (m *ListDeviceQueueItemsRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ListDeviceQueueItemsRequest.Merge(m, src)
}
func (m *ListDeviceQueueItemsRequest) XXX_Size() int {
	return xxx_messageInfo_ListDeviceQueueItemsRequest.Size(m)
}
func (m *ListDeviceQueueItemsRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_ListDeviceQueueItemsRequest.DiscardUnknown(m)
}

var xxx_messageInfo_ListDeviceQueueItemsRequest proto.InternalMessageInfo

func (m *ListDeviceQueueItemsRequest) GetDevEui() string {
	if m != nil {
		return m.DevEui
	}
	return ""
}

func (m *ListDeviceQueueItemsRequest) GetCountOnly() bool {
	if m != nil {
		return m.CountOnly
	}
	return false
}

type ListDeviceQueueItemsResponse struct {
	// The device queue items.
	DeviceQueueItems []*DeviceQueueItem `protobuf:"bytes,1,rep,name=device_queue_items,json=deviceQueueItems,proto3" json:"device_queue_items,omitempty"`
	// Total number of items in the queue.
	TotalCount           uint32   `protobuf:"varint,2,opt,name=total_count,json=totalCount,proto3" json:"total_count,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ListDeviceQueueItemsResponse) Reset()         { *m = ListDeviceQueueItemsResponse{} }
func (m *ListDeviceQueueItemsResponse) String() string { return proto.CompactTextString(m) }
func (*ListDeviceQueueItemsResponse) ProtoMessage()    {}
func (*ListDeviceQueueItemsResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_6bc7c26115164240, []int{5}
}

func (m *ListDeviceQueueItemsResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ListDeviceQueueItemsResponse.Unmarshal(m, b)
}
func (m *ListDeviceQueueItemsResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ListDeviceQueueItemsResponse.Marshal(b, m, deterministic)
}
func (m *ListDeviceQueueItemsResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ListDeviceQueueItemsResponse.Merge(m, src)
}
func (m *ListDeviceQueueItemsResponse) XXX_Size() int {
	return xxx_messageInfo_ListDeviceQueueItemsResponse.Size(m)
}
func (m *ListDeviceQueueItemsResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_ListDeviceQueueItemsResponse.DiscardUnknown(m)
}

var xxx_messageInfo_ListDeviceQueueItemsResponse proto.InternalMessageInfo

func (m *ListDeviceQueueItemsResponse) GetDeviceQueueItems() []*DeviceQueueItem {
	if m != nil {
		return m.DeviceQueueItems
	}
	return nil
}

func (m *ListDeviceQueueItemsResponse) GetTotalCount() uint32 {
	if m != nil {
		return m.TotalCount
	}
	return 0
}

type EnqueueDeviceQueueActilityItemRequest struct {
	// Device EUI (HEX encoded).
	DevEui string `protobuf:"bytes,1,opt,name=dev_eui,json=devEUI,proto3" json:"dev_eui,omitempty"`
	// Set this to true when an acknowledgement from the device is required.
	// Please note that this must not be used to guarantee a delivery.
	ConfirmDownlink bool `protobuf:"varint,2,opt,name=confirm_downlink,json=confirmDownlink,proto3" json:"confirm_downlink,omitempty"`
	// Indicates to flush the LRC downlink queue before adding the new message to the queue.
	// Default is false.
	FlushDownlinkQueue bool `protobuf:"varint,3,opt,name=flush_downlink_queue,json=flushDownlinkQueue,proto3" json:"flush_downlink_queue,omitempty"`
	// Payload of the message in hexadecimal format.
	PayloadHex string `protobuf:"bytes,4,opt,name=payload_hex,json=payloadHex,proto3" json:"payload_hex,omitempty"`
	// LoRa port(s) targetted by the message.
	TargetPorts          string   `protobuf:"bytes,5,opt,name=target_ports,json=targetPorts,proto3" json:"target_ports,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *EnqueueDeviceQueueActilityItemRequest) Reset()         { *m = EnqueueDeviceQueueActilityItemRequest{} }
func (m *EnqueueDeviceQueueActilityItemRequest) String() string { return proto.CompactTextString(m) }
func (*EnqueueDeviceQueueActilityItemRequest) ProtoMessage()    {}
func (*EnqueueDeviceQueueActilityItemRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_6bc7c26115164240, []int{6}
}

func (m *EnqueueDeviceQueueActilityItemRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_EnqueueDeviceQueueActilityItemRequest.Unmarshal(m, b)
}
func (m *EnqueueDeviceQueueActilityItemRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_EnqueueDeviceQueueActilityItemRequest.Marshal(b, m, deterministic)
}
func (m *EnqueueDeviceQueueActilityItemRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_EnqueueDeviceQueueActilityItemRequest.Merge(m, src)
}
func (m *EnqueueDeviceQueueActilityItemRequest) XXX_Size() int {
	return xxx_messageInfo_EnqueueDeviceQueueActilityItemRequest.Size(m)
}
func (m *EnqueueDeviceQueueActilityItemRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_EnqueueDeviceQueueActilityItemRequest.DiscardUnknown(m)
}

var xxx_messageInfo_EnqueueDeviceQueueActilityItemRequest proto.InternalMessageInfo

func (m *EnqueueDeviceQueueActilityItemRequest) GetDevEui() string {
	if m != nil {
		return m.DevEui
	}
	return ""
}

func (m *EnqueueDeviceQueueActilityItemRequest) GetConfirmDownlink() bool {
	if m != nil {
		return m.ConfirmDownlink
	}
	return false
}

func (m *EnqueueDeviceQueueActilityItemRequest) GetFlushDownlinkQueue() bool {
	if m != nil {
		return m.FlushDownlinkQueue
	}
	return false
}

func (m *EnqueueDeviceQueueActilityItemRequest) GetPayloadHex() string {
	if m != nil {
		return m.PayloadHex
	}
	return ""
}

func (m *EnqueueDeviceQueueActilityItemRequest) GetTargetPorts() string {
	if m != nil {
		return m.TargetPorts
	}
	return ""
}

type EnqueueDeviceQueueActilityItemResponse struct {
	// Frame-counter for the enqueued payload.
	ConfirmDownlink      bool     `protobuf:"varint,1,opt,name=confirm_downlink,json=confirmDownlink,proto3" json:"confirm_downlink,omitempty"`
	FlushDownlinkQueue   bool     `protobuf:"varint,2,opt,name=flush_downlink_queue,json=flushDownlinkQueue,proto3" json:"flush_downlink_queue,omitempty"`
	PayloadHex           string   `protobuf:"bytes,3,opt,name=payload_hex,json=payloadHex,proto3" json:"payload_hex,omitempty"`
	TargetPorts          string   `protobuf:"bytes,4,opt,name=target_ports,json=targetPorts,proto3" json:"target_ports,omitempty"`
	Status               string   `protobuf:"bytes,5,opt,name=status,proto3" json:"status,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *EnqueueDeviceQueueActilityItemResponse) Reset() {
	*m = EnqueueDeviceQueueActilityItemResponse{}
}
func (m *EnqueueDeviceQueueActilityItemResponse) String() string { return proto.CompactTextString(m) }
func (*EnqueueDeviceQueueActilityItemResponse) ProtoMessage()    {}
func (*EnqueueDeviceQueueActilityItemResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_6bc7c26115164240, []int{7}
}

func (m *EnqueueDeviceQueueActilityItemResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_EnqueueDeviceQueueActilityItemResponse.Unmarshal(m, b)
}
func (m *EnqueueDeviceQueueActilityItemResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_EnqueueDeviceQueueActilityItemResponse.Marshal(b, m, deterministic)
}
func (m *EnqueueDeviceQueueActilityItemResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_EnqueueDeviceQueueActilityItemResponse.Merge(m, src)
}
func (m *EnqueueDeviceQueueActilityItemResponse) XXX_Size() int {
	return xxx_messageInfo_EnqueueDeviceQueueActilityItemResponse.Size(m)
}
func (m *EnqueueDeviceQueueActilityItemResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_EnqueueDeviceQueueActilityItemResponse.DiscardUnknown(m)
}

var xxx_messageInfo_EnqueueDeviceQueueActilityItemResponse proto.InternalMessageInfo

func (m *EnqueueDeviceQueueActilityItemResponse) GetConfirmDownlink() bool {
	if m != nil {
		return m.ConfirmDownlink
	}
	return false
}

func (m *EnqueueDeviceQueueActilityItemResponse) GetFlushDownlinkQueue() bool {
	if m != nil {
		return m.FlushDownlinkQueue
	}
	return false
}

func (m *EnqueueDeviceQueueActilityItemResponse) GetPayloadHex() string {
	if m != nil {
		return m.PayloadHex
	}
	return ""
}

func (m *EnqueueDeviceQueueActilityItemResponse) GetTargetPorts() string {
	if m != nil {
		return m.TargetPorts
	}
	return ""
}

func (m *EnqueueDeviceQueueActilityItemResponse) GetStatus() string {
	if m != nil {
		return m.Status
	}
	return ""
}

func init() {
	proto.RegisterType((*DeviceQueueItem)(nil), "api.DeviceQueueItem")
	proto.RegisterType((*EnqueueDeviceQueueItemRequest)(nil), "api.EnqueueDeviceQueueItemRequest")
	proto.RegisterType((*EnqueueDeviceQueueItemResponse)(nil), "api.EnqueueDeviceQueueItemResponse")
	proto.RegisterType((*FlushDeviceQueueRequest)(nil), "api.FlushDeviceQueueRequest")
	proto.RegisterType((*ListDeviceQueueItemsRequest)(nil), "api.ListDeviceQueueItemsRequest")
	proto.RegisterType((*ListDeviceQueueItemsResponse)(nil), "api.ListDeviceQueueItemsResponse")
	proto.RegisterType((*EnqueueDeviceQueueActilityItemRequest)(nil), "api.EnqueueDeviceQueueActilityItemRequest")
	proto.RegisterType((*EnqueueDeviceQueueActilityItemResponse)(nil), "api.EnqueueDeviceQueueActilityItemResponse")
}

func init() {
	proto.RegisterFile("as/external/api/deviceQueue.proto", fileDescriptor_6bc7c26115164240)
}

var fileDescriptor_6bc7c26115164240 = []byte{
	// 721 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x94, 0x55, 0xcd, 0x6e, 0xd3, 0x4c,
	0x14, 0x95, 0x9b, 0x9f, 0xb6, 0xb7, 0xad, 0xd2, 0x6f, 0xbe, 0x7e, 0x6d, 0x94, 0xa6, 0xfd, 0x52,
	0xf3, 0xa3, 0x10, 0x84, 0x8d, 0x5a, 0x55, 0xa8, 0xac, 0xa0, 0x3f, 0x88, 0x4a, 0x48, 0x05, 0xa3,
	0x6e, 0xd8, 0x58, 0x13, 0x7b, 0x92, 0xb8, 0x75, 0x66, 0x5c, 0xcf, 0x75, 0x68, 0x84, 0xd8, 0xc0,
	0x9a, 0x15, 0x2f, 0x00, 0x4b, 0x9e, 0x87, 0x27, 0x40, 0xe2, 0x41, 0x90, 0x27, 0x13, 0x12, 0x92,
	0x26, 0x2d, 0xbb, 0xf8, 0xcc, 0x9d, 0x39, 0xf7, 0x9c, 0x39, 0x77, 0x02, 0x5b, 0x54, 0xda, 0xec,
	0x12, 0x59, 0xcc, 0x69, 0x68, 0xd3, 0x28, 0xb0, 0x7d, 0xd6, 0x09, 0x3c, 0xf6, 0x2a, 0x61, 0x09,
	0xb3, 0xa2, 0x58, 0xa0, 0x20, 0x19, 0x1a, 0x05, 0xa5, 0x72, 0x53, 0x88, 0x66, 0xc8, 0x54, 0x09,
	0xe5, 0x5c, 0x20, 0xc5, 0x40, 0x70, 0xd9, 0x2b, 0x29, 0xad, 0xeb, 0x55, 0xf5, 0x55, 0x4f, 0x1a,
	0x36, 0x6b, 0x47, 0xd8, 0xed, 0x2d, 0x9a, 0xdf, 0x0c, 0x28, 0x1c, 0x0e, 0x4e, 0x3d, 0x46, 0xd6,
	0x26, 0x6b, 0x30, 0xeb, 0xb3, 0x8e, 0xcb, 0x92, 0xa0, 0x68, 0x54, 0x8c, 0xea, 0xbc, 0x93, 0xf7,
	0x59, 0xe7, 0xe8, 0xf4, 0x98, 0x94, 0x61, 0xde, 0x13, 0xbc, 0x11, 0xc4, 0x6d, 0xe6, 0x17, 0x67,
	0x2a, 0x46, 0x75, 0xce, 0x19, 0x00, 0xe4, 0x5f, 0xc8, 0x35, 0x5c, 0x8f, 0x63, 0x31, 0x5f, 0x31,
	0xaa, 0x4b, 0x4e, 0xb6, 0x71, 0xc0, 0x91, 0xfc, 0x07, 0xf9, 0x86, 0x1b, 0x89, 0x18, 0x8b, 0x19,
	0x85, 0xe6, 0x1a, 0x2f, 0x45, 0x8c, 0x84, 0x40, 0xd6, 0xa7, 0x48, 0x8b, 0xd9, 0x8a, 0x51, 0x5d,
	0x74, 0xd4, 0x6f, 0xf2, 0x3f, 0x2c, 0x9c, 0x49, 0xc1, 0x5d, 0x51, 0x3f, 0x63, 0x1e, 0x16, 0x73,
	0x8a, 0x1a, 0x52, 0xe8, 0x44, 0x21, 0x26, 0x85, 0x8d, 0x23, 0x7e, 0x91, 0xb6, 0x39, 0xd2, 0xb1,
	0xc3, 0x2e, 0x12, 0x26, 0x91, 0x3c, 0x81, 0x7f, 0x7a, 0x0e, 0xb9, 0xaa, 0xca, 0x0d, 0x90, 0xb5,
	0x95, 0x84, 0x85, 0xed, 0x15, 0x8b, 0x46, 0x81, 0x35, 0xba, 0xaf, 0xe0, 0xff, 0x09, 0x98, 0xbb,
	0xb0, 0x39, 0x89, 0x42, 0x46, 0x82, 0x4b, 0x36, 0x50, 0x69, 0x0c, 0x54, 0x9a, 0xdb, 0xb0, 0xf6,
	0x2c, 0x4c, 0x64, 0x6b, 0x68, 0x53, 0xbf, 0xa7, 0x49, 0x66, 0x9a, 0xa7, 0xb0, 0xfe, 0x22, 0x90,
	0x38, 0xc2, 0x23, 0xaf, 0xdb, 0x47, 0x36, 0x00, 0x3c, 0x91, 0x70, 0x74, 0x05, 0x0f, 0xbb, 0x83,
	0x5b, 0x48, 0x38, 0x9e, 0xf0, 0xb0, 0x6b, 0x7e, 0x34, 0xa0, 0x7c, 0xf5, 0xb9, 0x5a, 0xc0, 0x3e,
	0x90, 0x31, 0x93, 0x64, 0xd1, 0xa8, 0x64, 0x26, 0xba, 0xb4, 0x3c, 0xe2, 0x92, 0x4c, 0xaf, 0x0a,
	0x05, 0xd2, 0xd0, 0x55, 0xbc, 0xaa, 0x89, 0x25, 0x07, 0x14, 0x74, 0x90, 0x22, 0xe6, 0x0f, 0x03,
	0xee, 0x8c, 0x1b, 0xf9, 0xd4, 0xc3, 0x20, 0x0c, 0xb0, 0x3b, 0x7c, 0x67, 0x13, 0x75, 0xde, 0x83,
	0x65, 0x9d, 0x2d, 0xd7, 0x17, 0x6f, 0x79, 0x18, 0xf0, 0x73, 0xad, 0xb6, 0xa0, 0xf1, 0x43, 0x0d,
	0x93, 0x87, 0xb0, 0xd2, 0x48, 0xed, 0xff, 0x5d, 0xd8, 0x93, 0xa6, 0x22, 0x37, 0xe7, 0x10, 0xb5,
	0xd6, 0x2f, 0x56, 0x8d, 0xa4, 0x02, 0x22, 0xda, 0x0d, 0x05, 0xf5, 0xdd, 0x16, 0xbb, 0x54, 0x31,
	0x9c, 0x77, 0x40, 0x43, 0xcf, 0xd9, 0x25, 0xd9, 0x82, 0x45, 0xa4, 0x71, 0x93, 0xa1, 0x0a, 0xaf,
	0xd4, 0x69, 0x5c, 0xe8, 0x61, 0x69, 0x84, 0x65, 0xaa, 0xf1, 0xee, 0x75, 0x1a, 0xb5, 0xe7, 0x57,
	0x69, 0x31, 0xfe, 0x4e, 0xcb, 0xcc, 0x4d, 0xb5, 0x64, 0xae, 0xd5, 0x92, 0x1d, 0xd3, 0x42, 0x56,
	0x21, 0x2f, 0x91, 0x62, 0xd2, 0x17, 0xaa, 0xbf, 0xb6, 0xbf, 0x64, 0x81, 0x0c, 0x89, 0x7b, 0xcd,
	0xe2, 0xf4, 0x37, 0xf9, 0x64, 0xc0, 0xac, 0x96, 0x4e, 0x4c, 0x95, 0x99, 0xa9, 0x83, 0x59, 0xba,
	0x35, 0xb5, 0xa6, 0x67, 0x92, 0xb9, 0xf7, 0xe1, 0xfb, 0xcf, 0xcf, 0x33, 0x3b, 0xa6, 0x35, 0xf4,
	0xd4, 0x49, 0xfb, 0xdd, 0x58, 0x58, 0x2d, 0x9d, 0x97, 0xf7, 0xb6, 0xc2, 0x1e, 0x1b, 0x35, 0xe2,
	0x41, 0x4e, 0xcd, 0x1f, 0x29, 0x2b, 0xa2, 0x09, 0xb3, 0x58, 0x5a, 0xb5, 0x7a, 0x4f, 0xa1, 0xd5,
	0x7f, 0x0a, 0xad, 0xa3, 0xf4, 0x29, 0x34, 0x6f, 0x2b, 0xe6, 0xcd, 0x5a, 0x79, 0x8c, 0x79, 0x88,
	0x87, 0x5c, 0x40, 0x36, 0x1d, 0x2c, 0x52, 0x51, 0x1c, 0x53, 0x66, 0xb7, 0xb4, 0x35, 0xa5, 0x42,
	0x8b, 0xd5, 0x94, 0x64, 0x3a, 0xe5, 0x57, 0x03, 0x0a, 0xfd, 0x40, 0xf5, 0xfd, 0xae, 0x4d, 0xf0,
	0xf2, 0x8a, 0xe1, 0x2a, 0xdd, 0xbf, 0x51, 0xad, 0x6e, 0x69, 0x57, 0xb5, 0x64, 0x9b, 0xb5, 0x69,
	0x2d, 0xd9, 0x54, 0x6f, 0x95, 0xd8, 0x0d, 0x53, 0xef, 0xf7, 0xf7, 0xde, 0x3c, 0x6a, 0x06, 0xd8,
	0x4a, 0xea, 0x96, 0x27, 0xda, 0x76, 0x3d, 0x16, 0x1e, 0xa5, 0xb1, 0xed, 0xb5, 0x82, 0x38, 0x92,
	0x48, 0xbd, 0xf3, 0x07, 0xe9, 0x69, 0x4d, 0x61, 0x77, 0x76, 0xec, 0x91, 0xbf, 0xb3, 0x7a, 0x5e,
	0xdd, 0xc3, 0xce, 0xaf, 0x00, 0x00, 0x00, 0xff, 0xff, 0xc8, 0xb4, 0xd0, 0xab, 0xe8, 0x06, 0x00,
	0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConnInterface

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion6

// DeviceQueueServiceClient is the client API for DeviceQueueService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type DeviceQueueServiceClient interface {
	// Enqueue adds the given item to the device-queue.
	Enqueue(ctx context.Context, in *EnqueueDeviceQueueItemRequest, opts ...grpc.CallOption) (*EnqueueDeviceQueueItemResponse, error)
	// Flush flushes the downlink device-queue.
	Flush(ctx context.Context, in *FlushDeviceQueueRequest, opts ...grpc.CallOption) (*empty.Empty, error)
	// List lists the items in the device-queue.
	List(ctx context.Context, in *ListDeviceQueueItemsRequest, opts ...grpc.CallOption) (*ListDeviceQueueItemsResponse, error)
	// ActilityEnqueue adds the given item to the device-queue with actility-styled request\response.
	ActilityEnqueue(ctx context.Context, in *EnqueueDeviceQueueActilityItemRequest, opts ...grpc.CallOption) (*EnqueueDeviceQueueActilityItemResponse, error)
}

type deviceQueueServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewDeviceQueueServiceClient(cc grpc.ClientConnInterface) DeviceQueueServiceClient {
	return &deviceQueueServiceClient{cc}
}

func (c *deviceQueueServiceClient) Enqueue(ctx context.Context, in *EnqueueDeviceQueueItemRequest, opts ...grpc.CallOption) (*EnqueueDeviceQueueItemResponse, error) {
	out := new(EnqueueDeviceQueueItemResponse)
	err := c.cc.Invoke(ctx, "/api.DeviceQueueService/Enqueue", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *deviceQueueServiceClient) Flush(ctx context.Context, in *FlushDeviceQueueRequest, opts ...grpc.CallOption) (*empty.Empty, error) {
	out := new(empty.Empty)
	err := c.cc.Invoke(ctx, "/api.DeviceQueueService/Flush", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *deviceQueueServiceClient) List(ctx context.Context, in *ListDeviceQueueItemsRequest, opts ...grpc.CallOption) (*ListDeviceQueueItemsResponse, error) {
	out := new(ListDeviceQueueItemsResponse)
	err := c.cc.Invoke(ctx, "/api.DeviceQueueService/List", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *deviceQueueServiceClient) ActilityEnqueue(ctx context.Context, in *EnqueueDeviceQueueActilityItemRequest, opts ...grpc.CallOption) (*EnqueueDeviceQueueActilityItemResponse, error) {
	out := new(EnqueueDeviceQueueActilityItemResponse)
	err := c.cc.Invoke(ctx, "/api.DeviceQueueService/ActilityEnqueue", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// DeviceQueueServiceServer is the server API for DeviceQueueService service.
type DeviceQueueServiceServer interface {
	// Enqueue adds the given item to the device-queue.
	Enqueue(context.Context, *EnqueueDeviceQueueItemRequest) (*EnqueueDeviceQueueItemResponse, error)
	// Flush flushes the downlink device-queue.
	Flush(context.Context, *FlushDeviceQueueRequest) (*empty.Empty, error)
	// List lists the items in the device-queue.
	List(context.Context, *ListDeviceQueueItemsRequest) (*ListDeviceQueueItemsResponse, error)
	// ActilityEnqueue adds the given item to the device-queue with actility-styled request\response.
	ActilityEnqueue(context.Context, *EnqueueDeviceQueueActilityItemRequest) (*EnqueueDeviceQueueActilityItemResponse, error)
}

// UnimplementedDeviceQueueServiceServer can be embedded to have forward compatible implementations.
type UnimplementedDeviceQueueServiceServer struct {
}

func (*UnimplementedDeviceQueueServiceServer) Enqueue(ctx context.Context, req *EnqueueDeviceQueueItemRequest) (*EnqueueDeviceQueueItemResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Enqueue not implemented")
}
func (*UnimplementedDeviceQueueServiceServer) Flush(ctx context.Context, req *FlushDeviceQueueRequest) (*empty.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Flush not implemented")
}
func (*UnimplementedDeviceQueueServiceServer) List(ctx context.Context, req *ListDeviceQueueItemsRequest) (*ListDeviceQueueItemsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (*UnimplementedDeviceQueueServiceServer) ActilityEnqueue(ctx context.Context, req *EnqueueDeviceQueueActilityItemRequest) (*EnqueueDeviceQueueActilityItemResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ActilityEnqueue not implemented")
}

func RegisterDeviceQueueServiceServer(s *grpc.Server, srv DeviceQueueServiceServer) {
	s.RegisterService(&_DeviceQueueService_serviceDesc, srv)
}

func _DeviceQueueService_Enqueue_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(EnqueueDeviceQueueItemRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DeviceQueueServiceServer).Enqueue(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/api.DeviceQueueService/Enqueue",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DeviceQueueServiceServer).Enqueue(ctx, req.(*EnqueueDeviceQueueItemRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DeviceQueueService_Flush_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(FlushDeviceQueueRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DeviceQueueServiceServer).Flush(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/api.DeviceQueueService/Flush",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DeviceQueueServiceServer).Flush(ctx, req.(*FlushDeviceQueueRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DeviceQueueService_List_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListDeviceQueueItemsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DeviceQueueServiceServer).List(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/api.DeviceQueueService/List",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DeviceQueueServiceServer).List(ctx, req.(*ListDeviceQueueItemsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DeviceQueueService_ActilityEnqueue_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(EnqueueDeviceQueueActilityItemRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DeviceQueueServiceServer).ActilityEnqueue(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/api.DeviceQueueService/ActilityEnqueue",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DeviceQueueServiceServer).ActilityEnqueue(ctx, req.(*EnqueueDeviceQueueActilityItemRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _DeviceQueueService_serviceDesc = grpc.ServiceDesc{
	ServiceName: "api.DeviceQueueService",
	HandlerType: (*DeviceQueueServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Enqueue",
			Handler:    _DeviceQueueService_Enqueue_Handler,
		},
		{
			MethodName: "Flush",
			Handler:    _DeviceQueueService_Flush_Handler,
		},
		{
			MethodName: "List",
			Handler:    _DeviceQueueService_List_Handler,
		},
		{
			MethodName: "ActilityEnqueue",
			Handler:    _DeviceQueueService_ActilityEnqueue_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "as/external/api/deviceQueue.proto",
}
