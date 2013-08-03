# -*- coding: utf-8 -*-
import os
import StringIO
from PIL import Image

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.urlresolvers import reverse

from iupload.forms import ImagesForm
from iupload.models import Images


def index(request):
    ''' Render main page with images list '''

    images = Images.objects.all()

    return render(request, 'index.html', {'images': images,})

def upload(request, uploaded=False):
    ''' Upload images '''
    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('upload_success')
    else:
        form = ImagesForm()

    return render(request, 'upload.html', {'form': form, 'uploaded': uploaded,} )

def resize(request, width, height, path):
    ''' Resize image and output to client '''

    infile = os.path.join(settings.MEDIA_ROOT, path)

    try:
        img = Image.open(infile)
        img = img.resize((int(width), int(height)), Image.ANTIALIAS)

        response = HttpResponse(mimetype="image/png")
        img.save(response, 'PNG')
        return response
    except:
        return HttpResponse(u'Возникла ошибка при изменение размера иллюстрации.')

