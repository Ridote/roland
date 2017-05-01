from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from datetime import datetime
from .models import *

class PublicationForm(forms.ModelForm):
	time = forms.TimeField(label=' ', input_formats=['%H:%M'], widget=forms.TimeInput(attrs={'class': 'form-control', 'type':'time'}))
	date = forms.DateField(label='Date', input_formats=['%Y-%m-%d'], widget=forms.TimeInput(attrs={'class': 'form-control', 'type':'date'}))
	def __init__(self, *args, **kwargs):
		super(PublicationForm, self).__init__(*args, **kwargs)
		self.fields['title'].label = "Title"
		self.fields['content'].label = ""
	class Meta:
		model = Publication
		fields = ('title', 'date', 'time', 'content')
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'min': 3, 'max': MODEL_PUBLICATION_TITLE_LENGTH}),
			'content': SummernoteWidget(attrs={'placeholder': 'Enter name'})
		}