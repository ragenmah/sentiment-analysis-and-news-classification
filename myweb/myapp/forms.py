from django import forms
from .models import *

class SearchForm(forms.ModelForm):

	class Meta:
		model = Search
		fields = ('text',)


class ClassifiedTextForm(forms.ModelForm):

	class Meta:
		model = ClassifiedText
		fields = ('text',)