// package: as
// file: as/as.proto

import * as jspb from "google-protobuf";
import * as google_protobuf_empty_pb from "google-protobuf/google/protobuf/empty_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";
import * as common_common_pb from "../common/common_pb";
import * as ns_profiles_pb from "../ns/profiles_pb";
import * as gw_gw_pb from "../gw/gw_pb";
import * as ns_ns_pb from "../ns/ns_pb";

export class UpdateSPonDeviceRequest extends jspb.Message {
  getId(): Uint8Array | string;
  getId_asU8(): Uint8Array;
  getId_asB64(): string;
  setId(value: Uint8Array | string): void;

  getSpId(): Uint8Array | string;
  getSpId_asU8(): Uint8Array;
  getSpId_asB64(): string;
  setSpId(value: Uint8Array | string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateSPonDeviceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateSPonDeviceRequest): UpdateSPonDeviceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateSPonDeviceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateSPonDeviceRequest;
  static deserializeBinaryFromReader(message: UpdateSPonDeviceRequest, reader: jspb.BinaryReader): UpdateSPonDeviceRequest;
}

export namespace UpdateSPonDeviceRequest {
  export type AsObject = {
    id: Uint8Array | string,
    spId: Uint8Array | string,
  }
}

export class GetServiceProfileRequest extends jspb.Message {
  getId(): Uint8Array | string;
  getId_asU8(): Uint8Array;
  getId_asB64(): string;
  setId(value: Uint8Array | string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetServiceProfileRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetServiceProfileRequest): GetServiceProfileRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetServiceProfileRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetServiceProfileRequest;
  static deserializeBinaryFromReader(message: GetServiceProfileRequest, reader: jspb.BinaryReader): GetServiceProfileRequest;
}

export namespace GetServiceProfileRequest {
  export type AsObject = {
    id: Uint8Array | string,
  }
}

export class GetServiceProfileResponse extends jspb.Message {
  hasAsData(): boolean;
  clearAsData(): void;
  getAsData(): ServiceProfileItem | undefined;
  setAsData(value?: ServiceProfileItem): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetServiceProfileResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetServiceProfileResponse): GetServiceProfileResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetServiceProfileResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetServiceProfileResponse;
  static deserializeBinaryFromReader(message: GetServiceProfileResponse, reader: jspb.BinaryReader): GetServiceProfileResponse;
}

export namespace GetServiceProfileResponse {
  export type AsObject = {
    asData?: ServiceProfileItem.AsObject,
  }
}

export class CreateServiceProfileRequest extends jspb.Message {
  hasAsData(): boolean;
  clearAsData(): void;
  getAsData(): ServiceProfileItem | undefined;
  setAsData(value?: ServiceProfileItem): void;

  hasNsData(): boolean;
  clearNsData(): void;
  getNsData(): ns_profiles_pb.ServiceProfile | undefined;
  setNsData(value?: ns_profiles_pb.ServiceProfile): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateServiceProfileRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateServiceProfileRequest): CreateServiceProfileRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateServiceProfileRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateServiceProfileRequest;
  static deserializeBinaryFromReader(message: CreateServiceProfileRequest, reader: jspb.BinaryReader): CreateServiceProfileRequest;
}

export namespace CreateServiceProfileRequest {
  export type AsObject = {
    asData?: ServiceProfileItem.AsObject,
    nsData?: ns_profiles_pb.ServiceProfile.AsObject,
  }
}

export class CreateServiceProfileResponse extends jspb.Message {
  getId(): Uint8Array | string;
  getId_asU8(): Uint8Array;
  getId_asB64(): string;
  setId(value: Uint8Array | string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateServiceProfileResponse.AsObject;
  static toObject(includeInstance: boolean, msg: CreateServiceProfileResponse): CreateServiceProfileResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateServiceProfileResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateServiceProfileResponse;
  static deserializeBinaryFromReader(message: CreateServiceProfileResponse, reader: jspb.BinaryReader): CreateServiceProfileResponse;
}

export namespace CreateServiceProfileResponse {
  export type AsObject = {
    id: Uint8Array | string,
  }
}

export class ServiceProfileItem extends jspb.Message {
  getNetworkServerId(): number;
  setNetworkServerId(value: number): void;

  getOrganizationId(): number;
  setOrganizationId(value: number): void;

  getName(): string;
  setName(value: string): void;

  getDescription(): string;
  setDescription(value: string): void;

  getDeviceCountLimit(): number;
  setDeviceCountLimit(value: number): void;

  hasCreatedAt(): boolean;
  clearCreatedAt(): void;
  getCreatedAt(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setCreatedAt(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasUpdatedAt(): boolean;
  clearUpdatedAt(): void;
  getUpdatedAt(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setUpdatedAt(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ServiceProfileItem.AsObject;
  static toObject(includeInstance: boolean, msg: ServiceProfileItem): ServiceProfileItem.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ServiceProfileItem, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ServiceProfileItem;
  static deserializeBinaryFromReader(message: ServiceProfileItem, reader: jspb.BinaryReader): ServiceProfileItem;
}

export namespace ServiceProfileItem {
  export type AsObject = {
    networkServerId: number,
    organizationId: number,
    name: string,
    description: string,
    deviceCountLimit: number,
    createdAt?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    updatedAt?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GatewayMetaData extends jspb.Message {
  getGwId(): string;
  setGwId(value: string): void;

  getMetadataMap(): jspb.Map<string, string>;
  clearMetadataMap(): void;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GatewayMetaData.AsObject;
  static toObject(includeInstance: boolean, msg: GatewayMetaData): GatewayMetaData.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GatewayMetaData, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GatewayMetaData;
  static deserializeBinaryFromReader(message: GatewayMetaData, reader: jspb.BinaryReader): GatewayMetaData;
}

export namespace GatewayMetaData {
  export type AsObject = {
    gwId: string,
    metadataMap: Array<[string, string]>,
  }
}

export class GetGWMetaDataResponse extends jspb.Message {
  clearMetadataListList(): void;
  getMetadataListList(): Array<GatewayMetaData>;
  setMetadataListList(value: Array<GatewayMetaData>): void;
  addMetadataList(value?: GatewayMetaData, index?: number): GatewayMetaData;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGWMetaDataResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetGWMetaDataResponse): GetGWMetaDataResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGWMetaDataResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGWMetaDataResponse;
  static deserializeBinaryFromReader(message: GetGWMetaDataResponse, reader: jspb.BinaryReader): GetGWMetaDataResponse;
}

export namespace GetGWMetaDataResponse {
  export type AsObject = {
    metadataListList: Array<GatewayMetaData.AsObject>,
  }
}

export class GetDictionaryRequest extends jspb.Message {
  getDicType(): string;
  setDicType(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetDictionaryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetDictionaryRequest): GetDictionaryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetDictionaryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetDictionaryRequest;
  static deserializeBinaryFromReader(message: GetDictionaryRequest, reader: jspb.BinaryReader): GetDictionaryRequest;
}

export namespace GetDictionaryRequest {
  export type AsObject = {
    dicType: string,
  }
}

export class GetDictionaryResponse extends jspb.Message {
  getDicType(): string;
  setDicType(value: string): void;

  clearListList(): void;
  getListList(): Array<Dictionary>;
  setListList(value: Array<Dictionary>): void;
  addList(value?: Dictionary, index?: number): Dictionary;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetDictionaryResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetDictionaryResponse): GetDictionaryResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetDictionaryResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetDictionaryResponse;
  static deserializeBinaryFromReader(message: GetDictionaryResponse, reader: jspb.BinaryReader): GetDictionaryResponse;
}

export namespace GetDictionaryResponse {
  export type AsObject = {
    dicType: string,
    listList: Array<Dictionary.AsObject>,
  }
}

export class Dictionary extends jspb.Message {
  getCode(): number;
  setCode(value: number): void;

  getDicType(): string;
  setDicType(value: string): void;

  getLabel(): string;
  setLabel(value: string): void;

  getIsActual(): boolean;
  setIsActual(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Dictionary.AsObject;
  static toObject(includeInstance: boolean, msg: Dictionary): Dictionary.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Dictionary, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Dictionary;
  static deserializeBinaryFromReader(message: Dictionary, reader: jspb.BinaryReader): Dictionary;
}

export namespace Dictionary {
  export type AsObject = {
    code: number,
    dicType: string,
    label: string,
    isActual: boolean,
  }
}

export class GetOrgByDevEUIRequest extends jspb.Message {
  getDevEui(): string;
  setDevEui(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetOrgByDevEUIRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetOrgByDevEUIRequest): GetOrgByDevEUIRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetOrgByDevEUIRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetOrgByDevEUIRequest;
  static deserializeBinaryFromReader(message: GetOrgByDevEUIRequest, reader: jspb.BinaryReader): GetOrgByDevEUIRequest;
}

export namespace GetOrgByDevEUIRequest {
  export type AsObject = {
    devEui: string,
  }
}

export class GetOrgIDByGwIDRequest extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetOrgIDByGwIDRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetOrgIDByGwIDRequest): GetOrgIDByGwIDRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetOrgIDByGwIDRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetOrgIDByGwIDRequest;
  static deserializeBinaryFromReader(message: GetOrgIDByGwIDRequest, reader: jspb.BinaryReader): GetOrgIDByGwIDRequest;
}

export namespace GetOrgIDByGwIDRequest {
  export type AsObject = {
    id: string,
  }
}

export class GetDeviceAppSKeyResponse extends jspb.Message {
  getValue(): Uint8Array | string;
  getValue_asU8(): Uint8Array;
  getValue_asB64(): string;
  setValue(value: Uint8Array | string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetDeviceAppSKeyResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetDeviceAppSKeyResponse): GetDeviceAppSKeyResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetDeviceAppSKeyResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetDeviceAppSKeyResponse;
  static deserializeBinaryFromReader(message: GetDeviceAppSKeyResponse, reader: jspb.BinaryReader): GetDeviceAppSKeyResponse;
}

export namespace GetDeviceAppSKeyResponse {
  export type AsObject = {
    value: Uint8Array | string,
  }
}

export class GetOrgByDevEUIResponse extends jspb.Message {
  getId(): number;
  setId(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetOrgByDevEUIResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetOrgByDevEUIResponse): GetOrgByDevEUIResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetOrgByDevEUIResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetOrgByDevEUIResponse;
  static deserializeBinaryFromReader(message: GetOrgByDevEUIResponse, reader: jspb.BinaryReader): GetOrgByDevEUIResponse;
}

export namespace GetOrgByDevEUIResponse {
  export type AsObject = {
    id: number,
  }
}

export class ListOrganizationRequest extends jspb.Message {
  getLimit(): number;
  setLimit(value: number): void;

  getOffset(): number;
  setOffset(value: number): void;

  getSearch(): string;
  setSearch(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListOrganizationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ListOrganizationRequest): ListOrganizationRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ListOrganizationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListOrganizationRequest;
  static deserializeBinaryFromReader(message: ListOrganizationRequest, reader: jspb.BinaryReader): ListOrganizationRequest;
}

export namespace ListOrganizationRequest {
  export type AsObject = {
    limit: number,
    offset: number,
    search: string,
  }
}

export class ListOrganizationResponse extends jspb.Message {
  getTotalCount(): number;
  setTotalCount(value: number): void;

  clearResultList(): void;
  getResultList(): Array<OrganizationListItem>;
  setResultList(value: Array<OrganizationListItem>): void;
  addResult(value?: OrganizationListItem, index?: number): OrganizationListItem;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListOrganizationResponse.AsObject;
  static toObject(includeInstance: boolean, msg: ListOrganizationResponse): ListOrganizationResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ListOrganizationResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListOrganizationResponse;
  static deserializeBinaryFromReader(message: ListOrganizationResponse, reader: jspb.BinaryReader): ListOrganizationResponse;
}

export namespace ListOrganizationResponse {
  export type AsObject = {
    totalCount: number,
    resultList: Array<OrganizationListItem.AsObject>,
  }
}

export class OrganizationListItem extends jspb.Message {
  getId(): number;
  setId(value: number): void;

  getName(): string;
  setName(value: string): void;

  getDisplayName(): string;
  setDisplayName(value: string): void;

  getCanHaveGateways(): boolean;
  setCanHaveGateways(value: boolean): void;

  hasCreatedAt(): boolean;
  clearCreatedAt(): void;
  getCreatedAt(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setCreatedAt(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasUpdatedAt(): boolean;
  clearUpdatedAt(): void;
  getUpdatedAt(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setUpdatedAt(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OrganizationListItem.AsObject;
  static toObject(includeInstance: boolean, msg: OrganizationListItem): OrganizationListItem.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OrganizationListItem, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OrganizationListItem;
  static deserializeBinaryFromReader(message: OrganizationListItem, reader: jspb.BinaryReader): OrganizationListItem;
}

export namespace OrganizationListItem {
  export type AsObject = {
    id: number,
    name: string,
    displayName: string,
    canHaveGateways: boolean,
    createdAt?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    updatedAt?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetDevicesSummaryRequest extends jspb.Message {
  getOrganizationId(): number;
  setOrganizationId(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetDevicesSummaryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetDevicesSummaryRequest): GetDevicesSummaryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetDevicesSummaryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetDevicesSummaryRequest;
  static deserializeBinaryFromReader(message: GetDevicesSummaryRequest, reader: jspb.BinaryReader): GetDevicesSummaryRequest;
}

export namespace GetDevicesSummaryRequest {
  export type AsObject = {
    organizationId: number,
  }
}

export class GetDevicesSummaryResponse extends jspb.Message {
  getActiveCount(): number;
  setActiveCount(value: number): void;

  getInactiveCount(): number;
  setInactiveCount(value: number): void;

  getDrCountMap(): jspb.Map<number, number>;
  clearDrCountMap(): void;
  getNeverSeenCount(): number;
  setNeverSeenCount(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetDevicesSummaryResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetDevicesSummaryResponse): GetDevicesSummaryResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetDevicesSummaryResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetDevicesSummaryResponse;
  static deserializeBinaryFromReader(message: GetDevicesSummaryResponse, reader: jspb.BinaryReader): GetDevicesSummaryResponse;
}

export namespace GetDevicesSummaryResponse {
  export type AsObject = {
    activeCount: number,
    inactiveCount: number,
    drCountMap: Array<[number, number]>,
    neverSeenCount: number,
  }
}

export class GetGatewaysSummaryRequest extends jspb.Message {
  getOrganizationId(): number;
  setOrganizationId(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGatewaysSummaryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetGatewaysSummaryRequest): GetGatewaysSummaryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGatewaysSummaryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGatewaysSummaryRequest;
  static deserializeBinaryFromReader(message: GetGatewaysSummaryRequest, reader: jspb.BinaryReader): GetGatewaysSummaryRequest;
}

export namespace GetGatewaysSummaryRequest {
  export type AsObject = {
    organizationId: number,
  }
}

export class GetGatewaysSummaryResponse extends jspb.Message {
  getActiveCount(): number;
  setActiveCount(value: number): void;

  getInactiveCount(): number;
  setInactiveCount(value: number): void;

  getNeverSeenCount(): number;
  setNeverSeenCount(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetGatewaysSummaryResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetGatewaysSummaryResponse): GetGatewaysSummaryResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetGatewaysSummaryResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetGatewaysSummaryResponse;
  static deserializeBinaryFromReader(message: GetGatewaysSummaryResponse, reader: jspb.BinaryReader): GetGatewaysSummaryResponse;
}

export namespace GetGatewaysSummaryResponse {
  export type AsObject = {
    activeCount: number,
    inactiveCount: number,
    neverSeenCount: number,
  }
}

export class DeviceActivationContext extends jspb.Message {
  getDevAddr(): Uint8Array | string;
  getDevAddr_asU8(): Uint8Array;
  getDevAddr_asB64(): string;
  setDevAddr(value: Uint8Array | string): void;

  hasAppSKey(): boolean;
  clearAppSKey(): void;
  getAppSKey(): common_common_pb.KeyEnvelope | undefined;
  setAppSKey(value?: common_common_pb.KeyEnvelope): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeviceActivationContext.AsObject;
  static toObject(includeInstance: boolean, msg: DeviceActivationContext): DeviceActivationContext.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeviceActivationContext, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeviceActivationContext;
  static deserializeBinaryFromReader(message: DeviceActivationContext, reader: jspb.BinaryReader): DeviceActivationContext;
}

export namespace DeviceActivationContext {
  export type AsObject = {
    devAddr: Uint8Array | string,
    appSKey?: common_common_pb.KeyEnvelope.AsObject,
  }
}

export class HandleUplinkDataRequest extends jspb.Message {
  getDevEui(): Uint8Array | string;
  getDevEui_asU8(): Uint8Array;
  getDevEui_asB64(): string;
  setDevEui(value: Uint8Array | string): void;

  getJoinEui(): Uint8Array | string;
  getJoinEui_asU8(): Uint8Array;
  getJoinEui_asB64(): string;
  setJoinEui(value: Uint8Array | string): void;

  getFCnt(): number;
  setFCnt(value: number): void;

  getFPort(): number;
  setFPort(value: number): void;

  getAdr(): boolean;
  setAdr(value: boolean): void;

  getDr(): number;
  setDr(value: number): void;

  hasTxInfo(): boolean;
  clearTxInfo(): void;
  getTxInfo(): gw_gw_pb.UplinkTXInfo | undefined;
  setTxInfo(value?: gw_gw_pb.UplinkTXInfo): void;

  clearRxInfoList(): void;
  getRxInfoList(): Array<gw_gw_pb.UplinkRXInfo>;
  setRxInfoList(value: Array<gw_gw_pb.UplinkRXInfo>): void;
  addRxInfo(value?: gw_gw_pb.UplinkRXInfo, index?: number): gw_gw_pb.UplinkRXInfo;

  getData(): Uint8Array | string;
  getData_asU8(): Uint8Array;
  getData_asB64(): string;
  setData(value: Uint8Array | string): void;

  hasDeviceActivationContext(): boolean;
  clearDeviceActivationContext(): void;
  getDeviceActivationContext(): DeviceActivationContext | undefined;
  setDeviceActivationContext(value?: DeviceActivationContext): void;

  getConfirmedUplink(): boolean;
  setConfirmedUplink(value: boolean): void;

  getLate(): boolean;
  setLate(value: boolean): void;

  getMic(): Uint8Array | string;
  getMic_asU8(): Uint8Array;
  getMic_asB64(): string;
  setMic(value: Uint8Array | string): void;

  hasTime(): boolean;
  clearTime(): void;
  getTime(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTime(value?: google_protobuf_timestamp_pb.Timestamp): void;

  getLimit(): ns_ns_pb.RateLimitMap[keyof ns_ns_pb.RateLimitMap];
  setLimit(value: ns_ns_pb.RateLimitMap[keyof ns_ns_pb.RateLimitMap]): void;

  getPer(): number;
  setPer(value: number): void;

  getSnr(): number;
  setSnr(value: number): void;

  getRssi(): number;
  setRssi(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HandleUplinkDataRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HandleUplinkDataRequest): HandleUplinkDataRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HandleUplinkDataRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HandleUplinkDataRequest;
  static deserializeBinaryFromReader(message: HandleUplinkDataRequest, reader: jspb.BinaryReader): HandleUplinkDataRequest;
}

export namespace HandleUplinkDataRequest {
  export type AsObject = {
    devEui: Uint8Array | string,
    joinEui: Uint8Array | string,
    fCnt: number,
    fPort: number,
    adr: boolean,
    dr: number,
    txInfo?: gw_gw_pb.UplinkTXInfo.AsObject,
    rxInfoList: Array<gw_gw_pb.UplinkRXInfo.AsObject>,
    data: Uint8Array | string,
    deviceActivationContext?: DeviceActivationContext.AsObject,
    confirmedUplink: boolean,
    late: boolean,
    mic: Uint8Array | string,
    time?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    limit: ns_ns_pb.RateLimitMap[keyof ns_ns_pb.RateLimitMap],
    per: number,
    snr: number,
    rssi: number,
  }
}

export class HandleProprietaryUplinkRequest extends jspb.Message {
  getMacPayload(): Uint8Array | string;
  getMacPayload_asU8(): Uint8Array;
  getMacPayload_asB64(): string;
  setMacPayload(value: Uint8Array | string): void;

  getMic(): Uint8Array | string;
  getMic_asU8(): Uint8Array;
  getMic_asB64(): string;
  setMic(value: Uint8Array | string): void;

  hasTxInfo(): boolean;
  clearTxInfo(): void;
  getTxInfo(): gw_gw_pb.UplinkTXInfo | undefined;
  setTxInfo(value?: gw_gw_pb.UplinkTXInfo): void;

  clearRxInfoList(): void;
  getRxInfoList(): Array<gw_gw_pb.UplinkRXInfo>;
  setRxInfoList(value: Array<gw_gw_pb.UplinkRXInfo>): void;
  addRxInfo(value?: gw_gw_pb.UplinkRXInfo, index?: number): gw_gw_pb.UplinkRXInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HandleProprietaryUplinkRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HandleProprietaryUplinkRequest): HandleProprietaryUplinkRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HandleProprietaryUplinkRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HandleProprietaryUplinkRequest;
  static deserializeBinaryFromReader(message: HandleProprietaryUplinkRequest, reader: jspb.BinaryReader): HandleProprietaryUplinkRequest;
}

export namespace HandleProprietaryUplinkRequest {
  export type AsObject = {
    macPayload: Uint8Array | string,
    mic: Uint8Array | string,
    txInfo?: gw_gw_pb.UplinkTXInfo.AsObject,
    rxInfoList: Array<gw_gw_pb.UplinkRXInfo.AsObject>,
  }
}

export class HandleErrorRequest extends jspb.Message {
  getDevEui(): Uint8Array | string;
  getDevEui_asU8(): Uint8Array;
  getDevEui_asB64(): string;
  setDevEui(value: Uint8Array | string): void;

  getType(): ErrorTypeMap[keyof ErrorTypeMap];
  setType(value: ErrorTypeMap[keyof ErrorTypeMap]): void;

  getError(): string;
  setError(value: string): void;

  getFCnt(): number;
  setFCnt(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HandleErrorRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HandleErrorRequest): HandleErrorRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HandleErrorRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HandleErrorRequest;
  static deserializeBinaryFromReader(message: HandleErrorRequest, reader: jspb.BinaryReader): HandleErrorRequest;
}

export namespace HandleErrorRequest {
  export type AsObject = {
    devEui: Uint8Array | string,
    type: ErrorTypeMap[keyof ErrorTypeMap],
    error: string,
    fCnt: number,
  }
}

export class HandleDownlinkACKRequest extends jspb.Message {
  getDevEui(): Uint8Array | string;
  getDevEui_asU8(): Uint8Array;
  getDevEui_asB64(): string;
  setDevEui(value: Uint8Array | string): void;

  getFCnt(): number;
  setFCnt(value: number): void;

  getAcknowledged(): boolean;
  setAcknowledged(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HandleDownlinkACKRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HandleDownlinkACKRequest): HandleDownlinkACKRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HandleDownlinkACKRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HandleDownlinkACKRequest;
  static deserializeBinaryFromReader(message: HandleDownlinkACKRequest, reader: jspb.BinaryReader): HandleDownlinkACKRequest;
}

export namespace HandleDownlinkACKRequest {
  export type AsObject = {
    devEui: Uint8Array | string,
    fCnt: number,
    acknowledged: boolean,
  }
}

export class SetDeviceStatusRequest extends jspb.Message {
  getDevEui(): Uint8Array | string;
  getDevEui_asU8(): Uint8Array;
  getDevEui_asB64(): string;
  setDevEui(value: Uint8Array | string): void;

  getBattery(): number;
  setBattery(value: number): void;

  getMargin(): number;
  setMargin(value: number): void;

  getExternalPowerSource(): boolean;
  setExternalPowerSource(value: boolean): void;

  getBatteryLevelUnavailable(): boolean;
  setBatteryLevelUnavailable(value: boolean): void;

  getBatteryLevel(): number;
  setBatteryLevel(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SetDeviceStatusRequest.AsObject;
  static toObject(includeInstance: boolean, msg: SetDeviceStatusRequest): SetDeviceStatusRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SetDeviceStatusRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SetDeviceStatusRequest;
  static deserializeBinaryFromReader(message: SetDeviceStatusRequest, reader: jspb.BinaryReader): SetDeviceStatusRequest;
}

export namespace SetDeviceStatusRequest {
  export type AsObject = {
    devEui: Uint8Array | string,
    battery: number,
    margin: number,
    externalPowerSource: boolean,
    batteryLevelUnavailable: boolean,
    batteryLevel: number,
  }
}

export class SetDeviceLocationRequest extends jspb.Message {
  getDevEui(): Uint8Array | string;
  getDevEui_asU8(): Uint8Array;
  getDevEui_asB64(): string;
  setDevEui(value: Uint8Array | string): void;

  hasLocation(): boolean;
  clearLocation(): void;
  getLocation(): common_common_pb.Location | undefined;
  setLocation(value?: common_common_pb.Location): void;

  clearUplinkIdsList(): void;
  getUplinkIdsList(): Array<Uint8Array | string>;
  getUplinkIdsList_asU8(): Array<Uint8Array>;
  getUplinkIdsList_asB64(): Array<string>;
  setUplinkIdsList(value: Array<Uint8Array | string>): void;
  addUplinkIds(value: Uint8Array | string, index?: number): Uint8Array | string;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SetDeviceLocationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: SetDeviceLocationRequest): SetDeviceLocationRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SetDeviceLocationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SetDeviceLocationRequest;
  static deserializeBinaryFromReader(message: SetDeviceLocationRequest, reader: jspb.BinaryReader): SetDeviceLocationRequest;
}

export namespace SetDeviceLocationRequest {
  export type AsObject = {
    devEui: Uint8Array | string,
    location?: common_common_pb.Location.AsObject,
    uplinkIdsList: Array<Uint8Array | string>,
  }
}

export class HandleGatewayStatsRequest extends jspb.Message {
  getGatewayId(): Uint8Array | string;
  getGatewayId_asU8(): Uint8Array;
  getGatewayId_asB64(): string;
  setGatewayId(value: Uint8Array | string): void;

  getStatsId(): Uint8Array | string;
  getStatsId_asU8(): Uint8Array;
  getStatsId_asB64(): string;
  setStatsId(value: Uint8Array | string): void;

  hasTime(): boolean;
  clearTime(): void;
  getTime(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTime(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasLocation(): boolean;
  clearLocation(): void;
  getLocation(): common_common_pb.Location | undefined;
  setLocation(value?: common_common_pb.Location): void;

  getRxPacketsReceived(): number;
  setRxPacketsReceived(value: number): void;

  getRxPacketsReceivedOk(): number;
  setRxPacketsReceivedOk(value: number): void;

  getTxPacketsReceived(): number;
  setTxPacketsReceived(value: number): void;

  getTxPacketsEmitted(): number;
  setTxPacketsEmitted(value: number): void;

  getMetadataMap(): jspb.Map<string, string>;
  clearMetadataMap(): void;
  getTxPacketsPerFrequencyMap(): jspb.Map<number, number>;
  clearTxPacketsPerFrequencyMap(): void;
  getRxPacketsPerFrequencyMap(): jspb.Map<number, number>;
  clearRxPacketsPerFrequencyMap(): void;
  getTxPacketsPerDrMap(): jspb.Map<number, number>;
  clearTxPacketsPerDrMap(): void;
  getRxPacketsPerDrMap(): jspb.Map<number, number>;
  clearRxPacketsPerDrMap(): void;
  getTxPacketsPerStatusMap(): jspb.Map<string, number>;
  clearTxPacketsPerStatusMap(): void;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HandleGatewayStatsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HandleGatewayStatsRequest): HandleGatewayStatsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HandleGatewayStatsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HandleGatewayStatsRequest;
  static deserializeBinaryFromReader(message: HandleGatewayStatsRequest, reader: jspb.BinaryReader): HandleGatewayStatsRequest;
}

export namespace HandleGatewayStatsRequest {
  export type AsObject = {
    gatewayId: Uint8Array | string,
    statsId: Uint8Array | string,
    time?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    location?: common_common_pb.Location.AsObject,
    rxPacketsReceived: number,
    rxPacketsReceivedOk: number,
    txPacketsReceived: number,
    txPacketsEmitted: number,
    metadataMap: Array<[string, string]>,
    txPacketsPerFrequencyMap: Array<[number, number]>,
    rxPacketsPerFrequencyMap: Array<[number, number]>,
    txPacketsPerDrMap: Array<[number, number]>,
    rxPacketsPerDrMap: Array<[number, number]>,
    txPacketsPerStatusMap: Array<[string, number]>,
  }
}

export class HandleTxAckRequest extends jspb.Message {
  getDevEui(): Uint8Array | string;
  getDevEui_asU8(): Uint8Array;
  getDevEui_asB64(): string;
  setDevEui(value: Uint8Array | string): void;

  getFCnt(): number;
  setFCnt(value: number): void;

  getGatewayId(): Uint8Array | string;
  getGatewayId_asU8(): Uint8Array;
  getGatewayId_asB64(): string;
  setGatewayId(value: Uint8Array | string): void;

  hasTxInfo(): boolean;
  clearTxInfo(): void;
  getTxInfo(): gw_gw_pb.DownlinkTXInfo | undefined;
  setTxInfo(value?: gw_gw_pb.DownlinkTXInfo): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HandleTxAckRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HandleTxAckRequest): HandleTxAckRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HandleTxAckRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HandleTxAckRequest;
  static deserializeBinaryFromReader(message: HandleTxAckRequest, reader: jspb.BinaryReader): HandleTxAckRequest;
}

export namespace HandleTxAckRequest {
  export type AsObject = {
    devEui: Uint8Array | string,
    fCnt: number,
    gatewayId: Uint8Array | string,
    txInfo?: gw_gw_pb.DownlinkTXInfo.AsObject,
  }
}

export class ReEncryptDeviceQueueItemsRequest extends jspb.Message {
  getDevEui(): Uint8Array | string;
  getDevEui_asU8(): Uint8Array;
  getDevEui_asB64(): string;
  setDevEui(value: Uint8Array | string): void;

  getDevAddr(): Uint8Array | string;
  getDevAddr_asU8(): Uint8Array;
  getDevAddr_asB64(): string;
  setDevAddr(value: Uint8Array | string): void;

  getFCntStart(): number;
  setFCntStart(value: number): void;

  clearItemsList(): void;
  getItemsList(): Array<ReEncryptDeviceQueueItem>;
  setItemsList(value: Array<ReEncryptDeviceQueueItem>): void;
  addItems(value?: ReEncryptDeviceQueueItem, index?: number): ReEncryptDeviceQueueItem;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReEncryptDeviceQueueItemsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ReEncryptDeviceQueueItemsRequest): ReEncryptDeviceQueueItemsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReEncryptDeviceQueueItemsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReEncryptDeviceQueueItemsRequest;
  static deserializeBinaryFromReader(message: ReEncryptDeviceQueueItemsRequest, reader: jspb.BinaryReader): ReEncryptDeviceQueueItemsRequest;
}

export namespace ReEncryptDeviceQueueItemsRequest {
  export type AsObject = {
    devEui: Uint8Array | string,
    devAddr: Uint8Array | string,
    fCntStart: number,
    itemsList: Array<ReEncryptDeviceQueueItem.AsObject>,
  }
}

export class ReEncryptDeviceQueueItemsResponse extends jspb.Message {
  clearItemsList(): void;
  getItemsList(): Array<ReEncryptedDeviceQueueItem>;
  setItemsList(value: Array<ReEncryptedDeviceQueueItem>): void;
  addItems(value?: ReEncryptedDeviceQueueItem, index?: number): ReEncryptedDeviceQueueItem;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReEncryptDeviceQueueItemsResponse.AsObject;
  static toObject(includeInstance: boolean, msg: ReEncryptDeviceQueueItemsResponse): ReEncryptDeviceQueueItemsResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReEncryptDeviceQueueItemsResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReEncryptDeviceQueueItemsResponse;
  static deserializeBinaryFromReader(message: ReEncryptDeviceQueueItemsResponse, reader: jspb.BinaryReader): ReEncryptDeviceQueueItemsResponse;
}

export namespace ReEncryptDeviceQueueItemsResponse {
  export type AsObject = {
    itemsList: Array<ReEncryptedDeviceQueueItem.AsObject>,
  }
}

export class ReEncryptDeviceQueueItem extends jspb.Message {
  getFrmPayload(): Uint8Array | string;
  getFrmPayload_asU8(): Uint8Array;
  getFrmPayload_asB64(): string;
  setFrmPayload(value: Uint8Array | string): void;

  getFCnt(): number;
  setFCnt(value: number): void;

  getFPort(): number;
  setFPort(value: number): void;

  getConfirmed(): boolean;
  setConfirmed(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReEncryptDeviceQueueItem.AsObject;
  static toObject(includeInstance: boolean, msg: ReEncryptDeviceQueueItem): ReEncryptDeviceQueueItem.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReEncryptDeviceQueueItem, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReEncryptDeviceQueueItem;
  static deserializeBinaryFromReader(message: ReEncryptDeviceQueueItem, reader: jspb.BinaryReader): ReEncryptDeviceQueueItem;
}

export namespace ReEncryptDeviceQueueItem {
  export type AsObject = {
    frmPayload: Uint8Array | string,
    fCnt: number,
    fPort: number,
    confirmed: boolean,
  }
}

export class ReEncryptedDeviceQueueItem extends jspb.Message {
  getFrmPayload(): Uint8Array | string;
  getFrmPayload_asU8(): Uint8Array;
  getFrmPayload_asB64(): string;
  setFrmPayload(value: Uint8Array | string): void;

  getFCnt(): number;
  setFCnt(value: number): void;

  getFPort(): number;
  setFPort(value: number): void;

  getConfirmed(): boolean;
  setConfirmed(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReEncryptedDeviceQueueItem.AsObject;
  static toObject(includeInstance: boolean, msg: ReEncryptedDeviceQueueItem): ReEncryptedDeviceQueueItem.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReEncryptedDeviceQueueItem, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReEncryptedDeviceQueueItem;
  static deserializeBinaryFromReader(message: ReEncryptedDeviceQueueItem, reader: jspb.BinaryReader): ReEncryptedDeviceQueueItem;
}

export namespace ReEncryptedDeviceQueueItem {
  export type AsObject = {
    frmPayload: Uint8Array | string,
    fCnt: number,
    fPort: number,
    confirmed: boolean,
  }
}

export class GatewayTaskResponseData extends jspb.Message {
  getGatewayId(): Uint8Array | string;
  getGatewayId_asU8(): Uint8Array;
  getGatewayId_asB64(): string;
  setGatewayId(value: Uint8Array | string): void;

  getExecId(): Uint8Array | string;
  getExecId_asU8(): Uint8Array;
  getExecId_asB64(): string;
  setExecId(value: Uint8Array | string): void;

  getCmd(): string;
  setCmd(value: string): void;

  getStderr(): Uint8Array | string;
  getStderr_asU8(): Uint8Array;
  getStderr_asB64(): string;
  setStderr(value: Uint8Array | string): void;

  getError(): string;
  setError(value: string): void;

  getDescription(): string;
  setDescription(value: string): void;

  getName(): string;
  setName(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GatewayTaskResponseData.AsObject;
  static toObject(includeInstance: boolean, msg: GatewayTaskResponseData): GatewayTaskResponseData.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GatewayTaskResponseData, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GatewayTaskResponseData;
  static deserializeBinaryFromReader(message: GatewayTaskResponseData, reader: jspb.BinaryReader): GatewayTaskResponseData;
}

export namespace GatewayTaskResponseData {
  export type AsObject = {
    gatewayId: Uint8Array | string,
    execId: Uint8Array | string,
    cmd: string,
    stderr: Uint8Array | string,
    error: string,
    description: string,
    name: string,
  }
}

export class GatewayTaskResult extends jspb.Message {
  hasMetadata(): boolean;
  clearMetadata(): void;
  getMetadata(): GatewayTaskResponseData | undefined;
  setMetadata(value?: GatewayTaskResponseData): void;

  hasChunk(): boolean;
  clearChunk(): void;
  getChunk(): Uint8Array | string;
  getChunk_asU8(): Uint8Array;
  getChunk_asB64(): string;
  setChunk(value: Uint8Array | string): void;

  getResultCase(): GatewayTaskResult.ResultCase;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GatewayTaskResult.AsObject;
  static toObject(includeInstance: boolean, msg: GatewayTaskResult): GatewayTaskResult.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GatewayTaskResult, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GatewayTaskResult;
  static deserializeBinaryFromReader(message: GatewayTaskResult, reader: jspb.BinaryReader): GatewayTaskResult;
}

export namespace GatewayTaskResult {
  export type AsObject = {
    metadata?: GatewayTaskResponseData.AsObject,
    chunk: Uint8Array | string,
  }

  export enum ResultCase {
    RESULT_NOT_SET = 0,
    METADATA = 1,
    CHUNK = 2,
  }
}

export interface RXWindowMap {
  RX1: 0;
  RX2: 1;
}

export const RXWindow: RXWindowMap;

export interface ErrorTypeMap {
  GENERIC: 0;
  OTAA: 1;
  DATA_UP_FCNT_RESET: 2;
  DATA_UP_MIC: 3;
  DEVICE_QUEUE_ITEM_SIZE: 4;
  DEVICE_QUEUE_ITEM_FCNT: 5;
  DATA_UP_FCNT_RETRANSMISSION: 6;
  DATA_DOWN_GATEWAY: 7;
}

export const ErrorType: ErrorTypeMap;

