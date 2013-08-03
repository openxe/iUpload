import os

from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from iupload.forms import ImagesForm
from iupload.models import Images


def index(request):
    ''' Render main page with images list '''

    images = Images.objects.all()

    return render(request, 'index.html', {'images': images,})

def upload(request):
    ''' Upload images '''
    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            render(request, 'upload.html', {'form': form,} )
    else:
        form = ImagesForm()

    return render(request, 'upload.html', {'form': form,} )


