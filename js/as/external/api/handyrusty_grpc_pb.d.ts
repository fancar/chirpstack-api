// GENERATED CODE -- DO NOT EDIT!

// package: api
// file: as/external/api/handyrusty.proto

import * as as_external_api_handyrusty_pb from "../../../as/external/api/handyrusty_pb";
import * as handyrusty_hr_pb from "../../../handyrusty/hr_pb";
import * as gw_gw_pb from "../../../gw/gw_pb";
import * as grpc from "grpc";

interface IHandyRustyServiceService extends grpc.ServiceDefinition<grpc.UntypedServiceImplementation> {
  getFrameCounters: grpc.MethodDefinition<handyrusty_hr_pb.GetFrameCountersRequest, handyrusty_hr_pb.GetFrameCountersResponse>;
  getFrameSpeed: grpc.MethodDefinition<handyrusty_hr_pb.GetFrameSpeedRequest, handyrusty_hr_pb.GetFrameSpeedResponse>;
  execCommand: grpc.MethodDefinition<handyrusty_hr_pb.ExecCommandRequest, gw_gw_pb.GatewayCommandExecResponse>;
  getDeviceFramesLog: grpc.MethodDefinition<handyrusty_hr_pb.GetDeviceFramesLogRequest, handyrusty_hr_pb.GetDeviceFramesLogResponse>;
  streamDeviceFramesLogCSV: grpc.MethodDefinition<handyrusty_hr_pb.GetDeviceFramesLogRequest, handyrusty_hr_pb.StreamDeviceFramesLogCSVResponse>;
}

export const HandyRustyServiceService: IHandyRustyServiceService;

export class HandyRustyServiceClient extends grpc.Client {
  constructor(address: string, credentials: grpc.ChannelCredentials, options?: object);
  getFrameCounters(argument: handyrusty_hr_pb.GetFrameCountersRequest, callback: grpc.requestCallback<handyrusty_hr_pb.GetFrameCountersResponse>): grpc.ClientUnaryCall;
  getFrameCounters(argument: handyrusty_hr_pb.GetFrameCountersRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<handyrusty_hr_pb.GetFrameCountersResponse>): grpc.ClientUnaryCall;
  getFrameCounters(argument: handyrusty_hr_pb.GetFrameCountersRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<handyrusty_hr_pb.GetFrameCountersResponse>): grpc.ClientUnaryCall;
  getFrameSpeed(argument: handyrusty_hr_pb.GetFrameSpeedRequest, callback: grpc.requestCallback<handyrusty_hr_pb.GetFrameSpeedResponse>): grpc.ClientUnaryCall;
  getFrameSpeed(argument: handyrusty_hr_pb.GetFrameSpeedRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<handyrusty_hr_pb.GetFrameSpeedResponse>): grpc.ClientUnaryCall;
  getFrameSpeed(argument: handyrusty_hr_pb.GetFrameSpeedRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<handyrusty_hr_pb.GetFrameSpeedResponse>): grpc.ClientUnaryCall;
  execCommand(argument: handyrusty_hr_pb.ExecCommandRequest, callback: grpc.requestCallback<gw_gw_pb.GatewayCommandExecResponse>): grpc.ClientUnaryCall;
  execCommand(argument: handyrusty_hr_pb.ExecCommandRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<gw_gw_pb.GatewayCommandExecResponse>): grpc.ClientUnaryCall;
  execCommand(argument: handyrusty_hr_pb.ExecCommandRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<gw_gw_pb.GatewayCommandExecResponse>): grpc.ClientUnaryCall;
  getDeviceFramesLog(argument: handyrusty_hr_pb.GetDeviceFramesLogRequest, callback: grpc.requestCallback<handyrusty_hr_pb.GetDeviceFramesLogResponse>): grpc.ClientUnaryCall;
  getDeviceFramesLog(argument: handyrusty_hr_pb.GetDeviceFramesLogRequest, metadataOrOptions: grpc.Metadata | grpc.CallOptions | null, callback: grpc.requestCallback<handyrusty_hr_pb.GetDeviceFramesLogResponse>): grpc.ClientUnaryCall;
  getDeviceFramesLog(argument: handyrusty_hr_pb.GetDeviceFramesLogRequest, metadata: grpc.Metadata | null, options: grpc.CallOptions | null, callback: grpc.requestCallback<handyrusty_hr_pb.GetDeviceFramesLogResponse>): grpc.ClientUnaryCall;
  streamDeviceFramesLogCSV(argument: handyrusty_hr_pb.GetDeviceFramesLogRequest, metadataOrOptions?: grpc.Metadata | grpc.CallOptions | null): grpc.ClientReadableStream<handyrusty_hr_pb.StreamDeviceFramesLogCSVResponse>;
  streamDeviceFramesLogCSV(argument: handyrusty_hr_pb.GetDeviceFramesLogRequest, metadata?: grpc.Metadata | null, options?: grpc.CallOptions | null): grpc.ClientReadableStream<handyrusty_hr_pb.StreamDeviceFramesLogCSVResponse>;
}
