from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from datetime import datetime
from .models import *

class PublicationForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PublicationForm, self).__init__(*args, **kwargs)
		self.fields['title'] = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'min': 3, 'max': MODEL_PUBLICATION_TITLE_LENGTH}))
		self.fields['content'] = forms.CharField(label='', widget=SummernoteWidget(attrs={'placeholder': 'Enter name'}))
		self.fields['time'] = forms.TimeField(label=' ', input_formats=['%H:%M'], widget=forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}))
		self.fields['date'] = forms.DateField(label='Date', input_formats=['%Y-%m-%d'], widget=forms.TimeInput(attrs={'class': 'form-control', 'type':'date'}))
	class Meta:
		model = Publication
		fields = ('title', 'content')