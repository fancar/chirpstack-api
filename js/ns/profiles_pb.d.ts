// package: ns
// file: ns/profiles.proto

import * as jspb from "google-protobuf";

export class ServiceProfile extends jspb.Message {
  getId(): Uint8Array | string;
  getId_asU8(): Uint8Array;
  getId_asB64(): string;
  setId(value: Uint8Array | string): void;

  getUlRate(): number;
  setUlRate(value: number): void;

  getUlBucketSize(): number;
  setUlBucketSize(value: number): void;

  getUlRatePolicy(): RatePolicyMap[keyof RatePolicyMap];
  setUlRatePolicy(value: RatePolicyMap[keyof RatePolicyMap]): void;

  getUlRateUnit(): RateUnitMap[keyof RateUnitMap];
  setUlRateUnit(value: RateUnitMap[keyof RateUnitMap]): void;

  getDlRate(): number;
  setDlRate(value: number): void;

  getDlBucketSize(): number;
  setDlBucketSize(value: number): void;

  getDlRatePolicy(): RatePolicyMap[keyof RatePolicyMap];
  setDlRatePolicy(value: RatePolicyMap[keyof RatePolicyMap]): void;

  getDlRateUnit(): RateUnitMap[keyof RateUnitMap];
  setDlRateUnit(value: RateUnitMap[keyof RateUnitMap]): void;

  getAddGwMetadata(): boolean;
  setAddGwMetadata(value: boolean): void;

  getDevStatusReqFreq(): number;
  setDevStatusReqFreq(value: number): void;

  getReportDevStatusBattery(): boolean;
  setReportDevStatusBattery(value: boolean): void;

  getReportDevStatusMargin(): boolean;
  setReportDevStatusMargin(value: boolean): void;

  getDrMin(): number;
  setDrMin(value: number): void;

  getDrMax(): number;
  setDrMax(value: number): void;

  getChannelMask(): Uint8Array | string;
  getChannelMask_asU8(): Uint8Array;
  getChannelMask_asB64(): string;
  setChannelMask(value: Uint8Array | string): void;

  getPrAllowed(): boolean;
  setPrAllowed(value: boolean): void;

  getHrAllowed(): boolean;
  setHrAllowed(value: boolean): void;

  getRaAllowed(): boolean;
  setRaAllowed(value: boolean): void;

  getNwkGeoLoc(): boolean;
  setNwkGeoLoc(value: boolean): void;

  getTargetPer(): number;
  setTargetPer(value: number): void;

  getMinGwDiversity(): number;
  setMinGwDiversity(value: number): void;

  getGwsPrivate(): boolean;
  setGwsPrivate(value: boolean): void;

  getIsDisabled(): boolean;
  setIsDisabled(value: boolean): void;

  getAdrAlgorithmId(): string;
  setAdrAlgorithmId(value: string): void;

  getMinTxPowerIndex(): number;
  setMinTxPowerIndex(value: number): void;

  getMaxTxPowerIndex(): number;
  setMaxTxPowerIndex(value: number): void;

  getMaxNbTrans(): number;
  setMaxNbTrans(value: number): void;

  getMinNbTrans(): number;
  setMinNbTrans(value: number): void;

  getAllowRxConfirmed(): boolean;
  setAllowRxConfirmed(value: boolean): void;

  getAllowTxUnconfirmed(): boolean;
  setAllowTxUnconfirmed(value: boolean): void;

  getAllowTxConfirmed(): boolean;
  setAllowTxConfirmed(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ServiceProfile.AsObject;
  static toObject(includeInstance: boolean, msg: ServiceProfile): ServiceProfile.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ServiceProfile, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ServiceProfile;
  static deserializeBinaryFromReader(message: ServiceProfile, reader: jspb.BinaryReader): ServiceProfile;
}

export namespace ServiceProfile {
  export type AsObject = {
    id: Uint8Array | string,
    ulRate: number,
    ulBucketSize: number,
    ulRatePolicy: RatePolicyMap[keyof RatePolicyMap],
    ulRateUnit: RateUnitMap[keyof RateUnitMap],
    dlRate: number,
    dlBucketSize: number,
    dlRatePolicy: RatePolicyMap[keyof RatePolicyMap],
    dlRateUnit: RateUnitMap[keyof RateUnitMap],
    addGwMetadata: boolean,
    devStatusReqFreq: number,
    reportDevStatusBattery: boolean,
    reportDevStatusMargin: boolean,
    drMin: number,
    drMax: number,
    channelMask: Uint8Array | string,
    prAllowed: boolean,
    hrAllowed: boolean,
    raAllowed: boolean,
    nwkGeoLoc: boolean,
    targetPer: number,
    minGwDiversity: number,
    gwsPrivate: boolean,
    isDisabled: boolean,
    adrAlgorithmId: string,
    minTxPowerIndex: number,
    maxTxPowerIndex: number,
    maxNbTrans: number,
    minNbTrans: number,
    allowRxConfirmed: boolean,
    allowTxUnconfirmed: boolean,
    allowTxConfirmed: boolean,
  }
}

export class DeviceProfile extends jspb.Message {
  getId(): Uint8Array | string;
  getId_asU8(): Uint8Array;
  getId_asB64(): string;
  setId(value: Uint8Array | string): void;

  getSupportsClassB(): boolean;
  setSupportsClassB(value: boolean): void;

  getClassBTimeout(): number;
  setClassBTimeout(value: number): void;

  getPingSlotPeriod(): number;
  setPingSlotPeriod(value: number): void;

  getPingSlotDr(): number;
  setPingSlotDr(value: number): void;

  getPingSlotFreq(): number;
  setPingSlotFreq(value: number): void;

  getSupportsClassC(): boolean;
  setSupportsClassC(value: boolean): void;

  getClassCTimeout(): number;
  setClassCTimeout(value: number): void;

  getMacVersion(): string;
  setMacVersion(value: string): void;

  getRegParamsRevision(): string;
  setRegParamsRevision(value: string): void;

  getRxDelay1(): number;
  setRxDelay1(value: number): void;

  getRxDrOffset1(): number;
  setRxDrOffset1(value: number): void;

  getRxDatarate2(): number;
  setRxDatarate2(value: number): void;

  getRxFreq2(): number;
  setRxFreq2(value: number): void;

  clearFactoryPresetFreqsList(): void;
  getFactoryPresetFreqsList(): Array<number>;
  setFactoryPresetFreqsList(value: Array<number>): void;
  addFactoryPresetFreqs(value: number, index?: number): number;

  getMaxEirp(): number;
  setMaxEirp(value: number): void;

  getMaxDutyCycle(): number;
  setMaxDutyCycle(value: number): void;

  getSupportsJoin(): boolean;
  setSupportsJoin(value: boolean): void;

  getRfRegion(): string;
  setRfRegion(value: string): void;

  getSupports32bitFCnt(): boolean;
  setSupports32bitFCnt(value: boolean): void;

  getJoinAcceptDelay1(): number;
  setJoinAcceptDelay1(value: number): void;

  getJoinAcceptDelay2(): number;
  setJoinAcceptDelay2(value: number): void;

  getFCntAutomaticReset(): boolean;
  setFCntAutomaticReset(value: boolean): void;

  clearCmdSwitchesList(): void;
  getCmdSwitchesList(): Array<MacCommandSwitch>;
  setCmdSwitchesList(value: Array<MacCommandSwitch>): void;
  addCmdSwitches(value?: MacCommandSwitch, index?: number): MacCommandSwitch;

  getAdrAlgorithmId(): string;
  setAdrAlgorithmId(value: string): void;

  getRx1Delay(): number;
  setRx1Delay(value: number): void;

  getRx1DrOffset(): number;
  setRx1DrOffset(value: number): void;

  getRx2Datarate(): number;
  setRx2Datarate(value: number): void;

  getRx2Freq(): number;
  setRx2Freq(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeviceProfile.AsObject;
  static toObject(includeInstance: boolean, msg: DeviceProfile): DeviceProfile.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeviceProfile, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeviceProfile;
  static deserializeBinaryFromReader(message: DeviceProfile, reader: jspb.BinaryReader): DeviceProfile;
}

export namespace DeviceProfile {
  export type AsObject = {
    id: Uint8Array | string,
    supportsClassB: boolean,
    classBTimeout: number,
    pingSlotPeriod: number,
    pingSlotDr: number,
    pingSlotFreq: number,
    supportsClassC: boolean,
    classCTimeout: number,
    macVersion: string,
    regParamsRevision: string,
    rxDelay1: number,
    rxDrOffset1: number,
    rxDatarate2: number,
    rxFreq2: number,
    factoryPresetFreqsList: Array<number>,
    maxEirp: number,
    maxDutyCycle: number,
    supportsJoin: boolean,
    rfRegion: string,
    supports32bitFCnt: boolean,
    joinAcceptDelay1: number,
    joinAcceptDelay2: number,
    fCntAutomaticReset: boolean,
    cmdSwitchesList: Array<MacCommandSwitch.AsObject>,
    adrAlgorithmId: string,
    rx1Delay: number,
    rx1DrOffset: number,
    rx2Datarate: number,
    rx2Freq: number,
  }
}

export class RoutingProfile extends jspb.Message {
  getId(): Uint8Array | string;
  getId_asU8(): Uint8Array;
  getId_asB64(): string;
  setId(value: Uint8Array | string): void;

  getAsId(): string;
  setAsId(value: string): void;

  getCaCert(): string;
  setCaCert(value: string): void;

  getTlsCert(): string;
  setTlsCert(value: string): void;

  getTlsKey(): string;
  setTlsKey(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RoutingProfile.AsObject;
  static toObject(includeInstance: boolean, msg: RoutingProfile): RoutingProfile.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RoutingProfile, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RoutingProfile;
  static deserializeBinaryFromReader(message: RoutingProfile, reader: jspb.BinaryReader): RoutingProfile;
}

export namespace RoutingProfile {
  export type AsObject = {
    id: Uint8Array | string,
    asId: string,
    caCert: string,
    tlsCert: string,
    tlsKey: string,
  }
}

export class MacCommandSwitch extends jspb.Message {
  getCid(): number;
  setCid(value: number): void;

  getEnabled(): boolean;
  setEnabled(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MacCommandSwitch.AsObject;
  static toObject(includeInstance: boolean, msg: MacCommandSwitch): MacCommandSwitch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MacCommandSwitch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MacCommandSwitch;
  static deserializeBinaryFromReader(message: MacCommandSwitch, reader: jspb.BinaryReader): MacCommandSwitch;
}

export namespace MacCommandSwitch {
  export type AsObject = {
    cid: number,
    enabled: boolean,
  }
}

export interface RatePolicyMap {
  DROP: 0;
  MARK: 1;
}

export const RatePolicy: RatePolicyMap;

export interface RateUnitMap {
  HOUR: 0;
  DAY: 1;
  WEEK: 2;
  MONTH: 3;
  YEAR: 4;
}

export const RateUnit: RateUnitMap;

