# IoT Server API (ChirpStack fork)

## mqtt examples

### ernet msg status: relay_on
 mosquitto_pub -h localhost -p 1883 -t "application/561/device/867723030031587/event/up" -m '{"nsID":1,"orgID":101,"deviceName":"STM32_debugger#1","devEUI":"867723030031587","adr":true,"dr":5,"fCnt":190063,"fPort":10,"data":"c195a905dcdeb16601","tags":{},"confirmed":false,"devAddr":"69a5fb72","mic":"9770e7c0","late":false,"time":"2024-08-08T14:25:53.226804552Z","dpID":"2a753a4c-bc9b-4121-8a1e-84566b78cf16","spID":"b2a1d0fc-1782-4d41-837f-a60c29d51516","class":"C","batTime":"2024-02-29T16:34:10.413614Z","batLevel":100,"extPower":false,"noBatLvl":false,"objectJSON":"{\"C_PM\":1.5,\"C_SI\":100,\"C_SSU\":\"Останов\",\"C_TFA\":0.1,\"C_TFB\":0.2,\"C_TFC\":0.3,\"C_V1\":10,\"C_V3\":-5.0,\"C_V5\":3,\"C_VCHPCH\":50.0,\"C_VNAB\":380,\"C_VNBC\":370,\"C_VNCA\":360,\"device\":\"Thingenix RS485\"}","rxInfo":[{"gatewayID":"46584254c0001614","rssi":-25,"loRaSNR":8.75,"channel":0,"location":{"latitude":55,"longitude":38,"altitude":0,"source":"UNKNOWN","accuracy":0},"fineTimestampType":"NONE","context":"00000000000000000055000096618fdb","uplinkID":"123233025d304f9e86633c561a61f6e0"}]}'
### ernet msg status: relay_off
mosquitto_pub -h localhost -p 1883 -t "application/561/device/867723030031587/event/up" -m 
'{"nsID":1,"orgID":101,"deviceName":"STM32_debugger#1","devEUI":"867723030031587","adr":true,"dr":5,"fCnt":190063,"fPort":10,"data":"c195a905dcdeb16600","tags":{},"confirmed":false,"devAddr":"69a5fb72","mic":"9770e7c0","late":false,"time":"2024-08-08T14:25:53.226804552Z","dpID":"2a753a4c-bc9b-4121-8a1e-84566b78cf16","spID":"b2a1d0fc-1782-4d41-837f-a60c29d51516","class":"C","batTime":"2024-02-29T16:34:10.413614Z","batLevel":100,"extPower":false,"noBatLvl":false,"objectJSON":"{\"C_PM\":1.5,\"C_SI\":100,\"C_SSU\":\"Останов\",\"C_TFA\":0.1,\"C_TFB\":0.2,\"C_TFC\":0.3,\"C_V1\":10,\"C_V3\":-5.0,\"C_V5\":3,\"C_VCHPCH\":50.0,\"C_VNAB\":380,\"C_VNBC\":370,\"C_VNCA\":360,\"device\":\"Thingenix RS485\"}","rxInfo":[{"gatewayID":"46584254c0001614","rssi":-25,"loRaSNR":8.75,"channel":0,"location":{"latitude":55,"longitude":38,"altitude":0,"source":"UNKNOWN","accuracy":0},"fineTimestampType":"NONE","context":"00000000000000000055000096618fdb","uplinkID":"123233025d304f9e86633c561a61f6e0"}]}'


![Tests](https://github.com/brocaar/chirpstack-api/actions/workflows/main.yml/badge.svg?branch=master)

This repository contains the [Protobuf](https://developers.google.com/protocol-buffers/)
and [gRPC](https://grpc.io/) API definitions for the [ChirpStack](https://www.chirpstack.io)
components.

## Protobuf / gRPC structure

```
protobuf             - Protobuf and gRPC source files
├── as
│   ├── external
│   │   └── api      - Application Server External API definitions
│   └── integration  - Application Server integration definitions
├── common           - Definitions shared across ChirpStack components
├── geo              - Geolocation Server API definitions
├── gw               - LoRa gateway definitions
├── nc               - Network Controller definitions
└── ns               - Network Server definitions
```

## Supported languages

### Go

Documentation: https://godoc.org/github.com/brocaar/chirpstack-api/go

```bash
go get github.com/brocaar/chirpstack-api/go/v3
```

### JavaScript / Typescript

See: https://www.npmjs.com/package/@chirpstack/chirpstack-api.

### Python

See: https://pypi.org/project/chirpstack-api/.

### Rust

See: https://crates.io/crates/chirpstack_api.

### Java

See the README in /java subfolder: https://github.com/brocaar/chirpstack-api/tree/master/java.

## Generating client libraries

These instructions require [Docker](https://docs.docker.com/install/) and
[Docker Compose](https://docs.docker.com/compose/install/) to be installed.

```bash
# (re)generate all client libraries
make all

# only (re)generate go client library and swagger
make go

# only (re)generate JavaScript / Typescript
make js

# only (re)generate Python client library
make python

# only (re)generate Java definitions
make java
```
