import os

from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from iupload.forms import ImagesForm


def index(request):
    ''' Render main page with images list '''
    return render(request, 'index.html')

def upload(request):
    print settings.MEDIA_ROOT
    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            render(request, 'upload.html', {'form': form,} )
    else:
        form = ImagesForm()

    return render(request, 'upload.html', {'form': form,} )


