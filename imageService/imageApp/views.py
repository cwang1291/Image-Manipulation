# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
import os
import datetime
from django.core.files.images import get_image_dimensions


# Create your views here.
def home(request):
    return render(request, 'index.html', {'what':'Django File Upload'})
 
def handleGETandPOST(request):
    if (request.method == 'GET'): 
        return render(request, 'index.html', {'what':'Django File Upload'})

    if request.method == 'POST':
        file_type = request.FILES['file'].content_type.split('/')[1]
        file_size = request.FILES['file']._size
        w, h = get_image_dimensions(request.FILES['file'])
        print 'file type: ', file_type
        print 'filesize: ', file_size
        print 'width: ', w
        print 'height: ', h
        print 'timestamp: ', datetime.datetime.now()
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse("Successful")
 
    return HttpResponse("Failed")

def handlePUTandDELETE(request):
    return HttpResponse("Successful")

def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
 
    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)