# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v5.proto.services import invoice_service_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_invoice__service__pb2


class InvoiceServiceStub(object):
    """Proto file describing the Invoice service.

    A service to fetch invoices issued for a billing setup during a given month.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListInvoices = channel.unary_unary(
                '/google.ads.googleads.v5.services.InvoiceService/ListInvoices',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_invoice__service__pb2.ListInvoicesRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_invoice__service__pb2.ListInvoicesResponse.FromString,
                )


class InvoiceServiceServicer(object):
    """Proto file describing the Invoice service.

    A service to fetch invoices issued for a billing setup during a given month.
    """

    def ListInvoices(self, request, context):
        """Returns all invoices associated with a billing setup, for a given month.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InvoiceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListInvoices': grpc.unary_unary_rpc_method_handler(
                    servicer.ListInvoices,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_invoice__service__pb2.ListInvoicesRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_invoice__service__pb2.ListInvoicesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v5.services.InvoiceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InvoiceService(object):
    """Proto file describing the Invoice service.

    A service to fetch invoices issued for a billing setup during a given month.
    """

    @staticmethod
    def ListInvoices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.InvoiceService/ListInvoices',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_invoice__service__pb2.ListInvoicesRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_invoice__service__pb2.ListInvoicesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)