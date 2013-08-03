# -*- coding: utf-8 -*-
from django import forms

from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from iupload.models import Images

class ImagesForm(forms.ModelForm):

	def clean_file(self):
	    content = self.cleaned_data['file']
	    content_type = content.content_type.split('/')[0]
	    if content_type in settings.CONTENT_TYPES:
	        if content._size > settings.MAX_UPLOAD_SIZE:
	            raise forms.ValidationError(u'Размер файла должен быть не больше %s. Текущий размер %s' % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
	    else:
	        raise forms.ValidationError(u'Не поддерживаемый тип загружаемого файла')

	    return content

	class Meta:
		model = Images


