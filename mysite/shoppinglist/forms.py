from django import forms

from .models import Product, Unity, PredefinedProduct

class ProductForm(forms.ModelForm):
	name = forms.ModelChoiceField(queryset=PredefinedProduct.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
	unity = forms.ModelChoiceField(queryset=Unity.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
	def __init__(self, *args, **kwargs):
		super(ProductForm, self).__init__(*args, **kwargs)
		self.fields['quantity'].label = "Product quantity"
		self.fields['name'].label = "Product name"
	class Meta:
		model = Product
		fields = ('name', 'quantity', 'unity')
		widgets = {
			'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity', 'min': 0, 'max': 1000})
		}