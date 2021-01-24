import logging

from django.utils.deprecation import MiddlewareMixin
from uuid import uuid4


class LogMiddleware(MiddlewareMixin):
    logging.basicConfig(level=logging.INFO)

    def process_view(self, request, view_func, view_args, view_kwargs):
        logging.info("Process request %s for the %s view",
                     request.method, view_func)

        return view_func(request, *view_args, **view_kwargs)

    def process_request(self, request):

        logging.info(request)

    def process_response(self, request, response):

        logging.info(response)

        return response


class RawDataMiddleware(MiddlewareMixin):

    def process_request(self, request):
        hash_value = uuid4()
        request.META["hash_value"] = hash_value


class IdentifyResponseMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        logging.basicConfig(level=logging.INFO)
        logging.info("hash value: %s", request.META["hash_value"])
        return response
