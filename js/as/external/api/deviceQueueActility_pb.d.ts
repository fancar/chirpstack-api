// package: api
// file: as/external/api/deviceQueueActility.proto

import * as jspb from "google-protobuf";
import * as google_api_annotations_pb from "../../../google/api/annotations_pb";

export class EnqueueDeviceQueueActilityItemRequest extends jspb.Message {
  getDevEui(): string;
  setDevEui(value: string): void;

  getConfirmDownlink(): boolean;
  setConfirmDownlink(value: boolean): void;

  getFlushDownlinkQueue(): boolean;
  setFlushDownlinkQueue(value: boolean): void;

  getPayloadHex(): string;
  setPayloadHex(value: string): void;

  getTargetPorts(): string;
  setTargetPorts(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EnqueueDeviceQueueActilityItemRequest.AsObject;
  static toObject(includeInstance: boolean, msg: EnqueueDeviceQueueActilityItemRequest): EnqueueDeviceQueueActilityItemRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EnqueueDeviceQueueActilityItemRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EnqueueDeviceQueueActilityItemRequest;
  static deserializeBinaryFromReader(message: EnqueueDeviceQueueActilityItemRequest, reader: jspb.BinaryReader): EnqueueDeviceQueueActilityItemRequest;
}

export namespace EnqueueDeviceQueueActilityItemRequest {
  export type AsObject = {
    devEui: string,
    confirmDownlink: boolean,
    flushDownlinkQueue: boolean,
    payloadHex: string,
    targetPorts: string,
  }
}

export class EnqueueDeviceQueueActilityItemResponse extends jspb.Message {
  getConfirmDownlink(): boolean;
  setConfirmDownlink(value: boolean): void;

  getFlushDownlinkQueue(): boolean;
  setFlushDownlinkQueue(value: boolean): void;

  getPayloadHex(): string;
  setPayloadHex(value: string): void;

  getTargetPorts(): string;
  setTargetPorts(value: string): void;

  getStatus(): string;
  setStatus(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EnqueueDeviceQueueActilityItemResponse.AsObject;
  static toObject(includeInstance: boolean, msg: EnqueueDeviceQueueActilityItemResponse): EnqueueDeviceQueueActilityItemResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EnqueueDeviceQueueActilityItemResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EnqueueDeviceQueueActilityItemResponse;
  static deserializeBinaryFromReader(message: EnqueueDeviceQueueActilityItemResponse, reader: jspb.BinaryReader): EnqueueDeviceQueueActilityItemResponse;
}

export namespace EnqueueDeviceQueueActilityItemResponse {
  export type AsObject = {
    confirmDownlink: boolean,
    flushDownlinkQueue: boolean,
    payloadHex: string,
    targetPorts: string,
    status: string,
  }
}

