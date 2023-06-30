// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.3.0
// - protoc             (unknown)
// source: as/external/api/gateway.proto

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
	GatewayService_Create_FullMethodName                           = "/api.GatewayService/Create"
	GatewayService_Get_FullMethodName                              = "/api.GatewayService/Get"
	GatewayService_GetStatus_FullMethodName                        = "/api.GatewayService/GetStatus"
	GatewayService_Update_FullMethodName                           = "/api.GatewayService/Update"
	GatewayService_Delete_FullMethodName                           = "/api.GatewayService/Delete"
	GatewayService_List_FullMethodName                             = "/api.GatewayService/List"
	GatewayService_GetGatewayLogs_FullMethodName                   = "/api.GatewayService/GetGatewayLogs"
	GatewayService_ListActilityStyled_FullMethodName               = "/api.GatewayService/ListActilityStyled"
	GatewayService_ListMon_FullMethodName                          = "/api.GatewayService/ListMon"
	GatewayService_GetStats_FullMethodName                         = "/api.GatewayService/GetStats"
	GatewayService_GetLastPing_FullMethodName                      = "/api.GatewayService/GetLastPing"
	GatewayService_GenerateGatewayClientCertificate_FullMethodName = "/api.GatewayService/GenerateGatewayClientCertificate"
	GatewayService_StreamFrameLogs_FullMethodName                  = "/api.GatewayService/StreamFrameLogs"
	GatewayService_GetTaskResults_FullMethodName                   = "/api.GatewayService/GetTaskResults"
)

// GatewayServiceClient is the client API for GatewayService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type GatewayServiceClient interface {
	// Create creates the given gateway.
	Create(ctx context.Context, in *CreateGatewayRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	// Get returns the gateway for the requested mac address.
	Get(ctx context.Context, in *GetGatewayRequest, opts ...grpc.CallOption) (*GetGatewayResponse, error)
	// GetStatus returns the gateway status for the requested mac address.
	GetStatus(ctx context.Context, in *GetGatewayRequest, opts ...grpc.CallOption) (*GetGatewayStatusResponse, error)
	// Update updates the gateway matching the given mac address.
	Update(ctx context.Context, in *UpdateGatewayRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	// Delete deletes the gateway matching the given mac address.
	Delete(ctx context.Context, in *DeleteGatewayRequest, opts ...grpc.CallOption) (*emptypb.Empty, error)
	// List lists the gateways.
	List(ctx context.Context, in *ListGatewayRequest, opts ...grpc.CallOption) (*ListGatewayResponse, error)
	// GetGatewayLogs returns logs of statistics state changed.
	GetGatewayLogs(ctx context.Context, in *handyrusty.LogsGatewayRequest, opts ...grpc.CallOption) (*handyrusty.LogsGatewayResponse, error)
	// ListActilityStyled lists the gateways with legacy [Actility] json-format.
	ListActilityStyled(ctx context.Context, in *ListGatewayRequest, opts ...grpc.CallOption) (*ListGwActilityStyledResponse, error)
	// ListMon lists all gateways with the metrics for monitoring purposes
	ListMon(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*ListMonResponse, error)
	// GetStats lists the gateway stats given the query parameters.
	GetStats(ctx context.Context, in *GetGatewayStatsRequest, opts ...grpc.CallOption) (*GetGatewayStatsResponse, error)
	// GetLastPing returns the last emitted ping and gateways receiving this ping.
	GetLastPing(ctx context.Context, in *GetLastPingRequest, opts ...grpc.CallOption) (*GetLastPingResponse, error)
	// GenerateGatewayClientCertificate returns TLS certificate gateway authentication / authorization.
	// This endpoint can ony be used when Network Server is configured with a gateway
	// CA certificate and key, which is used for signing the TLS certificate. The returned TLS
	// certificate will have the Gateway ID as Common Name.
	GenerateGatewayClientCertificate(ctx context.Context, in *GenerateGatewayClientCertificateRequest, opts ...grpc.CallOption) (*GenerateGatewayClientCertificateResponse, error)
	// StreamFrameLogs streams the uplink and downlink frame-logs for the given gateway ID.
	// Notes:
	//   - These are the raw LoRaWAN frames and this endpoint is intended for debugging only.
	//     (!) websocket required! The endpoint does not work from a web-swagger.
	StreamFrameLogs(ctx context.Context, in *StreamGatewayFrameLogsRequest, opts ...grpc.CallOption) (GatewayService_StreamFrameLogsClient, error)
	// GetTaskResults lists the gateway tasks had been done by ExecCommand in background mode
	GetTaskResults(ctx context.Context, in *GetGatewayRequest, opts ...grpc.CallOption) (*GetTaskResultsResponse, error)
}

type gatewayServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewGatewayServiceClient(cc grpc.ClientConnInterface) GatewayServiceClient {
	return &gatewayServiceClient{cc}
}

func (c *gatewayServiceClient) Create(ctx context.Context, in *CreateGatewayRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, GatewayService_Create_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayServiceClient) Get(ctx context.Context, in *GetGatewayRequest, opts ...grpc.CallOption) (*GetGatewayResponse, error) {
	out := new(GetGatewayResponse)
	err := c.cc.Invoke(ctx, GatewayService_Get_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayServiceClient) GetStatus(ctx context.Context, in *GetGatewayRequest, opts ...grpc.CallOption) (*GetGatewayStatusResponse, error) {
	out := new(GetGatewayStatusResponse)
	err := c.cc.Invoke(ctx, GatewayService_GetStatus_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayServiceClient) Update(ctx context.Context, in *UpdateGatewayRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, GatewayService_Update_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayServiceClient) Delete(ctx context.Context, in *DeleteGatewayRequest, opts ...grpc.CallOption) (*emptypb.Empty, error) {
	out := new(emptypb.Empty)
	err := c.cc.Invoke(ctx, GatewayService_Delete_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayServiceClient) List(ctx context.Context, in *ListGatewayRequest, opts ...grpc.CallOption) (*ListGatewayResponse, error) {
	out := new(ListGatewayResponse)
	err := c.cc.Invoke(ctx, GatewayService_List_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayServiceClient) GetGatewayLogs(ctx context.Context, in *handyrusty.LogsGatewayRequest, opts ...grpc.CallOption) (*handyrusty.LogsGatewayResponse, error) {
	out := new(handyrusty.LogsGatewayResponse)
	err := c.cc.Invoke(ctx, GatewayService_GetGatewayLogs_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayServiceClient) ListActilityStyled(ctx context.Context, in *ListGatewayRequest, opts ...grpc.CallOption) (*ListGwActilityStyledResponse, error) {
	out := new(ListGwActilityStyledResponse)
	err := c.cc.Invoke(ctx, GatewayService_ListActilityStyled_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayServiceClient) ListMon(ctx context.Context, in *emptypb.Empty, opts ...grpc.CallOption) (*ListMonResponse, error) {
	out := new(ListMonResponse)
	err := c.cc.Invoke(ctx, GatewayService_ListMon_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayServiceClient) GetStats(ctx context.Context, in *GetGatewayStatsRequest, opts ...grpc.CallOption) (*GetGatewayStatsResponse, error) {
	out := new(GetGatewayStatsResponse)
	err := c.cc.Invoke(ctx, GatewayService_GetStats_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayServiceClient) GetLastPing(ctx context.Context, in *GetLastPingRequest, opts ...grpc.CallOption) (*GetLastPingResponse, error) {
	out := new(GetLastPingResponse)
	err := c.cc.Invoke(ctx, GatewayService_GetLastPing_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayServiceClient) GenerateGatewayClientCertificate(ctx context.Context, in *GenerateGatewayClientCertificateRequest, opts ...grpc.CallOption) (*GenerateGatewayClientCertificateResponse, error) {
	out := new(GenerateGatewayClientCertificateResponse)
	err := c.cc.Invoke(ctx, GatewayService_GenerateGatewayClientCertificate_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *gatewayServiceClient) StreamFrameLogs(ctx context.Context, in *StreamGatewayFrameLogsRequest, opts ...grpc.CallOption) (GatewayService_StreamFrameLogsClient, error) {
	stream, err := c.cc.NewStream(ctx, &GatewayService_ServiceDesc.Streams[0], GatewayService_StreamFrameLogs_FullMethodName, opts...)
	if err != nil {
		return nil, err
	}
	x := &gatewayServiceStreamFrameLogsClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type GatewayService_StreamFrameLogsClient interface {
	Recv() (*StreamGatewayFrameLogsResponse, error)
	grpc.ClientStream
}

type gatewayServiceStreamFrameLogsClient struct {
	grpc.ClientStream
}

func (x *gatewayServiceStreamFrameLogsClient) Recv() (*StreamGatewayFrameLogsResponse, error) {
	m := new(StreamGatewayFrameLogsResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *gatewayServiceClient) GetTaskResults(ctx context.Context, in *GetGatewayRequest, opts ...grpc.CallOption) (*GetTaskResultsResponse, error) {
	out := new(GetTaskResultsResponse)
	err := c.cc.Invoke(ctx, GatewayService_GetTaskResults_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// GatewayServiceServer is the server API for GatewayService service.
// All implementations must embed UnimplementedGatewayServiceServer
// for forward compatibility
type GatewayServiceServer interface {
	// Create creates the given gateway.
	Create(context.Context, *CreateGatewayRequest) (*emptypb.Empty, error)
	// Get returns the gateway for the requested mac address.
	Get(context.Context, *GetGatewayRequest) (*GetGatewayResponse, error)
	// GetStatus returns the gateway status for the requested mac address.
	GetStatus(context.Context, *GetGatewayRequest) (*GetGatewayStatusResponse, error)
	// Update updates the gateway matching the given mac address.
	Update(context.Context, *UpdateGatewayRequest) (*emptypb.Empty, error)
	// Delete deletes the gateway matching the given mac address.
	Delete(context.Context, *DeleteGatewayRequest) (*emptypb.Empty, error)
	// List lists the gateways.
	List(context.Context, *ListGatewayRequest) (*ListGatewayResponse, error)
	// GetGatewayLogs returns logs of statistics state changed.
	GetGatewayLogs(context.Context, *handyrusty.LogsGatewayRequest) (*handyrusty.LogsGatewayResponse, error)
	// ListActilityStyled lists the gateways with legacy [Actility] json-format.
	ListActilityStyled(context.Context, *ListGatewayRequest) (*ListGwActilityStyledResponse, error)
	// ListMon lists all gateways with the metrics for monitoring purposes
	ListMon(context.Context, *emptypb.Empty) (*ListMonResponse, error)
	// GetStats lists the gateway stats given the query parameters.
	GetStats(context.Context, *GetGatewayStatsRequest) (*GetGatewayStatsResponse, error)
	// GetLastPing returns the last emitted ping and gateways receiving this ping.
	GetLastPing(context.Context, *GetLastPingRequest) (*GetLastPingResponse, error)
	// GenerateGatewayClientCertificate returns TLS certificate gateway authentication / authorization.
	// This endpoint can ony be used when Network Server is configured with a gateway
	// CA certificate and key, which is used for signing the TLS certificate. The returned TLS
	// certificate will have the Gateway ID as Common Name.
	GenerateGatewayClientCertificate(context.Context, *GenerateGatewayClientCertificateRequest) (*GenerateGatewayClientCertificateResponse, error)
	// StreamFrameLogs streams the uplink and downlink frame-logs for the given gateway ID.
	// Notes:
	//   - These are the raw LoRaWAN frames and this endpoint is intended for debugging only.
	//     (!) websocket required! The endpoint does not work from a web-swagger.
	StreamFrameLogs(*StreamGatewayFrameLogsRequest, GatewayService_StreamFrameLogsServer) error
	// GetTaskResults lists the gateway tasks had been done by ExecCommand in background mode
	GetTaskResults(context.Context, *GetGatewayRequest) (*GetTaskResultsResponse, error)
	mustEmbedUnimplementedGatewayServiceServer()
}

// UnimplementedGatewayServiceServer must be embedded to have forward compatible implementations.
type UnimplementedGatewayServiceServer struct {
}

func (UnimplementedGatewayServiceServer) Create(context.Context, *CreateGatewayRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Create not implemented")
}
func (UnimplementedGatewayServiceServer) Get(context.Context, *GetGatewayRequest) (*GetGatewayResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Get not implemented")
}
func (UnimplementedGatewayServiceServer) GetStatus(context.Context, *GetGatewayRequest) (*GetGatewayStatusResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetStatus not implemented")
}
func (UnimplementedGatewayServiceServer) Update(context.Context, *UpdateGatewayRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Update not implemented")
}
func (UnimplementedGatewayServiceServer) Delete(context.Context, *DeleteGatewayRequest) (*emptypb.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Delete not implemented")
}
func (UnimplementedGatewayServiceServer) List(context.Context, *ListGatewayRequest) (*ListGatewayResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (UnimplementedGatewayServiceServer) GetGatewayLogs(context.Context, *handyrusty.LogsGatewayRequest) (*handyrusty.LogsGatewayResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetGatewayLogs not implemented")
}
func (UnimplementedGatewayServiceServer) ListActilityStyled(context.Context, *ListGatewayRequest) (*ListGwActilityStyledResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListActilityStyled not implemented")
}
func (UnimplementedGatewayServiceServer) ListMon(context.Context, *emptypb.Empty) (*ListMonResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListMon not implemented")
}
func (UnimplementedGatewayServiceServer) GetStats(context.Context, *GetGatewayStatsRequest) (*GetGatewayStatsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetStats not implemented")
}
func (UnimplementedGatewayServiceServer) GetLastPing(context.Context, *GetLastPingRequest) (*GetLastPingResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetLastPing not implemented")
}
func (UnimplementedGatewayServiceServer) GenerateGatewayClientCertificate(context.Context, *GenerateGatewayClientCertificateRequest) (*GenerateGatewayClientCertificateResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GenerateGatewayClientCertificate not implemented")
}
func (UnimplementedGatewayServiceServer) StreamFrameLogs(*StreamGatewayFrameLogsRequest, GatewayService_StreamFrameLogsServer) error {
	return status.Errorf(codes.Unimplemented, "method StreamFrameLogs not implemented")
}
func (UnimplementedGatewayServiceServer) GetTaskResults(context.Context, *GetGatewayRequest) (*GetTaskResultsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetTaskResults not implemented")
}
func (UnimplementedGatewayServiceServer) mustEmbedUnimplementedGatewayServiceServer() {}

// UnsafeGatewayServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to GatewayServiceServer will
// result in compilation errors.
type UnsafeGatewayServiceServer interface {
	mustEmbedUnimplementedGatewayServiceServer()
}

func RegisterGatewayServiceServer(s grpc.ServiceRegistrar, srv GatewayServiceServer) {
	s.RegisterService(&GatewayService_ServiceDesc, srv)
}

func _GatewayService_Create_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateGatewayRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServiceServer).Create(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayService_Create_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServiceServer).Create(ctx, req.(*CreateGatewayRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GatewayService_Get_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetGatewayRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServiceServer).Get(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayService_Get_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServiceServer).Get(ctx, req.(*GetGatewayRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GatewayService_GetStatus_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetGatewayRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServiceServer).GetStatus(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayService_GetStatus_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServiceServer).GetStatus(ctx, req.(*GetGatewayRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GatewayService_Update_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateGatewayRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServiceServer).Update(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayService_Update_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServiceServer).Update(ctx, req.(*UpdateGatewayRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GatewayService_Delete_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DeleteGatewayRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServiceServer).Delete(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayService_Delete_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServiceServer).Delete(ctx, req.(*DeleteGatewayRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GatewayService_List_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListGatewayRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServiceServer).List(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayService_List_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServiceServer).List(ctx, req.(*ListGatewayRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GatewayService_GetGatewayLogs_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(handyrusty.LogsGatewayRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServiceServer).GetGatewayLogs(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayService_GetGatewayLogs_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServiceServer).GetGatewayLogs(ctx, req.(*handyrusty.LogsGatewayRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GatewayService_ListActilityStyled_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListGatewayRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServiceServer).ListActilityStyled(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayService_ListActilityStyled_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServiceServer).ListActilityStyled(ctx, req.(*ListGatewayRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GatewayService_ListMon_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(emptypb.Empty)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServiceServer).ListMon(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayService_ListMon_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServiceServer).ListMon(ctx, req.(*emptypb.Empty))
	}
	return interceptor(ctx, in, info, handler)
}

func _GatewayService_GetStats_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetGatewayStatsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServiceServer).GetStats(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayService_GetStats_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServiceServer).GetStats(ctx, req.(*GetGatewayStatsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GatewayService_GetLastPing_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetLastPingRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServiceServer).GetLastPing(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayService_GetLastPing_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServiceServer).GetLastPing(ctx, req.(*GetLastPingRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GatewayService_GenerateGatewayClientCertificate_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GenerateGatewayClientCertificateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServiceServer).GenerateGatewayClientCertificate(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayService_GenerateGatewayClientCertificate_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServiceServer).GenerateGatewayClientCertificate(ctx, req.(*GenerateGatewayClientCertificateRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _GatewayService_StreamFrameLogs_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(StreamGatewayFrameLogsRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(GatewayServiceServer).StreamFrameLogs(m, &gatewayServiceStreamFrameLogsServer{stream})
}

type GatewayService_StreamFrameLogsServer interface {
	Send(*StreamGatewayFrameLogsResponse) error
	grpc.ServerStream
}

type gatewayServiceStreamFrameLogsServer struct {
	grpc.ServerStream
}

func (x *gatewayServiceStreamFrameLogsServer) Send(m *StreamGatewayFrameLogsResponse) error {
	return x.ServerStream.SendMsg(m)
}

func _GatewayService_GetTaskResults_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetGatewayRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GatewayServiceServer).GetTaskResults(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: GatewayService_GetTaskResults_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GatewayServiceServer).GetTaskResults(ctx, req.(*GetGatewayRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// GatewayService_ServiceDesc is the grpc.ServiceDesc for GatewayService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var GatewayService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "api.GatewayService",
	HandlerType: (*GatewayServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Create",
			Handler:    _GatewayService_Create_Handler,
		},
		{
			MethodName: "Get",
			Handler:    _GatewayService_Get_Handler,
		},
		{
			MethodName: "GetStatus",
			Handler:    _GatewayService_GetStatus_Handler,
		},
		{
			MethodName: "Update",
			Handler:    _GatewayService_Update_Handler,
		},
		{
			MethodName: "Delete",
			Handler:    _GatewayService_Delete_Handler,
		},
		{
			MethodName: "List",
			Handler:    _GatewayService_List_Handler,
		},
		{
			MethodName: "GetGatewayLogs",
			Handler:    _GatewayService_GetGatewayLogs_Handler,
		},
		{
			MethodName: "ListActilityStyled",
			Handler:    _GatewayService_ListActilityStyled_Handler,
		},
		{
			MethodName: "ListMon",
			Handler:    _GatewayService_ListMon_Handler,
		},
		{
			MethodName: "GetStats",
			Handler:    _GatewayService_GetStats_Handler,
		},
		{
			MethodName: "GetLastPing",
			Handler:    _GatewayService_GetLastPing_Handler,
		},
		{
			MethodName: "GenerateGatewayClientCertificate",
			Handler:    _GatewayService_GenerateGatewayClientCertificate_Handler,
		},
		{
			MethodName: "GetTaskResults",
			Handler:    _GatewayService_GetTaskResults_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "StreamFrameLogs",
			Handler:       _GatewayService_StreamFrameLogs_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "as/external/api/gateway.proto",
}