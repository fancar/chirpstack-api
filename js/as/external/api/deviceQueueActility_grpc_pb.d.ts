// GENERATED CODE -- DO NOT EDIT!

// package: api
// file: as/external/api/deviceQueueActility.proto

import * as as_external_api_deviceQueueActility_pb from "../../../as/external/api/deviceQueueActility_pb";
import * as grpc from "grpc";

interface IDeviceQueueServiceActilityService extends grpc.ServiceDefinition<grpc.UntypedServiceImplementation> {
  actilityEnqueue: grpc.MethodDefinition<as_external_api_deviceQueueActility_pb.EnqueueDeviceQueueActilityItemRequest, as_external_api_deviceQueueActility_pb.EnqueueDeviceQueueActilityItemResponse>;
}

export const DeviceQueueServiceActilityService: IDeviceQueueServiceActilityService;

export class DeviceQueueServiceActilityClient extends grpc.Client {
  constructor(address: string, credentials: grpc.ChannelCredentials, options?: object);
  actilityEnqueue(argument: as_external_api_deviceQueueActility_pb.EnqueueDeviceQueueActilityItemRequest, callback: grpc.requestCallback<as_external_api_deviceQueueActility_pb.EnqueueDeviceQueueActilityItemResponse>): grpc.ClientUnaryCall;
  actilityEnqueue(argument: as_external_api_deviceQueueActility_pb.EnqueueDeviceQueueActilityItemRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_deviceQueueActility_pb.EnqueueDeviceQueueActilityItemResponse>): grpc.ClientUnaryCall;
  actilityEnqueue(argument: as_external_api_deviceQueueActility_pb.EnqueueDeviceQueueActilityItemRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<as_external_api_deviceQueueActility_pb.EnqueueDeviceQueueActilityItemResponse>): grpc.ClientUnaryCall;
}
