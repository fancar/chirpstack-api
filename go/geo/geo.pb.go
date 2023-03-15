// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.29.1
// 	protoc        v3.13.0
// source: geo/geo.proto

package geo

import (
	context "context"
	common "github.com/brocaar/chirpstack-api/go/v3/common"
	gw "github.com/brocaar/chirpstack-api/go/v3/gw"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
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

type ResolveResult struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Resolved location.
	Location *common.Location `protobuf:"bytes,1,opt,name=location,proto3" json:"location,omitempty"`
}

func (x *ResolveResult) Reset() {
	*x = ResolveResult{}
	if protoimpl.UnsafeEnabled {
		mi := &file_geo_geo_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ResolveResult) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ResolveResult) ProtoMessage() {}

func (x *ResolveResult) ProtoReflect() protoreflect.Message {
	mi := &file_geo_geo_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ResolveResult.ProtoReflect.Descriptor instead.
func (*ResolveResult) Descriptor() ([]byte, []int) {
	return file_geo_geo_proto_rawDescGZIP(), []int{0}
}

func (x *ResolveResult) GetLocation() *common.Location {
	if x != nil {
		return x.Location
	}
	return nil
}

type FrameRXInfo struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Uplink Gateway meta-data.
	RxInfo []*gw.UplinkRXInfo `protobuf:"bytes,1,rep,name=rx_info,json=rxInfo,proto3" json:"rx_info,omitempty"`
}

func (x *FrameRXInfo) Reset() {
	*x = FrameRXInfo{}
	if protoimpl.UnsafeEnabled {
		mi := &file_geo_geo_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *FrameRXInfo) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*FrameRXInfo) ProtoMessage() {}

func (x *FrameRXInfo) ProtoReflect() protoreflect.Message {
	mi := &file_geo_geo_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use FrameRXInfo.ProtoReflect.Descriptor instead.
func (*FrameRXInfo) Descriptor() ([]byte, []int) {
	return file_geo_geo_proto_rawDescGZIP(), []int{1}
}

func (x *FrameRXInfo) GetRxInfo() []*gw.UplinkRXInfo {
	if x != nil {
		return x.RxInfo
	}
	return nil
}

type ResolveTDOARequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Device ID.
	DevEui []byte `protobuf:"bytes,1,opt,name=dev_eui,json=devEUI,proto3" json:"dev_eui,omitempty"`
	// Frame meta-data.
	FrameRxInfo *FrameRXInfo `protobuf:"bytes,2,opt,name=frame_rx_info,json=frameRXInfo,proto3" json:"frame_rx_info,omitempty"`
	// Device reference altitude.
	DeviceReferenceAltitude float64 `protobuf:"fixed64,3,opt,name=device_reference_altitude,json=deviceReferenceAltitude,proto3" json:"device_reference_altitude,omitempty"`
}

func (x *ResolveTDOARequest) Reset() {
	*x = ResolveTDOARequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_geo_geo_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ResolveTDOARequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ResolveTDOARequest) ProtoMessage() {}

func (x *ResolveTDOARequest) ProtoReflect() protoreflect.Message {
	mi := &file_geo_geo_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ResolveTDOARequest.ProtoReflect.Descriptor instead.
func (*ResolveTDOARequest) Descriptor() ([]byte, []int) {
	return file_geo_geo_proto_rawDescGZIP(), []int{2}
}

func (x *ResolveTDOARequest) GetDevEui() []byte {
	if x != nil {
		return x.DevEui
	}
	return nil
}

func (x *ResolveTDOARequest) GetFrameRxInfo() *FrameRXInfo {
	if x != nil {
		return x.FrameRxInfo
	}
	return nil
}

func (x *ResolveTDOARequest) GetDeviceReferenceAltitude() float64 {
	if x != nil {
		return x.DeviceReferenceAltitude
	}
	return 0
}

type ResolveMultiFrameTDOARequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Device ID.
	DevEui []byte `protobuf:"bytes,1,opt,name=dev_eui,json=devEUI,proto3" json:"dev_eui,omitempty"`
	// Frames meta-data.
	FrameRxInfoSet []*FrameRXInfo `protobuf:"bytes,2,rep,name=frame_rx_info_set,json=frameRXInfoSet,proto3" json:"frame_rx_info_set,omitempty"`
	// Device reference altitude.
	DeviceReferenceAltitude float64 `protobuf:"fixed64,3,opt,name=device_reference_altitude,json=deviceReferenceAltitude,proto3" json:"device_reference_altitude,omitempty"`
}

func (x *ResolveMultiFrameTDOARequest) Reset() {
	*x = ResolveMultiFrameTDOARequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_geo_geo_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ResolveMultiFrameTDOARequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ResolveMultiFrameTDOARequest) ProtoMessage() {}

func (x *ResolveMultiFrameTDOARequest) ProtoReflect() protoreflect.Message {
	mi := &file_geo_geo_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ResolveMultiFrameTDOARequest.ProtoReflect.Descriptor instead.
func (*ResolveMultiFrameTDOARequest) Descriptor() ([]byte, []int) {
	return file_geo_geo_proto_rawDescGZIP(), []int{3}
}

func (x *ResolveMultiFrameTDOARequest) GetDevEui() []byte {
	if x != nil {
		return x.DevEui
	}
	return nil
}

func (x *ResolveMultiFrameTDOARequest) GetFrameRxInfoSet() []*FrameRXInfo {
	if x != nil {
		return x.FrameRxInfoSet
	}
	return nil
}

func (x *ResolveMultiFrameTDOARequest) GetDeviceReferenceAltitude() float64 {
	if x != nil {
		return x.DeviceReferenceAltitude
	}
	return 0
}

type ResolveTDOAResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Resolve result.
	Result *ResolveResult `protobuf:"bytes,1,opt,name=result,proto3" json:"result,omitempty"`
}

func (x *ResolveTDOAResponse) Reset() {
	*x = ResolveTDOAResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_geo_geo_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ResolveTDOAResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ResolveTDOAResponse) ProtoMessage() {}

func (x *ResolveTDOAResponse) ProtoReflect() protoreflect.Message {
	mi := &file_geo_geo_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ResolveTDOAResponse.ProtoReflect.Descriptor instead.
func (*ResolveTDOAResponse) Descriptor() ([]byte, []int) {
	return file_geo_geo_proto_rawDescGZIP(), []int{4}
}

func (x *ResolveTDOAResponse) GetResult() *ResolveResult {
	if x != nil {
		return x.Result
	}
	return nil
}

type ResolveMultiFrameTDOAResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Resolve result.
	Result *ResolveResult `protobuf:"bytes,1,opt,name=result,proto3" json:"result,omitempty"`
}

func (x *ResolveMultiFrameTDOAResponse) Reset() {
	*x = ResolveMultiFrameTDOAResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_geo_geo_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ResolveMultiFrameTDOAResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ResolveMultiFrameTDOAResponse) ProtoMessage() {}

func (x *ResolveMultiFrameTDOAResponse) ProtoReflect() protoreflect.Message {
	mi := &file_geo_geo_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ResolveMultiFrameTDOAResponse.ProtoReflect.Descriptor instead.
func (*ResolveMultiFrameTDOAResponse) Descriptor() ([]byte, []int) {
	return file_geo_geo_proto_rawDescGZIP(), []int{5}
}

func (x *ResolveMultiFrameTDOAResponse) GetResult() *ResolveResult {
	if x != nil {
		return x.Result
	}
	return nil
}

var File_geo_geo_proto protoreflect.FileDescriptor

var file_geo_geo_proto_rawDesc = []byte{
	0x0a, 0x0d, 0x67, 0x65, 0x6f, 0x2f, 0x67, 0x65, 0x6f, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12,
	0x03, 0x67, 0x65, 0x6f, 0x1a, 0x0b, 0x67, 0x77, 0x2f, 0x67, 0x77, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x1a, 0x13, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x2f, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x3d, 0x0a, 0x0d, 0x52, 0x65, 0x73, 0x6f, 0x6c, 0x76,
	0x65, 0x52, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x12, 0x2c, 0x0a, 0x08, 0x6c, 0x6f, 0x63, 0x61, 0x74,
	0x69, 0x6f, 0x6e, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x10, 0x2e, 0x63, 0x6f, 0x6d, 0x6d,
	0x6f, 0x6e, 0x2e, 0x4c, 0x6f, 0x63, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x52, 0x08, 0x6c, 0x6f, 0x63,
	0x61, 0x74, 0x69, 0x6f, 0x6e, 0x22, 0x38, 0x0a, 0x0b, 0x46, 0x72, 0x61, 0x6d, 0x65, 0x52, 0x58,
	0x49, 0x6e, 0x66, 0x6f, 0x12, 0x29, 0x0a, 0x07, 0x72, 0x78, 0x5f, 0x69, 0x6e, 0x66, 0x6f, 0x18,
	0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x10, 0x2e, 0x67, 0x77, 0x2e, 0x55, 0x70, 0x6c, 0x69, 0x6e,
	0x6b, 0x52, 0x58, 0x49, 0x6e, 0x66, 0x6f, 0x52, 0x06, 0x72, 0x78, 0x49, 0x6e, 0x66, 0x6f, 0x22,
	0x9f, 0x01, 0x0a, 0x12, 0x52, 0x65, 0x73, 0x6f, 0x6c, 0x76, 0x65, 0x54, 0x44, 0x4f, 0x41, 0x52,
	0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x17, 0x0a, 0x07, 0x64, 0x65, 0x76, 0x5f, 0x65, 0x75,
	0x69, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0c, 0x52, 0x06, 0x64, 0x65, 0x76, 0x45, 0x55, 0x49, 0x12,
	0x34, 0x0a, 0x0d, 0x66, 0x72, 0x61, 0x6d, 0x65, 0x5f, 0x72, 0x78, 0x5f, 0x69, 0x6e, 0x66, 0x6f,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x10, 0x2e, 0x67, 0x65, 0x6f, 0x2e, 0x46, 0x72, 0x61,
	0x6d, 0x65, 0x52, 0x58, 0x49, 0x6e, 0x66, 0x6f, 0x52, 0x0b, 0x66, 0x72, 0x61, 0x6d, 0x65, 0x52,
	0x58, 0x49, 0x6e, 0x66, 0x6f, 0x12, 0x3a, 0x0a, 0x19, 0x64, 0x65, 0x76, 0x69, 0x63, 0x65, 0x5f,
	0x72, 0x65, 0x66, 0x65, 0x72, 0x65, 0x6e, 0x63, 0x65, 0x5f, 0x61, 0x6c, 0x74, 0x69, 0x74, 0x75,
	0x64, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x01, 0x52, 0x17, 0x64, 0x65, 0x76, 0x69, 0x63, 0x65,
	0x52, 0x65, 0x66, 0x65, 0x72, 0x65, 0x6e, 0x63, 0x65, 0x41, 0x6c, 0x74, 0x69, 0x74, 0x75, 0x64,
	0x65, 0x22, 0xb0, 0x01, 0x0a, 0x1c, 0x52, 0x65, 0x73, 0x6f, 0x6c, 0x76, 0x65, 0x4d, 0x75, 0x6c,
	0x74, 0x69, 0x46, 0x72, 0x61, 0x6d, 0x65, 0x54, 0x44, 0x4f, 0x41, 0x52, 0x65, 0x71, 0x75, 0x65,
	0x73, 0x74, 0x12, 0x17, 0x0a, 0x07, 0x64, 0x65, 0x76, 0x5f, 0x65, 0x75, 0x69, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x0c, 0x52, 0x06, 0x64, 0x65, 0x76, 0x45, 0x55, 0x49, 0x12, 0x3b, 0x0a, 0x11, 0x66,
	0x72, 0x61, 0x6d, 0x65, 0x5f, 0x72, 0x78, 0x5f, 0x69, 0x6e, 0x66, 0x6f, 0x5f, 0x73, 0x65, 0x74,
	0x18, 0x02, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x10, 0x2e, 0x67, 0x65, 0x6f, 0x2e, 0x46, 0x72, 0x61,
	0x6d, 0x65, 0x52, 0x58, 0x49, 0x6e, 0x66, 0x6f, 0x52, 0x0e, 0x66, 0x72, 0x61, 0x6d, 0x65, 0x52,
	0x58, 0x49, 0x6e, 0x66, 0x6f, 0x53, 0x65, 0x74, 0x12, 0x3a, 0x0a, 0x19, 0x64, 0x65, 0x76, 0x69,
	0x63, 0x65, 0x5f, 0x72, 0x65, 0x66, 0x65, 0x72, 0x65, 0x6e, 0x63, 0x65, 0x5f, 0x61, 0x6c, 0x74,
	0x69, 0x74, 0x75, 0x64, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x01, 0x52, 0x17, 0x64, 0x65, 0x76,
	0x69, 0x63, 0x65, 0x52, 0x65, 0x66, 0x65, 0x72, 0x65, 0x6e, 0x63, 0x65, 0x41, 0x6c, 0x74, 0x69,
	0x74, 0x75, 0x64, 0x65, 0x22, 0x41, 0x0a, 0x13, 0x52, 0x65, 0x73, 0x6f, 0x6c, 0x76, 0x65, 0x54,
	0x44, 0x4f, 0x41, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x2a, 0x0a, 0x06, 0x72,
	0x65, 0x73, 0x75, 0x6c, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x12, 0x2e, 0x67, 0x65,
	0x6f, 0x2e, 0x52, 0x65, 0x73, 0x6f, 0x6c, 0x76, 0x65, 0x52, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x52,
	0x06, 0x72, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x22, 0x4b, 0x0a, 0x1d, 0x52, 0x65, 0x73, 0x6f, 0x6c,
	0x76, 0x65, 0x4d, 0x75, 0x6c, 0x74, 0x69, 0x46, 0x72, 0x61, 0x6d, 0x65, 0x54, 0x44, 0x4f, 0x41,
	0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x2a, 0x0a, 0x06, 0x72, 0x65, 0x73, 0x75,
	0x6c, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x12, 0x2e, 0x67, 0x65, 0x6f, 0x2e, 0x52,
	0x65, 0x73, 0x6f, 0x6c, 0x76, 0x65, 0x52, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x52, 0x06, 0x72, 0x65,
	0x73, 0x75, 0x6c, 0x74, 0x32, 0xc0, 0x01, 0x0a, 0x18, 0x47, 0x65, 0x6f, 0x6c, 0x6f, 0x63, 0x61,
	0x74, 0x69, 0x6f, 0x6e, 0x53, 0x65, 0x72, 0x76, 0x65, 0x72, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63,
	0x65, 0x12, 0x42, 0x0a, 0x0b, 0x52, 0x65, 0x73, 0x6f, 0x6c, 0x76, 0x65, 0x54, 0x44, 0x4f, 0x41,
	0x12, 0x17, 0x2e, 0x67, 0x65, 0x6f, 0x2e, 0x52, 0x65, 0x73, 0x6f, 0x6c, 0x76, 0x65, 0x54, 0x44,
	0x4f, 0x41, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x18, 0x2e, 0x67, 0x65, 0x6f, 0x2e,
	0x52, 0x65, 0x73, 0x6f, 0x6c, 0x76, 0x65, 0x54, 0x44, 0x4f, 0x41, 0x52, 0x65, 0x73, 0x70, 0x6f,
	0x6e, 0x73, 0x65, 0x22, 0x00, 0x12, 0x60, 0x0a, 0x15, 0x52, 0x65, 0x73, 0x6f, 0x6c, 0x76, 0x65,
	0x4d, 0x75, 0x6c, 0x74, 0x69, 0x46, 0x72, 0x61, 0x6d, 0x65, 0x54, 0x44, 0x4f, 0x41, 0x12, 0x21,
	0x2e, 0x67, 0x65, 0x6f, 0x2e, 0x52, 0x65, 0x73, 0x6f, 0x6c, 0x76, 0x65, 0x4d, 0x75, 0x6c, 0x74,
	0x69, 0x46, 0x72, 0x61, 0x6d, 0x65, 0x54, 0x44, 0x4f, 0x41, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x1a, 0x22, 0x2e, 0x67, 0x65, 0x6f, 0x2e, 0x52, 0x65, 0x73, 0x6f, 0x6c, 0x76, 0x65, 0x4d,
	0x75, 0x6c, 0x74, 0x69, 0x46, 0x72, 0x61, 0x6d, 0x65, 0x54, 0x44, 0x4f, 0x41, 0x52, 0x65, 0x73,
	0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x00, 0x42, 0x5e, 0x0a, 0x15, 0x69, 0x6f, 0x2e, 0x63, 0x68,
	0x69, 0x72, 0x70, 0x73, 0x74, 0x61, 0x63, 0x6b, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x67, 0x65, 0x6f,
	0x42, 0x16, 0x47, 0x65, 0x6f, 0x6c, 0x6f, 0x63, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x53, 0x65, 0x72,
	0x76, 0x65, 0x72, 0x50, 0x72, 0x6f, 0x74, 0x6f, 0x50, 0x01, 0x5a, 0x2b, 0x67, 0x69, 0x74, 0x68,
	0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x62, 0x72, 0x6f, 0x63, 0x61, 0x61, 0x72, 0x2f, 0x63,
	0x68, 0x69, 0x72, 0x70, 0x73, 0x74, 0x61, 0x63, 0x6b, 0x2d, 0x61, 0x70, 0x69, 0x2f, 0x67, 0x6f,
	0x2f, 0x76, 0x33, 0x2f, 0x67, 0x65, 0x6f, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_geo_geo_proto_rawDescOnce sync.Once
	file_geo_geo_proto_rawDescData = file_geo_geo_proto_rawDesc
)

func file_geo_geo_proto_rawDescGZIP() []byte {
	file_geo_geo_proto_rawDescOnce.Do(func() {
		file_geo_geo_proto_rawDescData = protoimpl.X.CompressGZIP(file_geo_geo_proto_rawDescData)
	})
	return file_geo_geo_proto_rawDescData
}

var file_geo_geo_proto_msgTypes = make([]protoimpl.MessageInfo, 6)
var file_geo_geo_proto_goTypes = []interface{}{
	(*ResolveResult)(nil),                 // 0: geo.ResolveResult
	(*FrameRXInfo)(nil),                   // 1: geo.FrameRXInfo
	(*ResolveTDOARequest)(nil),            // 2: geo.ResolveTDOARequest
	(*ResolveMultiFrameTDOARequest)(nil),  // 3: geo.ResolveMultiFrameTDOARequest
	(*ResolveTDOAResponse)(nil),           // 4: geo.ResolveTDOAResponse
	(*ResolveMultiFrameTDOAResponse)(nil), // 5: geo.ResolveMultiFrameTDOAResponse
	(*common.Location)(nil),               // 6: common.Location
	(*gw.UplinkRXInfo)(nil),               // 7: gw.UplinkRXInfo
}
var file_geo_geo_proto_depIdxs = []int32{
	6, // 0: geo.ResolveResult.location:type_name -> common.Location
	7, // 1: geo.FrameRXInfo.rx_info:type_name -> gw.UplinkRXInfo
	1, // 2: geo.ResolveTDOARequest.frame_rx_info:type_name -> geo.FrameRXInfo
	1, // 3: geo.ResolveMultiFrameTDOARequest.frame_rx_info_set:type_name -> geo.FrameRXInfo
	0, // 4: geo.ResolveTDOAResponse.result:type_name -> geo.ResolveResult
	0, // 5: geo.ResolveMultiFrameTDOAResponse.result:type_name -> geo.ResolveResult
	2, // 6: geo.GeolocationServerService.ResolveTDOA:input_type -> geo.ResolveTDOARequest
	3, // 7: geo.GeolocationServerService.ResolveMultiFrameTDOA:input_type -> geo.ResolveMultiFrameTDOARequest
	4, // 8: geo.GeolocationServerService.ResolveTDOA:output_type -> geo.ResolveTDOAResponse
	5, // 9: geo.GeolocationServerService.ResolveMultiFrameTDOA:output_type -> geo.ResolveMultiFrameTDOAResponse
	8, // [8:10] is the sub-list for method output_type
	6, // [6:8] is the sub-list for method input_type
	6, // [6:6] is the sub-list for extension type_name
	6, // [6:6] is the sub-list for extension extendee
	0, // [0:6] is the sub-list for field type_name
}

func init() { file_geo_geo_proto_init() }
func file_geo_geo_proto_init() {
	if File_geo_geo_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_geo_geo_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ResolveResult); i {
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
		file_geo_geo_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*FrameRXInfo); i {
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
		file_geo_geo_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ResolveTDOARequest); i {
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
		file_geo_geo_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ResolveMultiFrameTDOARequest); i {
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
		file_geo_geo_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ResolveTDOAResponse); i {
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
		file_geo_geo_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ResolveMultiFrameTDOAResponse); i {
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
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_geo_geo_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   6,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_geo_geo_proto_goTypes,
		DependencyIndexes: file_geo_geo_proto_depIdxs,
		MessageInfos:      file_geo_geo_proto_msgTypes,
	}.Build()
	File_geo_geo_proto = out.File
	file_geo_geo_proto_rawDesc = nil
	file_geo_geo_proto_goTypes = nil
	file_geo_geo_proto_depIdxs = nil
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConnInterface

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion6

// GeolocationServerServiceClient is the client API for GeolocationServerService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type GeolocationServerServiceClient interface {
	// ResolveTDOA resolves the location based on TDOA.
	ResolveTDOA(ctx context.Context, in *ResolveTDOARequest, opts ...grpc.CallOption) (*ResolveTDOAResponse, error)
	// ResolveMultiFrameTDOA resolves the location using TDOA, based on
	// multiple frames.
	ResolveMultiFrameTDOA(ctx context.Context, in *ResolveMultiFrameTDOARequest, opts ...grpc.CallOption) (*ResolveMultiFrameTDOAResponse, error)
}

type geolocationServerServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewGeolocationServerServiceClient(cc grpc.ClientConnInterface) GeolocationServerServiceClient {
	return &geolocationServerServiceClient{cc}
}

func (c *geolocationServerServiceClient) ResolveTDOA(ctx context.Context, in *ResolveTDOARequest, opts ...grpc.CallOption) (*ResolveTDOAResponse, error) {
	out := new(ResolveTDOAResponse)
	err := c.cc.Invoke(ctx, "/geo.GeolocationServerService/ResolveTDOA", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *geolocationServerServiceClient) ResolveMultiFrameTDOA(ctx context.Context, in *ResolveMultiFrameTDOARequest, opts ...grpc.CallOption) (*ResolveMultiFrameTDOAResponse, error) {
	out := new(ResolveMultiFrameTDOAResponse)
	err := c.cc.Invoke(ctx, "/geo.GeolocationServerService/ResolveMultiFrameTDOA", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// GeolocationServerServiceServer is the server API for GeolocationServerService service.
type GeolocationServerServiceServer interface {
	// ResolveTDOA resolves the location based on TDOA.
	ResolveTDOA(context.Context, *ResolveTDOARequest) (*ResolveTDOAResponse, error)
	// ResolveMultiFrameTDOA resolves the location using TDOA, based on
	// multiple frames.
	ResolveMultiFrameTDOA(context.Context, *ResolveMultiFrameTDOARequest) (*ResolveMultiFrameTDOAResponse, error)
}

// UnimplementedGeolocationServerServiceServer can be embedded to have forward compatible implementations.
type UnimplementedGeolocationServerServiceServer struct {
}

func (*UnimplementedGeolocationServerServiceServer) ResolveTDOA(context.Context, *ResolveTDOARequest) (*ResolveTDOAResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ResolveTDOA not implemented")
}
func (*UnimplementedGeolocationServerServiceServer) ResolveMultiFrameTDOA(context.Context, *ResolveMultiFrameTDOARequest) (*ResolveMultiFrameTDOAResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ResolveMultiFrameTDOA not implemented")
}

func RegisterGeolocationServerServiceServer(s *grpc.Server, srv GeolocationServerServiceServer) {
	s.RegisterService(&_GeolocationServerService_serviceDesc, srv)
}

func _GeolocationServerService_ResolveTDOA_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ResolveTDOARequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GeolocationServerServiceServer).ResolveTDOA(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/geo.GeolocationServerService/ResolveTDOA",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GeolocationServerServiceServer).ResolveTDOA(ctx, req.(*ResolveTDOARequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GeolocationServerService_ResolveMultiFrameTDOA_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ResolveMultiFrameTDOARequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GeolocationServerServiceServer).ResolveMultiFrameTDOA(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/geo.GeolocationServerService/ResolveMultiFrameTDOA",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GeolocationServerServiceServer).ResolveMultiFrameTDOA(ctx, req.(*ResolveMultiFrameTDOARequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _GeolocationServerService_serviceDesc = grpc.ServiceDesc{
	ServiceName: "geo.GeolocationServerService",
	HandlerType: (*GeolocationServerServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "ResolveTDOA",
			Handler:    _GeolocationServerService_ResolveTDOA_Handler,
		},
		{
			MethodName: "ResolveMultiFrameTDOA",
			Handler:    _GeolocationServerService_ResolveMultiFrameTDOA_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "geo/geo.proto",
}
