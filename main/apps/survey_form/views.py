from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import *
# Create your views here.

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['name'] = 'name'
    request.session['location'] = 'location'
    request.session['language'] = 'language'
    request.session['comment'] = 'comment'
    request.session['counter'] += 1


    
    return render(request,'survey_form/index.html')
def result(request):
    
    return render(request, 'survey_form/result.html')
# def reset(request):
#    request.session['counter'] = 0
#    return redirect('surveys/process') 
# this could be used to reset the counter if needed