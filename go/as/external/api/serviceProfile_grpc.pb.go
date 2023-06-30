// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.3.0
// - protoc             (unknown)
// source: as/external/api/serviceProfile.proto

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
	ServiceProfileService_Create_FullMethodName = "/api.ServiceProfileService/Create"
	ServiceProfileService_Get_FullMethodName    = "/api.ServiceProfileService/Get"
	ServiceProfileService_Update_FullMethodName = "/api.ServiceProfileService/Update"
	ServiceProfileService_Delete_FullMethodName = "/api.ServiceProfileService/Delete"
	ServiceProfileService_List_FullMethodName   = "/api.ServiceProfileService/List"
)

// ServiceProfileServiceClient is the client API for ServiceProfileService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ServiceProfileServiceClient interface {
	// Create creates the given service-profile.
	Create(ctx context.Context, in *CreateServiceProfileRequest, opts ...grpc.CallOption) (*CreateServiceProfileResponse, error)
	// Get returns the service-profile matching the given id.
	Get(ctx context.Context, in *GetServiceProfileRequest, opts ...grpc.CallOption) (*GetServiceProfileResponse, error)
	// Update updates the given serviceprofile.
	Update(ctx context.Context, in *UpdateServiceProfileRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	// Delete deletes the service-profile matching the given id.
	Delete(ctx context.Context, in *DeleteServiceProfileRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	// List lists the available service-profiles.
	List(ctx context.Context, in *ListServiceProfileRequest, opts ...grpc.CallOption) (*ListServiceProfileResponse, error)
}

type serviceProfileServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewServiceProfileServiceClient(cc grpc.ClientConnInterface) ServiceProfileServiceClient {
	return &serviceProfileServiceClient{cc}
}

func (c *serviceProfileServiceClient) Create(ctx context.Context, in *CreateServiceProfileRequest, opts ...grpc.CallOption) (*CreateServiceProfileResponse, error) {
	out := new(CreateServiceProfileResponse)
	err := c.cc.Invoke(ctx, ServiceProfileService_Create_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *serviceProfileServiceClient) Get(ctx context.Context, in *GetServiceProfileRequest, opts ...grpc.CallOption) (*GetServiceProfileResponse, error) {
	out := new(GetServiceProfileResponse)
	err := c.cc.Invoke(ctx, ServiceProfileService_Get_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *serviceProfileServiceClient) Update(ctx context.Context, in *UpdateServiceProfileRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, ServiceProfileService_Update_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *serviceProfileServiceClient) Delete(ctx context.Context, in *DeleteServiceProfileRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, ServiceProfileService_Delete_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *serviceProfileServiceClient) List(ctx context.Context, in *ListServiceProfileRequest, opts ...grpc.CallOption) (*ListServiceProfileResponse, error) {
	out := new(ListServiceProfileResponse)
	err := c.cc.Invoke(ctx, ServiceProfileService_List_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ServiceProfileServiceServer is the server API for ServiceProfileService service.
// All implementations must embed UnimplementedServiceProfileServiceServer
// for forward compatibility
type ServiceProfileServiceServer interface {
	// Create creates the given service-profile.
	Create(context.Context, *CreateServiceProfileRequest) (*CreateServiceProfileResponse, error)
	// Get returns the service-profile matching the given id.
	Get(context.Context, *GetServiceProfileRequest) (*GetServiceProfileResponse, error)
	// Update updates the given serviceprofile.
	Update(context.Context, *UpdateServiceProfileRequest) (*emptypb.Empty, error)
	// Delete deletes the service-profile matching the given id.
	Delete(context.Context, *DeleteServiceProfileRequest) (*emptypb.Empty, error)
	// List lists the available service-profiles.
	List(context.Context, *ListServiceProfileRequest) (*ListServiceProfileResponse, error)
	mustEmbedUnimplementedServiceProfileServiceServer()
}

// UnimplementedServiceProfileServiceServer must be embedded to have forward compatible implementations.
type UnimplementedServiceProfileServiceServer struct {
}

func (UnimplementedServiceProfileServiceServer) Create(context.Context, *CreateServiceProfileRequest) (*CreateServiceProfileResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Create not implemented")
}
func (UnimplementedServiceProfileServiceServer) Get(context.Context, *GetServiceProfileRequest) (*GetServiceProfileResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Get not implemented")
}
func (UnimplementedServiceProfileServiceServer) Update(context.Context, *UpdateServiceProfileRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Update not implemented")
}
func (UnimplementedServiceProfileServiceServer) Delete(context.Context, *DeleteServiceProfileRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Delete not implemented")
}
func (UnimplementedServiceProfileServiceServer) List(context.Context, *ListServiceProfileRequest) (*ListServiceProfileResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (UnimplementedServiceProfileServiceServer) mustEmbedUnimplementedServiceProfileServiceServer() {}

// UnsafeServiceProfileServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to ServiceProfileServiceServer will
// result in compilation errors.
type UnsafeServiceProfileServiceServer interface {
	mustEmbedUnimplementedServiceProfileServiceServer()
}

func RegisterServiceProfileServiceServer(s grpc.ServiceRegistrar, srv ServiceProfileServiceServer) {
	s.RegisterService(&ServiceProfileService_ServiceDesc, srv)
}

func _ServiceProfileService_Create_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateServiceProfileRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ServiceProfileServiceServer).Create(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ServiceProfileService_Create_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ServiceProfileServiceServer).Create(ctx, req.(*CreateServiceProfileRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ServiceProfileService_Get_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetServiceProfileRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ServiceProfileServiceServer).Get(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ServiceProfileService_Get_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ServiceProfileServiceServer).Get(ctx, req.(*GetServiceProfileRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ServiceProfileService_Update_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateServiceProfileRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ServiceProfileServiceServer).Update(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ServiceProfileService_Update_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ServiceProfileServiceServer).Update(ctx, req.(*UpdateServiceProfileRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ServiceProfileService_Delete_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DeleteServiceProfileRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ServiceProfileServiceServer).Delete(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ServiceProfileService_Delete_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ServiceProfileServiceServer).Delete(ctx, req.(*DeleteServiceProfileRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ServiceProfileService_List_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListServiceProfileRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ServiceProfileServiceServer).List(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ServiceProfileService_List_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ServiceProfileServiceServer).List(ctx, req.(*ListServiceProfileRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// ServiceProfileService_ServiceDesc is the grpc.ServiceDesc for ServiceProfileService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var ServiceProfileService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "api.ServiceProfileService",
	HandlerType: (*ServiceProfileServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Create",
			Handler:    _ServiceProfileService_Create_Handler,
		},
		{
			MethodName: "Get",
			Handler:    _ServiceProfileService_Get_Handler,
		},
		{
			MethodName: "Update",
			Handler:    _ServiceProfileService_Update_Handler,
		},
		{
			MethodName: "Delete",
			Handler:    _ServiceProfileService_Delete_Handler,
		},
		{
			MethodName: "List",
			Handler:    _ServiceProfileService_List_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "as/external/api/serviceProfile.proto",
}