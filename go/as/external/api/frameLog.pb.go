// Code generated by protoc-gen-go. DO NOT EDIT.
// source: as/external/api/frameLog.proto

package api

import (
	fmt "fmt"
	gw "github.com/brocaar/chirpstack-api/go/v3/gw"
	proto "github.com/golang/protobuf/proto"
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

type RXWindow int32

const (
	RXWindow_RX1 RXWindow = 0
	RXWindow_RX2 RXWindow = 1
)

var RXWindow_name = map[int32]string{
	0: "RX1",
	1: "RX2",
}

var RXWindow_value = map[string]int32{
	"RX1": 0,
	"RX2": 1,
}

func (x RXWindow) String() string {
	return proto.EnumName(RXWindow_name, int32(x))
}

func (RXWindow) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_d215818867a60801, []int{0}
}

type UplinkFrameLog struct {
	// TX information of the uplink.
	TxInfo *gw.UplinkTXInfo `protobuf:"bytes,1,opt,name=tx_info,json=txInfo,proto3" json:"tx_info,omitempty"`
	// RX information of the uplink.
	RxInfo []*gw.UplinkRXInfo `protobuf:"bytes,2,rep,name=rx_info,json=rxInfo,proto3" json:"rx_info,omitempty"`
	// LoRaWAN PHYPayload.
	PhyPayloadJson       string   `protobuf:"bytes,3,opt,name=phy_payload_json,json=phyPayloadJSON,proto3" json:"phy_payload_json,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *UplinkFrameLog) Reset()         { *m = UplinkFrameLog{} }
func (m *UplinkFrameLog) String() string { return proto.CompactTextString(m) }
func (*UplinkFrameLog) ProtoMessage()    {}
func (*UplinkFrameLog) Descriptor() ([]byte, []int) {
	return fileDescriptor_d215818867a60801, []int{0}
}

func (m *UplinkFrameLog) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_UplinkFrameLog.Unmarshal(m, b)
}
func (m *UplinkFrameLog) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_UplinkFrameLog.Marshal(b, m, deterministic)
}
func (m *UplinkFrameLog) XXX_Merge(src proto.Message) {
	xxx_messageInfo_UplinkFrameLog.Merge(m, src)
}
func (m *UplinkFrameLog) XXX_Size() int {
	return xxx_messageInfo_UplinkFrameLog.Size(m)
}
func (m *UplinkFrameLog) XXX_DiscardUnknown() {
	xxx_messageInfo_UplinkFrameLog.DiscardUnknown(m)
}

var xxx_messageInfo_UplinkFrameLog proto.InternalMessageInfo

func (m *UplinkFrameLog) GetTxInfo() *gw.UplinkTXInfo {
	if m != nil {
		return m.TxInfo
	}
	return nil
}

func (m *UplinkFrameLog) GetRxInfo() []*gw.UplinkRXInfo {
	if m != nil {
		return m.RxInfo
	}
	return nil
}

func (m *UplinkFrameLog) GetPhyPayloadJson() string {
	if m != nil {
		return m.PhyPayloadJson
	}
	return ""
}

type DownlinkFrameLog struct {
	// TX information of the downlink.
	TxInfo *gw.DownlinkTXInfo `protobuf:"bytes,1,opt,name=tx_info,json=txInfo,proto3" json:"tx_info,omitempty"`
	// LoRaWAN PHYPayload.
	PhyPayloadJson string `protobuf:"bytes,2,opt,name=phy_payload_json,json=phyPayloadJSON,proto3" json:"phy_payload_json,omitempty"`
	// Gateway ID.
	GatewayId            string   `protobuf:"bytes,3,opt,name=gateway_id,json=gatewayID,proto3" json:"gateway_id,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *DownlinkFrameLog) Reset()         { *m = DownlinkFrameLog{} }
func (m *DownlinkFrameLog) String() string { return proto.CompactTextString(m) }
func (*DownlinkFrameLog) ProtoMessage()    {}
func (*DownlinkFrameLog) Descriptor() ([]byte, []int) {
	return fileDescriptor_d215818867a60801, []int{1}
}

func (m *DownlinkFrameLog) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_DownlinkFrameLog.Unmarshal(m, b)
}
func (m *DownlinkFrameLog) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_DownlinkFrameLog.Marshal(b, m, deterministic)
}
func (m *DownlinkFrameLog) XXX_Merge(src proto.Message) {
	xxx_messageInfo_DownlinkFrameLog.Merge(m, src)
}
func (m *DownlinkFrameLog) XXX_Size() int {
	return xxx_messageInfo_DownlinkFrameLog.Size(m)
}
func (m *DownlinkFrameLog) XXX_DiscardUnknown() {
	xxx_messageInfo_DownlinkFrameLog.DiscardUnknown(m)
}

var xxx_messageInfo_DownlinkFrameLog proto.InternalMessageInfo

func (m *DownlinkFrameLog) GetTxInfo() *gw.DownlinkTXInfo {
	if m != nil {
		return m.TxInfo
	}
	return nil
}

func (m *DownlinkFrameLog) GetPhyPayloadJson() string {
	if m != nil {
		return m.PhyPayloadJson
	}
	return ""
}

func (m *DownlinkFrameLog) GetGatewayId() string {
	if m != nil {
		return m.GatewayId
	}
	return ""
}

func init() {
	proto.RegisterEnum("api.RXWindow", RXWindow_name, RXWindow_value)
	proto.RegisterType((*UplinkFrameLog)(nil), "api.UplinkFrameLog")
	proto.RegisterType((*DownlinkFrameLog)(nil), "api.DownlinkFrameLog")
}

func init() {
	proto.RegisterFile("as/external/api/frameLog.proto", fileDescriptor_d215818867a60801)
}

var fileDescriptor_d215818867a60801 = []byte{
	// 293 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x6c, 0x91, 0x41, 0x4b, 0xfb, 0x30,
	0x18, 0xc6, 0xff, 0x59, 0x61, 0xfb, 0x2f, 0x83, 0x51, 0x7a, 0x1a, 0xa2, 0x32, 0x76, 0x9a, 0x8a,
	0x0d, 0x6e, 0x07, 0xf1, 0x2a, 0x43, 0x98, 0x88, 0x4a, 0x55, 0x1c, 0x5e, 0xca, 0xbb, 0xae, 0x4b,
	0xe3, 0xba, 0xbc, 0x21, 0x8d, 0xa6, 0xfd, 0x06, 0x1e, 0xfd, 0xc8, 0x52, 0x5b, 0x0f, 0x2b, 0x3b,
	0x25, 0x3c, 0xfc, 0xe0, 0xf9, 0xf1, 0x3e, 0xf4, 0x18, 0x32, 0x16, 0xe7, 0x26, 0xd6, 0x12, 0x52,
	0x06, 0x4a, 0xb0, 0xb5, 0x86, 0x6d, 0x7c, 0x87, 0xdc, 0x57, 0x1a, 0x0d, 0x7a, 0x0e, 0x28, 0x71,
	0xd0, 0xe3, 0x96, 0x71, 0x5b, 0x25, 0xa3, 0x6f, 0x42, 0xfb, 0x2f, 0x2a, 0x15, 0x72, 0x73, 0x53,
	0xa3, 0xde, 0x09, 0xed, 0x98, 0x3c, 0x14, 0x72, 0x8d, 0x03, 0x32, 0x24, 0xe3, 0xde, 0xc4, 0xf5,
	0xb9, 0xf5, 0x2b, 0xe8, 0x79, 0x31, 0x97, 0x6b, 0x0c, 0xda, 0x26, 0x2f, 0xdf, 0x12, 0xd5, 0x35,
	0xda, 0x1a, 0x3a, 0xbb, 0x68, 0x50, 0xa3, 0xba, 0x42, 0xc7, 0xd4, 0x55, 0x49, 0x11, 0x2a, 0x28,
	0x52, 0x84, 0x55, 0xf8, 0x9e, 0xa1, 0x1c, 0x38, 0x43, 0x32, 0xee, 0x06, 0x7d, 0x95, 0x14, 0x8f,
	0x55, 0x7c, 0xfb, 0xf4, 0x70, 0x3f, 0xfa, 0x22, 0xd4, 0x9d, 0xa1, 0x95, 0x3b, 0x52, 0x67, 0x4d,
	0x29, 0xaf, 0x6c, 0xfa, 0xc3, 0x1a, 0x5a, 0xfb, 0xba, 0x5a, 0xfb, 0xba, 0xbc, 0x23, 0x4a, 0x39,
	0x98, 0xd8, 0x42, 0x11, 0x8a, 0x55, 0xed, 0xd3, 0xad, 0x93, 0xf9, 0xec, 0xf4, 0x90, 0xfe, 0x0f,
	0x16, 0xaf, 0x42, 0xae, 0xd0, 0x7a, 0x1d, 0xea, 0x04, 0x8b, 0x0b, 0xf7, 0x5f, 0xf5, 0x99, 0xb8,
	0xe4, 0xfa, 0xea, 0xed, 0x92, 0x0b, 0x93, 0x7c, 0x2c, 0xfd, 0x08, 0xb7, 0x6c, 0xa9, 0x31, 0x02,
	0xd0, 0x2c, 0x4a, 0x84, 0x56, 0x99, 0x81, 0x68, 0x73, 0x5e, 0x2e, 0xc0, 0x91, 0x7d, 0x4e, 0x59,
	0x63, 0x97, 0x65, 0xfb, 0xf7, 0xfa, 0xd3, 0x9f, 0x00, 0x00, 0x00, 0xff, 0xff, 0x68, 0x0a, 0x3b,
	0xa3, 0xb1, 0x01, 0x00, 0x00,
}
