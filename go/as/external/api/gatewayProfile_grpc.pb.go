// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.3.0
// - protoc             (unknown)
// source: as/external/api/gatewayProfile.proto

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
	GatewayProfileService_Create_FullMethodName        = "/api.GatewayProfileService/Create"
	GatewayProfileService_Get_FullMethodName           = "/api.GatewayProfileService/Get"
	GatewayProfileService_Update_FullMethodName        = "/api.GatewayProfileService/Update"
	GatewayProfileService_Delete_FullMethodName        = "/api.GatewayProfileService/Delete"
	GatewayProfileService_List_FullMethodName          = "/api.GatewayProfileService/List"
	GatewayProfileService_CountGateways_FullMethodName = "/api.GatewayProfileService/CountGateways"
)

// GatewayProfileServiceClient is the client API for GatewayProfileService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type GatewayProfileServiceClient interface {
	// Create creates the given gateway-profile.
	Create(ctx context.Context, in *CreateGatewayProfileRequest, opts ...grpc.CallOption) (*CreateGatewayProfileResponse, error)
	// Get returns the gateway-profile matching the given id.
	Get(ctx context.Context, in *GetGatewayProfileRequest, opts ...grpc.CallOption) (*GetGatewayProfileResponse, error)
	// Update updates the given gateway-profile.
	Update(ctx context.Context, in *UpdateGatewayProfileRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	// Delete deletes the gateway-profile matching the given id.
	Delete(ctx context.Context, in *DeleteGatewayProfileRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	// List returns the existing gateway-profiles.
	List(ctx context.Context, in *ListGatewayProfilesRequest, opts ...grpc.CallOption) (*ListGatewayProfilesResponse, error)
	// CountGateways returns counts of gateways grouped by gateway-profiles.
	CountGateways(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*CountGatewaysResponse, error)
}

type gatewayProfileServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewGatewayProfileServiceClient(cc grpc.ClientConnInterface) GatewayProfileServiceClient {
	return &gatewayProfileServiceClient{cc}
}

func (c *gatewayProfileServiceClient) Create(ctx context.Context, in *CreateGatewayProfileRequest, opts ...grpc.CallOption) (*CreateGatewayProfileResponse, error) {
	out := new(CreateGatewayProfileResponse)
	err := c.cc.Invoke(ctx, GatewayProfileService_Create_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayProfileServiceClient) Get(ctx context.Context, in *GetGatewayProfileRequest, opts ...grpc.CallOption) (*GetGatewayProfileResponse, error) {
	out := new(GetGatewayProfileResponse)
	err := c.cc.Invoke(ctx, GatewayProfileService_Get_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayProfileServiceClient) Update(ctx context.Context, in *UpdateGatewayProfileRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, GatewayProfileService_Update_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayProfileServiceClient) Delete(ctx context.Context, in *DeleteGatewayProfileRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, GatewayProfileService_Delete_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayProfileServiceClient) List(ctx context.Context, in *ListGatewayProfilesRequest, opts ...grpc.CallOption) (*ListGatewayProfilesResponse, error) {
	out := new(ListGatewayProfilesResponse)
	err := c.cc.Invoke(ctx, GatewayProfileService_List_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayProfileServiceClient) CountGateways(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*CountGatewaysResponse, error) {
	out := new(CountGatewaysResponse)
	err := c.cc.Invoke(ctx, GatewayProfileService_CountGateways_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// GatewayProfileServiceServer is the server API for GatewayProfileService service.
// All implementations must embed UnimplementedGatewayProfileServiceServer
// for forward compatibility
type GatewayProfileServiceServer interface {
	// Create creates the given gateway-profile.
	Create(context.Context, *CreateGatewayProfileRequest) (*CreateGatewayProfileResponse, error)
	// Get returns the gateway-profile matching the given id.
	Get(context.Context, *GetGatewayProfileRequest) (*GetGatewayProfileResponse, error)
	// Update updates the given gateway-profile.
	Update(context.Context, *UpdateGatewayProfileRequest) (*emptypb.Empty, error)
	// Delete deletes the gateway-profile matching the given id.
	Delete(context.Context, *DeleteGatewayProfileRequest) (*emptypb.Empty, error)
	// List returns the existing gateway-profiles.
	List(context.Context, *ListGatewayProfilesRequest) (*ListGatewayProfilesResponse, error)
	// CountGateways returns counts of gateways grouped by gateway-profiles.
	CountGateways(context.Context, *emptypb.Empty) (*CountGatewaysResponse, error)
	mustEmbedUnimplementedGatewayProfileServiceServer()
}

// UnimplementedGatewayProfileServiceServer must be embedded to have forward compatible implementations.
type UnimplementedGatewayProfileServiceServer struct {
}

func (UnimplementedGatewayProfileServiceServer) Create(context.Context, *CreateGatewayProfileRequest) (*CreateGatewayProfileResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Create not implemented")
}
func (UnimplementedGatewayProfileServiceServer) Get(context.Context, *GetGatewayProfileRequest) (*GetGatewayProfileResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Get not implemented")
}
func (UnimplementedGatewayProfileServiceServer) Update(context.Context, *UpdateGatewayProfileRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Update not implemented")
}
func (UnimplementedGatewayProfileServiceServer) Delete(context.Context, *DeleteGatewayProfileRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Delete not implemented")
}
func (UnimplementedGatewayProfileServiceServer) List(context.Context, *ListGatewayProfilesRequest) (*ListGatewayProfilesResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (UnimplementedGatewayProfileServiceServer) CountGateways(context.Context, *emptypb.Empty) (*CountGatewaysResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CountGateways not implemented")
}
func (UnimplementedGatewayProfileServiceServer) mustEmbedUnimplementedGatewayProfileServiceServer() {}

// UnsafeGatewayProfileServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to GatewayProfileServiceServer will
// result in compilation errors.
type UnsafeGatewayProfileServiceServer interface {
	mustEmbedUnimplementedGatewayProfileServiceServer()
}

func RegisterGatewayProfileServiceServer(s grpc.ServiceRegistrar, srv GatewayProfileServiceServer) {
	s.RegisterService(&GatewayProfileService_ServiceDesc, srv)
}

func _GatewayProfileService_Create_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateGatewayProfileRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayProfileServiceServer).Create(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayProfileService_Create_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayProfileServiceServer).Create(ctx, req.(*CreateGatewayProfileRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GatewayProfileService_Get_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetGatewayProfileRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayProfileServiceServer).Get(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayProfileService_Get_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayProfileServiceServer).Get(ctx, req.(*GetGatewayProfileRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GatewayProfileService_Update_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateGatewayProfileRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayProfileServiceServer).Update(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayProfileService_Update_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayProfileServiceServer).Update(ctx, req.(*UpdateGatewayProfileRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GatewayProfileService_Delete_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DeleteGatewayProfileRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayProfileServiceServer).Delete(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayProfileService_Delete_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayProfileServiceServer).Delete(ctx, req.(*DeleteGatewayProfileRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GatewayProfileService_List_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListGatewayProfilesRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayProfileServiceServer).List(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayProfileService_List_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayProfileServiceServer).List(ctx, req.(*ListGatewayProfilesRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GatewayProfileService_CountGateways_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(emptypb.Empty)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayProfileServiceServer).CountGateways(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayProfileService_CountGateways_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayProfileServiceServer).CountGateways(ctx, req.(*emptypb.Empty))
	}
	return interceptor(ctx, in, info, handler)
}

// GatewayProfileService_ServiceDesc is the grpc.ServiceDesc for GatewayProfileService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var GatewayProfileService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "api.GatewayProfileService",
	HandlerType: (*GatewayProfileServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Create",
			Handler:    _GatewayProfileService_Create_Handler,
		},
		{
			MethodName: "Get",
			Handler:    _GatewayProfileService_Get_Handler,
		},
		{
			MethodName: "Update",
			Handler:    _GatewayProfileService_Update_Handler,
		},
		{
			MethodName: "Delete",
			Handler:    _GatewayProfileService_Delete_Handler,
		},
		{
			MethodName: "List",
			Handler:    _GatewayProfileService_List_Handler,
		},
		{
			MethodName: "CountGateways",
			Handler:    _GatewayProfileService_CountGateways_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "as/external/api/gatewayProfile.proto",
}