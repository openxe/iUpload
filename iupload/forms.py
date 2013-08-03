from django import forms
from iupload.models import Images


class ImagesForm(forms.ModelForm):
	class Meta:
		model = Images