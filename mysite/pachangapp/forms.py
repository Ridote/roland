from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from datetime import datetime
from .models import *

class UserForm(forms.ModelForm):
	def __init__(self, user, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['first_name'] = forms.CharField(label='First name', initial=user.user.first_name, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name', 'min': 3, 'max': MODEL_USER_FIRST_NAME}))
		self.fields['last_name'] = forms.CharField(label='Last name', initial=user.user.last_name, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name', 'min': 3, 'max': MODEL_USER_LAST_NAME}))
		self.fields['known_as'] = forms.CharField(label='Known as', initial=user.known_as, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Known as', 'min': 3, 'max': MODEL_USER_KNOWN_AS}))
	class Meta:
		model = User
		fields = ('known_as',)
class StatsForm(forms.ModelForm):
	def __init__(self, user, choices, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['group'] = forms.ChoiceField(label='Group', choices=choices, widget=forms.SelectInput(attrs={'class': 'form-control',}))
	class Meta:
		fields = ('user',)