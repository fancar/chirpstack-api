// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('@grpc/grpc-js');
var as_as_pb = require('../as/as_pb.js');
var google_protobuf_empty_pb = require('google-protobuf/google/protobuf/empty_pb.js');
var google_protobuf_timestamp_pb = require('google-protobuf/google/protobuf/timestamp_pb.js');
var common_common_pb = require('../common/common_pb.js');
var ns_profiles_pb = require('../ns/profiles_pb.js');
var gw_gw_pb = require('../gw/gw_pb.js');
var ns_ns_pb = require('../ns/ns_pb.js');

function serialize_as_CreateServiceProfileRequest(arg) {
  if (!(arg instanceof as_as_pb.CreateServiceProfileRequest)) {
    throw new Error('Expected argument of type as.CreateServiceProfileRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_CreateServiceProfileRequest(buffer_arg) {
  return as_as_pb.CreateServiceProfileRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_CreateServiceProfileResponse(arg) {
  if (!(arg instanceof as_as_pb.CreateServiceProfileResponse)) {
    throw new Error('Expected argument of type as.CreateServiceProfileResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_CreateServiceProfileResponse(buffer_arg) {
  return as_as_pb.CreateServiceProfileResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_GatewayTaskResult(arg) {
  if (!(arg instanceof as_as_pb.GatewayTaskResult)) {
    throw new Error('Expected argument of type as.GatewayTaskResult');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_GatewayTaskResult(buffer_arg) {
  return as_as_pb.GatewayTaskResult.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_GetDeviceAppSKeyResponse(arg) {
  if (!(arg instanceof as_as_pb.GetDeviceAppSKeyResponse)) {
    throw new Error('Expected argument of type as.GetDeviceAppSKeyResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_GetDeviceAppSKeyResponse(buffer_arg) {
  return as_as_pb.GetDeviceAppSKeyResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_GetDevicesSummaryRequest(arg) {
  if (!(arg instanceof as_as_pb.GetDevicesSummaryRequest)) {
    throw new Error('Expected argument of type as.GetDevicesSummaryRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_GetDevicesSummaryRequest(buffer_arg) {
  return as_as_pb.GetDevicesSummaryRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_GetDevicesSummaryResponse(arg) {
  if (!(arg instanceof as_as_pb.GetDevicesSummaryResponse)) {
    throw new Error('Expected argument of type as.GetDevicesSummaryResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_GetDevicesSummaryResponse(buffer_arg) {
  return as_as_pb.GetDevicesSummaryResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_GetDictionaryRequest(arg) {
  if (!(arg instanceof as_as_pb.GetDictionaryRequest)) {
    throw new Error('Expected argument of type as.GetDictionaryRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_GetDictionaryRequest(buffer_arg) {
  return as_as_pb.GetDictionaryRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_GetDictionaryResponse(arg) {
  if (!(arg instanceof as_as_pb.GetDictionaryResponse)) {
    throw new Error('Expected argument of type as.GetDictionaryResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_GetDictionaryResponse(buffer_arg) {
  return as_as_pb.GetDictionaryResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_GetGWMetaDataResponse(arg) {
  if (!(arg instanceof as_as_pb.GetGWMetaDataResponse)) {
    throw new Error('Expected argument of type as.GetGWMetaDataResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_GetGWMetaDataResponse(buffer_arg) {
  return as_as_pb.GetGWMetaDataResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_GetGatewaysSummaryRequest(arg) {
  if (!(arg instanceof as_as_pb.GetGatewaysSummaryRequest)) {
    throw new Error('Expected argument of type as.GetGatewaysSummaryRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_GetGatewaysSummaryRequest(buffer_arg) {
  return as_as_pb.GetGatewaysSummaryRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_GetGatewaysSummaryResponse(arg) {
  if (!(arg instanceof as_as_pb.GetGatewaysSummaryResponse)) {
    throw new Error('Expected argument of type as.GetGatewaysSummaryResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_GetGatewaysSummaryResponse(buffer_arg) {
  return as_as_pb.GetGatewaysSummaryResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_GetOrgByDevEUIRequest(arg) {
  if (!(arg instanceof as_as_pb.GetOrgByDevEUIRequest)) {
    throw new Error('Expected argument of type as.GetOrgByDevEUIRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_GetOrgByDevEUIRequest(buffer_arg) {
  return as_as_pb.GetOrgByDevEUIRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_GetOrgByDevEUIResponse(arg) {
  if (!(arg instanceof as_as_pb.GetOrgByDevEUIResponse)) {
    throw new Error('Expected argument of type as.GetOrgByDevEUIResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_GetOrgByDevEUIResponse(buffer_arg) {
  return as_as_pb.GetOrgByDevEUIResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_GetOrgIDByGwIDRequest(arg) {
  if (!(arg instanceof as_as_pb.GetOrgIDByGwIDRequest)) {
    throw new Error('Expected argument of type as.GetOrgIDByGwIDRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_GetOrgIDByGwIDRequest(buffer_arg) {
  return as_as_pb.GetOrgIDByGwIDRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_GetServiceProfileRequest(arg) {
  if (!(arg instanceof as_as_pb.GetServiceProfileRequest)) {
    throw new Error('Expected argument of type as.GetServiceProfileRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_GetServiceProfileRequest(buffer_arg) {
  return as_as_pb.GetServiceProfileRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_GetServiceProfileResponse(arg) {
  if (!(arg instanceof as_as_pb.GetServiceProfileResponse)) {
    throw new Error('Expected argument of type as.GetServiceProfileResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_GetServiceProfileResponse(buffer_arg) {
  return as_as_pb.GetServiceProfileResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_HandleDownlinkACKRequest(arg) {
  if (!(arg instanceof as_as_pb.HandleDownlinkACKRequest)) {
    throw new Error('Expected argument of type as.HandleDownlinkACKRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_HandleDownlinkACKRequest(buffer_arg) {
  return as_as_pb.HandleDownlinkACKRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_HandleErrorRequest(arg) {
  if (!(arg instanceof as_as_pb.HandleErrorRequest)) {
    throw new Error('Expected argument of type as.HandleErrorRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_HandleErrorRequest(buffer_arg) {
  return as_as_pb.HandleErrorRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_HandleGatewayStatsRequest(arg) {
  if (!(arg instanceof as_as_pb.HandleGatewayStatsRequest)) {
    throw new Error('Expected argument of type as.HandleGatewayStatsRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_HandleGatewayStatsRequest(buffer_arg) {
  return as_as_pb.HandleGatewayStatsRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_HandleProprietaryUplinkRequest(arg) {
  if (!(arg instanceof as_as_pb.HandleProprietaryUplinkRequest)) {
    throw new Error('Expected argument of type as.HandleProprietaryUplinkRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_HandleProprietaryUplinkRequest(buffer_arg) {
  return as_as_pb.HandleProprietaryUplinkRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_HandleTxAckRequest(arg) {
  if (!(arg instanceof as_as_pb.HandleTxAckRequest)) {
    throw new Error('Expected argument of type as.HandleTxAckRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_HandleTxAckRequest(buffer_arg) {
  return as_as_pb.HandleTxAckRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_HandleUplinkDataRequest(arg) {
  if (!(arg instanceof as_as_pb.HandleUplinkDataRequest)) {
    throw new Error('Expected argument of type as.HandleUplinkDataRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_HandleUplinkDataRequest(buffer_arg) {
  return as_as_pb.HandleUplinkDataRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_ListOrganizationRequest(arg) {
  if (!(arg instanceof as_as_pb.ListOrganizationRequest)) {
    throw new Error('Expected argument of type as.ListOrganizationRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_ListOrganizationRequest(buffer_arg) {
  return as_as_pb.ListOrganizationRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_ListOrganizationResponse(arg) {
  if (!(arg instanceof as_as_pb.ListOrganizationResponse)) {
    throw new Error('Expected argument of type as.ListOrganizationResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_ListOrganizationResponse(buffer_arg) {
  return as_as_pb.ListOrganizationResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_ReEncryptDeviceQueueItemsRequest(arg) {
  if (!(arg instanceof as_as_pb.ReEncryptDeviceQueueItemsRequest)) {
    throw new Error('Expected argument of type as.ReEncryptDeviceQueueItemsRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_ReEncryptDeviceQueueItemsRequest(buffer_arg) {
  return as_as_pb.ReEncryptDeviceQueueItemsRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_ReEncryptDeviceQueueItemsResponse(arg) {
  if (!(arg instanceof as_as_pb.ReEncryptDeviceQueueItemsResponse)) {
    throw new Error('Expected argument of type as.ReEncryptDeviceQueueItemsResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_ReEncryptDeviceQueueItemsResponse(buffer_arg) {
  return as_as_pb.ReEncryptDeviceQueueItemsResponse.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_SetDeviceLocationRequest(arg) {
  if (!(arg instanceof as_as_pb.SetDeviceLocationRequest)) {
    throw new Error('Expected argument of type as.SetDeviceLocationRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_SetDeviceLocationRequest(buffer_arg) {
  return as_as_pb.SetDeviceLocationRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_SetDeviceStatusRequest(arg) {
  if (!(arg instanceof as_as_pb.SetDeviceStatusRequest)) {
    throw new Error('Expected argument of type as.SetDeviceStatusRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_SetDeviceStatusRequest(buffer_arg) {
  return as_as_pb.SetDeviceStatusRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_as_UpdateSPonDeviceRequest(arg) {
  if (!(arg instanceof as_as_pb.UpdateSPonDeviceRequest)) {
    throw new Error('Expected argument of type as.UpdateSPonDeviceRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_as_UpdateSPonDeviceRequest(buffer_arg) {
  return as_as_pb.UpdateSPonDeviceRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_google_protobuf_Empty(arg) {
  if (!(arg instanceof google_protobuf_empty_pb.Empty)) {
    throw new Error('Expected argument of type google.protobuf.Empty');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_google_protobuf_Empty(buffer_arg) {
  return google_protobuf_empty_pb.Empty.deserializeBinary(new Uint8Array(buffer_arg));
}


// ApplicationServerService is the service providing the application-server interface.
var ApplicationServerServiceService = exports.ApplicationServerServiceService = {
  // HandleUplinkData handles uplink data received from an end-device.
handleUplinkData: {
    path: '/as.ApplicationServerService/HandleUplinkData',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.HandleUplinkDataRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_as_HandleUplinkDataRequest,
    requestDeserialize: deserialize_as_HandleUplinkDataRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // HandleProprietaryUplink handles proprietary uplink payloads.
handleProprietaryUplink: {
    path: '/as.ApplicationServerService/HandleProprietaryUplink',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.HandleProprietaryUplinkRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_as_HandleProprietaryUplinkRequest,
    requestDeserialize: deserialize_as_HandleProprietaryUplinkRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // HandleError handles an error message.
handleError: {
    path: '/as.ApplicationServerService/HandleError',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.HandleErrorRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_as_HandleErrorRequest,
    requestDeserialize: deserialize_as_HandleErrorRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // HandleDownlinkACK handles a downlink ACK or nACK response.
handleDownlinkACK: {
    path: '/as.ApplicationServerService/HandleDownlinkACK',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.HandleDownlinkACKRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_as_HandleDownlinkACKRequest,
    requestDeserialize: deserialize_as_HandleDownlinkACKRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // HandleGatewayStats handles the given gateway stats.
handleGatewayStats: {
    path: '/as.ApplicationServerService/HandleGatewayStats',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.HandleGatewayStatsRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_as_HandleGatewayStatsRequest,
    requestDeserialize: deserialize_as_HandleGatewayStatsRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // HandleTXACK handles the TX acknowledgement.
handleTxAck: {
    path: '/as.ApplicationServerService/HandleTxAck',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.HandleTxAckRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_as_HandleTxAckRequest,
    requestDeserialize: deserialize_as_HandleTxAckRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // SetDeviceStatus updates the device-status for a device.
setDeviceStatus: {
    path: '/as.ApplicationServerService/SetDeviceStatus',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.SetDeviceStatusRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_as_SetDeviceStatusRequest,
    requestDeserialize: deserialize_as_SetDeviceStatusRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // SetDeviceLocation updates the device-location for a device.
setDeviceLocation: {
    path: '/as.ApplicationServerService/SetDeviceLocation',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.SetDeviceLocationRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_as_SetDeviceLocationRequest,
    requestDeserialize: deserialize_as_SetDeviceLocationRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // SetDeviceLocation updates the device-location for a device.
getDevicesSummary: {
    path: '/as.ApplicationServerService/GetDevicesSummary',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.GetDevicesSummaryRequest,
    responseType: as_as_pb.GetDevicesSummaryResponse,
    requestSerialize: serialize_as_GetDevicesSummaryRequest,
    requestDeserialize: deserialize_as_GetDevicesSummaryRequest,
    responseSerialize: serialize_as_GetDevicesSummaryResponse,
    responseDeserialize: deserialize_as_GetDevicesSummaryResponse,
  },
  // SetDeviceLocation updates the device-location for a device.
getGatewaysSummary: {
    path: '/as.ApplicationServerService/GetGatewaysSummary',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.GetGatewaysSummaryRequest,
    responseType: as_as_pb.GetGatewaysSummaryResponse,
    requestSerialize: serialize_as_GetGatewaysSummaryRequest,
    requestDeserialize: deserialize_as_GetGatewaysSummaryRequest,
    responseSerialize: serialize_as_GetGatewaysSummaryResponse,
    responseDeserialize: deserialize_as_GetGatewaysSummaryResponse,
  },
  // SetDeviceLocation updates the device-location for a device.
listOrganisation: {
    path: '/as.ApplicationServerService/ListOrganisation',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.ListOrganizationRequest,
    responseType: as_as_pb.ListOrganizationResponse,
    requestSerialize: serialize_as_ListOrganizationRequest,
    requestDeserialize: deserialize_as_ListOrganizationRequest,
    responseSerialize: serialize_as_ListOrganizationResponse,
    responseDeserialize: deserialize_as_ListOrganizationResponse,
  },
  // GetOrgByDevEUI returns organization id by devEUI. Modification.
getOrgByDevEUI: {
    path: '/as.ApplicationServerService/GetOrgByDevEUI',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.GetOrgByDevEUIRequest,
    responseType: as_as_pb.GetOrgByDevEUIResponse,
    requestSerialize: serialize_as_GetOrgByDevEUIRequest,
    requestDeserialize: deserialize_as_GetOrgByDevEUIRequest,
    responseSerialize: serialize_as_GetOrgByDevEUIResponse,
    responseDeserialize: deserialize_as_GetOrgByDevEUIResponse,
  },
  // GetOrgIDByGwID returns organization id by gwID. Modification.
getOrgIDByGwID: {
    path: '/as.ApplicationServerService/GetOrgIDByGwID',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.GetOrgIDByGwIDRequest,
    responseType: as_as_pb.GetOrgByDevEUIResponse,
    requestSerialize: serialize_as_GetOrgIDByGwIDRequest,
    requestDeserialize: deserialize_as_GetOrgIDByGwIDRequest,
    responseSerialize: serialize_as_GetOrgByDevEUIResponse,
    responseDeserialize: deserialize_as_GetOrgByDevEUIResponse,
  },
  // GetDeviceAppSKey returns AES128Key by devEUI. Modification.
getDeviceAppSKey: {
    path: '/as.ApplicationServerService/GetDeviceAppSKey',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.GetOrgByDevEUIRequest,
    responseType: as_as_pb.GetDeviceAppSKeyResponse,
    requestSerialize: serialize_as_GetOrgByDevEUIRequest,
    requestDeserialize: deserialize_as_GetOrgByDevEUIRequest,
    responseSerialize: serialize_as_GetDeviceAppSKeyResponse,
    responseDeserialize: deserialize_as_GetDeviceAppSKeyResponse,
  },
  // ReEncryptDeviceQueueItems requests the application-server to re-encrypt
// the given payload items using the new parameters. This request is
// for example triggered when the associated frame-counter of a downlink
// payload will be used by a mac-layer only payload, e.g. when the NS has
// mac-commands (or ACKs) to send to the device and combining this with
// an application-layer payload would exceed the max. payload size.
// Note there is no requirement that the number of returned items must be
// equal to the number of requested items.
reEncryptDeviceQueueItems: {
    path: '/as.ApplicationServerService/ReEncryptDeviceQueueItems',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.ReEncryptDeviceQueueItemsRequest,
    responseType: as_as_pb.ReEncryptDeviceQueueItemsResponse,
    requestSerialize: serialize_as_ReEncryptDeviceQueueItemsRequest,
    requestDeserialize: deserialize_as_ReEncryptDeviceQueueItemsRequest,
    responseSerialize: serialize_as_ReEncryptDeviceQueueItemsResponse,
    responseDeserialize: deserialize_as_ReEncryptDeviceQueueItemsResponse,
  },
  // StreamGatewayTaskResult stream ExecCmd results from gateway to save into as-db
streamGatewayTaskResult: {
    path: '/as.ApplicationServerService/StreamGatewayTaskResult',
    requestStream: true,
    responseStream: false,
    requestType: as_as_pb.GatewayTaskResult,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_as_GatewayTaskResult,
    requestDeserialize: deserialize_as_GatewayTaskResult,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
  // GetDictionary returns list of dictionary by the type. Modification.
getDictionary: {
    path: '/as.ApplicationServerService/GetDictionary',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.GetDictionaryRequest,
    responseType: as_as_pb.GetDictionaryResponse,
    requestSerialize: serialize_as_GetDictionaryRequest,
    requestDeserialize: deserialize_as_GetDictionaryRequest,
    responseSerialize: serialize_as_GetDictionaryResponse,
    responseDeserialize: deserialize_as_GetDictionaryResponse,
  },
  // GetGWMetaData returns a map with last metadata for the gw
getGWMetaData: {
    path: '/as.ApplicationServerService/GetGWMetaData',
    requestStream: false,
    responseStream: false,
    requestType: google_protobuf_empty_pb.Empty,
    responseType: as_as_pb.GetGWMetaDataResponse,
    requestSerialize: serialize_google_protobuf_Empty,
    requestDeserialize: deserialize_google_protobuf_Empty,
    responseSerialize: serialize_as_GetGWMetaDataResponse,
    responseDeserialize: deserialize_as_GetGWMetaDataResponse,
  },
  // GetServiceProfile (TEMP for ADR MIGRATE) returns sp from as-database (local only)
getServiceProfile: {
    path: '/as.ApplicationServerService/GetServiceProfile',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.GetServiceProfileRequest,
    responseType: as_as_pb.GetServiceProfileResponse,
    requestSerialize: serialize_as_GetServiceProfileRequest,
    requestDeserialize: deserialize_as_GetServiceProfileRequest,
    responseSerialize: serialize_as_GetServiceProfileResponse,
    responseDeserialize: deserialize_as_GetServiceProfileResponse,
  },
  // CreateServiceProfile (TEMP for ADR MIGRATE) creates service profile in as local db.
createServiceProfile: {
    path: '/as.ApplicationServerService/CreateServiceProfile',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.CreateServiceProfileRequest,
    responseType: as_as_pb.CreateServiceProfileResponse,
    requestSerialize: serialize_as_CreateServiceProfileRequest,
    requestDeserialize: deserialize_as_CreateServiceProfileRequest,
    responseSerialize: serialize_as_CreateServiceProfileResponse,
    responseDeserialize: deserialize_as_CreateServiceProfileResponse,
  },
  // UpdateSPonDevice (TEMP for ADR MIGRATE) update SP for device in local db.
updateSPonDevice: {
    path: '/as.ApplicationServerService/UpdateSPonDevice',
    requestStream: false,
    responseStream: false,
    requestType: as_as_pb.UpdateSPonDeviceRequest,
    responseType: google_protobuf_empty_pb.Empty,
    requestSerialize: serialize_as_UpdateSPonDeviceRequest,
    requestDeserialize: deserialize_as_UpdateSPonDeviceRequest,
    responseSerialize: serialize_google_protobuf_Empty,
    responseDeserialize: deserialize_google_protobuf_Empty,
  },
};

exports.ApplicationServerServiceClient = grpc.makeGenericClientConstructor(ApplicationServerServiceService);
