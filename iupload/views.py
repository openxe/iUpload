import os

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


