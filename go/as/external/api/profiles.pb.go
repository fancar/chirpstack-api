// Code generated by protoc-gen-go. DO NOT EDIT.
// source: as/external/api/profiles.proto

package api

import (
	fmt "fmt"
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

type ServiceProfile struct {
	// Service-profile ID (UUID string).
	// This will be automatically set on create.
	Id string `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	// Service-profile name.
	Name string `protobuf:"bytes,21,opt,name=name,proto3" json:"name,omitempty"`
	// Maximum device count limit for service-profile.
	DeviceCountLimit uint32 `protobuf:"varint,27,opt,name=device_count_limit,json=deviceCountLimit,proto3" json:"device_count_limit,omitempty"`
	// Organization ID to which the service-profile is assigned.
	OrganizationId int64 `protobuf:"varint,22,opt,name=organization_id,json=organizationID,proto3" json:"organization_id,omitempty"`
	// Network-server ID on which the service-profile is provisioned.
	NetworkServerId int64 `protobuf:"varint,23,opt,name=network_server_id,json=networkServerID,proto3" json:"network_server_id,omitempty"`
	// Token bucket filling rate, including ACKs (packet/h).
	UlRate uint32 `protobuf:"varint,2,opt,name=ul_rate,json=ulRate,proto3" json:"ul_rate,omitempty"`
	// Token bucket burst size.
	UlBucketSize uint32 `protobuf:"varint,3,opt,name=ul_bucket_size,json=ulBucketSize,proto3" json:"ul_bucket_size,omitempty"`
	// Drop or mark when exceeding ULRate.
	UlRatePolicy RatePolicy `protobuf:"varint,4,opt,name=ul_rate_policy,json=ulRatePolicy,proto3,enum=api.RatePolicy" json:"ul_rate_policy,omitempty"`
	// Token bucket filling rate, including ACKs (packet/h).
	DlRate uint32 `protobuf:"varint,5,opt,name=dl_rate,json=dlRate,proto3" json:"dl_rate,omitempty"`
	// Token bucket burst size.
	DlBucketSize uint32 `protobuf:"varint,6,opt,name=dl_bucket_size,json=dlBucketSize,proto3" json:"dl_bucket_size,omitempty"`
	// Drop or mark when exceeding DLRate.
	DlRatePolicy RatePolicy `protobuf:"varint,7,opt,name=dl_rate_policy,json=dlRatePolicy,proto3,enum=api.RatePolicy" json:"dl_rate_policy,omitempty"`
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
	GwsPrivate           bool     `protobuf:"varint,24,opt,name=gws_private,json=gwsPrivate,proto3" json:"gws_private,omitempty"`
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

func (m *ServiceProfile) GetUlRate() uint32 {
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

func (m *ServiceProfile) GetDlRate() uint32 {
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
	// Maximum EIRP supported by the End-Device.
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
	// ADR algorithm ID.
	// In case this is left blank, or is configured to a non-existing ADR
	// algorithm (plugin), then it falls back to 'default'.
	AdrAlgorithmId       string   `protobuf:"bytes,31,opt,name=adr_algorithm_id,json=adrAlgorithmID,proto3" json:"adr_algorithm_id,omitempty"`
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

func init() {
	proto.RegisterEnum("api.RatePolicy", RatePolicy_name, RatePolicy_value)
	proto.RegisterType((*ServiceProfile)(nil), "api.ServiceProfile")
	proto.RegisterType((*DeviceProfile)(nil), "api.DeviceProfile")
	proto.RegisterMapType((map[string]string)(nil), "api.DeviceProfile.TagsEntry")
}

func init() { proto.RegisterFile("as/external/api/profiles.proto", fileDescriptor_a1c507fa3dbc9903) }

var fileDescriptor_a1c507fa3dbc9903 = []byte{
	// 1282 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xb4, 0x56, 0x5d, 0x6f, 0xdb, 0x36,
	0x17, 0x7e, 0x9d, 0xa4, 0x89, 0x4d, 0x7f, 0x25, 0x4c, 0x9a, 0x2a, 0x69, 0x9b, 0xba, 0xed, 0x8b,
	0xcd, 0x28, 0x56, 0xbb, 0x71, 0x36, 0x74, 0xdb, 0x5d, 0x1d, 0xa5, 0x45, 0xb6, 0x06, 0x35, 0x94,
	0x60, 0x05, 0x76, 0x43, 0x1c, 0x8b, 0xb4, 0xc2, 0x59, 0x12, 0x15, 0x8a, 0x72, 0xec, 0xfe, 0x9d,
	0x01, 0xfb, 0x9d, 0x03, 0x8f, 0xe4, 0x8f, 0xa4, 0xd8, 0xc5, 0x2e, 0x76, 0x27, 0x3d, 0x1f, 0x3a,
	0xe2, 0x21, 0x1f, 0x92, 0xe4, 0x08, 0xd2, 0xae, 0x98, 0x1a, 0xa1, 0x63, 0x08, 0xbb, 0x90, 0xc8,
	0x6e, 0xa2, 0xd5, 0x48, 0x86, 0x22, 0xed, 0x24, 0x5a, 0x19, 0x45, 0xd7, 0x21, 0x91, 0x87, 0x47,
	0x81, 0x52, 0x41, 0x28, 0xba, 0x08, 0x0d, 0xb3, 0x51, 0x97, 0x67, 0x1a, 0x8c, 0x54, 0x71, 0x2e,
	0x7a, 0xf1, 0xd7, 0x16, 0x69, 0x5c, 0x0a, 0x3d, 0x91, 0xbe, 0x18, 0xe4, 0x76, 0xda, 0x20, 0x6b,
	0x92, 0x3b, 0xa5, 0x56, 0xa9, 0x5d, 0xf1, 0xd6, 0x24, 0xa7, 0x94, 0x6c, 0xc4, 0x10, 0x09, 0xe7,
	0x21, 0x22, 0xf8, 0x4c, 0xbf, 0x23, 0x94, 0x0b, 0x6b, 0x62, 0xbe, 0xca, 0x62, 0xc3, 0x42, 0x19,
	0x49, 0xe3, 0x3c, 0x6e, 0x95, 0xda, 0x75, 0x6f, 0x3b, 0x67, 0x4e, 0x2d, 0xf1, 0xd1, 0xe2, 0xf4,
	0x5b, 0xd2, 0x54, 0x3a, 0x80, 0x58, 0x7e, 0xc1, 0xd2, 0x4c, 0x72, 0x67, 0xbf, 0x55, 0x6a, 0xaf,
	0x7b, 0x8d, 0x55, 0xf8, 0xdc, 0xa5, 0xaf, 0xc8, 0x4e, 0x2c, 0xcc, 0xad, 0xd2, 0x63, 0x96, 0x0a,
	0x3d, 0x11, 0xda, 0x4a, 0x1f, 0xa1, 0xb4, 0x59, 0x10, 0x97, 0x88, 0x9f, 0xbb, 0xf4, 0x11, 0xd9,
	0xca, 0x42, 0xa6, 0xc1, 0x08, 0x67, 0x0d, 0xeb, 0x6e, 0x66, 0xa1, 0x07, 0x46, 0xd0, 0xff, 0x93,
	0x46, 0x16, 0xb2, 0x61, 0xe6, 0x8f, 0x85, 0x61, 0xa9, 0xfc, 0x22, 0x9c, 0x75, 0xe4, 0x6b, 0x59,
	0xd8, 0x47, 0xf0, 0x52, 0x7e, 0x11, 0xf4, 0x07, 0x54, 0x59, 0x3b, 0x4b, 0x54, 0x28, 0xfd, 0x99,
	0xb3, 0xd1, 0x2a, 0xb5, 0x1b, 0xbd, 0x66, 0x07, 0x12, 0xd9, 0xb1, 0x1f, 0x1a, 0x20, 0x6c, 0x6d,
	0xcb, 0x37, 0x5b, 0x95, 0x17, 0x55, 0x1f, 0xe4, 0x55, 0xf9, 0xa2, 0x2a, 0xbf, 0x5b, 0x75, 0x33,
	0xaf, 0xca, 0xef, 0x55, 0xe5, 0x77, 0xab, 0x6e, 0xfd, 0x43, 0x55, 0xbe, 0x5a, 0xf5, 0x1b, 0xd2,
	0x04, 0xce, 0x59, 0x70, 0xcb, 0x22, 0x61, 0x80, 0x83, 0x01, 0xa7, 0xdc, 0x2a, 0xb5, 0xcb, 0x5e,
	0x1d, 0x38, 0xff, 0xf0, 0xf9, 0x42, 0x18, 0x70, 0xc1, 0x00, 0x7d, 0x4d, 0x76, 0xb9, 0x98, 0xb0,
	0xd4, 0x80, 0xc9, 0x52, 0xa6, 0xc5, 0x0d, 0x1b, 0x69, 0x71, 0xe3, 0x54, 0x16, 0xf3, 0x72, 0x89,
	0x8c, 0x27, 0x6e, 0xde, 0x6b, 0x71, 0x43, 0x7f, 0x22, 0x07, 0x5a, 0x24, 0x4a, 0x1b, 0xb6, 0xe2,
	0x1a, 0x82, 0x31, 0x42, 0xcf, 0x1c, 0x82, 0x05, 0xf6, 0x73, 0x81, 0x3b, 0xb7, 0xf6, 0x73, 0x96,
	0xbe, 0x25, 0xce, 0xd7, 0xd6, 0x08, 0x74, 0x20, 0x63, 0xa7, 0x8a, 0xce, 0x87, 0xf7, 0x9c, 0x17,
	0x48, 0xd2, 0x87, 0x64, 0x93, 0x6b, 0x16, 0xc9, 0xd8, 0xa9, 0xe1, 0x5f, 0x3d, 0xe0, 0xfa, 0x62,
	0x09, 0xc3, 0xd4, 0xa9, 0x2f, 0x60, 0x98, 0xd2, 0xe7, 0xa4, 0xe6, 0x5f, 0x43, 0x1c, 0x8b, 0x90,
	0x45, 0x90, 0x8e, 0x9d, 0x46, 0xab, 0xd4, 0xae, 0x79, 0xd5, 0x02, 0xbb, 0x80, 0x74, 0x4c, 0x9f,
	0x12, 0x92, 0x68, 0x06, 0x61, 0xa8, 0x6e, 0x05, 0x77, 0x9a, 0x58, 0xbb, 0x92, 0xe8, 0x77, 0x39,
	0x60, 0xe9, 0xeb, 0x25, 0xbd, 0x9d, 0xd3, 0xd7, 0xab, 0xb4, 0x86, 0x05, 0xbd, 0x93, 0xd3, 0x1a,
	0xe6, 0xf4, 0x11, 0xa9, 0xc6, 0xb7, 0x63, 0x16, 0x08, 0xc5, 0x42, 0xe5, 0x3b, 0x34, 0xe7, 0xe3,
	0xdb, 0xf1, 0x07, 0xa1, 0x3e, 0x2a, 0xdf, 0xda, 0x0d, 0xe8, 0x40, 0x18, 0x96, 0x08, 0xed, 0xec,
	0xe2, 0xaf, 0x57, 0x72, 0x64, 0x70, 0xe6, 0xd1, 0x36, 0xd9, 0x8e, 0x64, 0x6c, 0xe7, 0x8d, 0xcb,
	0x89, 0xd0, 0xa9, 0x34, 0x33, 0x67, 0x0f, 0x45, 0x8d, 0x48, 0xc6, 0x1f, 0x3e, 0xbb, 0x73, 0x94,
	0x3e, 0x23, 0xd5, 0xe0, 0x36, 0x65, 0x89, 0x96, 0x13, 0xbb, 0xb6, 0x1c, 0x2c, 0x44, 0x82, 0xdb,
	0x74, 0x90, 0x23, 0x2f, 0xfe, 0x24, 0xa4, 0xee, 0x8a, 0x7f, 0x9b, 0xd3, 0xff, 0x24, 0x79, 0x6d,
	0xb2, 0x9d, 0x66, 0x89, 0x9d, 0xdc, 0x94, 0xf9, 0x21, 0xa4, 0x29, 0x1b, 0x62, 0x04, 0xcb, 0x5e,
	0x63, 0x8e, 0x9f, 0x5a, 0xb8, 0x6f, 0xd7, 0x6d, 0x21, 0x60, 0x46, 0x46, 0x42, 0x65, 0xa6, 0xc8,
	0x62, 0x1d, 0xe1, 0xfe, 0x55, 0x0e, 0xda, 0x2f, 0x26, 0x32, 0x0e, 0x58, 0x1a, 0x2a, 0xec, 0xa4,
	0x54, 0x1c, 0xe3, 0x58, 0xf7, 0x1a, 0x16, 0xbf, 0x0c, 0x95, 0x19, 0x20, 0x4a, 0x5b, 0xa4, 0xb6,
	0x54, 0x72, 0x5d, 0x84, 0x90, 0xcc, 0x55, 0xae, 0x67, 0x83, 0xb8, 0x54, 0xe0, 0xf2, 0x2f, 0x82,
	0x38, 0xd7, 0xe0, 0xd2, 0xff, 0x7a, 0x0c, 0x3e, 0x46, 0xf1, 0xfe, 0x18, 0x4e, 0x97, 0x63, 0xf0,
	0x17, 0x63, 0x28, 0xaf, 0x8c, 0xe1, 0x74, 0x3e, 0x86, 0x67, 0xa4, 0x1a, 0x81, 0xcf, 0x70, 0x42,
	0x55, 0x8c, 0x99, 0xab, 0x78, 0x24, 0x02, 0xff, 0xb7, 0x1c, 0xa1, 0x1d, 0xb2, 0xab, 0x45, 0xc0,
	0x12, 0xd0, 0x10, 0xd9, 0x70, 0x4e, 0x24, 0x0a, 0x09, 0x0a, 0x77, 0xb4, 0x08, 0x06, 0xc8, 0x78,
	0x05, 0x41, 0x9f, 0x10, 0xa2, 0xa7, 0x8c, 0x8b, 0x10, 0x66, 0xec, 0x18, 0x43, 0x55, 0xf7, 0xca,
	0x7a, 0xea, 0x5a, 0xe0, 0x98, 0xbe, 0x24, 0x0d, 0xcb, 0x6a, 0xa6, 0x46, 0xa3, 0x54, 0x18, 0x76,
	0x5c, 0xe4, 0xa9, 0xaa, 0xa7, 0xae, 0xf7, 0x09, 0xb1, 0x63, 0xfa, 0x82, 0xd4, 0xad, 0x08, 0x0c,
	0xe0, 0x96, 0xd3, 0x2b, 0xc2, 0x65, 0x35, 0x60, 0xc0, 0x6e, 0x30, 0x3d, 0x7a, 0x48, 0x2a, 0x7a,
	0x8a, 0x8d, 0x62, 0x3d, 0xcc, 0x57, 0xdd, 0xdb, 0xd2, 0x53, 0xdb, 0xa4, 0x1e, 0x7d, 0x43, 0xf6,
	0x46, 0xe0, 0x1b, 0xa5, 0x67, 0x2c, 0xd1, 0xc2, 0x96, 0xb1, 0xba, 0xd4, 0x69, 0xb6, 0xd6, 0xdb,
	0x75, 0x8f, 0x16, 0xdc, 0x00, 0x29, 0xeb, 0x48, 0xe9, 0x01, 0x29, 0x47, 0x30, 0x65, 0x42, 0xea,
	0x04, 0xc3, 0x56, 0xf7, 0xb6, 0x22, 0x98, 0x9e, 0x9d, 0x7b, 0x03, 0x3b, 0x31, 0x96, 0xe2, 0x99,
	0x99, 0x31, 0x7f, 0xe6, 0x87, 0x02, 0xe3, 0x56, 0xf7, 0x6a, 0x11, 0x4c, 0xdd, 0xcc, 0xcc, 0x4e,
	0x2d, 0x46, 0x5f, 0x92, 0xfa, 0x62, 0x62, 0xfe, 0x50, 0x32, 0x2e, 0x32, 0x57, 0x9b, 0x83, 0xbf,
	0x28, 0x19, 0xd3, 0xc7, 0xa4, 0xa2, 0x47, 0x4c, 0x8b, 0xc0, 0x36, 0x70, 0x17, 0x1b, 0x58, 0xd6,
	0x23, 0x0f, 0xdf, 0x69, 0x97, 0xec, 0x2d, 0xbe, 0x70, 0xd2, 0x1b, 0x4a, 0xc3, 0x46, 0xcc, 0x8f,
	0x0d, 0x06, 0xaf, 0xec, 0xed, 0xcc, 0xb9, 0x93, 0x5e, 0x5f, 0x9a, 0xf7, 0xa7, 0xb1, 0xb1, 0x25,
	0x13, 0x98, 0x85, 0x0a, 0x38, 0xf3, 0x15, 0x17, 0x3e, 0xa6, 0xaf, 0xe2, 0xd5, 0x0a, 0xf0, 0xd4,
	0x62, 0xf4, 0x7b, 0xb2, 0x3f, 0x17, 0x89, 0xd8, 0xca, 0x34, 0x4b, 0x7d, 0x2d, 0x13, 0xe3, 0x1c,
	0xa0, 0x7a, 0xaf, 0x60, 0xcf, 0x72, 0xf2, 0x12, 0xb9, 0x55, 0x17, 0x17, 0x77, 0x5c, 0x87, 0x77,
	0x5c, 0xae, 0x58, 0x75, 0xbd, 0x22, 0x3b, 0x81, 0x50, 0xa1, 0xf2, 0xd9, 0x30, 0x1b, 0x8d, 0x84,
	0x66, 0xc6, 0x84, 0xc5, 0xe1, 0xda, 0xcc, 0x89, 0x3e, 0xe2, 0x57, 0x57, 0x1f, 0xe9, 0x09, 0xd9,
	0x2f, 0xb4, 0x76, 0xa7, 0x29, 0xf4, 0x78, 0xfe, 0x3c, 0x41, 0xc3, 0x6e, 0xce, 0x5e, 0xc8, 0x38,
	0xf7, 0xe0, 0x31, 0xf4, 0x86, 0x6c, 0x18, 0x08, 0x52, 0xe7, 0x69, 0x6b, 0xbd, 0x5d, 0xed, 0x3d,
	0xc1, 0xc3, 0xe7, 0xce, 0xe6, 0xd2, 0xb9, 0x82, 0x20, 0x3d, 0x8b, 0x8d, 0x9e, 0x79, 0xa8, 0xa4,
	0x7d, 0xd2, 0xcc, 0x92, 0x50, 0xc6, 0x63, 0x26, 0x63, 0x23, 0xf4, 0x04, 0x42, 0xe7, 0xa8, 0x55,
	0x6a, 0x57, 0x7b, 0x07, 0x9d, 0xfc, 0x86, 0xd1, 0x99, 0xdf, 0x30, 0x3a, 0x6e, 0x71, 0xc3, 0xf0,
	0x1a, 0xb9, 0xe3, 0xbc, 0x30, 0xd8, 0xcc, 0x01, 0xb7, 0x7b, 0x71, 0xa0, 0xb4, 0x34, 0xd7, 0x91,
	0xdd, 0x62, 0x9e, 0x61, 0x1b, 0x1a, 0xc0, 0xf5, 0xbb, 0x39, 0x7c, 0xee, 0x1e, 0xbe, 0x25, 0x95,
	0xc5, 0x0f, 0xd0, 0x6d, 0xb2, 0x3e, 0x16, 0xb3, 0x62, 0xa3, 0xb3, 0x8f, 0x74, 0x8f, 0x3c, 0x98,
	0x40, 0x98, 0xe5, 0x07, 0x7f, 0xc5, 0xcb, 0x5f, 0x7e, 0x5e, 0xfb, 0xb1, 0xf4, 0xaa, 0x45, 0xc8,
	0xca, 0xb1, 0x59, 0x26, 0x1b, 0xae, 0xf7, 0x69, 0xb0, 0xfd, 0x3f, 0xfb, 0x74, 0xf1, 0xce, 0xfb,
	0x75, 0xbb, 0xd4, 0x8f, 0xc8, 0x73, 0xa9, 0x3a, 0xfe, 0xb5, 0xd4, 0x49, 0x6a, 0xc0, 0x1f, 0xe3,
	0xd8, 0x21, 0xed, 0xcc, 0x6f, 0x52, 0xf6, 0xbd, 0x5f, 0x2f, 0xda, 0x90, 0x0e, 0xec, 0xa0, 0x06,
	0xa5, 0xdf, 0xdf, 0x06, 0xd2, 0x5c, 0x67, 0xc3, 0x8e, 0xaf, 0xa2, 0xee, 0x50, 0x2b, 0x1f, 0x40,
	0x77, 0x97, 0xdf, 0x78, 0x6d, 0x6f, 0x5f, 0x81, 0xea, 0x4e, 0x4e, 0xba, 0xf7, 0xee, 0x64, 0xc3,
	0x4d, 0x6c, 0xcb, 0xc9, 0xdf, 0x01, 0x00, 0x00, 0xff, 0xff, 0x08, 0x23, 0x28, 0x05, 0xad, 0x09,
	0x00, 0x00,
}
