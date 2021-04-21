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
	// 315 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x6c, 0x91, 0xc1, 0x4f, 0xc2, 0x30,
	0x14, 0xc6, 0x2d, 0x4b, 0x40, 0x4a, 0x24, 0xcb, 0x4e, 0xc4, 0xa8, 0x41, 0x4e, 0xa8, 0xb1, 0x8d,
	0x70, 0xf0, 0x4e, 0x88, 0x09, 0xc6, 0x28, 0x99, 0x1a, 0x89, 0x97, 0xe5, 0x31, 0x46, 0x57, 0x81,
	0xbe, 0xa6, 0xab, 0x8e, 0xfd, 0x07, 0x1e, 0xfd, 0x93, 0xcd, 0xdc, 0x88, 0x81, 0x70, 0x6a, 0xfb,
	0xe5, 0x97, 0x7e, 0xdf, 0x7b, 0x1f, 0x3d, 0x83, 0x84, 0x47, 0x6b, 0x1b, 0x19, 0x05, 0x4b, 0x0e,
	0x5a, 0xf2, 0xb9, 0x81, 0x55, 0xf4, 0x80, 0x82, 0x69, 0x83, 0x16, 0x3d, 0x07, 0xb4, 0x3c, 0x6e,
	0x88, 0x94, 0x8b, 0xb4, 0x50, 0x3a, 0x3f, 0x84, 0x36, 0x5f, 0xf5, 0x52, 0xaa, 0xc5, 0x5d, 0x89,
	0x7a, 0x17, 0xb4, 0x66, 0xd7, 0x81, 0x54, 0x73, 0x6c, 0x91, 0x36, 0xe9, 0x36, 0x7a, 0x2e, 0x13,
	0x29, 0x2b, 0xa0, 0x97, 0xc9, 0x48, 0xcd, 0xd1, 0xaf, 0xda, 0x75, 0x7e, 0xe6, 0xa8, 0x29, 0xd1,
	0x4a, 0xdb, 0xd9, 0x46, 0xfd, 0x12, 0x35, 0x05, 0xda, 0xa5, 0xae, 0x8e, 0xb3, 0x40, 0x43, 0xb6,
	0x44, 0x98, 0x05, 0x1f, 0x09, 0xaa, 0x96, 0xd3, 0x26, 0xdd, 0xba, 0xdf, 0xd4, 0x71, 0x36, 0x2e,
	0xe4, 0xfb, 0xe7, 0xa7, 0xc7, 0xce, 0x37, 0xa1, 0xee, 0x10, 0x53, 0xb5, 0x15, 0xea, 0x6a, 0x37,
	0x94, 0x97, 0x3b, 0x6d, 0xb0, 0x9d, 0x58, 0xfb, 0xbc, 0x2a, 0xfb, 0xbc, 0xbc, 0x53, 0x4a, 0x05,
	0xd8, 0x28, 0x85, 0x2c, 0x90, 0xb3, 0x32, 0x4f, 0xbd, 0x54, 0x46, 0xc3, 0xcb, 0x13, 0x7a, 0xe8,
	0x4f, 0xde, 0xa4, 0x9a, 0x61, 0xea, 0xd5, 0xa8, 0xe3, 0x4f, 0x6e, 0xdc, 0x83, 0xe2, 0xd2, 0x73,
	0xc9, 0x60, 0x45, 0xcf, 0x25, 0xb2, 0x30, 0x96, 0x46, 0x27, 0x16, 0xc2, 0x05, 0x03, 0x2d, 0x19,
	0x24, 0x6c, 0xd3, 0x40, 0xfe, 0x1e, 0x1c, 0x6d, 0x46, 0x18, 0xe7, 0xfb, 0x1e, 0x93, 0xf7, 0x5b,
	0x21, 0x6d, 0xfc, 0x39, 0x65, 0x21, 0xae, 0xf8, 0xd4, 0x60, 0x08, 0x60, 0xf8, 0xff, 0x1f, 0xd7,
	0x79, 0x6b, 0x02, 0xf9, 0x57, 0x9f, 0xef, 0x74, 0x39, 0xad, 0xfe, 0x35, 0xd6, 0xff, 0x0d, 0x00,
	0x00, 0xff, 0xff, 0x94, 0x7f, 0x29, 0xe8, 0xe5, 0x01, 0x00, 0x00,
}
