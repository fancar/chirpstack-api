// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.3.0
// - protoc             (unknown)
// source: as/external/api/deviceQueue.proto

package api

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	emptypb "google.golang.org/protobuf/types/known/emptypb"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

const (
	DeviceQueueService_Enqueue_FullMethodName             = "/api.DeviceQueueService/Enqueue"
	DeviceQueueService_EnqueueHex_FullMethodName          = "/api.DeviceQueueService/EnqueueHex"
	DeviceQueueService_Flush_FullMethodName               = "/api.DeviceQueueService/Flush"
	DeviceQueueService_List_FullMethodName                = "/api.DeviceQueueService/List"
	DeviceQueueService_ActilityEnqueue_FullMethodName     = "/api.DeviceQueueService/ActilityEnqueue"
	DeviceQueueService_GetNextDownlinkFCnt_FullMethodName = "/api.DeviceQueueService/GetNextDownlinkFCnt"
)

// DeviceQueueServiceClient is the client API for DeviceQueueService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type DeviceQueueServiceClient interface {
	// Enqueue adds the given item to the device-queue.
	Enqueue(ctx context.Context, in *EnqueueDeviceQueueItemRequest, opts ...grpc.CallOption) (*EnqueueDeviceQueueItemResponse, error)
	// EnqueueHex adds the given item to the device-queue with hex-payload.
	EnqueueHex(ctx context.Context, in *EnqueueDeviceQueueItemHexRequest, opts ...grpc.CallOption) (*EnqueueDeviceQueueItemResponse, error)
	// Flush flushes the downlink device-queue.
	Flush(ctx context.Context, in *FlushDeviceQueueRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	// List lists the items in the device-queue.
	List(ctx context.Context, in *ListDeviceQueueItemsRequest, opts ...grpc.CallOption) (*ListDeviceQueueItemsResponse, error)
	// ActilityEnqueue adds the given item to the device-queue with actility-styled request\response.
	ActilityEnqueue(ctx context.Context, in *EnqueueDeviceQueueActilityItemRequest, opts ...grpc.CallOption) (*EnqueueDeviceQueueActilityItemResponse, error)
	// GetNextDownlinkFCnt returns next downlink f-counter for the device
	// used by clients who encrypt payload data themself
	GetNextDownlinkFCnt(ctx context.Context, in *GetNextDownlinkFCntRequest, opts ...grpc.CallOption) (*GetNextDownlinkFCntResponse, error)
}

type deviceQueueServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewDeviceQueueServiceClient(cc grpc.ClientConnInterface) DeviceQueueServiceClient {
	return &deviceQueueServiceClient{cc}
}

func (c *deviceQueueServiceClient) Enqueue(ctx context.Context, in *EnqueueDeviceQueueItemRequest, opts ...grpc.CallOption) (*EnqueueDeviceQueueItemResponse, error) {
	out := new(EnqueueDeviceQueueItemResponse)
	err := c.cc.Invoke(ctx, DeviceQueueService_Enqueue_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *deviceQueueServiceClient) EnqueueHex(ctx context.Context, in *EnqueueDeviceQueueItemHexRequest, opts ...grpc.CallOption) (*EnqueueDeviceQueueItemResponse, error) {
	out := new(EnqueueDeviceQueueItemResponse)
	err := c.cc.Invoke(ctx, DeviceQueueService_EnqueueHex_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *deviceQueueServiceClient) Flush(ctx context.Context, in *FlushDeviceQueueRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, DeviceQueueService_Flush_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *deviceQueueServiceClient) List(ctx context.Context, in *ListDeviceQueueItemsRequest, opts ...grpc.CallOption) (*ListDeviceQueueItemsResponse, error) {
	out := new(ListDeviceQueueItemsResponse)
	err := c.cc.Invoke(ctx, DeviceQueueService_List_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *deviceQueueServiceClient) ActilityEnqueue(ctx context.Context, in *EnqueueDeviceQueueActilityItemRequest, opts ...grpc.CallOption) (*EnqueueDeviceQueueActilityItemResponse, error) {
	out := new(EnqueueDeviceQueueActilityItemResponse)
	err := c.cc.Invoke(ctx, DeviceQueueService_ActilityEnqueue_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *deviceQueueServiceClient) GetNextDownlinkFCnt(ctx context.Context, in *GetNextDownlinkFCntRequest, opts ...grpc.CallOption) (*GetNextDownlinkFCntResponse, error) {
	out := new(GetNextDownlinkFCntResponse)
	err := c.cc.Invoke(ctx, DeviceQueueService_GetNextDownlinkFCnt_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// DeviceQueueServiceServer is the server API for DeviceQueueService service.
// All implementations must embed UnimplementedDeviceQueueServiceServer
// for forward compatibility
type DeviceQueueServiceServer interface {
	// Enqueue adds the given item to the device-queue.
	Enqueue(context.Context, *EnqueueDeviceQueueItemRequest) (*EnqueueDeviceQueueItemResponse, error)
	// EnqueueHex adds the given item to the device-queue with hex-payload.
	EnqueueHex(context.Context, *EnqueueDeviceQueueItemHexRequest) (*EnqueueDeviceQueueItemResponse, error)
	// Flush flushes the downlink device-queue.
	Flush(context.Context, *FlushDeviceQueueRequest) (*emptypb.Empty, error)
	// List lists the items in the device-queue.
	List(context.Context, *ListDeviceQueueItemsRequest) (*ListDeviceQueueItemsResponse, error)
	// ActilityEnqueue adds the given item to the device-queue with actility-styled request\response.
	ActilityEnqueue(context.Context, *EnqueueDeviceQueueActilityItemRequest) (*EnqueueDeviceQueueActilityItemResponse, error)
	// GetNextDownlinkFCnt returns next downlink f-counter for the device
	// used by clients who encrypt payload data themself
	GetNextDownlinkFCnt(context.Context, *GetNextDownlinkFCntRequest) (*GetNextDownlinkFCntResponse, error)
	mustEmbedUnimplementedDeviceQueueServiceServer()
}

// UnimplementedDeviceQueueServiceServer must be embedded to have forward compatible implementations.
type UnimplementedDeviceQueueServiceServer struct {
}

func (UnimplementedDeviceQueueServiceServer) Enqueue(context.Context, *EnqueueDeviceQueueItemRequest) (*EnqueueDeviceQueueItemResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Enqueue not implemented")
}
func (UnimplementedDeviceQueueServiceServer) EnqueueHex(context.Context, *EnqueueDeviceQueueItemHexRequest) (*EnqueueDeviceQueueItemResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method EnqueueHex not implemented")
}
func (UnimplementedDeviceQueueServiceServer) Flush(context.Context, *FlushDeviceQueueRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Flush not implemented")
}
func (UnimplementedDeviceQueueServiceServer) List(context.Context, *ListDeviceQueueItemsRequest) (*ListDeviceQueueItemsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (UnimplementedDeviceQueueServiceServer) ActilityEnqueue(context.Context, *EnqueueDeviceQueueActilityItemRequest) (*EnqueueDeviceQueueActilityItemResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ActilityEnqueue not implemented")
}
func (UnimplementedDeviceQueueServiceServer) GetNextDownlinkFCnt(context.Context, *GetNextDownlinkFCntRequest) (*GetNextDownlinkFCntResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetNextDownlinkFCnt not implemented")
}
func (UnimplementedDeviceQueueServiceServer) mustEmbedUnimplementedDeviceQueueServiceServer() {}

// UnsafeDeviceQueueServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to DeviceQueueServiceServer will
// result in compilation errors.
type UnsafeDeviceQueueServiceServer interface {
	mustEmbedUnimplementedDeviceQueueServiceServer()
}

func RegisterDeviceQueueServiceServer(s grpc.ServiceRegistrar, srv DeviceQueueServiceServer) {
	s.RegisterService(&DeviceQueueService_ServiceDesc, srv)
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
		FullMethod: DeviceQueueService_Enqueue_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DeviceQueueServiceServer).Enqueue(ctx, req.(*EnqueueDeviceQueueItemRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DeviceQueueService_EnqueueHex_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(EnqueueDeviceQueueItemHexRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DeviceQueueServiceServer).EnqueueHex(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: DeviceQueueService_EnqueueHex_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DeviceQueueServiceServer).EnqueueHex(ctx, req.(*EnqueueDeviceQueueItemHexRequest))
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
		FullMethod: DeviceQueueService_Flush_FullMethodName,
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
		FullMethod: DeviceQueueService_List_FullMethodName,
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
		FullMethod: DeviceQueueService_ActilityEnqueue_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DeviceQueueServiceServer).ActilityEnqueue(ctx, req.(*EnqueueDeviceQueueActilityItemRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DeviceQueueService_GetNextDownlinkFCnt_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetNextDownlinkFCntRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DeviceQueueServiceServer).GetNextDownlinkFCnt(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: DeviceQueueService_GetNextDownlinkFCnt_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DeviceQueueServiceServer).GetNextDownlinkFCnt(ctx, req.(*GetNextDownlinkFCntRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// DeviceQueueService_ServiceDesc is the grpc.ServiceDesc for DeviceQueueService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var DeviceQueueService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "api.DeviceQueueService",
	HandlerType: (*DeviceQueueServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Enqueue",
			Handler:    _DeviceQueueService_Enqueue_Handler,
		},
		{
			MethodName: "EnqueueHex",
			Handler:    _DeviceQueueService_EnqueueHex_Handler,
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
		{
			MethodName: "GetNextDownlinkFCnt",
			Handler:    _DeviceQueueService_GetNextDownlinkFCnt_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "as/external/api/deviceQueue.proto",
}
