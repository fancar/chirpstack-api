// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var as_external_api_deviceQueueActility_pb = require('../../../as/external/api/deviceQueueActility_pb.js');
var google_api_annotations_pb = require('../../../google/api/annotations_pb.js');

function serialize_api_EnqueueDeviceQueueActilityItemRequest(arg) {
  if (!(arg instanceof as_external_api_deviceQueueActility_pb.EnqueueDeviceQueueActilityItemRequest)) {
    throw new Error('Expected argument of type api.EnqueueDeviceQueueActilityItemRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_EnqueueDeviceQueueActilityItemRequest(buffer_arg) {
  return as_external_api_deviceQueueActility_pb.EnqueueDeviceQueueActilityItemRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_api_EnqueueDeviceQueueActilityItemResponse(arg) {
  if (!(arg instanceof as_external_api_deviceQueueActility_pb.EnqueueDeviceQueueActilityItemResponse)) {
    throw new Error('Expected argument of type api.EnqueueDeviceQueueActilityItemResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_api_EnqueueDeviceQueueActilityItemResponse(buffer_arg) {
  return as_external_api_deviceQueueActility_pb.EnqueueDeviceQueueActilityItemResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


// DeviceQueueServiceActility is the service managing the downlink data queue with Actility styled message (legacy).
var DeviceQueueServiceActilityService = exports.DeviceQueueServiceActilityService = {
  // Enqueue adds the given item to the device-queue.
  actilityEnqueue: {
    path: '/api.DeviceQueueServiceActility/ActilityEnqueue',
    requestStream: false,
    responseStream: false,
    requestType: as_external_api_deviceQueueActility_pb.EnqueueDeviceQueueActilityItemRequest,
    responseType: as_external_api_deviceQueueActility_pb.EnqueueDeviceQueueActilityItemResponse,
    requestSerialize: serialize_api_EnqueueDeviceQueueActilityItemRequest,
    requestDeserialize: deserialize_api_EnqueueDeviceQueueActilityItemRequest,
    responseSerialize: serialize_api_EnqueueDeviceQueueActilityItemResponse,
    responseDeserialize: deserialize_api_EnqueueDeviceQueueActilityItemResponse,
  },
};

exports.DeviceQueueServiceActilityClient = grpc.makeGenericClientConstructor(DeviceQueueServiceActilityService);
