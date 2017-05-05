from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from datetime import datetime
from .models import *
from .constants import *
class UserForm(forms.ModelForm):
	def __init__(self, user, *args, **kwargs):
		if not user.country:
			default_country='ND'
		else:
			default_country=user.country
		super(UserForm, self).__init__(*args, **kwargs)
		#self.fields['avatar'] = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
		self.fields['first_name'] = forms.CharField(label='First name', initial=user.user.first_name, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name', 'min': 3, 'max': MODEL_USER_FIRST_NAME}))
		self.fields['last_name'] = forms.CharField(label='Last name', initial=user.user.last_name, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name', 'min': 3, 'max': MODEL_USER_LAST_NAME}))
		self.fields['known_as'] = forms.CharField(label='Known as', initial=user.known_as, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Known as', 'min': 3, 'max': MODEL_USER_KNOWN_AS}))
		self.fields['country'] = forms.ChoiceField(choices=MODEL_USER_COUNTRIES, initial=default_country, label='Country', widget=forms.Select(attrs={'class': 'form-control'}))
		self.fields['avatar'] = forms.ImageField(label='Avatar', initial=user.avatar)
	class Meta:
		model = User
		fields = ('avatar', 'known_as', 'country')
class StatsForm(forms.ModelForm):
	def __init__(self, user, choices, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
	class Meta:
		fields = ('user',)