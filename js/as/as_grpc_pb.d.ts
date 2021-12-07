// GENERATED CODE -- DO NOT EDIT!

// package: as
// file: as/as.proto

import * as as_as_pb from "../as/as_pb";
import * as google_protobuf_empty_pb from "google-protobuf/google/protobuf/empty_pb";
import * as grpc from "@grpc/grpc-js";

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
  getOrgByDevEUI: grpc.MethodDefinition<as_as_pb.GetOrgByDevEUIRequest, as_as_pb.GetOrgByDevEUIResponse>;
  getOrgIDByGwID: grpc.MethodDefinition<as_as_pb.GetOrgIDByGwIDRequest, as_as_pb.GetOrgByDevEUIResponse>;
  getDeviceAppSKey: grpc.MethodDefinition<as_as_pb.GetOrgByDevEUIRequest, as_as_pb.GetDeviceAppSKeyResponse>;
  reEncryptDeviceQueueItems: grpc.MethodDefinition<as_as_pb.ReEncryptDeviceQueueItemsRequest, as_as_pb.ReEncryptDeviceQueueItemsResponse>;
  streamGatewayTaskResult: grpc.MethodDefinition<as_as_pb.GatewayTaskResult, google_protobuf_empty_pb.Empty>;
  getDictionary: grpc.MethodDefinition<as_as_pb.GetDictionaryRequest, as_as_pb.GetDictionaryResponse>;
  getGWMetaData: grpc.MethodDefinition<google_protobuf_empty_pb.Empty, as_as_pb.GetGWMetaDataResponse>;
  getServiceProfile: grpc.MethodDefinition<as_as_pb.GetServiceProfileRequest, as_as_pb.GetServiceProfileResponse>;
  createServiceProfile: grpc.MethodDefinition<as_as_pb.CreateServiceProfileRequest, as_as_pb.CreateServiceProfileResponse>;
  updateSPonDevice: grpc.MethodDefinition<as_as_pb.UpdateSPonDeviceRequest, google_protobuf_empty_pb.Empty>;
}

export const ApplicationServerServiceService: IApplicationServerServiceService;

export interface IApplicationServerServiceServer extends grpc.UntypedServiceImplementation {
  handleUplinkData: grpc.handleUnaryCall<as_as_pb.HandleUplinkDataRequest, google_protobuf_empty_pb.Empty>;
  handleProprietaryUplink: grpc.handleUnaryCall<as_as_pb.HandleProprietaryUplinkRequest, google_protobuf_empty_pb.Empty>;
  handleError: grpc.handleUnaryCall<as_as_pb.HandleErrorRequest, google_protobuf_empty_pb.Empty>;
  handleDownlinkACK: grpc.handleUnaryCall<as_as_pb.HandleDownlinkACKRequest, google_protobuf_empty_pb.Empty>;
  handleGatewayStats: grpc.handleUnaryCall<as_as_pb.HandleGatewayStatsRequest, google_protobuf_empty_pb.Empty>;
  handleTxAck: grpc.handleUnaryCall<as_as_pb.HandleTxAckRequest, google_protobuf_empty_pb.Empty>;
  setDeviceStatus: grpc.handleUnaryCall<as_as_pb.SetDeviceStatusRequest, google_protobuf_empty_pb.Empty>;
  setDeviceLocation: grpc.handleUnaryCall<as_as_pb.SetDeviceLocationRequest, google_protobuf_empty_pb.Empty>;
  getDevicesSummary: grpc.handleUnaryCall<as_as_pb.GetDevicesSummaryRequest, as_as_pb.GetDevicesSummaryResponse>;
  getGatewaysSummary: grpc.handleUnaryCall<as_as_pb.GetGatewaysSummaryRequest, as_as_pb.GetGatewaysSummaryResponse>;
  listOrganisation: grpc.handleUnaryCall<as_as_pb.ListOrganizationRequest, as_as_pb.ListOrganizationResponse>;
  getOrgByDevEUI: grpc.handleUnaryCall<as_as_pb.GetOrgByDevEUIRequest, as_as_pb.GetOrgByDevEUIResponse>;
  getOrgIDByGwID: grpc.handleUnaryCall<as_as_pb.GetOrgIDByGwIDRequest, as_as_pb.GetOrgByDevEUIResponse>;
  getDeviceAppSKey: grpc.handleUnaryCall<as_as_pb.GetOrgByDevEUIRequest, as_as_pb.GetDeviceAppSKeyResponse>;
  reEncryptDeviceQueueItems: grpc.handleUnaryCall<as_as_pb.ReEncryptDeviceQueueItemsRequest, as_as_pb.ReEncryptDeviceQueueItemsResponse>;
  streamGatewayTaskResult: grpc.handleClientStreamingCall<as_as_pb.GatewayTaskResult, google_protobuf_empty_pb.Empty>;
  getDictionary: grpc.handleUnaryCall<as_as_pb.GetDictionaryRequest, as_as_pb.GetDictionaryResponse>;
  getGWMetaData: grpc.handleUnaryCall<google_protobuf_empty_pb.Empty, as_as_pb.GetGWMetaDataResponse>;
  getServiceProfile: grpc.handleUnaryCall<as_as_pb.GetServiceProfileRequest, as_as_pb.GetServiceProfileResponse>;
  createServiceProfile: grpc.handleUnaryCall<as_as_pb.CreateServiceProfileRequest, as_as_pb.CreateServiceProfileResponse>;
  updateSPonDevice: grpc.handleUnaryCall<as_as_pb.UpdateSPonDeviceRequest, google_protobuf_empty_pb.Empty>;
}

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
  getOrgByDevEUI(argument: as_as_pb.GetOrgByDevEUIRequest, callback: grpc.requestCallback<as_as_pb.GetOrgByDevEUIResponse>): grpc.ClientUnaryCall;
  getOrgByDevEUI(argument: as_as_pb.GetOrgByDevEUIRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.GetOrgByDevEUIResponse>): grpc.ClientUnaryCall;
  getOrgByDevEUI(argument: as_as_pb.GetOrgByDevEUIRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.GetOrgByDevEUIResponse>): grpc.ClientUnaryCall;
  getOrgIDByGwID(argument: as_as_pb.GetOrgIDByGwIDRequest, callback: grpc.requestCallback<as_as_pb.GetOrgByDevEUIResponse>): grpc.ClientUnaryCall;
  getOrgIDByGwID(argument: as_as_pb.GetOrgIDByGwIDRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.GetOrgByDevEUIResponse>): grpc.ClientUnaryCall;
  getOrgIDByGwID(argument: as_as_pb.GetOrgIDByGwIDRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.GetOrgByDevEUIResponse>): grpc.ClientUnaryCall;
  getDeviceAppSKey(argument: as_as_pb.GetOrgByDevEUIRequest, callback: grpc.requestCallback<as_as_pb.GetDeviceAppSKeyResponse>): grpc.ClientUnaryCall;
  getDeviceAppSKey(argument: as_as_pb.GetOrgByDevEUIRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.GetDeviceAppSKeyResponse>): grpc.ClientUnaryCall;
  getDeviceAppSKey(argument: as_as_pb.GetOrgByDevEUIRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.GetDeviceAppSKeyResponse>): grpc.ClientUnaryCall;
  reEncryptDeviceQueueItems(argument: as_as_pb.ReEncryptDeviceQueueItemsRequest, callback: grpc.requestCallback<as_as_pb.ReEncryptDeviceQueueItemsResponse>): grpc.ClientUnaryCall;
  reEncryptDeviceQueueItems(argument: as_as_pb.ReEncryptDeviceQueueItemsRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.ReEncryptDeviceQueueItemsResponse>): grpc.ClientUnaryCall;
  reEncryptDeviceQueueItems(argument: as_as_pb.ReEncryptDeviceQueueItemsRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.ReEncryptDeviceQueueItemsResponse>): grpc.ClientUnaryCall;
  streamGatewayTaskResult(callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientWritableStream<as_as_pb.GatewayTaskResult>;
  streamGatewayTaskResult(metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientWritableStream<as_as_pb.GatewayTaskResult>;
  streamGatewayTaskResult(metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientWritableStream<as_as_pb.GatewayTaskResult>;
  getDictionary(argument: as_as_pb.GetDictionaryRequest, callback: grpc.requestCallback<as_as_pb.GetDictionaryResponse>): grpc.ClientUnaryCall;
  getDictionary(argument: as_as_pb.GetDictionaryRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.GetDictionaryResponse>): grpc.ClientUnaryCall;
  getDictionary(argument: as_as_pb.GetDictionaryRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.GetDictionaryResponse>): grpc.ClientUnaryCall;
  getGWMetaData(argument: google_protobuf_empty_pb.Empty, callback: grpc.requestCallback<as_as_pb.GetGWMetaDataResponse>): grpc.ClientUnaryCall;
  getGWMetaData(argument: google_protobuf_empty_pb.Empty, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.GetGWMetaDataResponse>): grpc.ClientUnaryCall;
  getGWMetaData(argument: google_protobuf_empty_pb.Empty, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.GetGWMetaDataResponse>): grpc.ClientUnaryCall;
  getServiceProfile(argument: as_as_pb.GetServiceProfileRequest, callback: grpc.requestCallback<as_as_pb.GetServiceProfileResponse>): grpc.ClientUnaryCall;
  getServiceProfile(argument: as_as_pb.GetServiceProfileRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.GetServiceProfileResponse>): grpc.ClientUnaryCall;
  getServiceProfile(argument: as_as_pb.GetServiceProfileRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.GetServiceProfileResponse>): grpc.ClientUnaryCall;
  createServiceProfile(argument: as_as_pb.CreateServiceProfileRequest, callback: grpc.requestCallback<as_as_pb.CreateServiceProfileResponse>): grpc.ClientUnaryCall;
  createServiceProfile(argument: as_as_pb.CreateServiceProfileRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.CreateServiceProfileResponse>): grpc.ClientUnaryCall;
  createServiceProfile(argument: as_as_pb.CreateServiceProfileRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_as_pb.CreateServiceProfileResponse>): grpc.ClientUnaryCall;
  updateSPonDevice(argument: as_as_pb.UpdateSPonDeviceRequest, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  updateSPonDevice(argument: as_as_pb.UpdateSPonDeviceRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  updateSPonDevice(argument: as_as_pb.UpdateSPonDeviceRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
}
