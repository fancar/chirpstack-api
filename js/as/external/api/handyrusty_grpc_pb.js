// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var google_api_annotations_pb = require('../../../google/api/annotations_pb.js');
var google_protobuf_timestamp_pb = require('google-protobuf/google/protobuf/timestamp_pb.js');
var google_protobuf_empty_pb = require('google-protobuf/google/protobuf/empty_pb.js');
var handyrusty_hr_pb = require('../../../handyrusty/hr_pb.js');
var gw_gw_pb = require('../../../gw/gw_pb.js');

function serialize_gw_GatewayCommandExecResponse(arg) {
  if (!(arg instanceof gw_gw_pb.GatewayCommandExecResponse)) {
    throw new Error('Expected argument of type gw.GatewayCommandExecResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_gw_GatewayCommandExecResponse(buffer_arg) {
  return gw_gw_pb.GatewayCommandExecResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_hr_ExecCommandRequest(arg) {
  if (!(arg instanceof handyrusty_hr_pb.ExecCommandRequest)) {
    throw new Error('Expected argument of type hr.ExecCommandRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_hr_ExecCommandRequest(buffer_arg) {
  return handyrusty_hr_pb.ExecCommandRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_hr_GetDeviceFramesLogRequest(arg) {
  if (!(arg instanceof handyrusty_hr_pb.GetDeviceFramesLogRequest)) {
    throw new Error('Expected argument of type hr.GetDeviceFramesLogRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_hr_GetDeviceFramesLogRequest(buffer_arg) {
  return handyrusty_hr_pb.GetDeviceFramesLogRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_hr_GetDeviceFramesLogResponse(arg) {
  if (!(arg instanceof handyrusty_hr_pb.GetDeviceFramesLogResponse)) {
    throw new Error('Expected argument of type hr.GetDeviceFramesLogResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_hr_GetDeviceFramesLogResponse(buffer_arg) {
  return handyrusty_hr_pb.GetDeviceFramesLogResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_hr_GetFrameCountersRequest(arg) {
  if (!(arg instanceof handyrusty_hr_pb.GetFrameCountersRequest)) {
    throw new Error('Expected argument of type hr.GetFrameCountersRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_hr_GetFrameCountersRequest(buffer_arg) {
  return handyrusty_hr_pb.GetFrameCountersRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_hr_GetFrameCountersResponse(arg) {
  if (!(arg instanceof handyrusty_hr_pb.GetFrameCountersResponse)) {
    throw new Error('Expected argument of type hr.GetFrameCountersResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_hr_GetFrameCountersResponse(buffer_arg) {
  return handyrusty_hr_pb.GetFrameCountersResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_hr_GetFrameSpeedRequest(arg) {
  if (!(arg instanceof handyrusty_hr_pb.GetFrameSpeedRequest)) {
    throw new Error('Expected argument of type hr.GetFrameSpeedRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_hr_GetFrameSpeedRequest(buffer_arg) {
  return handyrusty_hr_pb.GetFrameSpeedRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_hr_GetFrameSpeedResponse(arg) {
  if (!(arg instanceof handyrusty_hr_pb.GetFrameSpeedResponse)) {
    throw new Error('Expected argument of type hr.GetFrameSpeedResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_hr_GetFrameSpeedResponse(buffer_arg) {
  return handyrusty_hr_pb.GetFrameSpeedResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_hr_StreamDeviceFramesLogCSVResponse(arg) {
  if (!(arg instanceof handyrusty_hr_pb.StreamDeviceFramesLogCSVResponse)) {
    throw new Error('Expected argument of type hr.StreamDeviceFramesLogCSVResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_hr_StreamDeviceFramesLogCSVResponse(buffer_arg) {
  return handyrusty_hr_pb.StreamDeviceFramesLogCSVResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


// HandyRustyService is the service managing additional erth  tools, such as clickhouse storage and logger.
var HandyRustyServiceService = exports.HandyRustyServiceService = {
  // GetFrameCounters returns frame counters by type for the given range. Aggregation: day
  getFrameCounters: {
    path: '/api.HandyRustyService/GetFrameCounters',
    requestStream: false,
    responseStream: false,
    requestType: handyrusty_hr_pb.GetFrameCountersRequest,
    responseType: handyrusty_hr_pb.GetFrameCountersResponse,
    requestSerialize: serialize_hr_GetFrameCountersRequest,
    requestDeserialize: deserialize_hr_GetFrameCountersRequest,
    responseSerialize: serialize_hr_GetFrameCountersResponse,
    responseDeserialize: deserialize_hr_GetFrameCountersResponse,
  },
  // GetFrameSpeed returns an array with rx+tx frames per minute measurments
  getFrameSpeed: {
    path: '/api.HandyRustyService/GetFrameSpeed',
    requestStream: false,
    responseStream: false,
    requestType: handyrusty_hr_pb.GetFrameSpeedRequest,
    responseType: handyrusty_hr_pb.GetFrameSpeedResponse,
    requestSerialize: serialize_hr_GetFrameSpeedRequest,
    requestDeserialize: deserialize_hr_GetFrameSpeedRequest,
    responseSerialize: serialize_hr_GetFrameSpeedResponse,
    responseDeserialize: deserialize_hr_GetFrameSpeedResponse,
  },
  // ExecCommand sends the command to execute on gw. It waits 30 sec for an answer from gw
  execCommand: {
    path: '/api.HandyRustyService/ExecCommand',
    requestStream: false,
    responseStream: false,
    requestType: handyrusty_hr_pb.ExecCommandRequest,
    responseType: gw_gw_pb.GatewayCommandExecResponse,
    requestSerialize: serialize_hr_ExecCommandRequest,
    requestDeserialize: deserialize_hr_ExecCommandRequest,
    responseSerialize: serialize_gw_GatewayCommandExecResponse,
    responseDeserialize: deserialize_gw_GatewayCommandExecResponse,
  },
  // GetDeviceFramesLog returns an array with recieved and transmitted device's frames
  getDeviceFramesLog: {
    path: '/api.HandyRustyService/GetDeviceFramesLog',
    requestStream: false,
    responseStream: false,
    requestType: handyrusty_hr_pb.GetDeviceFramesLogRequest,
    responseType: handyrusty_hr_pb.GetDeviceFramesLogResponse,
    requestSerialize: serialize_hr_GetDeviceFramesLogRequest,
    requestDeserialize: deserialize_hr_GetDeviceFramesLogRequest,
    responseSerialize: serialize_hr_GetDeviceFramesLogResponse,
    responseDeserialize: deserialize_hr_GetDeviceFramesLogResponse,
  },
  // StreamDeviceFramesLogCSV streams the frame-logs from handyrusty CH-storage.
  //   * The data is transferred by chunks (stream);
  //   * This endpoint does not work from a web-browser!
  streamDeviceFramesLogCSV: {
    path: '/api.HandyRustyService/StreamDeviceFramesLogCSV',
    requestStream: false,
    responseStream: true,
    requestType: handyrusty_hr_pb.GetDeviceFramesLogRequest,
    responseType: handyrusty_hr_pb.StreamDeviceFramesLogCSVResponse,
    requestSerialize: serialize_hr_GetDeviceFramesLogRequest,
    requestDeserialize: deserialize_hr_GetDeviceFramesLogRequest,
    responseSerialize: serialize_hr_StreamDeviceFramesLogCSVResponse,
    responseDeserialize: deserialize_hr_StreamDeviceFramesLogCSVResponse,
  },
};

exports.HandyRustyServiceClient = grpc.makeGenericClientConstructor(HandyRustyServiceService);
