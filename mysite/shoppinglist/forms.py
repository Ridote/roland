from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProductForm, self).__init__(*args, **kwargs)
		self.fields['quantity'].label = "Product quantity"
		self.fields['name'].label = "Product name"
	class Meta:
		model = Product
		fields = ('name', 'quantity')
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
			'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity', 'min': 0, 'max': 1000})
		}