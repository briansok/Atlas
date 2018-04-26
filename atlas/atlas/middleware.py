from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from location.models import Location

class LocationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response


