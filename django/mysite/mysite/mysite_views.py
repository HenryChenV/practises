#-*-coding=utf-8-*-

from django.template import RequestContext
from django.shortcuts import render_to_response
import datetime


def time(request):
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
