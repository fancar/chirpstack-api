//go:build tools
// +build tools

package tools

import (
	// _ "github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway"
	// _ "github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger"
	_ " github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-openapiv2"
	_ "github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-grpc-gateway"
)
