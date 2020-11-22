// GENERATED CODE -- DO NOT EDIT!

// package: as
// file: as/as.proto

import * as as_as_pb from "../as/as_pb";
import * as google_protobuf_empty_pb from "google-protobuf/google/protobuf/empty_pb";
import * as grpc from "grpc";

interface IApplicationServerServiceService extends grpc.ServiceDefinition<grpc.UntypedServiceImplementation> {
  handleUplinkData: grpc.MethodDefinition<as_as_pb.HandleUplinkDataRequest, google_protobuf_empty_pb.Empty>;
  handleProprietaryUplink: grpc.MethodDefinition<as_as_pb.HandleProprietaryUplinkRequest, google_protobuf_empty_pb.Empty>;
  handleError: grpc.MethodDefinition<as_as_pb.HandleErrorRequest, google_protobuf_empty_pb.Empty>;
  handleDownlinkACK: grpc.MethodDefinition<as_as_pb.HandleDownlinkACKRequest, google_protobuf_empty_pb.Empty>;
  handleGatewayStats: grpc.MethodDefinition<as_as_pb.HandleGatewayStatsRequest, google_protobuf_empty_pb.Empty>;
  handleTxAck: grpc.MethodDefinition<as_as_pb.HandleTxAckRequest, google_protobuf_empty_pb.Empty>;
  setDeviceStatus: grpc.MethodDefinition<as_as_pb.SetDeviceStatusRequest, google_protobuf_empty_pb.Empty>;
  setDeviceLocation: grpc.MethodDefinition<as_as_pb.SetDeviceLocationRequest, google_protobuf_empty_pb.Empty>;
  getDevicesSummary: grpc.MethodDefinition<as_as_pb.GetDevicesSummaryRequest, as_as_pb.GetDevicesSummaryResponse>;
  getGatewaysSummary: grpc.MethodDefinition<as_as_pb.GetGatewaysSummaryRequest, as_as_pb.GetGatewaysSummaryResponse>;
  listOrganisation: grpc.MethodDefinition<as_as_pb.ListOrganizationRequest, as_as_pb.ListOrganizationResponse>;
}

export const ApplicationServerServiceService: IApplicationServerServiceService;

export class ApplicationServerServiceClient extends grpc.Client {
  constructor(address: string, credentials: grpc.ChannelCredentials, options?: object);
  handleUplinkData(argument: as_as_pb.HandleUplinkDataRequest, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  handleUplinkData(argument: as_as_pb.HandleUplinkDataRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  handleUplinkData(argument: as_as_pb.HandleUplinkDataRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  handleProprietaryUplink(argument: as_as_pb.HandleProprietaryUplinkRequest, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  handleProprietaryUplink(argument: as_as_pb.HandleProprietaryUplinkRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  handleProprietaryUplink(argument: as_as_pb.HandleProprietaryUplinkRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  handleError(argument: as_as_pb.HandleErrorRequest, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  handleError(argument: as_as_pb.HandleErrorRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  handleError(argument: as_as_pb.HandleErrorRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  handleDownlinkACK(argument: as_as_pb.HandleDownlinkACKRequest, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  handleDownlinkACK(argument: as_as_pb.HandleDownlinkACKRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  handleDownlinkACK(argument: as_as_pb.HandleDownlinkACKRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  handleGatewayStats(argument: as_as_pb.HandleGatewayStatsRequest, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  handleGatewayStats(argument: as_as_pb.HandleGatewayStatsRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  handleGatewayStats(argument: as_as_pb.HandleGatewayStatsRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  handleTxAck(argument: as_as_pb.HandleTxAckRequest, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  handleTxAck(argument: as_as_pb.HandleTxAckRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  handleTxAck(argument: as_as_pb.HandleTxAckRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  setDeviceStatus(argument: as_as_pb.SetDeviceStatusRequest, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  setDeviceStatus(argument: as_as_pb.SetDeviceStatusRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  setDeviceStatus(argument: as_as_pb.SetDeviceStatusRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  setDeviceLocation(argument: as_as_pb.SetDeviceLocationRequest, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  setDeviceLocation(argument: as_as_pb.SetDeviceLocationRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  setDeviceLocation(argument: as_as_pb.SetDeviceLocationRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  getDevicesSummary(argument: as_as_pb.GetDevicesSummaryRequest, callback: grpc.requestCallback<as_as_pb.GetDevicesSummaryResponse>): grpc.ClientUnaryCall;
  getDevicesSummary(argument: as_as_pb.GetDevicesSummaryRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.GetDevicesSummaryResponse>): grpc.ClientUnaryCall;
  getDevicesSummary(argument: as_as_pb.GetDevicesSummaryRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.GetDevicesSummaryResponse>): grpc.ClientUnaryCall;
  getGatewaysSummary(argument: as_as_pb.GetGatewaysSummaryRequest, callback: grpc.requestCallback<as_as_pb.GetGatewaysSummaryResponse>): grpc.ClientUnaryCall;
  getGatewaysSummary(argument: as_as_pb.GetGatewaysSummaryRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.GetGatewaysSummaryResponse>): grpc.ClientUnaryCall;
  getGatewaysSummary(argument: as_as_pb.GetGatewaysSummaryRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.GetGatewaysSummaryResponse>): grpc.ClientUnaryCall;
  listOrganisation(argument: as_as_pb.ListOrganizationRequest, callback: grpc.requestCallback<as_as_pb.ListOrganizationResponse>): grpc.ClientUnaryCall;
  listOrganisation(argument: as_as_pb.ListOrganizationRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.ListOrganizationResponse>): grpc.ClientUnaryCall;
  listOrganisation(argument: as_as_pb.ListOrganizationRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.ListOrganizationResponse>): grpc.ClientUnaryCall;
}
