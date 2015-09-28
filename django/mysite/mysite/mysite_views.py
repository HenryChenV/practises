#-*-coding=utf-8-*-

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.core.cache import cache
from django.views.decorators.cache import cache_page

import datetime
import json
import random
import time


#@cache_page(60)  # maybe better to do this in urls.py
def test_cache_page(request):
    time.sleep(3)
    return render_to_response('mysite/test_cache_page.html')

#@cache_page(60)
def test_database_caching(request):
    random_id = random.choice(range(10))
    if cache.has_key(random_id):
        now = cache.get(random_id)
    else:
        time.sleep(3)
        now = str(datetime.datetime.now())
        cache.set(random_id, now, 60)
    return HttpResponse(json.dumps({random_id: now}))

def mytime(request):
    current_date = datetime.datetime.now()
    return render_to_response(
        'mysite/test_context_proc.html',
        {'current_date': current_date},
        context_instance=RequestContext(request)
    )


def error_500(request):
    return render_to_response('error/500.html')

def error_404(request):
    return render_to_response('error/404.html')
