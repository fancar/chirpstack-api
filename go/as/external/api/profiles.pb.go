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
	MinEirp uint32 `protobuf:"varint,31,opt,name=min_eirp,json=minEIRP,proto3" json:"min_eirp,omitempty"`
	// Maximum EIRP supported by the End-Device
	MaxEirp uint32 `protobuf:"varint,32,opt,name=max_eirp,json=maxEIRP,proto3" json:"max_eirp,omitempty"`
	// MAX NbTrans
	// the maximum number of transmissions for the device.
	MaxNbTrans uint32 `protobuf:"varint,33,opt,name=max_nb_trans,json=maxNbTrans,proto3" json:"max_nb_trans,omitempty"`
	// ADR algorithm ID.
	// In case this is left blank, or is configured to a non-existing ADR
	// algorithm (plugin), then it falls back to 'default'.
	AdrAlgorithmId       string   `protobuf:"bytes,34,opt,name=adr_algorithm_id,json=adrAlgorithmID,proto3" json:"adr_algorithm_id,omitempty"`
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

func (m *ServiceProfile) GetMinEirp() uint32 {
	if m != nil {
		return m.MinEirp
	}
	return 0
}

func (m *ServiceProfile) GetMaxEirp() uint32 {
	if m != nil {
		return m.MaxEirp
	}
	return 0
}

func (m *ServiceProfile) GetMaxNbTrans() uint32 {
	if m != nil {
		return m.MaxNbTrans
	}
	return 0
}

func (m *ServiceProfile) GetAdrAlgorithmId() string {
	if m != nil {
		return m.AdrAlgorithmId
	}
	return ""
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
	// Class A RX1 delay (mandatory for ABP).
	RxDelay_1 uint32 `protobuf:"varint,11,opt,name=rx_delay_1,json=rxDelay1,proto3" json:"rx_delay_1,omitempty"`
	// RX1 data rate offset (mandatory for ABP).
	RxDrOffset_1 uint32 `protobuf:"varint,12,opt,name=rx_dr_offset_1,json=rxDROffset1,proto3" json:"rx_dr_offset_1,omitempty"`
	// RX2 data rate (mandatory for ABP).
	RxDatarate_2 uint32 `protobuf:"varint,13,opt,name=rx_datarate_2,json=rxDataRate2,proto3" json:"rx_datarate_2,omitempty"`
	// RX2 channel frequency (mandatory for ABP).
	RxFreq_2 uint32 `protobuf:"varint,14,opt,name=rx_freq_2,json=rxFreq2,proto3" json:"rx_freq_2,omitempty"`
	// List of factory-preset frequencies (mandatory for ABP).
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
	FCntAutomaticReset   bool                   `protobuf:"varint,34,opt,name=f_cnt_automatic_reset,json=fCntAutomaticReset,proto3" json:"f_cnt_automatic_reset,omitempty"`
	CmdSwitches          []*ns.MacCommandSwitch `protobuf:"bytes,35,rep,name=cmd_switches,json=cmdSwitches,proto3" json:"cmd_switches,omitempty"`
	XXX_NoUnkeyedLiteral struct{}               `json:"-"`
	XXX_unrecognized     []byte                 `json:"-"`
	XXX_sizecache        int32                  `json:"-"`
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
	// 1533 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xb4, 0x56, 0x5b, 0x73, 0xdb, 0xb8,
	0x15, 0x5e, 0xf9, 0x12, 0x4b, 0xd0, 0xc5, 0x32, 0xec, 0x64, 0x19, 0x6f, 0x2e, 0x4a, 0xb2, 0xd3,
	0x6a, 0x32, 0x5d, 0x69, 0x2d, 0xb7, 0x93, 0xb6, 0xd3, 0x17, 0x4b, 0xcc, 0xa6, 0x6e, 0xe3, 0xae,
	0x06, 0x76, 0x9b, 0x69, 0x5f, 0x30, 0x10, 0x01, 0xd1, 0xa8, 0x48, 0x80, 0x01, 0x40, 0x59, 0xca,
	0x7f, 0xec, 0x4f, 0xe9, 0x7f, 0xe8, 0xe0, 0x90, 0x92, 0x65, 0xc7, 0x7d, 0xe8, 0x43, 0xdf, 0xc8,
	0xef, 0xfb, 0x0e, 0x70, 0x70, 0x39, 0x1f, 0x0e, 0x7a, 0xc1, 0x6c, 0x5f, 0x2c, 0x9c, 0x30, 0x8a,
	0x25, 0x7d, 0x96, 0xc9, 0x7e, 0x66, 0xf4, 0x54, 0x26, 0xc2, 0xf6, 0x32, 0xa3, 0x9d, 0xc6, 0xdb,
	0x2c, 0x93, 0xc7, 0x2f, 0x62, 0xad, 0xe3, 0x44, 0xf4, 0x01, 0x9a, 0xe4, 0xd3, 0x3e, 0xcf, 0x0d,
	0x73, 0x52, 0xab, 0x42, 0x74, 0x7c, 0xa0, 0xec, 0xbd, 0xb8, 0xd7, 0xff, 0xaa, 0xa1, 0xd6, 0xa5,
	0x30, 0x73, 0x19, 0x89, 0x71, 0xc1, 0xe0, 0x16, 0xda, 0x92, 0x3c, 0xa8, 0x74, 0x2a, 0xdd, 0x1a,
	0xd9, 0x92, 0x1c, 0x63, 0xb4, 0xa3, 0x58, 0x2a, 0x82, 0xc7, 0x80, 0xc0, 0x37, 0xee, 0xa0, 0x3a,
	0x17, 0x36, 0x32, 0x32, 0xf3, 0xc3, 0x07, 0x4f, 0x81, 0xda, 0x84, 0xf0, 0xaf, 0x10, 0xe6, 0xc2,
	0x0f, 0x4b, 0x23, 0x9d, 0x2b, 0x47, 0x13, 0x99, 0x4a, 0x17, 0x7c, 0xd7, 0xa9, 0x74, 0x9b, 0xa4,
	0x5d, 0x30, 0x23, 0x4f, 0x7c, 0xf4, 0x38, 0xfe, 0x25, 0xda, 0xd7, 0x26, 0x66, 0x4a, 0x7e, 0x81,
	0x7c, 0xa9, 0xe4, 0xc1, 0x93, 0x4e, 0xa5, 0xbb, 0x4d, 0x5a, 0x9b, 0xf0, 0x79, 0x88, 0xdf, 0xa2,
	0x03, 0x25, 0xdc, 0x8d, 0x36, 0x33, 0x6a, 0x85, 0x99, 0x0b, 0xe3, 0xa5, 0xdf, 0x82, 0x74, 0xbf,
	0x24, 0x2e, 0x01, 0x3f, 0x0f, 0xf1, 0xb7, 0x68, 0x2f, 0x4f, 0xa8, 0x61, 0x4e, 0x04, 0x5b, 0x9d,
	0x4a, 0x77, 0x97, 0x3c, 0xca, 0x13, 0xc2, 0x9c, 0xc0, 0xdf, 0xa3, 0x56, 0x9e, 0xd0, 0x49, 0x1e,
	0xcd, 0x84, 0xa3, 0x56, 0x7e, 0x11, 0xc1, 0x36, 0xe4, 0xd5, 0xc8, 0x93, 0x21, 0x80, 0x97, 0xf2,
	0x8b, 0xc0, 0xbf, 0x01, 0x95, 0x0f, 0xa7, 0x99, 0x4e, 0x64, 0xb4, 0x0c, 0x76, 0x3a, 0x95, 0x6e,
	0x6b, 0xb0, 0xdf, 0x63, 0x99, 0xec, 0xf9, 0x81, 0xc6, 0x00, 0xfb, 0xb0, 0xdb, 0x3f, 0xdc, 0x47,
	0x8d, 0x55, 0x58, 0xae, 0xa4, 0x0b, 0x9e, 0x43, 0x50, 0x73, 0x1d, 0xf4, 0x57, 0x25, 0x1d, 0x41,
	0x45, 0x88, 0xff, 0xf6, 0x69, 0xf2, 0x32, 0xcd, 0xdd, 0x22, 0x4d, 0xbe, 0x4e, 0x93, 0xdf, 0x4d,
	0xf3, 0x51, 0x91, 0x26, 0xbf, 0x97, 0x26, 0xbf, 0x9b, 0xe6, 0xde, 0x7f, 0x49, 0x93, 0xdf, 0x4b,
	0x93, 0x6f, 0xa6, 0xf9, 0xe2, 0xc1, 0x34, 0xf9, 0x6d, 0x9a, 0xbf, 0x40, 0xfb, 0x8c, 0x73, 0x1a,
	0xdf, 0xd0, 0x54, 0x38, 0xc6, 0x99, 0x63, 0x41, 0xb5, 0x53, 0xe9, 0x56, 0x49, 0x93, 0x71, 0xfe,
	0xe1, 0xd3, 0x85, 0x70, 0x2c, 0x64, 0x8e, 0xe1, 0x1f, 0xd0, 0x21, 0x17, 0x73, 0x6a, 0x1d, 0x73,
	0xb9, 0xa5, 0x46, 0x7c, 0xa6, 0x53, 0x23, 0x3e, 0x07, 0xb5, 0xf5, 0xc9, 0x5f, 0x02, 0x43, 0xc4,
	0xe7, 0x9f, 0x8c, 0xf8, 0x8c, 0x7f, 0x87, 0x9e, 0x1a, 0x91, 0x69, 0xe3, 0xe8, 0x46, 0xd4, 0x84,
	0x39, 0x27, 0xcc, 0x32, 0x40, 0x30, 0xc1, 0x93, 0x42, 0x10, 0xae, 0x42, 0x87, 0x05, 0x8b, 0xdf,
	0xa1, 0xe0, 0xeb, 0xd0, 0x94, 0x99, 0x58, 0xaa, 0xa0, 0x0e, 0x91, 0x8f, 0xef, 0x45, 0x5e, 0x00,
	0x89, 0x1f, 0xa3, 0x47, 0xdc, 0xd0, 0x54, 0xaa, 0xa0, 0x01, 0x59, 0xed, 0x72, 0x73, 0x71, 0x0b,
	0xb3, 0x45, 0xd0, 0x5c, 0xc3, 0x6c, 0x81, 0x5f, 0xa1, 0x46, 0x74, 0xcd, 0x94, 0x12, 0x09, 0x4d,
	0x99, 0x9d, 0x05, 0xad, 0x4e, 0xa5, 0xdb, 0x20, 0xf5, 0x12, 0xbb, 0x60, 0x76, 0x86, 0x9f, 0x23,
	0x94, 0x19, 0xca, 0x92, 0x44, 0xdf, 0x08, 0x1e, 0xec, 0xc3, 0xdc, 0xb5, 0xcc, 0x9c, 0x15, 0x80,
	0xa7, 0xaf, 0x6f, 0xe9, 0x76, 0x41, 0x5f, 0x6f, 0xd2, 0x86, 0xad, 0xe9, 0x83, 0x82, 0x36, 0x6c,
	0x45, 0xbf, 0x40, 0x75, 0x75, 0x33, 0xa3, 0xb1, 0xd0, 0x34, 0xd1, 0x51, 0x80, 0x0b, 0x5e, 0xdd,
	0xcc, 0x3e, 0x08, 0xfd, 0x51, 0x47, 0x3e, 0xdc, 0x31, 0x13, 0x0b, 0x47, 0x33, 0x61, 0x82, 0x43,
	0x48, 0xbd, 0x56, 0x20, 0xe3, 0xf7, 0x04, 0x77, 0x51, 0x3b, 0x95, 0xca, 0x9f, 0x1b, 0x97, 0x73,
	0x61, 0xac, 0x74, 0xcb, 0xe0, 0x08, 0x44, 0xad, 0x54, 0xaa, 0x0f, 0x9f, 0xc2, 0x15, 0x8a, 0x5f,
	0xa2, 0x7a, 0x7c, 0x63, 0x69, 0x66, 0xe4, 0xdc, 0x5f, 0xc6, 0x00, 0x26, 0x42, 0xf1, 0x8d, 0x1d,
	0x17, 0x88, 0x17, 0x48, 0x4b, 0xb9, 0xb4, 0x6c, 0x92, 0x08, 0x1e, 0x3c, 0x2b, 0x04, 0xd2, 0x86,
	0x25, 0x82, 0x9f, 0xa2, 0xaa, 0x9f, 0x4b, 0x48, 0x93, 0x05, 0x2f, 0x61, 0x8e, 0xbd, 0x54, 0xaa,
	0xf7, 0xe7, 0x64, 0x0c, 0x14, 0x5b, 0x14, 0x54, 0xa7, 0xa4, 0xd8, 0x02, 0xa8, 0x0e, 0x6a, 0x78,
	0x4a, 0x4d, 0xa8, 0x33, 0x4c, 0xd9, 0xe0, 0x15, 0xd0, 0x28, 0x65, 0x8b, 0xbf, 0x4c, 0xae, 0x3c,
	0xe2, 0xd7, 0xc0, 0xb8, 0xdf, 0xc1, 0x58, 0x1b, 0xe9, 0xae, 0x53, 0x5f, 0xf4, 0xaf, 0xc1, 0x73,
	0x5a, 0x8c, 0x9b, 0xb3, 0x15, 0x7c, 0x1e, 0xbe, 0xfe, 0x77, 0x1d, 0x35, 0x43, 0xf1, 0xbf, 0xda,
	0xd9, 0xff, 0xc5, 0x7e, 0xba, 0xa8, 0x6d, 0xf3, 0xcc, 0xdf, 0x3f, 0x4b, 0xa3, 0x84, 0x59, 0x4b,
	0x27, 0xe0, 0x43, 0x55, 0xd2, 0x5a, 0xe1, 0x23, 0x0f, 0x0f, 0x7d, 0x69, 0x95, 0x02, 0xea, 0x64,
	0x2a, 0x74, 0xee, 0x4a, 0x43, 0x6a, 0x02, 0x3c, 0xbc, 0x2a, 0x40, 0x3f, 0x62, 0x26, 0x55, 0x4c,
	0x6d, 0xa2, 0xe1, 0xb0, 0xa5, 0xe6, 0xe0, 0x49, 0x4d, 0xd2, 0xf2, 0xf8, 0x65, 0xa2, 0xdd, 0x18,
	0x50, 0xbf, 0xa5, 0xb7, 0x4a, 0x6e, 0xc0, 0x58, 0x9a, 0x04, 0xad, 0x54, 0x21, 0xf1, 0xe6, 0x72,
	0xab, 0x80, 0x0a, 0x2d, 0xcd, 0x65, 0xa5, 0x81, 0xea, 0xfc, 0x7a, 0x0d, 0x11, 0xd8, 0xcb, 0xfd,
	0x35, 0x8c, 0x6e, 0xd7, 0x10, 0xad, 0xd7, 0x50, 0xdd, 0x58, 0xc3, 0x68, 0xb5, 0x86, 0x97, 0xa8,
	0x9e, 0xb2, 0x88, 0xc2, 0x9d, 0xd3, 0x0a, 0x6c, 0xa1, 0xe6, 0xcf, 0x3a, 0xfa, 0x5b, 0x81, 0xe0,
	0x1e, 0x3a, 0x34, 0x22, 0xa6, 0x19, 0x33, 0x2c, 0xf5, 0xfe, 0x31, 0x97, 0x20, 0x44, 0x20, 0x3c,
	0x30, 0x22, 0x1e, 0x03, 0x43, 0x4a, 0x02, 0x3f, 0x43, 0xc8, 0x2c, 0x28, 0x17, 0x09, 0x5b, 0xd2,
	0x13, 0xa8, 0xfb, 0x26, 0xa9, 0x9a, 0x45, 0xe8, 0x81, 0x13, 0xfc, 0x06, 0xb5, 0x3c, 0x6b, 0xa8,
	0x9e, 0x4e, 0xad, 0x70, 0xf4, 0xa4, 0x2c, 0xf9, 0xba, 0x59, 0x84, 0xe4, 0x67, 0xc0, 0x4e, 0xf0,
	0x6b, 0xd4, 0xf4, 0x22, 0xe6, 0x18, 0xf8, 0xe1, 0xa0, 0xac, 0x7f, 0xaf, 0x61, 0x8e, 0x79, 0x07,
	0x1c, 0xe0, 0x63, 0x54, 0x33, 0x0b, 0xd8, 0x28, 0x3a, 0x00, 0x0b, 0x68, 0x92, 0x3d, 0xb3, 0xf0,
	0x9b, 0x34, 0xc0, 0x3f, 0xa2, 0xa3, 0x29, 0x8b, 0x9c, 0x36, 0x4b, 0x9a, 0x19, 0xe1, 0xa7, 0xf1,
	0x3a, 0x1b, 0xec, 0x77, 0xb6, 0xbb, 0x4d, 0x82, 0x4b, 0x6e, 0x0c, 0x94, 0x8f, 0xb0, 0x77, 0xaa,
	0xa1, 0x7d, 0xb7, 0x1a, 0xbe, 0x47, 0x2d, 0x4f, 0xf1, 0xdc, 0x2d, 0x69, 0xb4, 0x8c, 0x12, 0x01,
	0x8e, 0xd0, 0x24, 0xbe, 0x46, 0xc2, 0xdc, 0x2d, 0x47, 0x1e, 0xc3, 0x6f, 0x50, 0x73, 0x7d, 0x30,
	0xff, 0xd4, 0x52, 0x95, 0xb6, 0xd0, 0x58, 0x81, 0x7f, 0xd2, 0x52, 0xe1, 0xef, 0x50, 0xcd, 0x4c,
	0xa9, 0x11, 0xb1, 0xdf, 0xc0, 0x43, 0xd8, 0xc0, 0xaa, 0x99, 0x12, 0xf8, 0xc7, 0x7d, 0x74, 0xb4,
	0x1e, 0xe1, 0x74, 0x30, 0x91, 0x8e, 0x4e, 0x69, 0xa4, 0x1c, 0x78, 0x43, 0x95, 0x1c, 0xac, 0xb8,
	0xd3, 0xc1, 0x50, 0xba, 0x9f, 0x46, 0xca, 0xf9, 0x29, 0x33, 0xb6, 0x4c, 0x34, 0xe3, 0x34, 0xd2,
	0x5c, 0x44, 0x60, 0x10, 0x35, 0xd2, 0x28, 0xc1, 0x91, 0xc7, 0xf0, 0xaf, 0xd1, 0x93, 0x95, 0x48,
	0x28, 0x2f, 0x33, 0xb4, 0xe8, 0x09, 0xca, 0x1e, 0xe1, 0xa8, 0x64, 0xdf, 0x17, 0xe4, 0x25, 0x70,
	0x9b, 0x51, 0x5c, 0xdc, 0x89, 0x3a, 0xbe, 0x13, 0x15, 0x8a, 0xcd, 0xa8, 0xb7, 0xe8, 0x20, 0x16,
	0x3a, 0xd1, 0x11, 0x9d, 0xe4, 0xd3, 0xa9, 0x30, 0xd4, 0xb9, 0xa4, 0xec, 0x30, 0xf6, 0x0b, 0x62,
	0x08, 0xf8, 0xd5, 0xd5, 0x47, 0x7c, 0x8a, 0x9e, 0x94, 0x5a, 0x6f, 0x50, 0xa5, 0x1e, 0xde, 0xd4,
	0x67, 0x10, 0x70, 0x58, 0xb0, 0x17, 0x52, 0x15, 0x31, 0xf0, 0xb4, 0xfe, 0x88, 0x76, 0x1c, 0x8b,
	0x6d, 0xf0, 0xbc, 0xb3, 0xdd, 0xad, 0x0f, 0x9e, 0xc1, 0xdb, 0x78, 0xc7, 0x5c, 0x7a, 0x57, 0x2c,
	0xb6, 0xef, 0x95, 0x33, 0x4b, 0x02, 0x4a, 0x3c, 0x44, 0xfb, 0x79, 0x96, 0x48, 0x35, 0xa3, 0x52,
	0x39, 0x61, 0xe6, 0x2c, 0x81, 0x87, 0xb5, 0x3e, 0x78, 0xda, 0x2b, 0x7a, 0xb3, 0xde, 0xaa, 0x37,
	0xeb, 0x85, 0x65, 0x6f, 0x46, 0x5a, 0x45, 0xc4, 0x79, 0x19, 0xf0, 0xa0, 0xd9, 0xbd, 0x7c, 0xc8,
	0xec, 0xfc, 0x53, 0xeb, 0xcf, 0x9e, 0xb2, 0x28, 0x12, 0x99, 0x5b, 0xd7, 0x40, 0x61, 0xaf, 0x6d,
	0x4f, 0x9d, 0x01, 0x53, 0xd6, 0xc2, 0x83, 0xf2, 0x41, 0x69, 0xb7, 0xf7, 0xe5, 0x03, 0x7c, 0x82,
	0x1e, 0xc3, 0x8d, 0xa0, 0x2c, 0x77, 0x3a, 0x65, 0x4e, 0x46, 0x14, 0x6e, 0x30, 0x38, 0x6f, 0x95,
	0xe0, 0xe9, 0x48, 0xb9, 0xb3, 0x15, 0x45, 0x3c, 0x83, 0xdf, 0xa1, 0x46, 0x94, 0x72, 0x6a, 0x6f,
	0xa4, 0x8b, 0xae, 0x85, 0x0d, 0xde, 0xc0, 0xc6, 0x1d, 0xf5, 0x94, 0xed, 0x5d, 0xb0, 0x68, 0xa4,
	0xd3, 0x94, 0x29, 0x7e, 0x09, 0x2c, 0xa9, 0x47, 0x69, 0xf9, 0x29, 0xec, 0xf1, 0x3b, 0x54, 0x5b,
	0x6f, 0x25, 0x6e, 0xa3, 0xed, 0x99, 0x58, 0x96, 0x96, 0xed, 0x3f, 0xf1, 0x11, 0xda, 0x9d, 0xb3,
	0x24, 0x2f, 0xfa, 0xb8, 0x1a, 0x29, 0x7e, 0x7e, 0xbf, 0xf5, 0xdb, 0xca, 0xdb, 0x0e, 0x42, 0x1b,
	0x4d, 0x4d, 0x15, 0xed, 0x84, 0xe4, 0xe7, 0x71, 0xfb, 0x1b, 0xff, 0x75, 0x71, 0x46, 0xfe, 0xdc,
	0xae, 0xbc, 0xfd, 0x03, 0xaa, 0xae, 0x7b, 0x98, 0x2a, 0xda, 0xf9, 0xa3, 0xce, 0x4d, 0xfb, 0x1b,
	0xbc, 0x87, 0xb6, 0x43, 0xb6, 0x6c, 0x57, 0x3c, 0xf4, 0x49, 0x88, 0x59, 0x7b, 0x0b, 0xd7, 0xd0,
	0xee, 0x85, 0x56, 0xee, 0xba, 0xbd, 0xed, 0xc1, 0xbf, 0x0b, 0x66, 0xda, 0x3b, 0xc3, 0x14, 0xbd,
	0x92, 0xba, 0x17, 0x5d, 0x4b, 0x93, 0x59, 0xc7, 0xa2, 0x19, 0xdc, 0x01, 0x66, 0x7b, 0xab, 0x5e,
	0xdc, 0xff, 0x0f, 0x9b, 0xe5, 0x75, 0xb0, 0x63, 0x7f, 0xb8, 0xe3, 0xca, 0x3f, 0xde, 0xc5, 0xd2,
	0x5d, 0xe7, 0x93, 0x5e, 0xa4, 0xd3, 0xfe, 0xc4, 0xe8, 0x88, 0x31, 0xd3, 0xbf, 0x1d, 0xe3, 0x07,
	0xdf, 0xbf, 0xc7, 0xba, 0x3f, 0x3f, 0xed, 0xdf, 0xeb, 0xea, 0x27, 0x8f, 0xe0, 0x7a, 0x9c, 0xfe,
	0x27, 0x00, 0x00, 0xff, 0xff, 0x8d, 0x42, 0x22, 0x0f, 0xef, 0x0b, 0x00, 0x00,
}
