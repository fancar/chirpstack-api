.PHONY: requirements generate

all: requirements generate

requirements:
	@go mod download
	@go install github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-grpc-gateway
	@go install github.com/golang/protobuf/protoc-gen-go
	@go install google.golang.org/grpc/cmd/protoc-gen-go-grpc
	@go install github.com/pseudomuto/protoc-gen-doc/cmd/protoc-gen-doc
	@go install github.com/bufbuild/buf/cmd/buf

generate:
	@cd .. ; buf generate
