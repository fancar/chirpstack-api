# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from chirpstack_api.as_pb import as_pb_pb2 as chirpstack__api_dot_as__pb_dot_as__pb__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ApplicationServerServiceStub(object):
    """ApplicationServerService is the service providing the application-server interface.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HandleUplinkData = channel.unary_unary(
                '/as.ApplicationServerService/HandleUplinkData',
                request_serializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.HandleUplinkDataRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.HandleProprietaryUplink = channel.unary_unary(
                '/as.ApplicationServerService/HandleProprietaryUplink',
                request_serializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.HandleProprietaryUplinkRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.HandleError = channel.unary_unary(
                '/as.ApplicationServerService/HandleError',
                request_serializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.HandleErrorRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.HandleDownlinkACK = channel.unary_unary(
                '/as.ApplicationServerService/HandleDownlinkACK',
                request_serializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.HandleDownlinkACKRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.HandleGatewayStats = channel.unary_unary(
                '/as.ApplicationServerService/HandleGatewayStats',
                request_serializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.HandleGatewayStatsRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.HandleTxAck = channel.unary_unary(
                '/as.ApplicationServerService/HandleTxAck',
                request_serializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.HandleTxAckRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SetDeviceStatus = channel.unary_unary(
                '/as.ApplicationServerService/SetDeviceStatus',
                request_serializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.SetDeviceStatusRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SetDeviceLocation = channel.unary_unary(
                '/as.ApplicationServerService/SetDeviceLocation',
                request_serializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.SetDeviceLocationRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetDevicesSummary = channel.unary_unary(
                '/as.ApplicationServerService/GetDevicesSummary',
                request_serializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.GetDevicesSummaryRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.GetDevicesSummaryResponse.FromString,
                )
        self.GetGatewaysSummary = channel.unary_unary(
                '/as.ApplicationServerService/GetGatewaysSummary',
                request_serializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.GetGatewaysSummaryRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.GetGatewaysSummaryResponse.FromString,
                )
        self.ListOrganisation = channel.unary_unary(
                '/as.ApplicationServerService/ListOrganisation',
                request_serializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.ListOrganizationRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.ListOrganizationResponse.FromString,
                )


class ApplicationServerServiceServicer(object):
    """ApplicationServerService is the service providing the application-server interface.
    """

    def HandleUplinkData(self, request, context):
        """HandleUplinkData handles uplink data received from an end-device.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HandleProprietaryUplink(self, request, context):
        """HandleProprietaryUplink handles proprietary uplink payloads.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HandleError(self, request, context):
        """HandleError handles an error message.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HandleDownlinkACK(self, request, context):
        """HandleDownlinkACK handles a downlink ACK or nACK response.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HandleGatewayStats(self, request, context):
        """HandleGatewayStats handles the given gateway stats.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HandleTxAck(self, request, context):
        """HandleTXACK handles the TX acknowledgement.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDeviceStatus(self, request, context):
        """SetDeviceStatus updates the device-status for a device.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDeviceLocation(self, request, context):
        """SetDeviceLocation updates the device-location for a device.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDevicesSummary(self, request, context):
        """SetDeviceLocation updates the device-location for a device.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGatewaysSummary(self, request, context):
        """SetDeviceLocation updates the device-location for a device.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOrganisation(self, request, context):
        """SetDeviceLocation updates the device-location for a device.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ApplicationServerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HandleUplinkData': grpc.unary_unary_rpc_method_handler(
                    servicer.HandleUplinkData,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.HandleUplinkDataRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'HandleProprietaryUplink': grpc.unary_unary_rpc_method_handler(
                    servicer.HandleProprietaryUplink,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.HandleProprietaryUplinkRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'HandleError': grpc.unary_unary_rpc_method_handler(
                    servicer.HandleError,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.HandleErrorRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'HandleDownlinkACK': grpc.unary_unary_rpc_method_handler(
                    servicer.HandleDownlinkACK,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.HandleDownlinkACKRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'HandleGatewayStats': grpc.unary_unary_rpc_method_handler(
                    servicer.HandleGatewayStats,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.HandleGatewayStatsRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'HandleTxAck': grpc.unary_unary_rpc_method_handler(
                    servicer.HandleTxAck,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.HandleTxAckRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SetDeviceStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDeviceStatus,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.SetDeviceStatusRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SetDeviceLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDeviceLocation,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.SetDeviceLocationRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetDevicesSummary': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDevicesSummary,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.GetDevicesSummaryRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.GetDevicesSummaryResponse.SerializeToString,
            ),
            'GetGatewaysSummary': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGatewaysSummary,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.GetGatewaysSummaryRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.GetGatewaysSummaryResponse.SerializeToString,
            ),
            'ListOrganisation': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOrganisation,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.ListOrganizationRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_as__pb__pb2.ListOrganizationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'as.ApplicationServerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ApplicationServerService(object):
    """ApplicationServerService is the service providing the application-server interface.
    """

    @staticmethod
    def HandleUplinkData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/as.ApplicationServerService/HandleUplinkData',
            chirpstack__api_dot_as__pb_dot_as__pb__pb2.HandleUplinkDataRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HandleProprietaryUplink(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/as.ApplicationServerService/HandleProprietaryUplink',
            chirpstack__api_dot_as__pb_dot_as__pb__pb2.HandleProprietaryUplinkRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HandleError(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/as.ApplicationServerService/HandleError',
            chirpstack__api_dot_as__pb_dot_as__pb__pb2.HandleErrorRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HandleDownlinkACK(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/as.ApplicationServerService/HandleDownlinkACK',
            chirpstack__api_dot_as__pb_dot_as__pb__pb2.HandleDownlinkACKRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HandleGatewayStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/as.ApplicationServerService/HandleGatewayStats',
            chirpstack__api_dot_as__pb_dot_as__pb__pb2.HandleGatewayStatsRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HandleTxAck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/as.ApplicationServerService/HandleTxAck',
            chirpstack__api_dot_as__pb_dot_as__pb__pb2.HandleTxAckRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetDeviceStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/as.ApplicationServerService/SetDeviceStatus',
            chirpstack__api_dot_as__pb_dot_as__pb__pb2.SetDeviceStatusRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetDeviceLocation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/as.ApplicationServerService/SetDeviceLocation',
            chirpstack__api_dot_as__pb_dot_as__pb__pb2.SetDeviceLocationRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDevicesSummary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/as.ApplicationServerService/GetDevicesSummary',
            chirpstack__api_dot_as__pb_dot_as__pb__pb2.GetDevicesSummaryRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_as__pb__pb2.GetDevicesSummaryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGatewaysSummary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/as.ApplicationServerService/GetGatewaysSummary',
            chirpstack__api_dot_as__pb_dot_as__pb__pb2.GetGatewaysSummaryRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_as__pb__pb2.GetGatewaysSummaryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOrganisation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/as.ApplicationServerService/ListOrganisation',
            chirpstack__api_dot_as__pb_dot_as__pb__pb2.ListOrganizationRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_as__pb__pb2.ListOrganizationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
