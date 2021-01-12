import logging

import faker
from django.utils.deprecation import MiddlewareMixin
from uuid import uuid4

class LogMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        logging.basicConfig(level=logging.INFO)
        logging.info("process {}".format(view_func))

        return view_func(request, *view_args, **view_kwargs)

    def process_request(self, request):

        print(request)

    def process_response(self, request, response):

        print(response)

        return response


class RawDataMiddleware(MiddlewareMixin):

    def process_request(self, request):
        hash_value = uuid4()
        request.META["hash_value"] = hash_value


class IdentifyResponseMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        logging.basicConfig(level=logging.INFO)
        logging.info(request.META["hash_value"])
        return response



