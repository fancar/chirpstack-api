// Code generated by protoc-gen-go. DO NOT EDIT.
// source: as/external/api/profiles.proto

package api

import (
	fmt "fmt"
	ns "github.com/brocaar/chirpstack-api/go/v3/ns"
	proto "github.com/golang/protobuf/proto"
	duration "github.com/golang/protobuf/ptypes/duration"
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
	RatePolicy_DROP RatePolicy = 0
	// Mark
	RatePolicy_MARK RatePolicy = 1
)

var RatePolicy_name = map[int32]string{
	0: "DROP",
	1: "MARK",
}

var RatePolicy_value = map[string]int32{
	"DROP": 0,
	"MARK": 1,
}

func (x RatePolicy) String() string {
	return proto.EnumName(RatePolicy_name, int32(x))
}

func (RatePolicy) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_a1c507fa3dbc9903, []int{0}
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
	return fileDescriptor_a1c507fa3dbc9903, []int{1}
}

type ServiceProfile struct {
	// Service-profile ID (UUID string).
	// This will be automatically set on create.
	Id string `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	// Service-profile name.
	Name string `protobuf:"bytes,21,opt,name=name,proto3" json:"name,omitempty"`
	// Service-profile description.
	Description string `protobuf:"bytes,25,opt,name=description,proto3" json:"description,omitempty"`
	// Maximum device count limit for service-profile.
	DeviceCountLimit uint32 `protobuf:"varint,27,opt,name=device_count_limit,json=deviceCountLimit,proto3" json:"device_count_limit,omitempty"`
	// Organization ID to which the service-profile is assigned.
	OrganizationId int64 `protobuf:"varint,22,opt,name=organization_id,json=organizationID,proto3" json:"organization_id,omitempty"`
	// Network-server ID on which the service-profile is provisioned.
	NetworkServerId int64 `protobuf:"varint,23,opt,name=network_server_id,json=networkServerID,proto3" json:"network_server_id,omitempty"`
	// Token bucket filling rate, including ACKs (packet/h).
	UlRate int32 `protobuf:"varint,2,opt,name=ul_rate,json=ulRate,proto3" json:"ul_rate,omitempty"`
	// Token bucket burst size.
	UlBucketSize uint32 `protobuf:"varint,3,opt,name=ul_bucket_size,json=ulBucketSize,proto3" json:"ul_bucket_size,omitempty"`
	// Drop or mark when exceeding ULRate.
	UlRatePolicy RatePolicy `protobuf:"varint,4,opt,name=ul_rate_policy,json=ulRatePolicy,proto3,enum=api.RatePolicy" json:"ul_rate_policy,omitempty"`
	// Uplink rate unit (per hour, per day, per week, per month, per year)
	UlRateUnit RateUnit `protobuf:"varint,29,opt,name=ul_rate_unit,json=ulRateUnit,proto3,enum=api.RateUnit" json:"ul_rate_unit,omitempty"`
	// Token bucket filling rate, including ACKs (packet/h).
	DlRate int32 `protobuf:"varint,5,opt,name=dl_rate,json=dlRate,proto3" json:"dl_rate,omitempty"`
	// Token bucket burst size.
	DlBucketSize uint32 `protobuf:"varint,6,opt,name=dl_bucket_size,json=dlBucketSize,proto3" json:"dl_bucket_size,omitempty"`
	// Drop or mark when exceeding DLRate.
	DlRatePolicy RatePolicy `protobuf:"varint,7,opt,name=dl_rate_policy,json=dlRatePolicy,proto3,enum=api.RatePolicy" json:"dl_rate_policy,omitempty"`
	// Downlink rate unit (per hour, per day, per week, per month, per year)
	DlRateUnit RateUnit `protobuf:"varint,30,opt,name=dl_rate_unit,json=dlRateUnit,proto3,enum=api.RateUnit" json:"dl_rate_unit,omitempty"`
	// GW metadata (RSSI, SNR, GW geoloc., etc.) are added to the packet sent to AS.
	AddGwMetadata bool `protobuf:"varint,8,opt,name=add_gw_metadata,json=addGWMetaData,proto3" json:"add_gw_metadata,omitempty"`
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
	TargetPer uint32 `protobuf:"varint,19,opt,name=target_per,json=targetPER,proto3" json:"target_per,omitempty"`
	// Minimum number of receiving GWs (informative).
	MinGwDiversity uint32 `protobuf:"varint,20,opt,name=min_gw_diversity,json=minGWDiversity,proto3" json:"min_gw_diversity,omitempty"`
	// Gateways under this service-profile are private.
	// This means that these gateways can only be used by devices under the
	// same service-profile.
	GwsPrivate bool `protobuf:"varint,24,opt,name=gws_private,json=gwsPrivate,proto3" json:"gws_private,omitempty"`
	// Disabled service profile if set true
	IsDisabled bool `protobuf:"varint,28,opt,name=is_disabled,json=isDisabled,proto3" json:"is_disabled,omitempty"`
	// Maximum EIRP supported by the End-Device
	MinEirp int32 `protobuf:"varint,31,opt,name=min_eirp,json=minEIRP,proto3" json:"min_eirp,omitempty"`
	// Maximum EIRP supported by the End-Device
	MaxEirp int32 `protobuf:"varint,32,opt,name=max_eirp,json=maxEIRP,proto3" json:"max_eirp,omitempty"`
	// MAX NbTrans
	// the maximum number of transmissions.
	MaxNbTrans int32 `protobuf:"varint,33,opt,name=max_nb_trans,json=maxNbTrans,proto3" json:"max_nb_trans,omitempty"`
	// MIN NbTrans
	// the minimum number of transmissions.
	MinNbTrans int32 `protobuf:"varint,34,opt,name=min_nb_trans,json=minNbTrans,proto3" json:"min_nb_trans,omitempty"`
	// ADR algorithm ID.
	// In case this is left blank, or is configured to a non-existing ADR
	// algorithm (plugin), then it falls back to 'default'.
	AdrAlgorithmId string `protobuf:"bytes,35,opt,name=adr_algorithm_id,json=adrAlgorithmID,proto3" json:"adr_algorithm_id,omitempty"`
	// if true only uplink events are passing to client's applications
	UplinksOnly          bool     `protobuf:"varint,36,opt,name=uplinks_only,json=uplinksOnly,proto3" json:"uplinks_only,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ServiceProfile) Reset()         { *m = ServiceProfile{} }
func (m *ServiceProfile) String() string { return proto.CompactTextString(m) }
func (*ServiceProfile) ProtoMessage()    {}
func (*ServiceProfile) Descriptor() ([]byte, []int) {
	return fileDescriptor_a1c507fa3dbc9903, []int{0}
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

func (m *ServiceProfile) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

func (m *ServiceProfile) GetName() string {
	if m != nil {
		return m.Name
	}
	return ""
}

func (m *ServiceProfile) GetDescription() string {
	if m != nil {
		return m.Description
	}
	return ""
}

func (m *ServiceProfile) GetDeviceCountLimit() uint32 {
	if m != nil {
		return m.DeviceCountLimit
	}
	return 0
}

func (m *ServiceProfile) GetOrganizationId() int64 {
	if m != nil {
		return m.OrganizationId
	}
	return 0
}

func (m *ServiceProfile) GetNetworkServerId() int64 {
	if m != nil {
		return m.NetworkServerId
	}
	return 0
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
	return RatePolicy_DROP
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
	return RatePolicy_DROP
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

func (m *ServiceProfile) GetMinEirp() int32 {
	if m != nil {
		return m.MinEirp
	}
	return 0
}

func (m *ServiceProfile) GetMaxEirp() int32 {
	if m != nil {
		return m.MaxEirp
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

func (m *ServiceProfile) GetAdrAlgorithmId() string {
	if m != nil {
		return m.AdrAlgorithmId
	}
	return ""
}

func (m *ServiceProfile) GetUplinksOnly() bool {
	if m != nil {
		return m.UplinksOnly
	}
	return false
}

type DeviceProfile struct {
	// Device-profile ID (UUID string).
	Id string `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	// Device-profile name.
	Name string `protobuf:"bytes,21,opt,name=name,proto3" json:"name,omitempty"`
	// Organization ID to which the service-profile is assigned.
	OrganizationId int64 `protobuf:"varint,22,opt,name=organization_id,json=organizationID,proto3" json:"organization_id,omitempty"`
	// Network-server ID on which the service-profile is provisioned.
	NetworkServerId int64 `protobuf:"varint,23,opt,name=network_server_id,json=networkServerID,proto3" json:"network_server_id,omitempty"`
	// End-Device supports Class B.
	SupportsClassB bool `protobuf:"varint,2,opt,name=supports_class_b,json=supportsClassB,proto3" json:"supports_class_b,omitempty"`
	// Maximum delay for the End-Device to answer a MAC request or a confirmed DL frame (mandatory if class B mode supported).
	ClassBTimeout uint32 `protobuf:"varint,3,opt,name=class_b_timeout,json=classBTimeout,proto3" json:"class_b_timeout,omitempty"`
	// Mandatory if class B mode supported.
	PingSlotPeriod uint32 `protobuf:"varint,4,opt,name=ping_slot_period,json=pingSlotPeriod,proto3" json:"ping_slot_period,omitempty"`
	// Mandatory if class B mode supported.
	PingSlotDr uint32 `protobuf:"varint,5,opt,name=ping_slot_dr,json=pingSlotDR,proto3" json:"ping_slot_dr,omitempty"`
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
	// Class A RX1 delay (For ABP initialization  only! mandatory for ABP)..
	RxDelay_1 uint32 `protobuf:"varint,11,opt,name=rx_delay_1,json=rxDelay1,proto3" json:"rx_delay_1,omitempty"`
	// RX1 data rate offset (For ABP initialization  only! mandatory for ABP)..
	RxDrOffset_1 uint32 `protobuf:"varint,12,opt,name=rx_dr_offset_1,json=rxDROffset1,proto3" json:"rx_dr_offset_1,omitempty"`
	// RX2 data rate (For ABP initialization  only! mandatory for ABP)..
	RxDatarate_2 uint32 `protobuf:"varint,13,opt,name=rx_datarate_2,json=rxDataRate2,proto3" json:"rx_datarate_2,omitempty"`
	// RX2 channel frequency (For ABP initialization  only! mandatory for ABP)..
	RxFreq_2 uint32 `protobuf:"varint,14,opt,name=rx_freq_2,json=rxFreq2,proto3" json:"rx_freq_2,omitempty"`
	// List of factory-preset frequencies (mandatory for ABP)..
	FactoryPresetFreqs []uint32 `protobuf:"varint,15,rep,packed,name=factory_preset_freqs,json=factoryPresetFreqs,proto3" json:"factory_preset_freqs,omitempty"`
	// Deprecated. Moved to SP. Maximum EIRP supported by the End-Device. Moved to serivce profile
	MaxEirp uint32 `protobuf:"varint,16,opt,name=max_eirp,json=maxEIRP,proto3" json:"max_eirp,omitempty"`
	// Maximum duty cycle supported by the End-Device.
	MaxDutyCycle uint32 `protobuf:"varint,17,opt,name=max_duty_cycle,json=maxDutyCycle,proto3" json:"max_duty_cycle,omitempty"`
	// End-Device supports Join (OTAA) or not (ABP).
	SupportsJoin bool `protobuf:"varint,18,opt,name=supports_join,json=supportsJoin,proto3" json:"supports_join,omitempty"`
	// RF region name.
	RfRegion string `protobuf:"bytes,19,opt,name=rf_region,json=rfRegion,proto3" json:"rf_region,omitempty"`
	// End-Device uses 32bit FCnt (mandatory for LoRaWAN 1.0 End-Device).
	Supports_32BitFCnt bool `protobuf:"varint,20,opt,name=supports_32bit_f_cnt,json=supports32BitFCnt,proto3" json:"supports_32bit_f_cnt,omitempty"`
	// Payload codec.
	// Leave blank to disable the codec feature.
	PayloadCodec string `protobuf:"bytes,24,opt,name=payload_codec,json=payloadCodec,proto3" json:"payload_codec,omitempty"`
	// Payload encoder script.
	// Depending the codec, it is possible to provide a script which implements
	// the encoder function.
	PayloadEncoderScript string `protobuf:"bytes,25,opt,name=payload_encoder_script,json=payloadEncoderScript,proto3" json:"payload_encoder_script,omitempty"`
	// Payload decoder script.
	// Depending the codec, it is possible to provide a script which implements
	// the decoder function.
	PayloadDecoderScript string `protobuf:"bytes,26,opt,name=payload_decoder_script,json=payloadDecoderScript,proto3" json:"payload_decoder_script,omitempty"`
	// Geolocation buffer TTL (in seconds).
	// When > 0, uplink RX meta-data will be stored in a buffer so that
	// the meta-data of multiple uplinks can be used for geolocation.
	GeolocBufferTtl uint32 `protobuf:"varint,27,opt,name=geoloc_buffer_ttl,json=geolocBufferTTL,proto3" json:"geoloc_buffer_ttl,omitempty"`
	// Geolocation minimum buffer size.
	// When > 0, geolocation will only be performed when the buffer has
	// at least the given size.
	GeolocMinBufferSize uint32 `protobuf:"varint,28,opt,name=geoloc_min_buffer_size,json=geolocMinBufferSize,proto3" json:"geoloc_min_buffer_size,omitempty"`
	// User defined tags.
	Tags map[string]string `protobuf:"bytes,29,rep,name=tags,proto3" json:"tags,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	// Uplink interval.
	// This defines the expected uplink interval which the device uses for
	// communication. When the uplink interval has expired and no uplink has
	// been received, the device is considered inactive.
	UplinkInterval *duration.Duration `protobuf:"bytes,30,opt,name=uplink_interval,json=uplinkInterval,proto3" json:"uplink_interval,omitempty"`
	// Deprecated! ADR algorithm ID has been Moved to ServiceProfile
	// TODO: remove
	AdrAlgorithmId string `protobuf:"bytes,31,opt,name=adr_algorithm_id,json=adrAlgorithmID,proto3" json:"adr_algorithm_id,omitempty"`
	// delay between the end of join request message
	// and start of RX1 window to recieve a Join Accept
	// default 5000ms
	JoinAcceptDelay_1 uint32 `protobuf:"varint,32,opt,name=join_accept_delay_1,json=joinAcceptDelay1,proto3" json:"join_accept_delay_1,omitempty"`
	// delay between the end of join request message
	// and start of RX2 window to recieve a Join Accept
	// default 6000ms
	JoinAcceptDelay_2 uint32 `protobuf:"varint,33,opt,name=join_accept_delay_2,json=joinAcceptDelay2,proto3" json:"join_accept_delay_2,omitempty"`
	// allow autoreset for low counters recieved
	// (for ABP devices only)
	FCntAutomaticReset bool                   `protobuf:"varint,34,opt,name=f_cnt_automatic_reset,json=fCntAutomaticReset,proto3" json:"f_cnt_automatic_reset,omitempty"`
	CmdSwitches        []*ns.MacCommandSwitch `protobuf:"bytes,35,rep,name=cmd_switches,json=cmdSwitches,proto3" json:"cmd_switches,omitempty"`
	// Class A RX1 delay. If not set (-1) - default value from NS cfg in use
	// RX2 delay will be +1s to the rx1_delay
	Rx1Delay int32 `protobuf:"varint,36,opt,name=rx1_delay,json=rx1Delay,proto3" json:"rx1_delay,omitempty"`
	// RX1 data rate offset. If not set (-1) - default value from NS cfg in use
	Rx1DrOffset int32 `protobuf:"varint,37,opt,name=rx1_dr_offset,json=rx1DrOffset,proto3" json:"rx1_dr_offset,omitempty"`
	// RX2 data rate. If not set (-1) - default value from NS cfg in use
	Rx2Datarate int32 `protobuf:"varint,38,opt,name=rx2_datarate,json=rx2Datarate,proto3" json:"rx2_datarate,omitempty"`
	// RX2 channel frequency. If not set (-1) - default value from NS cfg in use
	Rx2Freq              int32    `protobuf:"varint,39,opt,name=rx2_freq,json=rx2Freq,proto3" json:"rx2_freq,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *DeviceProfile) Reset()         { *m = DeviceProfile{} }
func (m *DeviceProfile) String() string { return proto.CompactTextString(m) }
func (*DeviceProfile) ProtoMessage()    {}
func (*DeviceProfile) Descriptor() ([]byte, []int) {
	return fileDescriptor_a1c507fa3dbc9903, []int{1}
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

func (m *DeviceProfile) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

func (m *DeviceProfile) GetName() string {
	if m != nil {
		return m.Name
	}
	return ""
}

func (m *DeviceProfile) GetOrganizationId() int64 {
	if m != nil {
		return m.OrganizationId
	}
	return 0
}

func (m *DeviceProfile) GetNetworkServerId() int64 {
	if m != nil {
		return m.NetworkServerId
	}
	return 0
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

func (m *DeviceProfile) GetPayloadCodec() string {
	if m != nil {
		return m.PayloadCodec
	}
	return ""
}

func (m *DeviceProfile) GetPayloadEncoderScript() string {
	if m != nil {
		return m.PayloadEncoderScript
	}
	return ""
}

func (m *DeviceProfile) GetPayloadDecoderScript() string {
	if m != nil {
		return m.PayloadDecoderScript
	}
	return ""
}

func (m *DeviceProfile) GetGeolocBufferTtl() uint32 {
	if m != nil {
		return m.GeolocBufferTtl
	}
	return 0
}

func (m *DeviceProfile) GetGeolocMinBufferSize() uint32 {
	if m != nil {
		return m.GeolocMinBufferSize
	}
	return 0
}

func (m *DeviceProfile) GetTags() map[string]string {
	if m != nil {
		return m.Tags
	}
	return nil
}

func (m *DeviceProfile) GetUplinkInterval() *duration.Duration {
	if m != nil {
		return m.UplinkInterval
	}
	return nil
}

func (m *DeviceProfile) GetAdrAlgorithmId() string {
	if m != nil {
		return m.AdrAlgorithmId
	}
	return ""
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

func (m *DeviceProfile) GetCmdSwitches() []*ns.MacCommandSwitch {
	if m != nil {
		return m.CmdSwitches
	}
	return nil
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

func init() {
	proto.RegisterEnum("api.RatePolicy", RatePolicy_name, RatePolicy_value)
	proto.RegisterEnum("api.RateUnit", RateUnit_name, RateUnit_value)
	proto.RegisterType((*ServiceProfile)(nil), "api.ServiceProfile")
	proto.RegisterType((*DeviceProfile)(nil), "api.DeviceProfile")
	proto.RegisterMapType((map[string]string)(nil), "api.DeviceProfile.TagsEntry")
}

func init() {
	proto.RegisterFile("as/external/api/profiles.proto", fileDescriptor_a1c507fa3dbc9903)
}

var fileDescriptor_a1c507fa3dbc9903 = []byte{
	// 1622 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xb4, 0x57, 0x5b, 0x73, 0xdb, 0xb8,
	0x15, 0x5e, 0xf9, 0x12, 0x4b, 0xd0, 0xc5, 0x32, 0xec, 0x64, 0x19, 0x6f, 0x2e, 0xca, 0xa5, 0xbb,
	0x9a, 0x4c, 0x23, 0xad, 0xe5, 0x76, 0xd2, 0x76, 0xfa, 0x62, 0x89, 0x49, 0xea, 0x36, 0x6e, 0x34,
	0xb4, 0xdb, 0x4c, 0xfb, 0x82, 0x81, 0x08, 0x88, 0x46, 0x45, 0x02, 0x0c, 0x00, 0xca, 0x52, 0x7e,
	0x46, 0x7f, 0x67, 0x7f, 0x44, 0x07, 0x87, 0xa4, 0x24, 0x3b, 0xe9, 0x43, 0x1f, 0xf6, 0x8d, 0xfc,
	0xbe, 0xef, 0x80, 0x07, 0xc0, 0x39, 0x1f, 0x40, 0xf4, 0x84, 0x9a, 0x3e, 0x5f, 0x58, 0xae, 0x25,
	0x8d, 0xfb, 0x34, 0x15, 0xfd, 0x54, 0xab, 0xa9, 0x88, 0xb9, 0xe9, 0xa5, 0x5a, 0x59, 0x85, 0xb7,
	0x69, 0x2a, 0x8e, 0x9f, 0x44, 0x4a, 0x45, 0x31, 0xef, 0x03, 0x34, 0xc9, 0xa6, 0x7d, 0x96, 0x69,
	0x6a, 0x85, 0x92, 0xb9, 0xe8, 0xf8, 0x40, 0x9a, 0x3b, 0x71, 0xcf, 0xff, 0x8d, 0x50, 0xeb, 0x92,
	0xeb, 0xb9, 0x08, 0xf9, 0x38, 0x67, 0x70, 0x0b, 0x6d, 0x09, 0xe6, 0x55, 0x3a, 0x95, 0x6e, 0x2d,
	0xd8, 0x12, 0x0c, 0x63, 0xb4, 0x23, 0x69, 0xc2, 0xbd, 0xfb, 0x80, 0xc0, 0x33, 0xee, 0xa0, 0x3a,
	0xe3, 0x26, 0xd4, 0x22, 0x75, 0xc3, 0x7b, 0x0f, 0x81, 0xda, 0x84, 0xf0, 0xaf, 0x11, 0x66, 0xdc,
	0x0d, 0x4b, 0x42, 0x95, 0x49, 0x4b, 0x62, 0x91, 0x08, 0xeb, 0xfd, 0xd0, 0xa9, 0x74, 0x9b, 0x41,
	0x3b, 0x67, 0x46, 0x8e, 0xf8, 0xe0, 0x70, 0xfc, 0x13, 0xda, 0x57, 0x3a, 0xa2, 0x52, 0x7c, 0x81,
	0x7c, 0x89, 0x60, 0xde, 0x83, 0x4e, 0xa5, 0xbb, 0x1d, 0xb4, 0x36, 0xe1, 0x73, 0x1f, 0xbf, 0x42,
	0x07, 0x92, 0xdb, 0x1b, 0xa5, 0x67, 0xc4, 0x70, 0x3d, 0xe7, 0xda, 0x49, 0xbf, 0x07, 0xe9, 0x7e,
	0x41, 0x5c, 0x02, 0x7e, 0xee, 0xe3, 0xef, 0xd1, 0x5e, 0x16, 0x13, 0x4d, 0x2d, 0xf7, 0xb6, 0x3a,
	0x95, 0xee, 0x6e, 0x70, 0x2f, 0x8b, 0x03, 0x6a, 0x39, 0x7e, 0x89, 0x5a, 0x59, 0x4c, 0x26, 0x59,
	0x38, 0xe3, 0x96, 0x18, 0xf1, 0x85, 0x7b, 0xdb, 0x90, 0x57, 0x23, 0x8b, 0x87, 0x00, 0x5e, 0x8a,
	0x2f, 0x1c, 0xff, 0x16, 0x54, 0x2e, 0x9c, 0xa4, 0x2a, 0x16, 0xe1, 0xd2, 0xdb, 0xe9, 0x54, 0xba,
	0xad, 0xc1, 0x7e, 0x8f, 0xa6, 0xa2, 0xe7, 0x06, 0x1a, 0x03, 0xec, 0xc2, 0xd6, 0x6f, 0xb8, 0x8f,
	0x1a, 0x65, 0x58, 0x26, 0x85, 0xf5, 0x1e, 0x43, 0x50, 0x73, 0x15, 0xf4, 0x37, 0x29, 0x6c, 0x80,
	0xf2, 0x10, 0xf7, 0xec, 0xd2, 0x64, 0x45, 0x9a, 0xbb, 0x79, 0x9a, 0x6c, 0x95, 0x26, 0xbb, 0x9d,
	0xe6, 0xbd, 0x3c, 0x4d, 0x76, 0x27, 0x4d, 0x76, 0x3b, 0xcd, 0xbd, 0xff, 0x91, 0x26, 0xbb, 0x93,
	0x26, 0xdb, 0x4c, 0xf3, 0xc9, 0x37, 0xd3, 0x64, 0xeb, 0x34, 0x7f, 0x44, 0xfb, 0x94, 0x31, 0x12,
	0xdd, 0x90, 0x84, 0x5b, 0xca, 0xa8, 0xa5, 0x5e, 0xb5, 0x53, 0xe9, 0x56, 0x83, 0x26, 0x65, 0xec,
	0xfd, 0xa7, 0x0b, 0x6e, 0xa9, 0x4f, 0x2d, 0xc5, 0xaf, 0xd1, 0x21, 0xe3, 0x73, 0x62, 0x2c, 0xb5,
	0x99, 0x21, 0x9a, 0x7f, 0x26, 0x53, 0xcd, 0x3f, 0x7b, 0xb5, 0xd5, 0xce, 0x5f, 0x02, 0x13, 0xf0,
	0xcf, 0xef, 0x34, 0xff, 0x8c, 0x7f, 0x8f, 0x1e, 0x6a, 0x9e, 0x2a, 0x6d, 0xc9, 0x46, 0xd4, 0x84,
	0x5a, 0xcb, 0xf5, 0xd2, 0x43, 0xf0, 0x81, 0x07, 0xb9, 0xc0, 0x2f, 0x43, 0x87, 0x39, 0x8b, 0xdf,
	0x20, 0xef, 0xeb, 0xd0, 0x84, 0xea, 0x48, 0x48, 0xaf, 0x0e, 0x91, 0xf7, 0xef, 0x44, 0x5e, 0x00,
	0x89, 0xef, 0xa3, 0x7b, 0x4c, 0x93, 0x44, 0x48, 0xaf, 0x01, 0x59, 0xed, 0x32, 0x7d, 0xb1, 0x86,
	0xe9, 0xc2, 0x6b, 0xae, 0x60, 0xba, 0xc0, 0xcf, 0x50, 0x23, 0xbc, 0xa6, 0x52, 0xf2, 0x98, 0x24,
	0xd4, 0xcc, 0xbc, 0x56, 0xa7, 0xd2, 0x6d, 0x04, 0xf5, 0x02, 0xbb, 0xa0, 0x66, 0x86, 0x1f, 0x23,
	0x94, 0x6a, 0x42, 0xe3, 0x58, 0xdd, 0x70, 0xe6, 0xed, 0xc3, 0xb7, 0x6b, 0xa9, 0x3e, 0xcb, 0x01,
	0x47, 0x5f, 0xaf, 0xe9, 0x76, 0x4e, 0x5f, 0x6f, 0xd2, 0x9a, 0xae, 0xe8, 0x83, 0x9c, 0xd6, 0xb4,
	0xa4, 0x9f, 0xa0, 0xba, 0xbc, 0x99, 0x91, 0x88, 0x2b, 0x12, 0xab, 0xd0, 0xc3, 0x39, 0x2f, 0x6f,
	0x66, 0xef, 0xb9, 0xfa, 0xa0, 0x42, 0x17, 0x6e, 0xa9, 0x8e, 0xb8, 0x25, 0x29, 0xd7, 0xde, 0x21,
	0xa4, 0x5e, 0xcb, 0x91, 0xf1, 0xdb, 0x00, 0x77, 0x51, 0x3b, 0x11, 0xd2, 0xed, 0x1b, 0x13, 0x73,
	0xae, 0x8d, 0xb0, 0x4b, 0xef, 0x08, 0x44, 0xad, 0x44, 0xc8, 0xf7, 0x9f, 0xfc, 0x12, 0xc5, 0x4f,
	0x51, 0x3d, 0xba, 0x31, 0x24, 0xd5, 0x62, 0xee, 0x8a, 0xd1, 0x83, 0x0f, 0xa1, 0xe8, 0xc6, 0x8c,
	0x73, 0xc4, 0x09, 0x84, 0x21, 0x4c, 0x18, 0x3a, 0x89, 0x39, 0xf3, 0x1e, 0xe5, 0x02, 0x61, 0xfc,
	0x02, 0xc1, 0x0f, 0x51, 0xd5, 0x7d, 0x8b, 0x0b, 0x9d, 0x7a, 0x4f, 0xa1, 0x96, 0xf7, 0x12, 0x21,
	0xdf, 0x9e, 0x07, 0x63, 0xa0, 0xe8, 0x22, 0xa7, 0x3a, 0x05, 0x45, 0x17, 0x40, 0x75, 0x50, 0xc3,
	0x51, 0x72, 0x42, 0xac, 0xa6, 0xd2, 0x78, 0xcf, 0x80, 0x46, 0x09, 0x5d, 0xfc, 0x75, 0x72, 0xe5,
	0x10, 0x50, 0x08, 0xb9, 0x56, 0x3c, 0x2f, 0x14, 0x42, 0x96, 0x8a, 0x2e, 0x6a, 0x53, 0xe6, 0xd6,
	0x38, 0x52, 0x5a, 0xd8, 0xeb, 0xc4, 0xd9, 0xc2, 0x0b, 0x70, 0xa5, 0x16, 0x65, 0xfa, 0xac, 0x84,
	0xcf, 0x7d, 0xb7, 0x9d, 0x59, 0x1a, 0x0b, 0x39, 0x33, 0x44, 0xc9, 0x78, 0xe9, 0xbd, 0x84, 0x59,
	0xd4, 0x0b, 0xec, 0xa3, 0x8c, 0x97, 0xcf, 0xff, 0xd3, 0x40, 0x4d, 0x9f, 0xff, 0xbf, 0x9e, 0xf8,
	0x8b, 0x78, 0x58, 0x17, 0xb5, 0x4d, 0x96, 0xba, 0x22, 0x36, 0x24, 0x8c, 0xa9, 0x31, 0x64, 0x02,
	0x66, 0x56, 0x0d, 0x5a, 0x25, 0x3e, 0x72, 0xf0, 0xd0, 0xf5, 0x67, 0x21, 0x20, 0x56, 0x24, 0x5c,
	0x65, 0xb6, 0x70, 0xb5, 0x26, 0xc0, 0xc3, 0xab, 0x1c, 0x74, 0x23, 0xa6, 0x42, 0x46, 0xc4, 0xc4,
	0x0a, 0x2a, 0x46, 0x28, 0x06, 0xc6, 0xd6, 0x0c, 0x5a, 0x0e, 0xbf, 0x8c, 0x95, 0x1d, 0x03, 0xea,
	0x56, 0x7d, 0xad, 0x64, 0x1a, 0xdc, 0xa9, 0x19, 0xa0, 0x52, 0xe5, 0x07, 0xce, 0xa1, 0xd6, 0x0a,
	0x68, 0xf3, 0xc2, 0xa1, 0x4a, 0x0d, 0xb4, 0xf8, 0xd7, 0x73, 0x08, 0xc1, 0xa3, 0xee, 0xce, 0x61,
	0xb4, 0x9e, 0x43, 0xb8, 0x9a, 0x43, 0x75, 0x63, 0x0e, 0xa3, 0x72, 0x0e, 0x4f, 0x51, 0x3d, 0xa1,
	0x21, 0x81, 0xc2, 0x55, 0x12, 0xbc, 0xa5, 0xe6, 0x0a, 0x26, 0xfc, 0x7b, 0x8e, 0xe0, 0x1e, 0x3a,
	0xd4, 0x3c, 0x22, 0x29, 0xd5, 0x34, 0x71, 0x26, 0x34, 0x17, 0x20, 0x44, 0x20, 0x3c, 0xd0, 0x3c,
	0x1a, 0x03, 0x13, 0x14, 0x04, 0x7e, 0x84, 0x90, 0x5e, 0x10, 0xc6, 0x63, 0xba, 0x24, 0x27, 0x60,
	0x1e, 0xcd, 0xa0, 0xaa, 0x17, 0xbe, 0x03, 0x4e, 0xf0, 0x0b, 0xd4, 0x72, 0xac, 0x26, 0x6a, 0x3a,
	0x35, 0xdc, 0x92, 0x93, 0xc2, 0x37, 0xea, 0x7a, 0xe1, 0x07, 0x1f, 0x01, 0x3b, 0xc1, 0xcf, 0x51,
	0xd3, 0x89, 0xa8, 0xa5, 0x60, 0xaa, 0x83, 0xc2, 0x44, 0x9c, 0x86, 0x5a, 0xea, 0x6c, 0x74, 0x80,
	0x8f, 0x51, 0x4d, 0x2f, 0x60, 0xa1, 0xc8, 0x00, 0x7c, 0xa4, 0x19, 0xec, 0xe9, 0x85, 0x5b, 0xa4,
	0x01, 0xfe, 0x19, 0x1d, 0x4d, 0x69, 0x68, 0x95, 0x5e, 0x92, 0x54, 0x73, 0xf7, 0x19, 0xa7, 0x33,
	0xde, 0x7e, 0x67, 0xbb, 0xdb, 0x0c, 0x70, 0xc1, 0x8d, 0x81, 0x72, 0x11, 0xe6, 0x56, 0x4b, 0xb5,
	0xf3, 0xc1, 0xca, 0x96, 0x7a, 0x89, 0x5a, 0x8e, 0x62, 0x99, 0x5d, 0x92, 0x70, 0x19, 0xc6, 0x1c,
	0x6c, 0xa5, 0x19, 0xb8, 0x46, 0xf3, 0x33, 0xbb, 0x1c, 0x39, 0x0c, 0xbf, 0x40, 0xcd, 0xd5, 0xc6,
	0xfc, 0x4b, 0x09, 0x59, 0x78, 0x4b, 0xa3, 0x04, 0xff, 0xac, 0x84, 0xc4, 0x3f, 0xa0, 0x9a, 0x9e,
	0x12, 0xcd, 0x23, 0xb7, 0x80, 0x87, 0xb0, 0x80, 0x55, 0x3d, 0x0d, 0xe0, 0x1d, 0xf7, 0xd1, 0xd1,
	0x6a, 0x84, 0xd3, 0xc1, 0x44, 0x58, 0x32, 0x25, 0xa1, 0xb4, 0x60, 0x30, 0xd5, 0xe0, 0xa0, 0xe4,
	0x4e, 0x07, 0x43, 0x61, 0xdf, 0x8d, 0xa4, 0x75, 0x9f, 0x4c, 0xe9, 0x32, 0x56, 0x94, 0x91, 0x50,
	0x31, 0x1e, 0x82, 0xcb, 0xd4, 0x82, 0x46, 0x01, 0x8e, 0x1c, 0x86, 0x7f, 0x83, 0x1e, 0x94, 0x22,
	0x2e, 0x9d, 0x4c, 0x93, 0xfc, 0x62, 0x51, 0x5c, 0x34, 0x8e, 0x0a, 0xf6, 0x6d, 0x4e, 0x5e, 0x02,
	0xb7, 0x19, 0xc5, 0xf8, 0xad, 0xa8, 0xe3, 0x5b, 0x51, 0x3e, 0xdf, 0x8c, 0x7a, 0x85, 0x0e, 0x22,
	0xae, 0x62, 0x15, 0x92, 0x49, 0x36, 0x9d, 0x72, 0x4d, 0xac, 0x8d, 0x8b, 0x6b, 0xca, 0x7e, 0x4e,
	0x0c, 0x01, 0xbf, 0xba, 0xfa, 0x80, 0x4f, 0xd1, 0x83, 0x42, 0xeb, 0xdc, 0xa8, 0xd0, 0xc3, 0xc1,
	0xfc, 0x08, 0x02, 0x0e, 0x73, 0xf6, 0x42, 0xc8, 0x3c, 0x06, 0xce, 0xe7, 0x9f, 0xd1, 0x8e, 0xa5,
	0x91, 0xf1, 0x1e, 0x77, 0xb6, 0xbb, 0xf5, 0xc1, 0x23, 0x38, 0x60, 0x6f, 0x99, 0x4b, 0xef, 0x8a,
	0x46, 0xe6, 0xad, 0xb4, 0x7a, 0x19, 0x80, 0x12, 0x0f, 0xd1, 0x7e, 0xee, 0x46, 0x44, 0x48, 0xcb,
	0xf5, 0x9c, 0xc6, 0x70, 0x3a, 0xd7, 0x07, 0x0f, 0x7b, 0xf9, 0x05, 0xaf, 0x57, 0x5e, 0xf0, 0x7a,
	0x7e, 0x71, 0xc1, 0x0b, 0x5a, 0x79, 0xc4, 0x79, 0x11, 0xf0, 0x4d, 0x3f, 0x7c, 0xfa, 0x4d, 0x3f,
	0x7c, 0x8d, 0x0e, 0xdd, 0xde, 0x13, 0x1a, 0x86, 0x3c, 0xb5, 0xab, 0x1e, 0xe8, 0xe4, 0xe7, 0xb5,
	0xa3, 0xce, 0x80, 0x29, 0x7a, 0xe1, 0x9b, 0xf2, 0x01, 0x78, 0xf6, 0xd7, 0xf2, 0x01, 0x3e, 0x41,
	0xf7, 0xa1, 0x22, 0x08, 0xcd, 0xac, 0x4a, 0xa8, 0x15, 0x21, 0x81, 0x0a, 0x06, 0x0b, 0xaf, 0x06,
	0x78, 0x3a, 0x92, 0xf6, 0xac, 0xa4, 0x02, 0xc7, 0xe0, 0x37, 0xa8, 0x11, 0x26, 0x8c, 0x98, 0x1b,
	0x61, 0xc3, 0x6b, 0x6e, 0xbc, 0x17, 0xb0, 0x70, 0x47, 0x3d, 0x69, 0x7a, 0x17, 0x34, 0x1c, 0xa9,
	0x24, 0xa1, 0x92, 0x5d, 0x02, 0x1b, 0xd4, 0xc3, 0xa4, 0x78, 0xe4, 0x06, 0x2a, 0x75, 0x71, 0x92,
	0xa7, 0x04, 0xb6, 0xbe, 0xeb, 0x7a, 0xf8, 0x04, 0x32, 0xc9, 0xdb, 0xf3, 0x64, 0xdd, 0xc4, 0xde,
	0xaf, 0x40, 0x50, 0x77, 0x02, 0x9d, 0xf7, 0xb0, 0x3b, 0x1a, 0xf4, 0x62, 0xb0, 0xea, 0x61, 0xef,
	0xc7, 0x52, 0x32, 0xf0, 0x0b, 0xc8, 0xf5, 0x9c, 0x93, 0x80, 0xd7, 0xfd, 0x94, 0x1f, 0x63, 0x7a,
	0x31, 0x70, 0xfd, 0x78, 0xfc, 0x06, 0xd5, 0x56, 0x3b, 0x89, 0xdb, 0x68, 0x7b, 0xc6, 0x97, 0xc5,
	0x89, 0xe1, 0x1e, 0xf1, 0x11, 0xda, 0x9d, 0xd3, 0x38, 0xcb, 0xef, 0xa2, 0xb5, 0x20, 0x7f, 0xf9,
	0xc3, 0xd6, 0xef, 0x2a, 0xaf, 0x3a, 0x08, 0x6d, 0x5c, 0xcc, 0xaa, 0x68, 0xc7, 0x0f, 0x3e, 0x8e,
	0xdb, 0xdf, 0xb9, 0xa7, 0x8b, 0xb3, 0xe0, 0x2f, 0xed, 0xca, 0xab, 0x3f, 0xa2, 0xea, 0xea, 0x1e,
	0x56, 0x45, 0x3b, 0x7f, 0x52, 0x99, 0x6e, 0x7f, 0x87, 0xf7, 0xd0, 0xb6, 0x4f, 0x97, 0xed, 0x8a,
	0x83, 0x3e, 0x71, 0x3e, 0x6b, 0x6f, 0xe1, 0x1a, 0xda, 0xbd, 0x50, 0xd2, 0x5e, 0xb7, 0xb7, 0x1d,
	0xf8, 0x0f, 0x4e, 0x75, 0x7b, 0x67, 0x98, 0xa0, 0x67, 0x42, 0xf5, 0xc2, 0x6b, 0xa1, 0x53, 0x63,
	0x69, 0x38, 0x83, 0x12, 0xa4, 0xa6, 0x57, 0xfe, 0x4f, 0xb8, 0xf7, 0x61, 0xb3, 0xa8, 0x46, 0x33,
	0x76, 0xb5, 0x35, 0xae, 0xfc, 0xf3, 0x4d, 0x24, 0xec, 0x75, 0x36, 0xe9, 0x85, 0x2a, 0xe9, 0x4f,
	0xb4, 0x0a, 0x29, 0xd5, 0xfd, 0xf5, 0x18, 0xaf, 0xdd, 0x3f, 0x48, 0xa4, 0xfa, 0xf3, 0xd3, 0xfe,
	0x9d, 0x3f, 0x93, 0xc9, 0x3d, 0xa8, 0xce, 0xd3, 0xff, 0x06, 0x00, 0x00, 0xff, 0xff, 0xf6, 0x5b,
	0xd3, 0x55, 0xb3, 0x0c, 0x00, 0x00,
}
