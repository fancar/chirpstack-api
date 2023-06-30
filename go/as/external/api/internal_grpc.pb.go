// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.3.0
// - protoc             (unknown)
// source: as/external/api/internal.proto

package api

import (
	context "context"
	handyrusty "github.com/brocaar/chirpstack-api/go/v3/handyrusty"
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
	InternalService_Login_FullMethodName                 = "/api.InternalService/Login"
	InternalService_Profile_FullMethodName               = "/api.InternalService/Profile"
	InternalService_GlobalSearch_FullMethodName          = "/api.InternalService/GlobalSearch"
	InternalService_CreateAPIKey_FullMethodName          = "/api.InternalService/CreateAPIKey"
	InternalService_DeleteAPIKey_FullMethodName          = "/api.InternalService/DeleteAPIKey"
	InternalService_ListAPIKeys_FullMethodName           = "/api.InternalService/ListAPIKeys"
	InternalService_Settings_FullMethodName              = "/api.InternalService/Settings"
	InternalService_OpenIDConnectLogin_FullMethodName    = "/api.InternalService/OpenIDConnectLogin"
	InternalService_GetDevicesSummary_FullMethodName     = "/api.InternalService/GetDevicesSummary"
	InternalService_GetDevicesSummaryLog_FullMethodName  = "/api.InternalService/GetDevicesSummaryLog"
	InternalService_GetGatewaysSummaryLog_FullMethodName = "/api.InternalService/GetGatewaysSummaryLog"
	InternalService_GetGatewaysSummary_FullMethodName    = "/api.InternalService/GetGatewaysSummary"
	InternalService_GetInfo_FullMethodName               = "/api.InternalService/GetInfo"
	InternalService_GetMainCounters_FullMethodName       = "/api.InternalService/GetMainCounters"
)

// InternalServiceClient is the client API for InternalService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type InternalServiceClient interface {
	// Log in a user
	Login(ctx context.Context, in *LoginRequest, opts ...grpc.CallOption) (*LoginResponse, error)
	// Get the current user's profile
	Profile(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*ProfileResponse, error)
	// Perform a global search.
	GlobalSearch(ctx context.Context, in *GlobalSearchRequest, opts ...grpc.CallOption) (*GlobalSearchResponse, error)
	// CreateAPIKey creates the given API key.
	CreateAPIKey(ctx context.Context, in *CreateAPIKeyRequest, opts ...grpc.CallOption) (*CreateAPIKeyResponse, error)
	// DeleteAPIKey deletes the API key.
	DeleteAPIKey(ctx context.Context, in *DeleteAPIKeyRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	// ListAPIKeys lists the available API keys.
	ListAPIKeys(ctx context.Context, in *ListAPIKeysRequest, opts ...grpc.CallOption) (*ListAPIKeysResponse, error)
	// Get the global settings.
	Settings(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*SettingsResponse, error)
	// OpenID Connect login.
	OpenIDConnectLogin(ctx context.Context, in *OpenIDConnectLoginRequest, opts ...grpc.CallOption) (*OpenIDConnectLoginResponse, error)
	// GetDevicesSummary returns an aggregated summary of the devices.
	GetDevicesSummary(ctx context.Context, in *GetDevicesSummaryRequest, opts ...grpc.CallOption) (*GetDevicesSummaryResponse, error)
	// GetDevicesSummaryLog returns log of aggregated summary.
	GetDevicesSummaryLog(ctx context.Context, in *handyrusty.GetDeviceCountersRequest, opts ...grpc.CallOption) (*handyrusty.GetDeviceCountersResponse, error)
	// GetGatewaysSummaryLog returns log of aggregated summary.
	GetGatewaysSummaryLog(ctx context.Context, in *handyrusty.GetGatewayCountersRequest, opts ...grpc.CallOption) (*handyrusty.GetGatewayCountersResponse, error)
	// GetGatewaysSummary returns an aggregated summary of the gateways.
	GetGatewaysSummary(ctx context.Context, in *GetGatewaysSummaryRequest, opts ...grpc.CallOption) (*GetGatewaysSummaryResponse, error)
	// GetInfo returns summary about versions and so on.
	GetInfo(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*GetInfoResponse, error)
	// GetMainCounters returns main app-server metrics
	GetMainCounters(ctx context.Context, in *GetMainCountersRequest, opts ...grpc.CallOption) (*GetMainCountersResponse, error)
}

type internalServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewInternalServiceClient(cc grpc.ClientConnInterface) InternalServiceClient {
	return &internalServiceClient{cc}
}

func (c *internalServiceClient) Login(ctx context.Context, in *LoginRequest, opts ...grpc.CallOption) (*LoginResponse, error) {
	out := new(LoginResponse)
	err := c.cc.Invoke(ctx, InternalService_Login_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *internalServiceClient) Profile(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*ProfileResponse, error) {
	out := new(ProfileResponse)
	err := c.cc.Invoke(ctx, InternalService_Profile_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *internalServiceClient) GlobalSearch(ctx context.Context, in *GlobalSearchRequest, opts ...grpc.CallOption) (*GlobalSearchResponse, error) {
	out := new(GlobalSearchResponse)
	err := c.cc.Invoke(ctx, InternalService_GlobalSearch_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *internalServiceClient) CreateAPIKey(ctx context.Context, in *CreateAPIKeyRequest, opts ...grpc.CallOption) (*CreateAPIKeyResponse, error) {
	out := new(CreateAPIKeyResponse)
	err := c.cc.Invoke(ctx, InternalService_CreateAPIKey_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *internalServiceClient) DeleteAPIKey(ctx context.Context, in *DeleteAPIKeyRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, InternalService_DeleteAPIKey_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *internalServiceClient) ListAPIKeys(ctx context.Context, in *ListAPIKeysRequest, opts ...grpc.CallOption) (*ListAPIKeysResponse, error) {
	out := new(ListAPIKeysResponse)
	err := c.cc.Invoke(ctx, InternalService_ListAPIKeys_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *internalServiceClient) Settings(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*SettingsResponse, error) {
	out := new(SettingsResponse)
	err := c.cc.Invoke(ctx, InternalService_Settings_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *internalServiceClient) OpenIDConnectLogin(ctx context.Context, in *OpenIDConnectLoginRequest, opts ...grpc.CallOption) (*OpenIDConnectLoginResponse, error) {
	out := new(OpenIDConnectLoginResponse)
	err := c.cc.Invoke(ctx, InternalService_OpenIDConnectLogin_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *internalServiceClient) GetDevicesSummary(ctx context.Context, in *GetDevicesSummaryRequest, opts ...grpc.CallOption) (*GetDevicesSummaryResponse, error) {
	out := new(GetDevicesSummaryResponse)
	err := c.cc.Invoke(ctx, InternalService_GetDevicesSummary_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *internalServiceClient) GetDevicesSummaryLog(ctx context.Context, in *handyrusty.GetDeviceCountersRequest, opts ...grpc.CallOption) (*handyrusty.GetDeviceCountersResponse, error) {
	out := new(handyrusty.GetDeviceCountersResponse)
	err := c.cc.Invoke(ctx, InternalService_GetDevicesSummaryLog_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *internalServiceClient) GetGatewaysSummaryLog(ctx context.Context, in *handyrusty.GetGatewayCountersRequest, opts ...grpc.CallOption) (*handyrusty.GetGatewayCountersResponse, error) {
	out := new(handyrusty.GetGatewayCountersResponse)
	err := c.cc.Invoke(ctx, InternalService_GetGatewaysSummaryLog_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *internalServiceClient) GetGatewaysSummary(ctx context.Context, in *GetGatewaysSummaryRequest, opts ...grpc.CallOption) (*GetGatewaysSummaryResponse, error) {
	out := new(GetGatewaysSummaryResponse)
	err := c.cc.Invoke(ctx, InternalService_GetGatewaysSummary_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *internalServiceClient) GetInfo(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*GetInfoResponse, error) {
	out := new(GetInfoResponse)
	err := c.cc.Invoke(ctx, InternalService_GetInfo_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *internalServiceClient) GetMainCounters(ctx context.Context, in *GetMainCountersRequest, opts ...grpc.CallOption) (*GetMainCountersResponse, error) {
	out := new(GetMainCountersResponse)
	err := c.cc.Invoke(ctx, InternalService_GetMainCounters_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// InternalServiceServer is the server API for InternalService service.
// All implementations must embed UnimplementedInternalServiceServer
// for forward compatibility
type InternalServiceServer interface {
	// Log in a user
	Login(context.Context, *LoginRequest) (*LoginResponse, error)
	// Get the current user's profile
	Profile(context.Context, *emptypb.Empty) (*ProfileResponse, error)
	// Perform a global search.
	GlobalSearch(context.Context, *GlobalSearchRequest) (*GlobalSearchResponse, error)
	// CreateAPIKey creates the given API key.
	CreateAPIKey(context.Context, *CreateAPIKeyRequest) (*CreateAPIKeyResponse, error)
	// DeleteAPIKey deletes the API key.
	DeleteAPIKey(context.Context, *DeleteAPIKeyRequest) (*emptypb.Empty, error)
	// ListAPIKeys lists the available API keys.
	ListAPIKeys(context.Context, *ListAPIKeysRequest) (*ListAPIKeysResponse, error)
	// Get the global settings.
	Settings(context.Context, *emptypb.Empty) (*SettingsResponse, error)
	// OpenID Connect login.
	OpenIDConnectLogin(context.Context, *OpenIDConnectLoginRequest) (*OpenIDConnectLoginResponse, error)
	// GetDevicesSummary returns an aggregated summary of the devices.
	GetDevicesSummary(context.Context, *GetDevicesSummaryRequest) (*GetDevicesSummaryResponse, error)
	// GetDevicesSummaryLog returns log of aggregated summary.
	GetDevicesSummaryLog(context.Context, *handyrusty.GetDeviceCountersRequest) (*handyrusty.GetDeviceCountersResponse, error)
	// GetGatewaysSummaryLog returns log of aggregated summary.
	GetGatewaysSummaryLog(context.Context, *handyrusty.GetGatewayCountersRequest) (*handyrusty.GetGatewayCountersResponse, error)
	// GetGatewaysSummary returns an aggregated summary of the gateways.
	GetGatewaysSummary(context.Context, *GetGatewaysSummaryRequest) (*GetGatewaysSummaryResponse, error)
	// GetInfo returns summary about versions and so on.
	GetInfo(context.Context, *emptypb.Empty) (*GetInfoResponse, error)
	// GetMainCounters returns main app-server metrics
	GetMainCounters(context.Context, *GetMainCountersRequest) (*GetMainCountersResponse, error)
	mustEmbedUnimplementedInternalServiceServer()
}

// UnimplementedInternalServiceServer must be embedded to have forward compatible implementations.
type UnimplementedInternalServiceServer struct {
}

func (UnimplementedInternalServiceServer) Login(context.Context, *LoginRequest) (*LoginResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Login not implemented")
}
func (UnimplementedInternalServiceServer) Profile(context.Context, *emptypb.Empty) (*ProfileResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Profile not implemented")
}
func (UnimplementedInternalServiceServer) GlobalSearch(context.Context, *GlobalSearchRequest) (*GlobalSearchResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GlobalSearch not implemented")
}
func (UnimplementedInternalServiceServer) CreateAPIKey(context.Context, *CreateAPIKeyRequest) (*CreateAPIKeyResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateAPIKey not implemented")
}
func (UnimplementedInternalServiceServer) DeleteAPIKey(context.Context, *DeleteAPIKeyRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DeleteAPIKey not implemented")
}
func (UnimplementedInternalServiceServer) ListAPIKeys(context.Context, *ListAPIKeysRequest) (*ListAPIKeysResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListAPIKeys not implemented")
}
func (UnimplementedInternalServiceServer) Settings(context.Context, *emptypb.Empty) (*SettingsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Settings not implemented")
}
func (UnimplementedInternalServiceServer) OpenIDConnectLogin(context.Context, *OpenIDConnectLoginRequest) (*OpenIDConnectLoginResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method OpenIDConnectLogin not implemented")
}
func (UnimplementedInternalServiceServer) GetDevicesSummary(context.Context, *GetDevicesSummaryRequest) (*GetDevicesSummaryResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetDevicesSummary not implemented")
}
func (UnimplementedInternalServiceServer) GetDevicesSummaryLog(context.Context, *handyrusty.GetDeviceCountersRequest) (*handyrusty.GetDeviceCountersResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetDevicesSummaryLog not implemented")
}
func (UnimplementedInternalServiceServer) GetGatewaysSummaryLog(context.Context, *handyrusty.GetGatewayCountersRequest) (*handyrusty.GetGatewayCountersResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetGatewaysSummaryLog not implemented")
}
func (UnimplementedInternalServiceServer) GetGatewaysSummary(context.Context, *GetGatewaysSummaryRequest) (*GetGatewaysSummaryResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetGatewaysSummary not implemented")
}
func (UnimplementedInternalServiceServer) GetInfo(context.Context, *emptypb.Empty) (*GetInfoResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetInfo not implemented")
}
func (UnimplementedInternalServiceServer) GetMainCounters(context.Context, *GetMainCountersRequest) (*GetMainCountersResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetMainCounters not implemented")
}
func (UnimplementedInternalServiceServer) mustEmbedUnimplementedInternalServiceServer() {}

// UnsafeInternalServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to InternalServiceServer will
// result in compilation errors.
type UnsafeInternalServiceServer interface {
	mustEmbedUnimplementedInternalServiceServer()
}

func RegisterInternalServiceServer(s grpc.ServiceRegistrar, srv InternalServiceServer) {
	s.RegisterService(&InternalService_ServiceDesc, srv)
}

func _InternalService_Login_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(LoginRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InternalServiceServer).Login(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InternalService_Login_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InternalServiceServer).Login(ctx, req.(*LoginRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _InternalService_Profile_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(emptypb.Empty)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InternalServiceServer).Profile(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InternalService_Profile_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InternalServiceServer).Profile(ctx, req.(*emptypb.Empty))
	}
	return interceptor(ctx, in, info, handler)
}

func _InternalService_GlobalSearch_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GlobalSearchRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InternalServiceServer).GlobalSearch(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InternalService_GlobalSearch_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InternalServiceServer).GlobalSearch(ctx, req.(*GlobalSearchRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _InternalService_CreateAPIKey_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateAPIKeyRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InternalServiceServer).CreateAPIKey(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InternalService_CreateAPIKey_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InternalServiceServer).CreateAPIKey(ctx, req.(*CreateAPIKeyRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _InternalService_DeleteAPIKey_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DeleteAPIKeyRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InternalServiceServer).DeleteAPIKey(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InternalService_DeleteAPIKey_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InternalServiceServer).DeleteAPIKey(ctx, req.(*DeleteAPIKeyRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _InternalService_ListAPIKeys_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListAPIKeysRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InternalServiceServer).ListAPIKeys(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InternalService_ListAPIKeys_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InternalServiceServer).ListAPIKeys(ctx, req.(*ListAPIKeysRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _InternalService_Settings_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(emptypb.Empty)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InternalServiceServer).Settings(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InternalService_Settings_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InternalServiceServer).Settings(ctx, req.(*emptypb.Empty))
	}
	return interceptor(ctx, in, info, handler)
}

func _InternalService_OpenIDConnectLogin_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(OpenIDConnectLoginRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InternalServiceServer).OpenIDConnectLogin(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InternalService_OpenIDConnectLogin_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InternalServiceServer).OpenIDConnectLogin(ctx, req.(*OpenIDConnectLoginRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _InternalService_GetDevicesSummary_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetDevicesSummaryRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InternalServiceServer).GetDevicesSummary(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InternalService_GetDevicesSummary_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InternalServiceServer).GetDevicesSummary(ctx, req.(*GetDevicesSummaryRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _InternalService_GetDevicesSummaryLog_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(handyrusty.GetDeviceCountersRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InternalServiceServer).GetDevicesSummaryLog(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InternalService_GetDevicesSummaryLog_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InternalServiceServer).GetDevicesSummaryLog(ctx, req.(*handyrusty.GetDeviceCountersRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _InternalService_GetGatewaysSummaryLog_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(handyrusty.GetGatewayCountersRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InternalServiceServer).GetGatewaysSummaryLog(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InternalService_GetGatewaysSummaryLog_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InternalServiceServer).GetGatewaysSummaryLog(ctx, req.(*handyrusty.GetGatewayCountersRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _InternalService_GetGatewaysSummary_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetGatewaysSummaryRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InternalServiceServer).GetGatewaysSummary(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InternalService_GetGatewaysSummary_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InternalServiceServer).GetGatewaysSummary(ctx, req.(*GetGatewaysSummaryRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _InternalService_GetInfo_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(emptypb.Empty)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InternalServiceServer).GetInfo(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InternalService_GetInfo_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InternalServiceServer).GetInfo(ctx, req.(*emptypb.Empty))
	}
	return interceptor(ctx, in, info, handler)
}

func _InternalService_GetMainCounters_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetMainCountersRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(InternalServiceServer).GetMainCounters(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: InternalService_GetMainCounters_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(InternalServiceServer).GetMainCounters(ctx, req.(*GetMainCountersRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// InternalService_ServiceDesc is the grpc.ServiceDesc for InternalService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var InternalService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "api.InternalService",
	HandlerType: (*InternalServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Login",
			Handler:    _InternalService_Login_Handler,
		},
		{
			MethodName: "Profile",
			Handler:    _InternalService_Profile_Handler,
		},
		{
			MethodName: "GlobalSearch",
			Handler:    _InternalService_GlobalSearch_Handler,
		},
		{
			MethodName: "CreateAPIKey",
			Handler:    _InternalService_CreateAPIKey_Handler,
		},
		{
			MethodName: "DeleteAPIKey",
			Handler:    _InternalService_DeleteAPIKey_Handler,
		},
		{
			MethodName: "ListAPIKeys",
			Handler:    _InternalService_ListAPIKeys_Handler,
		},
		{
			MethodName: "Settings",
			Handler:    _InternalService_Settings_Handler,
		},
		{
			MethodName: "OpenIDConnectLogin",
			Handler:    _InternalService_OpenIDConnectLogin_Handler,
		},
		{
			MethodName: "GetDevicesSummary",
			Handler:    _InternalService_GetDevicesSummary_Handler,
		},
		{
			MethodName: "GetDevicesSummaryLog",
			Handler:    _InternalService_GetDevicesSummaryLog_Handler,
		},
		{
			MethodName: "GetGatewaysSummaryLog",
			Handler:    _InternalService_GetGatewaysSummaryLog_Handler,
		},
		{
			MethodName: "GetGatewaysSummary",
			Handler:    _InternalService_GetGatewaysSummary_Handler,
		},
		{
			MethodName: "GetInfo",
			Handler:    _InternalService_GetInfo_Handler,
		},
		{
			MethodName: "GetMainCounters",
			Handler:    _InternalService_GetMainCounters_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "as/external/api/internal.proto",
}
