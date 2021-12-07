// GENERATED CODE -- DO NOT EDIT!

// package: api
// file: as/external/api/deviceQueue.proto

import * as as_external_api_deviceQueue_pb from "../../../as/external/api/deviceQueue_pb";
import * as google_protobuf_empty_pb from "google-protobuf/google/protobuf/empty_pb";
import * as grpc from "@grpc/grpc-js";

interface IDeviceQueueServiceService extends grpc.ServiceDefinition<grpc.UntypedServiceImplementation> {
  enqueue: grpc.MethodDefinition<as_external_api_deviceQueue_pb.EnqueueDeviceQueueItemRequest, as_external_api_deviceQueue_pb.EnqueueDeviceQueueItemResponse>;
  flush: grpc.MethodDefinition<as_external_api_deviceQueue_pb.FlushDeviceQueueRequest, google_protobuf_empty_pb.Empty>;
  list: grpc.MethodDefinition<as_external_api_deviceQueue_pb.ListDeviceQueueItemsRequest, as_external_api_deviceQueue_pb.ListDeviceQueueItemsResponse>;
  actilityEnqueue: grpc.MethodDefinition<as_external_api_deviceQueue_pb.EnqueueDeviceQueueActilityItemRequest, as_external_api_deviceQueue_pb.EnqueueDeviceQueueActilityItemResponse>;
  getNextDownlinkFCnt: grpc.MethodDefinition<as_external_api_deviceQueue_pb.GetNextDownlinkFCntRequest, as_external_api_deviceQueue_pb.GetNextDownlinkFCntResponse>;
}

export const DeviceQueueServiceService: IDeviceQueueServiceService;

export interface IDeviceQueueServiceServer extends grpc.UntypedServiceImplementation {
  enqueue: grpc.handleUnaryCall<as_external_api_deviceQueue_pb.EnqueueDeviceQueueItemRequest, as_external_api_deviceQueue_pb.EnqueueDeviceQueueItemResponse>;
  flush: grpc.handleUnaryCall<as_external_api_deviceQueue_pb.FlushDeviceQueueRequest, google_protobuf_empty_pb.Empty>;
  list: grpc.handleUnaryCall<as_external_api_deviceQueue_pb.ListDeviceQueueItemsRequest, as_external_api_deviceQueue_pb.ListDeviceQueueItemsResponse>;
  actilityEnqueue: grpc.handleUnaryCall<as_external_api_deviceQueue_pb.EnqueueDeviceQueueActilityItemRequest, as_external_api_deviceQueue_pb.EnqueueDeviceQueueActilityItemResponse>;
  getNextDownlinkFCnt: grpc.handleUnaryCall<as_external_api_deviceQueue_pb.GetNextDownlinkFCntRequest, as_external_api_deviceQueue_pb.GetNextDownlinkFCntResponse>;
}

export class DeviceQueueServiceClient extends grpc.Client {
  constructor(address: string, credentials: grpc.ChannelCredentials, options?: object);
  enqueue(argument: as_external_api_deviceQueue_pb.EnqueueDeviceQueueItemRequest, callback: grpc.requestCallback<as_external_api_deviceQueue_pb.EnqueueDeviceQueueItemResponse>): grpc.ClientUnaryCall;
  enqueue(argument: as_external_api_deviceQueue_pb.EnqueueDeviceQueueItemRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_deviceQueue_pb.EnqueueDeviceQueueItemResponse>): grpc.ClientUnaryCall;
  enqueue(argument: as_external_api_deviceQueue_pb.EnqueueDeviceQueueItemRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_deviceQueue_pb.EnqueueDeviceQueueItemResponse>): grpc.ClientUnaryCall;
  flush(argument: as_external_api_deviceQueue_pb.FlushDeviceQueueRequest, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  flush(argument: as_external_api_deviceQueue_pb.FlushDeviceQueueRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  flush(argument: as_external_api_deviceQueue_pb.FlushDeviceQueueRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<google_protobuf_empty_pb.Empty>): grpc.ClientUnaryCall;
  list(argument: as_external_api_deviceQueue_pb.ListDeviceQueueItemsRequest, callback: grpc.requestCallback<as_external_api_deviceQueue_pb.ListDeviceQueueItemsResponse>): grpc.ClientUnaryCall;
  list(argument: as_external_api_deviceQueue_pb.ListDeviceQueueItemsRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_deviceQueue_pb.ListDeviceQueueItemsResponse>): grpc.ClientUnaryCall;
  list(argument: as_external_api_deviceQueue_pb.ListDeviceQueueItemsRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_deviceQueue_pb.ListDeviceQueueItemsResponse>): grpc.ClientUnaryCall;
  actilityEnqueue(argument: as_external_api_deviceQueue_pb.EnqueueDeviceQueueActilityItemRequest, callback: grpc.requestCallback<as_external_api_deviceQueue_pb.EnqueueDeviceQueueActilityItemResponse>): grpc.ClientUnaryCall;
  actilityEnqueue(argument: as_external_api_deviceQueue_pb.EnqueueDeviceQueueActilityItemRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_deviceQueue_pb.EnqueueDeviceQueueActilityItemResponse>): grpc.ClientUnaryCall;
  actilityEnqueue(argument: as_external_api_deviceQueue_pb.EnqueueDeviceQueueActilityItemRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_deviceQueue_pb.EnqueueDeviceQueueActilityItemResponse>): grpc.ClientUnaryCall;
  getNextDownlinkFCnt(argument: as_external_api_deviceQueue_pb.GetNextDownlinkFCntRequest, callback: grpc.requestCallback<as_external_api_deviceQueue_pb.GetNextDownlinkFCntResponse>): grpc.ClientUnaryCall;
  getNextDownlinkFCnt(argument: as_external_api_deviceQueue_pb.GetNextDownlinkFCntRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_deviceQueue_pb.GetNextDownlinkFCntResponse>): grpc.ClientUnaryCall;
  getNextDownlinkFCnt(argument: as_external_api_deviceQueue_pb.GetNextDownlinkFCntRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_deviceQueue_pb.GetNextDownlinkFCntResponse>): grpc.ClientUnaryCall;
}
