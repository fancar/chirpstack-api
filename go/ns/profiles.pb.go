// Code generated by protoc-gen-go. DO NOT EDIT.
// source: ns/profiles.proto

package ns

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type RatePolicy int32

const (
	// Drop
	RatePolicy_Drop RatePolicy = 0
	// Mark
	RatePolicy_Mark RatePolicy = 1
)

var RatePolicy_name = map[int32]string{
	0: "Drop",
	1: "Mark",
}

var RatePolicy_value = map[string]int32{
	"Drop": 0,
	"Mark": 1,
}

func (x RatePolicy) String() string {
	return proto.EnumName(RatePolicy_name, int32(x))
}

func (RatePolicy) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_ee79be696a10f18b, []int{0}
}

type RateUnit int32

const (
	// Per Hour
	RateUnit_Hour RateUnit = 0
	// Per Day
	RateUnit_Day RateUnit = 1
	// Per Week
	RateUnit_Week RateUnit = 2
	// Per Month
	RateUnit_Month RateUnit = 3
	// Per Year
	RateUnit_Year RateUnit = 4
)

var RateUnit_name = map[int32]string{
	0: "Hour",
	1: "Day",
	2: "Week",
	3: "Month",
	4: "Year",
}

var RateUnit_value = map[string]int32{
	"Hour":  0,
	"Day":   1,
	"Week":  2,
	"Month": 3,
	"Year":  4,
}

func (x RateUnit) String() string {
	return proto.EnumName(RateUnit_name, int32(x))
}

func (RateUnit) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_ee79be696a10f18b, []int{1}
}

type ServiceProfile struct {
	// Service-profile ID.
	Id []byte `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	// Token bucket filling rate, including ACKs (packet/h).
	UlRate int32 `protobuf:"varint,2,opt,name=ul_rate,json=ulRate,proto3" json:"ul_rate,omitempty"`
	// Token bucket burst size.
	UlBucketSize uint32 `protobuf:"varint,3,opt,name=ul_bucket_size,json=ulBucketSize,proto3" json:"ul_bucket_size,omitempty"`
	// Drop or mark when exceeding ULRate.
	UlRatePolicy RatePolicy `protobuf:"varint,4,opt,name=ul_rate_policy,json=ulRatePolicy,proto3,enum=ns.RatePolicy" json:"ul_rate_policy,omitempty"`
	// Uplink rate unit (per hour, per day, per week, per month, per year)
	UlRateUnit RateUnit `protobuf:"varint,29,opt,name=ul_rate_unit,json=ulRateUnit,proto3,enum=ns.RateUnit" json:"ul_rate_unit,omitempty"`
	// Token bucket filling rate, including ACKs (packet/h).
	DlRate int32 `protobuf:"varint,5,opt,name=dl_rate,json=dlRate,proto3" json:"dl_rate,omitempty"`
	// Token bucket burst size.
	DlBucketSize uint32 `protobuf:"varint,6,opt,name=dl_bucket_size,json=dlBucketSize,proto3" json:"dl_bucket_size,omitempty"`
	// Drop or mark when exceeding DLRate.
	DlRatePolicy RatePolicy `protobuf:"varint,7,opt,name=dl_rate_policy,json=dlRatePolicy,proto3,enum=ns.RatePolicy" json:"dl_rate_policy,omitempty"`
	// Downlink rate unit (per hour, per day, per week, per month, per year)
	DlRateUnit RateUnit `protobuf:"varint,30,opt,name=dl_rate_unit,json=dlRateUnit,proto3,enum=ns.RateUnit" json:"dl_rate_unit,omitempty"`
	// GW metadata (RSSI, SNR, GW geoloc., etc.) are added to the packet sent to AS.
	AddGwMetadata bool `protobuf:"varint,8,opt,name=add_gw_metadata,json=addGwMetadata,proto3" json:"add_gw_metadata,omitempty"`
	// Frequency to initiate an End-Device status request (request/day).
	DevStatusReqFreq uint32 `protobuf:"varint,9,opt,name=dev_status_req_freq,json=devStatusReqFreq,proto3" json:"dev_status_req_freq,omitempty"`
	// Report End-Device battery level to AS.
	ReportDevStatusBattery bool `protobuf:"varint,10,opt,name=report_dev_status_battery,json=reportDevStatusBattery,proto3" json:"report_dev_status_battery,omitempty"`
	// Report End-Device margin to AS.
	ReportDevStatusMargin bool `protobuf:"varint,11,opt,name=report_dev_status_margin,json=reportDevStatusMargin,proto3" json:"report_dev_status_margin,omitempty"`
	// Minimum allowed data rate. Used for ADR.
	DrMin uint32 `protobuf:"varint,12,opt,name=dr_min,json=drMin,proto3" json:"dr_min,omitempty"`
	// Maximum allowed data rate. Used for ADR.
	DrMax uint32 `protobuf:"varint,13,opt,name=dr_max,json=drMax,proto3" json:"dr_max,omitempty"`
	// Channel mask. sNS does not have to obey (i.e., informative).
	ChannelMask []byte `protobuf:"bytes,14,opt,name=channel_mask,json=channelMask,proto3" json:"channel_mask,omitempty"`
	// Passive Roaming allowed.
	PrAllowed bool `protobuf:"varint,15,opt,name=pr_allowed,json=prAllowed,proto3" json:"pr_allowed,omitempty"`
	// Handover Roaming allowed.
	HrAllowed bool `protobuf:"varint,16,opt,name=hr_allowed,json=hrAllowed,proto3" json:"hr_allowed,omitempty"`
	// Roaming Activation allowed.
	RaAllowed bool `protobuf:"varint,17,opt,name=ra_allowed,json=raAllowed,proto3" json:"ra_allowed,omitempty"`
	// Enable network geolocation service.
	NwkGeoLoc bool `protobuf:"varint,18,opt,name=nwk_geo_loc,json=nwkGeoLoc,proto3" json:"nwk_geo_loc,omitempty"`
	// Target Packet Error Rate.
	TargetPer uint32 `protobuf:"varint,19,opt,name=target_per,json=targetPer,proto3" json:"target_per,omitempty"`
	// Minimum number of receiving GWs (informative).
	MinGwDiversity uint32 `protobuf:"varint,20,opt,name=min_gw_diversity,json=minGwDiversity,proto3" json:"min_gw_diversity,omitempty"`
	// Gateways under this service-profile are private.
	// This means that these gateways can only be used by devices under the
	// same service-profile.
	GwsPrivate bool `protobuf:"varint,21,opt,name=gws_private,json=gwsPrivate,proto3" json:"gws_private,omitempty"`
	// Service profile is disabled if true. UL DL packets droped and logged as DROP
	IsDisabled bool `protobuf:"varint,31,opt,name=is_disabled,json=isDisabled,proto3" json:"is_disabled,omitempty"`
	// ADR algorithm ID.
	// In case this is left blank, or is configured to a non-existing ADR
	// algorithm (plugin), then it falls back to 'default'.
	AdrAlgorithmId string `protobuf:"bytes,32,opt,name=adr_algorithm_id,json=adrAlgorithmId,proto3" json:"adr_algorithm_id,omitempty"`
	// Minimum TX power index that can't be overlaped by ADR.
	MinTxPowerIndex int32 `protobuf:"varint,33,opt,name=min_tx_power_index,json=minTxPowerIndex,proto3" json:"min_tx_power_index,omitempty"`
	// Maximum TX power index that can't be overlaped by ADR.
	// if adr=fixed - the value as fixed TxPowerIndex will be in use
	MaxTxPowerIndex int32 `protobuf:"varint,34,opt,name=max_tx_power_index,json=maxTxPowerIndex,proto3" json:"max_tx_power_index,omitempty"`
	// MAX NbTrans
	// the maximum number of transmissions.
	MaxNbTrans int32 `protobuf:"varint,35,opt,name=max_nb_trans,json=maxNbTrans,proto3" json:"max_nb_trans,omitempty"`
	// MIN NbTrans
	// the mininum number of transmissions.
	MinNbTrans int32 `protobuf:"varint,36,opt,name=min_nb_trans,json=minNbTrans,proto3" json:"min_nb_trans,omitempty"`
	// if true - allows processing confirmed uplinks
	AllowRxConfirmed bool `protobuf:"varint,37,opt,name=allow_rx_confirmed,json=allowRxConfirmed,proto3" json:"allow_rx_confirmed,omitempty"`
	// if true - allows processing unconfirmed downlinks
	AllowTxUnconfirmed bool `protobuf:"varint,38,opt,name=allow_tx_unconfirmed,json=allowTxUnconfirmed,proto3" json:"allow_tx_unconfirmed,omitempty"`
	// if true - allows processing confirmed downlinks
	AllowTxConfirmed     bool     `protobuf:"varint,39,opt,name=allow_tx_confirmed,json=allowTxConfirmed,proto3" json:"allow_tx_confirmed,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ServiceProfile) Reset()         { *m = ServiceProfile{} }
func (m *ServiceProfile) String() string { return proto.CompactTextString(m) }
func (*ServiceProfile) ProtoMessage()    {}
func (*ServiceProfile) Descriptor() ([]byte, []int) {
	return fileDescriptor_ee79be696a10f18b, []int{0}
}

func (m *ServiceProfile) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ServiceProfile.Unmarshal(m, b)
}
func (m *ServiceProfile) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ServiceProfile.Marshal(b, m, deterministic)
}
func (m *ServiceProfile) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ServiceProfile.Merge(m, src)
}
func (m *ServiceProfile) XXX_Size() int {
	return xxx_messageInfo_ServiceProfile.Size(m)
}
func (m *ServiceProfile) XXX_DiscardUnknown() {
	xxx_messageInfo_ServiceProfile.DiscardUnknown(m)
}

var xxx_messageInfo_ServiceProfile proto.InternalMessageInfo

func (m *ServiceProfile) GetId() []byte {
	if m != nil {
		return m.Id
	}
	return nil
}

func (m *ServiceProfile) GetUlRate() int32 {
	if m != nil {
		return m.UlRate
	}
	return 0
}

func (m *ServiceProfile) GetUlBucketSize() uint32 {
	if m != nil {
		return m.UlBucketSize
	}
	return 0
}

func (m *ServiceProfile) GetUlRatePolicy() RatePolicy {
	if m != nil {
		return m.UlRatePolicy
	}
	return RatePolicy_Drop
}

func (m *ServiceProfile) GetUlRateUnit() RateUnit {
	if m != nil {
		return m.UlRateUnit
	}
	return RateUnit_Hour
}

func (m *ServiceProfile) GetDlRate() int32 {
	if m != nil {
		return m.DlRate
	}
	return 0
}

func (m *ServiceProfile) GetDlBucketSize() uint32 {
	if m != nil {
		return m.DlBucketSize
	}
	return 0
}

func (m *ServiceProfile) GetDlRatePolicy() RatePolicy {
	if m != nil {
		return m.DlRatePolicy
	}
	return RatePolicy_Drop
}

func (m *ServiceProfile) GetDlRateUnit() RateUnit {
	if m != nil {
		return m.DlRateUnit
	}
	return RateUnit_Hour
}

func (m *ServiceProfile) GetAddGwMetadata() bool {
	if m != nil {
		return m.AddGwMetadata
	}
	return false
}

func (m *ServiceProfile) GetDevStatusReqFreq() uint32 {
	if m != nil {
		return m.DevStatusReqFreq
	}
	return 0
}

func (m *ServiceProfile) GetReportDevStatusBattery() bool {
	if m != nil {
		return m.ReportDevStatusBattery
	}
	return false
}

func (m *ServiceProfile) GetReportDevStatusMargin() bool {
	if m != nil {
		return m.ReportDevStatusMargin
	}
	return false
}

func (m *ServiceProfile) GetDrMin() uint32 {
	if m != nil {
		return m.DrMin
	}
	return 0
}

func (m *ServiceProfile) GetDrMax() uint32 {
	if m != nil {
		return m.DrMax
	}
	return 0
}

func (m *ServiceProfile) GetChannelMask() []byte {
	if m != nil {
		return m.ChannelMask
	}
	return nil
}

func (m *ServiceProfile) GetPrAllowed() bool {
	if m != nil {
		return m.PrAllowed
	}
	return false
}

func (m *ServiceProfile) GetHrAllowed() bool {
	if m != nil {
		return m.HrAllowed
	}
	return false
}

func (m *ServiceProfile) GetRaAllowed() bool {
	if m != nil {
		return m.RaAllowed
	}
	return false
}

func (m *ServiceProfile) GetNwkGeoLoc() bool {
	if m != nil {
		return m.NwkGeoLoc
	}
	return false
}

func (m *ServiceProfile) GetTargetPer() uint32 {
	if m != nil {
		return m.TargetPer
	}
	return 0
}

func (m *ServiceProfile) GetMinGwDiversity() uint32 {
	if m != nil {
		return m.MinGwDiversity
	}
	return 0
}

func (m *ServiceProfile) GetGwsPrivate() bool {
	if m != nil {
		return m.GwsPrivate
	}
	return false
}

func (m *ServiceProfile) GetIsDisabled() bool {
	if m != nil {
		return m.IsDisabled
	}
	return false
}

func (m *ServiceProfile) GetAdrAlgorithmId() string {
	if m != nil {
		return m.AdrAlgorithmId
	}
	return ""
}

func (m *ServiceProfile) GetMinTxPowerIndex() int32 {
	if m != nil {
		return m.MinTxPowerIndex
	}
	return 0
}

func (m *ServiceProfile) GetMaxTxPowerIndex() int32 {
	if m != nil {
		return m.MaxTxPowerIndex
	}
	return 0
}

func (m *ServiceProfile) GetMaxNbTrans() int32 {
	if m != nil {
		return m.MaxNbTrans
	}
	return 0
}

func (m *ServiceProfile) GetMinNbTrans() int32 {
	if m != nil {
		return m.MinNbTrans
	}
	return 0
}

func (m *ServiceProfile) GetAllowRxConfirmed() bool {
	if m != nil {
		return m.AllowRxConfirmed
	}
	return false
}

func (m *ServiceProfile) GetAllowTxUnconfirmed() bool {
	if m != nil {
		return m.AllowTxUnconfirmed
	}
	return false
}

func (m *ServiceProfile) GetAllowTxConfirmed() bool {
	if m != nil {
		return m.AllowTxConfirmed
	}
	return false
}

type DeviceProfile struct {
	// Device-profile ID.
	Id []byte `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	// End-Device supports Class B.
	SupportsClassB bool `protobuf:"varint,2,opt,name=supports_class_b,json=supportsClassB,proto3" json:"supports_class_b,omitempty"`
	// Maximum delay for the End-Device to answer a MAC request or a confirmed DL frame (mandatory if class B mode supported).
	ClassBTimeout uint32 `protobuf:"varint,3,opt,name=class_b_timeout,json=classBTimeout,proto3" json:"class_b_timeout,omitempty"`
	// Mandatory if class B mode supported.
	PingSlotPeriod uint32 `protobuf:"varint,4,opt,name=ping_slot_period,json=pingSlotPeriod,proto3" json:"ping_slot_period,omitempty"`
	// Mandatory if class B mode supported.
	PingSlotDr uint32 `protobuf:"varint,5,opt,name=ping_slot_dr,json=pingSlotDr,proto3" json:"ping_slot_dr,omitempty"`
	// Mandatory if class B mode supported.
	PingSlotFreq uint32 `protobuf:"varint,6,opt,name=ping_slot_freq,json=pingSlotFreq,proto3" json:"ping_slot_freq,omitempty"`
	// End-Device supports Class C.
	SupportsClassC bool `protobuf:"varint,7,opt,name=supports_class_c,json=supportsClassC,proto3" json:"supports_class_c,omitempty"`
	// Maximum delay for the End-Device to answer a MAC request or a confirmed DL frame (mandatory if class C mode supported).
	ClassCTimeout uint32 `protobuf:"varint,8,opt,name=class_c_timeout,json=classCTimeout,proto3" json:"class_c_timeout,omitempty"`
	// Version of the LoRaWAN supported by the End-Device.
	MacVersion string `protobuf:"bytes,9,opt,name=mac_version,json=macVersion,proto3" json:"mac_version,omitempty"`
	// Revision of the Regional Parameters document supported by the End-Device.
	RegParamsRevision string `protobuf:"bytes,10,opt,name=reg_params_revision,json=regParamsRevision,proto3" json:"reg_params_revision,omitempty"`
	// Class A RX1 delay (For ABP initialization  only! mandatory for ABP).
	RxDelay_1 uint32 `protobuf:"varint,11,opt,name=rx_delay_1,json=rxDelay1,proto3" json:"rx_delay_1,omitempty"`
	// RX1 data rate offset (For ABP initialization  only! mandatory for ABP).
	RxDrOffset_1 uint32 `protobuf:"varint,12,opt,name=rx_dr_offset_1,json=rxDrOffset1,proto3" json:"rx_dr_offset_1,omitempty"`
	// RX2 data rate (For ABP initialization  only! mandatory for ABP).
	RxDatarate_2 uint32 `protobuf:"varint,13,opt,name=rx_datarate_2,json=rxDatarate2,proto3" json:"rx_datarate_2,omitempty"`
	// RX2 channel frequency (For ABP initialization  only! mandatory for ABP).
	RxFreq_2 uint32 `protobuf:"varint,14,opt,name=rx_freq_2,json=rxFreq2,proto3" json:"rx_freq_2,omitempty"`
	// List of factory-preset frequencies (mandatory for ABP).
	FactoryPresetFreqs []uint32 `protobuf:"varint,15,rep,packed,name=factory_preset_freqs,json=factoryPresetFreqs,proto3" json:"factory_preset_freqs,omitempty"`
	// Deprecated. Moved to SP. Maximum EIRP supported by the End-Device.
	MaxEirp uint32 `protobuf:"varint,16,opt,name=max_eirp,json=maxEirp,proto3" json:"max_eirp,omitempty"`
	// Maximum duty cycle supported by the End-Device.
	MaxDutyCycle uint32 `protobuf:"varint,17,opt,name=max_duty_cycle,json=maxDutyCycle,proto3" json:"max_duty_cycle,omitempty"`
	// End-Device supports Join (OTAA) or not (ABP).
	SupportsJoin bool `protobuf:"varint,18,opt,name=supports_join,json=supportsJoin,proto3" json:"supports_join,omitempty"`
	// RF region name.
	RfRegion string `protobuf:"bytes,19,opt,name=rf_region,json=rfRegion,proto3" json:"rf_region,omitempty"`
	// End-Device uses 32bit FCnt (mandatory for LoRaWAN 1.0 End-Device).
	Supports_32BitFCnt bool `protobuf:"varint,20,opt,name=supports_32bit_f_cnt,json=supports32bitFCnt,proto3" json:"supports_32bit_f_cnt,omitempty"`
	// delay between the end of join request message
	// and start of RX1 window to recieve a Join Accept
	// default 5000ms
	JoinAcceptDelay_1 uint32 `protobuf:"varint,21,opt,name=join_accept_delay_1,json=joinAcceptDelay1,proto3" json:"join_accept_delay_1,omitempty"`
	// delay between the end of join request message
	// and start of RX2 window to recieve a Join Accept
	// default 6000ms
	JoinAcceptDelay_2 uint32 `protobuf:"varint,22,opt,name=join_accept_delay_2,json=joinAcceptDelay2,proto3" json:"join_accept_delay_2,omitempty"`
	// allow autoreset for low counters recieved
	// (for ABP devices only)
	FCntAutomaticReset bool                `protobuf:"varint,23,opt,name=f_cnt_automatic_reset,json=fCntAutomaticReset,proto3" json:"f_cnt_automatic_reset,omitempty"`
	CmdSwitches        []*MacCommandSwitch `protobuf:"bytes,24,rep,name=cmd_switches,json=cmdSwitches,proto3" json:"cmd_switches,omitempty"`
	// Deprecated. Moved to SP.
	// TODO: remove it
	AdrAlgorithmId string `protobuf:"bytes,25,opt,name=adr_algorithm_id,json=adrAlgorithmId,proto3" json:"adr_algorithm_id,omitempty"`
	// Class A RX1 delay. If not set (-1) - default value from NS cfg in use
	// RX2 delay will be +1s to the rx1_delay
	Rx1Delay int32 `protobuf:"varint,26,opt,name=rx1_delay,json=rx1Delay,proto3" json:"rx1_delay,omitempty"`
	// RX1 data rate offset. If not set (-1) - default value from NS cfg in use
	Rx1DrOffset int32 `protobuf:"varint,27,opt,name=rx1_dr_offset,json=rx1DrOffset,proto3" json:"rx1_dr_offset,omitempty"`
	// RX2 data rate. If not set (-1) - default value from NS cfg in use
	Rx2Datarate int32 `protobuf:"varint,28,opt,name=rx2_datarate,json=rx2Datarate,proto3" json:"rx2_datarate,omitempty"`
	// RX2 channel frequency. If not set (-1) - default value from NS cfg in use
	Rx2Freq              int32    `protobuf:"varint,29,opt,name=rx2_freq,json=rx2Freq,proto3" json:"rx2_freq,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *DeviceProfile) Reset()         { *m = DeviceProfile{} }
func (m *DeviceProfile) String() string { return proto.CompactTextString(m) }
func (*DeviceProfile) ProtoMessage()    {}
func (*DeviceProfile) Descriptor() ([]byte, []int) {
	return fileDescriptor_ee79be696a10f18b, []int{1}
}

func (m *DeviceProfile) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_DeviceProfile.Unmarshal(m, b)
}
func (m *DeviceProfile) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_DeviceProfile.Marshal(b, m, deterministic)
}
func (m *DeviceProfile) XXX_Merge(src proto.Message) {
	xxx_messageInfo_DeviceProfile.Merge(m, src)
}
func (m *DeviceProfile) XXX_Size() int {
	return xxx_messageInfo_DeviceProfile.Size(m)
}
func (m *DeviceProfile) XXX_DiscardUnknown() {
	xxx_messageInfo_DeviceProfile.DiscardUnknown(m)
}

var xxx_messageInfo_DeviceProfile proto.InternalMessageInfo

func (m *DeviceProfile) GetId() []byte {
	if m != nil {
		return m.Id
	}
	return nil
}

func (m *DeviceProfile) GetSupportsClassB() bool {
	if m != nil {
		return m.SupportsClassB
	}
	return false
}

func (m *DeviceProfile) GetClassBTimeout() uint32 {
	if m != nil {
		return m.ClassBTimeout
	}
	return 0
}

func (m *DeviceProfile) GetPingSlotPeriod() uint32 {
	if m != nil {
		return m.PingSlotPeriod
	}
	return 0
}

func (m *DeviceProfile) GetPingSlotDr() uint32 {
	if m != nil {
		return m.PingSlotDr
	}
	return 0
}

func (m *DeviceProfile) GetPingSlotFreq() uint32 {
	if m != nil {
		return m.PingSlotFreq
	}
	return 0
}

func (m *DeviceProfile) GetSupportsClassC() bool {
	if m != nil {
		return m.SupportsClassC
	}
	return false
}

func (m *DeviceProfile) GetClassCTimeout() uint32 {
	if m != nil {
		return m.ClassCTimeout
	}
	return 0
}

func (m *DeviceProfile) GetMacVersion() string {
	if m != nil {
		return m.MacVersion
	}
	return ""
}

func (m *DeviceProfile) GetRegParamsRevision() string {
	if m != nil {
		return m.RegParamsRevision
	}
	return ""
}

func (m *DeviceProfile) GetRxDelay_1() uint32 {
	if m != nil {
		return m.RxDelay_1
	}
	return 0
}

func (m *DeviceProfile) GetRxDrOffset_1() uint32 {
	if m != nil {
		return m.RxDrOffset_1
	}
	return 0
}

func (m *DeviceProfile) GetRxDatarate_2() uint32 {
	if m != nil {
		return m.RxDatarate_2
	}
	return 0
}

func (m *DeviceProfile) GetRxFreq_2() uint32 {
	if m != nil {
		return m.RxFreq_2
	}
	return 0
}

func (m *DeviceProfile) GetFactoryPresetFreqs() []uint32 {
	if m != nil {
		return m.FactoryPresetFreqs
	}
	return nil
}

func (m *DeviceProfile) GetMaxEirp() uint32 {
	if m != nil {
		return m.MaxEirp
	}
	return 0
}

func (m *DeviceProfile) GetMaxDutyCycle() uint32 {
	if m != nil {
		return m.MaxDutyCycle
	}
	return 0
}

func (m *DeviceProfile) GetSupportsJoin() bool {
	if m != nil {
		return m.SupportsJoin
	}
	return false
}

func (m *DeviceProfile) GetRfRegion() string {
	if m != nil {
		return m.RfRegion
	}
	return ""
}

func (m *DeviceProfile) GetSupports_32BitFCnt() bool {
	if m != nil {
		return m.Supports_32BitFCnt
	}
	return false
}

func (m *DeviceProfile) GetJoinAcceptDelay_1() uint32 {
	if m != nil {
		return m.JoinAcceptDelay_1
	}
	return 0
}

func (m *DeviceProfile) GetJoinAcceptDelay_2() uint32 {
	if m != nil {
		return m.JoinAcceptDelay_2
	}
	return 0
}

func (m *DeviceProfile) GetFCntAutomaticReset() bool {
	if m != nil {
		return m.FCntAutomaticReset
	}
	return false
}

func (m *DeviceProfile) GetCmdSwitches() []*MacCommandSwitch {
	if m != nil {
		return m.CmdSwitches
	}
	return nil
}

func (m *DeviceProfile) GetAdrAlgorithmId() string {
	if m != nil {
		return m.AdrAlgorithmId
	}
	return ""
}

func (m *DeviceProfile) GetRx1Delay() int32 {
	if m != nil {
		return m.Rx1Delay
	}
	return 0
}

func (m *DeviceProfile) GetRx1DrOffset() int32 {
	if m != nil {
		return m.Rx1DrOffset
	}
	return 0
}

func (m *DeviceProfile) GetRx2Datarate() int32 {
	if m != nil {
		return m.Rx2Datarate
	}
	return 0
}

func (m *DeviceProfile) GetRx2Freq() int32 {
	if m != nil {
		return m.Rx2Freq
	}
	return 0
}

type RoutingProfile struct {
	// ID of the routing profile.
	Id []byte `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	// Application-server ID.
	AsId string `protobuf:"bytes,2,opt,name=as_id,json=asId,proto3" json:"as_id,omitempty"`
	// CA certificate for connecting to the AS.
	CaCert string `protobuf:"bytes,3,opt,name=ca_cert,json=caCert,proto3" json:"ca_cert,omitempty"`
	// TLS certificate for connecting to the AS.
	TlsCert string `protobuf:"bytes,4,opt,name=tls_cert,json=tlsCert,proto3" json:"tls_cert,omitempty"`
	// TLS key for connecting to the AS.
	// Note: when retrieving the routing-profile, the tls_key is not returned
	// for security reasons. When updating the routing-profile, an empty tls_key
	// does not clear the certificate, unless the tls_cert is also left blank.
	TlsKey               string   `protobuf:"bytes,5,opt,name=tls_key,json=tlsKey,proto3" json:"tls_key,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *RoutingProfile) Reset()         { *m = RoutingProfile{} }
func (m *RoutingProfile) String() string { return proto.CompactTextString(m) }
func (*RoutingProfile) ProtoMessage()    {}
func (*RoutingProfile) Descriptor() ([]byte, []int) {
	return fileDescriptor_ee79be696a10f18b, []int{2}
}

func (m *RoutingProfile) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_RoutingProfile.Unmarshal(m, b)
}
func (m *RoutingProfile) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_RoutingProfile.Marshal(b, m, deterministic)
}
func (m *RoutingProfile) XXX_Merge(src proto.Message) {
	xxx_messageInfo_RoutingProfile.Merge(m, src)
}
func (m *RoutingProfile) XXX_Size() int {
	return xxx_messageInfo_RoutingProfile.Size(m)
}
func (m *RoutingProfile) XXX_DiscardUnknown() {
	xxx_messageInfo_RoutingProfile.DiscardUnknown(m)
}

var xxx_messageInfo_RoutingProfile proto.InternalMessageInfo

func (m *RoutingProfile) GetId() []byte {
	if m != nil {
		return m.Id
	}
	return nil
}

func (m *RoutingProfile) GetAsId() string {
	if m != nil {
		return m.AsId
	}
	return ""
}

func (m *RoutingProfile) GetCaCert() string {
	if m != nil {
		return m.CaCert
	}
	return ""
}

func (m *RoutingProfile) GetTlsCert() string {
	if m != nil {
		return m.TlsCert
	}
	return ""
}

func (m *RoutingProfile) GetTlsKey() string {
	if m != nil {
		return m.TlsKey
	}
	return ""
}

type MacCommandSwitch struct {
	// Command identifier (specified by the LoRaWAN specs).
	// see https://github.com/brocaar/lorawan/blob/master/mac_commands.go
	// for example 10 is 0x0A which is DLChannelReq command
	Cid uint32 `protobuf:"varint,1,opt,name=cid,proto3" json:"cid,omitempty"`
	// if true the MACcommand with the identifier will be allowed
	Enabled              bool     `protobuf:"varint,2,opt,name=enabled,proto3" json:"enabled,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *MacCommandSwitch) Reset()         { *m = MacCommandSwitch{} }
func (m *MacCommandSwitch) String() string { return proto.CompactTextString(m) }
func (*MacCommandSwitch) ProtoMessage()    {}
func (*MacCommandSwitch) Descriptor() ([]byte, []int) {
	return fileDescriptor_ee79be696a10f18b, []int{3}
}

func (m *MacCommandSwitch) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_MacCommandSwitch.Unmarshal(m, b)
}
func (m *MacCommandSwitch) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_MacCommandSwitch.Marshal(b, m, deterministic)
}
func (m *MacCommandSwitch) XXX_Merge(src proto.Message) {
	xxx_messageInfo_MacCommandSwitch.Merge(m, src)
}
func (m *MacCommandSwitch) XXX_Size() int {
	return xxx_messageInfo_MacCommandSwitch.Size(m)
}
func (m *MacCommandSwitch) XXX_DiscardUnknown() {
	xxx_messageInfo_MacCommandSwitch.DiscardUnknown(m)
}

var xxx_messageInfo_MacCommandSwitch proto.InternalMessageInfo

func (m *MacCommandSwitch) GetCid() uint32 {
	if m != nil {
		return m.Cid
	}
	return 0
}

func (m *MacCommandSwitch) GetEnabled() bool {
	if m != nil {
		return m.Enabled
	}
	return false
}

func init() {
	proto.RegisterEnum("ns.RatePolicy", RatePolicy_name, RatePolicy_value)
	proto.RegisterEnum("ns.RateUnit", RateUnit_name, RateUnit_value)
	proto.RegisterType((*ServiceProfile)(nil), "ns.ServiceProfile")
	proto.RegisterType((*DeviceProfile)(nil), "ns.DeviceProfile")
	proto.RegisterType((*RoutingProfile)(nil), "ns.RoutingProfile")
	proto.RegisterType((*MacCommandSwitch)(nil), "ns.MacCommandSwitch")
}

func init() {
	proto.RegisterFile("ns/profiles.proto", fileDescriptor_ee79be696a10f18b)
}

var fileDescriptor_ee79be696a10f18b = []byte{
	// 1421 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x7c, 0x56, 0x5f, 0x6f, 0xdb, 0xbe,
	0x15, 0xad, 0xf3, 0xcf, 0x36, 0x6d, 0x39, 0x0e, 0x93, 0xb4, 0xea, 0x7f, 0x37, 0xed, 0x3a, 0xa3,
	0x5b, 0x9d, 0xd9, 0x1d, 0x50, 0x0c, 0x18, 0x06, 0x24, 0xf6, 0xda, 0x75, 0x5b, 0x36, 0x43, 0x49,
	0x37, 0x6c, 0x2f, 0x04, 0x2d, 0xd2, 0x36, 0x67, 0x89, 0x54, 0x48, 0x2a, 0x96, 0xfb, 0xb8, 0x8f,
	0x3a, 0xec, 0x83, 0x0c, 0xbc, 0x92, 0xec, 0x34, 0xcd, 0x7e, 0x6f, 0xd2, 0x39, 0xe7, 0x92, 0x87,
	0x57, 0x57, 0x47, 0x42, 0x07, 0xd2, 0x9c, 0x26, 0x5a, 0x4d, 0x45, 0xc4, 0x4d, 0x2f, 0xd1, 0xca,
	0x2a, 0xbc, 0x25, 0xcd, 0xc9, 0x7f, 0xeb, 0xa8, 0x75, 0xc9, 0xf5, 0x8d, 0x08, 0xf9, 0x38, 0x67,
	0x71, 0x0b, 0x6d, 0x09, 0xe6, 0x57, 0x3a, 0x95, 0x6e, 0x33, 0xd8, 0x12, 0x0c, 0x3f, 0x42, 0xd5,
	0x34, 0x22, 0x9a, 0x5a, 0xee, 0x6f, 0x75, 0x2a, 0xdd, 0xdd, 0x60, 0x2f, 0x8d, 0x02, 0x6a, 0x39,
	0x7e, 0x83, 0x5a, 0x69, 0x44, 0x26, 0x69, 0xb8, 0xe0, 0x96, 0x18, 0xf1, 0x8d, 0xfb, 0xdb, 0x9d,
	0x4a, 0xd7, 0x0b, 0x9a, 0x69, 0x74, 0x0e, 0xe0, 0xa5, 0xf8, 0xc6, 0xf1, 0xaf, 0x41, 0xe5, 0xca,
	0x49, 0xa2, 0x22, 0x11, 0xae, 0xfc, 0x9d, 0x4e, 0xa5, 0xdb, 0x1a, 0xb4, 0x7a, 0xd2, 0xf4, 0xdc,
	0x3a, 0x63, 0x40, 0x5d, 0xd5, 0xe6, 0x0e, 0xf7, 0x50, 0xb3, 0xac, 0x4a, 0xa5, 0xb0, 0xfe, 0x73,
	0xa8, 0x69, 0x96, 0x35, 0x5f, 0xa5, 0xb0, 0x01, 0xca, 0x2b, 0xdc, 0xb5, 0x33, 0xc9, 0x0a, 0x93,
	0xbb, 0xb9, 0x49, 0xb6, 0x36, 0xc9, 0xbe, 0x37, 0xb9, 0x97, 0x9b, 0x64, 0x77, 0x4c, 0xb2, 0xef,
	0x4d, 0x56, 0xef, 0x37, 0xc9, 0xee, 0x98, 0x64, 0xb7, 0x4d, 0xbe, 0xb8, 0xcf, 0x24, 0xdb, 0x98,
	0x7c, 0x8b, 0xf6, 0x29, 0x63, 0x64, 0xb6, 0x24, 0x31, 0xb7, 0x94, 0x51, 0x4b, 0xfd, 0x5a, 0xa7,
	0xd2, 0xad, 0x05, 0x1e, 0x65, 0xec, 0xf3, 0xf2, 0xa2, 0x00, 0xf1, 0x7b, 0x74, 0xc8, 0xf8, 0x0d,
	0x31, 0x96, 0xda, 0xd4, 0x10, 0xcd, 0xaf, 0xc9, 0x54, 0xf3, 0x6b, 0xbf, 0x0e, 0xc6, 0xdb, 0x8c,
	0xdf, 0x5c, 0x02, 0x13, 0xf0, 0xeb, 0x4f, 0x9a, 0x5f, 0xe3, 0xdf, 0xa0, 0xc7, 0x9a, 0x27, 0x4a,
	0x5b, 0x72, 0xab, 0x6a, 0x42, 0xad, 0xe5, 0x7a, 0xe5, 0x23, 0xd8, 0xe0, 0x61, 0x2e, 0x18, 0x95,
	0xa5, 0xe7, 0x39, 0x8b, 0x3f, 0x22, 0xff, 0xc7, 0xd2, 0x98, 0xea, 0x99, 0x90, 0x7e, 0x03, 0x2a,
	0x8f, 0xef, 0x54, 0x5e, 0x00, 0x89, 0x8f, 0xd1, 0x1e, 0xd3, 0x24, 0x16, 0xd2, 0x6f, 0x82, 0xab,
	0x5d, 0xa6, 0x2f, 0x36, 0x30, 0xcd, 0x7c, 0x6f, 0x0d, 0xd3, 0x0c, 0xbf, 0x42, 0xcd, 0x70, 0x4e,
	0xa5, 0xe4, 0x11, 0x89, 0xa9, 0x59, 0xf8, 0x2d, 0x18, 0xae, 0x46, 0x81, 0x5d, 0x50, 0xb3, 0xc0,
	0xcf, 0x11, 0x4a, 0x34, 0xa1, 0x51, 0xa4, 0x96, 0x9c, 0xf9, 0xfb, 0xb0, 0x77, 0x3d, 0xd1, 0x67,
	0x39, 0xe0, 0xe8, 0xf9, 0x86, 0x6e, 0xe7, 0xf4, 0xfc, 0x36, 0xad, 0xe9, 0x9a, 0x3e, 0xc8, 0x69,
	0x4d, 0x4b, 0xfa, 0x05, 0x6a, 0xc8, 0xe5, 0x82, 0xcc, 0xb8, 0x22, 0x91, 0x0a, 0x7d, 0x9c, 0xf3,
	0x72, 0xb9, 0xf8, 0xcc, 0xd5, 0x9f, 0x55, 0xe8, 0xca, 0x2d, 0xd5, 0x33, 0x6e, 0x49, 0xc2, 0xb5,
	0x7f, 0x08, 0xd6, 0xeb, 0x39, 0x32, 0xe6, 0x1a, 0x77, 0x51, 0x3b, 0x16, 0xd2, 0x3d, 0x37, 0x26,
	0x6e, 0xb8, 0x36, 0xc2, 0xae, 0xfc, 0x23, 0x10, 0xb5, 0x62, 0x21, 0x3f, 0x2f, 0x47, 0x25, 0x8a,
	0x5f, 0xa2, 0xc6, 0x6c, 0x69, 0x48, 0xa2, 0xc5, 0x8d, 0x1b, 0xc5, 0x63, 0xd8, 0x08, 0xcd, 0x96,
	0x66, 0x9c, 0x23, 0x4e, 0x20, 0x0c, 0x61, 0xc2, 0xd0, 0x49, 0xc4, 0x99, 0xff, 0x32, 0x17, 0x08,
	0x33, 0x2a, 0x10, 0xb7, 0x17, 0x65, 0xee, 0xa4, 0x33, 0xa5, 0x85, 0x9d, 0xc7, 0x44, 0x30, 0xbf,
	0xd3, 0xa9, 0x74, 0xeb, 0x41, 0x8b, 0x32, 0x7d, 0x56, 0xc2, 0x5f, 0x18, 0xfe, 0x05, 0xc2, 0xce,
	0x95, 0xcd, 0x48, 0xa2, 0x96, 0x5c, 0x13, 0x21, 0x19, 0xcf, 0xfc, 0x57, 0x30, 0xfd, 0xfb, 0xb1,
	0x90, 0x57, 0xd9, 0xd8, 0xe1, 0x5f, 0x1c, 0x0c, 0x62, 0x9a, 0xdd, 0x15, 0x9f, 0x14, 0x62, 0x9a,
	0x7d, 0x27, 0xee, 0xa0, 0xa6, 0x13, 0xcb, 0x09, 0xb1, 0x9a, 0x4a, 0xe3, 0xbf, 0x06, 0x19, 0x8a,
	0x69, 0xf6, 0x97, 0xc9, 0x95, 0x43, 0x40, 0x21, 0xe4, 0x46, 0xf1, 0xa6, 0x50, 0x08, 0x59, 0x2a,
	0x7e, 0x89, 0x30, 0x3c, 0x0e, 0xa2, 0x33, 0x12, 0x2a, 0x39, 0x15, 0x3a, 0xe6, 0xcc, 0xff, 0x19,
	0x9c, 0xb7, 0x0d, 0x4c, 0x90, 0x0d, 0x4b, 0x1c, 0xff, 0x0a, 0x1d, 0xe5, 0x6a, 0x9b, 0x91, 0x54,
	0x6e, 0xf4, 0x6f, 0x41, 0x9f, 0xaf, 0x74, 0x95, 0x7d, 0xdd, 0x30, 0x9b, 0xf5, 0xed, 0xed, 0xf5,
	0x7f, 0x7e, 0x6b, 0xfd, 0xab, 0xcd, 0xfa, 0x27, 0xff, 0xa9, 0x21, 0x6f, 0xc4, 0x7f, 0x2a, 0xe5,
	0xba, 0xa8, 0x6d, 0xd2, 0xc4, 0x8d, 0xba, 0x21, 0x61, 0x44, 0x8d, 0x21, 0x13, 0x88, 0xbb, 0x5a,
	0xd0, 0x2a, 0xf1, 0xa1, 0x83, 0xcf, 0xdd, 0x5b, 0x5c, 0x08, 0x88, 0x15, 0x31, 0x57, 0xa9, 0x2d,
	0x72, 0xcf, 0x03, 0xf8, 0xfc, 0x2a, 0x07, 0xdd, 0x8a, 0x89, 0x90, 0x33, 0x62, 0x22, 0x05, 0x73,
	0x25, 0x14, 0x83, 0xe8, 0xf3, 0x82, 0x96, 0xc3, 0x2f, 0x23, 0xe5, 0x86, 0x4b, 0x28, 0xe6, 0xba,
	0xb9, 0x51, 0x32, 0x0d, 0x09, 0xe6, 0x05, 0xa8, 0x54, 0x8d, 0xb4, 0x4b, 0xb1, 0x8d, 0x02, 0xc2,
	0xa0, 0x48, 0xb1, 0x52, 0x03, 0x41, 0xf0, 0xe3, 0x19, 0x42, 0xc8, 0xb1, 0xbb, 0x67, 0x18, 0x6e,
	0xce, 0x10, 0xae, 0xcf, 0x50, 0xbb, 0x75, 0x86, 0x61, 0x79, 0x86, 0x97, 0xa8, 0x11, 0xd3, 0x90,
	0xc0, 0x78, 0x2b, 0x09, 0x09, 0x54, 0x77, 0x83, 0x10, 0xfe, 0x2d, 0x47, 0x70, 0x0f, 0x1d, 0x6a,
	0x3e, 0x23, 0x09, 0xd5, 0x34, 0x76, 0x51, 0x75, 0x23, 0x40, 0x88, 0x40, 0x78, 0xa0, 0xf9, 0x6c,
	0x0c, 0x4c, 0x50, 0x10, 0xf8, 0x19, 0x42, 0x3a, 0x23, 0x8c, 0x47, 0x74, 0x45, 0xfa, 0x10, 0x31,
	0x5e, 0x50, 0xd3, 0xd9, 0xc8, 0x01, 0x7d, 0xfc, 0x1a, 0xb5, 0x1c, 0xab, 0x89, 0x9a, 0x4e, 0x0d,
	0xb7, 0xa4, 0x5f, 0xa4, 0x4b, 0x43, 0x67, 0x23, 0xfd, 0x57, 0xc0, 0xfa, 0xf8, 0x04, 0x79, 0x4e,
	0x44, 0x2d, 0x85, 0xe4, 0x1d, 0x14, 0x51, 0xe3, 0x34, 0x05, 0x36, 0xc0, 0x4f, 0x50, 0x5d, 0x67,
	0xd0, 0x28, 0x32, 0x80, 0xb4, 0xf1, 0x82, 0xaa, 0xce, 0x5c, 0x93, 0x06, 0x6e, 0xd6, 0xa6, 0x34,
	0xb4, 0x4a, 0xaf, 0x48, 0xa2, 0xb9, 0xdb, 0xc6, 0xe9, 0x8c, 0xbf, 0xdf, 0xd9, 0xee, 0x7a, 0x01,
	0x2e, 0xb8, 0x31, 0x50, 0xae, 0xc2, 0xe0, 0xc7, 0xa8, 0xe6, 0xde, 0x07, 0x2e, 0x74, 0x02, 0xd1,
	0xe3, 0x05, 0xd5, 0x98, 0x66, 0xbf, 0x17, 0x3a, 0x71, 0x0f, 0xc6, 0x51, 0x2c, 0xb5, 0x2b, 0x12,
	0xae, 0xc2, 0x88, 0x43, 0xf8, 0x78, 0x81, 0x7b, 0x81, 0x46, 0xa9, 0x5d, 0x0d, 0x1d, 0x86, 0x5f,
	0x23, 0x6f, 0xfd, 0x60, 0xfe, 0xa5, 0x84, 0x2c, 0x12, 0xa8, 0x59, 0x82, 0x7f, 0x54, 0x42, 0xe2,
	0xa7, 0xa8, 0xae, 0xa7, 0x44, 0xf3, 0x99, 0x6b, 0xe0, 0x21, 0x34, 0xb0, 0xa6, 0xa7, 0x01, 0xdc,
	0xe3, 0x53, 0x74, 0xb4, 0x5e, 0xe1, 0xc3, 0x60, 0x22, 0x2c, 0x99, 0x92, 0x50, 0x5a, 0x88, 0xa1,
	0x5a, 0x70, 0x50, 0x72, 0x40, 0x7d, 0x1a, 0x4a, 0xeb, 0xbe, 0x21, 0x6e, 0x27, 0x42, 0xc3, 0x90,
	0x27, 0x76, 0xdd, 0xf1, 0xe3, 0xfc, 0x1b, 0xe2, 0xa8, 0x33, 0x60, 0x8a, 0xce, 0xdf, 0x2b, 0x1f,
	0xf8, 0x0f, 0xef, 0x95, 0x0f, 0x70, 0x1f, 0x1d, 0xc3, 0xfe, 0x84, 0xa6, 0x56, 0xc5, 0xd4, 0x8a,
	0x90, 0x40, 0xbf, 0xfc, 0x47, 0xf9, 0x0b, 0x3b, 0x1d, 0x4a, 0x7b, 0x56, 0x52, 0x81, 0x63, 0xf0,
	0x47, 0xd4, 0x0c, 0x63, 0x46, 0xcc, 0x52, 0xd8, 0x70, 0xce, 0x8d, 0xef, 0x77, 0xb6, 0xbb, 0x8d,
	0xc1, 0x91, 0xfb, 0x58, 0x5e, 0xd0, 0x70, 0xa8, 0xe2, 0x98, 0x4a, 0x76, 0x09, 0x6c, 0xd0, 0x08,
	0xe3, 0xe2, 0x92, 0x9b, 0x7b, 0x13, 0xf1, 0xf1, 0xbd, 0x89, 0xe8, 0x3a, 0x98, 0xf5, 0x73, 0xf3,
	0xfe, 0x13, 0x88, 0xa4, 0x9a, 0xce, 0xfa, 0xe0, 0x39, 0x1f, 0x9b, 0xfe, 0x66, 0xb8, 0xfc, 0xa7,
	0x20, 0x68, 0x38, 0x41, 0x31, 0x5b, 0xee, 0x3b, 0xa5, 0xb3, 0xc1, 0x7a, 0xb6, 0xfc, 0x67, 0xa5,
	0x64, 0x50, 0x8e, 0x96, 0x9b, 0x05, 0x27, 0x81, 0x77, 0xf0, 0x39, 0xd0, 0x55, 0x9d, 0x0d, 0xdc,
	0x9c, 0x9c, 0xfc, 0xbb, 0x82, 0x5a, 0x81, 0x4a, 0xad, 0x90, 0xb3, 0xff, 0x97, 0x32, 0x87, 0x68,
	0x97, 0x1a, 0x77, 0x80, 0x2d, 0x38, 0xc0, 0x0e, 0x35, 0x5f, 0xe0, 0x07, 0x2b, 0xa4, 0x24, 0xe4,
	0x3a, 0x0f, 0x92, 0x7a, 0xb0, 0x17, 0xd2, 0x21, 0xd7, 0xd6, 0xed, 0x65, 0x23, 0x93, 0x33, 0x3b,
	0xc0, 0x54, 0x6d, 0x64, 0x80, 0x7a, 0x84, 0xdc, 0x25, 0x59, 0xf0, 0x15, 0xa4, 0x45, 0x3d, 0xd8,
	0xb3, 0x91, 0xf9, 0x13, 0x5f, 0x9d, 0xfc, 0x0e, 0xb5, 0xef, 0xb6, 0x13, 0xb7, 0xd1, 0x76, 0x58,
	0xd8, 0xf0, 0x02, 0x77, 0x89, 0x7d, 0x54, 0xe5, 0x32, 0xff, 0x04, 0xe5, 0x21, 0x57, 0xde, 0xbe,
	0xeb, 0x20, 0x74, 0xeb, 0x0f, 0xa7, 0x86, 0x76, 0x46, 0x5a, 0x25, 0xed, 0x07, 0xee, 0xea, 0x82,
	0xea, 0x45, 0xbb, 0xf2, 0xee, 0xb7, 0xa8, 0xb6, 0xfe, 0xa3, 0xa9, 0xa1, 0x9d, 0x3f, 0xa8, 0x54,
	0xb7, 0x1f, 0xe0, 0x2a, 0xda, 0x1e, 0xd1, 0x55, 0xbb, 0xe2, 0xa0, 0xbf, 0x73, 0xbe, 0x68, 0x6f,
	0xe1, 0x3a, 0xda, 0xbd, 0x50, 0xd2, 0xce, 0xdb, 0xdb, 0x0e, 0xfc, 0x07, 0xa7, 0xba, 0xbd, 0x73,
	0x7e, 0x89, 0x8e, 0x84, 0xea, 0x85, 0x73, 0xa1, 0x13, 0x63, 0x69, 0xb8, 0xe8, 0xd1, 0x44, 0xf4,
	0xa4, 0x39, 0xf7, 0x8a, 0x96, 0x99, 0xb1, 0xfb, 0x37, 0x1d, 0x57, 0xfe, 0xf9, 0x6e, 0x26, 0xec,
	0x3c, 0x9d, 0xf4, 0x42, 0x15, 0x9f, 0x4e, 0xb4, 0x0a, 0x29, 0xd5, 0xa7, 0x9b, 0xb2, 0xf7, 0x34,
	0x11, 0xa7, 0x33, 0x75, 0x7a, 0xf3, 0xe1, 0x54, 0x9a, 0xc9, 0x1e, 0xfc, 0xd0, 0x7e, 0xf8, 0x5f,
	0x00, 0x00, 0x00, 0xff, 0xff, 0xce, 0x8e, 0x22, 0x99, 0xe5, 0x0a, 0x00, 0x00,
}
