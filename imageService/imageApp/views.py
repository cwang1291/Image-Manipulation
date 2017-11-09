# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
import os


# Create your views here.
def home(request):
    return render(request, 'index.html', {'what':'Django File Upload'})
 
def handleGETandPOST(request):
    if (request.method == 'GET'): 
        return render(request, 'index.html', {'what':'Django File Upload'})

    if request.method == 'POST':
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