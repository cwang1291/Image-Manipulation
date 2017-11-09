# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
import os
import datetime
from django.core.files.images import get_image_dimensions
from PIL import Image as PIL
from .models import Image
import json
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers





# Create your views here.
def home(request):
    return render(request, 'index.html', {'what':'Django File Upload'})

 
def find():
    response_data = []
    image_list = Image.objects.all()
    for im in image_list:
        obj = {}
        obj['image_size'] = im.image_size
        obj['image_type'] = im.image_type
        obj['id'] = im.id
        obj['image_width'] = im.image_width
        obj['image_height'] = im.image_height
        obj['uploaded_time'] = str(im.created_at)
        response_data.append(obj);
    return response_data

def findOne(id):
    try:
        im = Image.objects.get(id=id)
        print im
        response_data = {}
        response_data['image_size'] = im.image_size
        response_data['image_type'] = im.image_type
        response_data['id'] = im.id
        response_data['image_width'] = im.image_width
        response_data['image_height'] = im.image_height
        response_data['uploaded_time'] = str(im.created_at)
        return response_data
    except ObjectDoesNotExist:
        return None

def handleCRUD(request, id=None):

    if (request.method == 'GET'): 
        if not (id is None):
            response_data = findOne(id)
            if not (response_data is None):
                return HttpResponse(json.dumps(response_data))
            else:
                return HttpResponseNotFound('id does not exist')
        else: 
            response_data = find()
            return HttpResponse(json.dumps(response_data))




    if request.method == 'POST':
        try: 
            im = PIL.open(request.FILES['file'])
            if im.format not in ('PNG', 'JPEG'):
                return HttpResponseBadRequest('invalid image type') 
        except Exception:
            return HttpResponseBadRequest('please upload an image file')

        image_type = request.FILES['file'].content_type.split('/')[1]
        image_size = request.FILES['file']._size
        w, h = get_image_dimensions(request.FILES['file'])
        now = datetime.datetime.now()

        Image.objects.create(image=request.FILES['file'], image_type=image_type, image_size=image_size, image_width=w, image_height=h)


        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse("Successful")

    return HttpResponse("Failed")



def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
 
    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)