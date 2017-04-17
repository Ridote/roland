from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from datetime import datetime
from .models import *
'''
# Activamos el editor Summernote en campos especificos.
class ContactoForm(forms.Form):
	mensaje = forms.CharField(widget=SummernoteWidget())  # en lugar de forms.Textarea

# Si no quieres usar un <iframe>, en tonces debes usar el widget inplace.
# o si estás usando django-crispy-forms, debes usar:
class ContactoForm(forms.Form):
	mensaje = forms.CharField(widget=SummernoteInplaceWidget())
'''


'''
	class ArticuloForm(forms.ModelForm):
	    class Meta:
	        model = Articulo
	        widgets = {
	            'foo': SummernoteWidget(),
	            'bar': SummernoteInplaceWidget(),
	        }



	RECUERDA USAR {{ contenido|safe }}!!
	https://openwebinars.net/blog/para-programadores-django-summernote-el-editor-wysiwyg-que-te-ahorrara-tiempo/        
'''

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