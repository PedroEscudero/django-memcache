from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core.cache import cache
import json
from thing.connector import Connector

class Middleware(View):
    def get(self, request):
        cache_key = 'sample_keyy'
        cache_time = 7200
        data = cache.get(cache_key)
        if not data:
            connector = Connector().call_endpoints()
            data = json.dumps(connector)
            cache.set(cache_key, data, cache_time)
        response = HttpResponse(data)
        response ['content-type'] = 'application/json'
        response ['Cache-Control'] =  'no-cache'
        return response
