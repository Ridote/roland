from django import forms

from .models import *
from .constants import *

'''
class CategoryTreeWidget(SelectMultiple):
    def render_options(self, choices, selected_choices):
        selected_choices=set([force_unicode(v) for v in selected_choices])
        top_level_cats = Category.objects.filter(parent=None)
        def _render_category_list(cat_list, level=0):
            for category in cat_list:
                self.render_option(selected_choices, category.pk, (("---"*level + " ") if level) + category.name)
                def _render_category_list(category.children, level+1)
        _render_category_list(top_level_cats)
'''

class ProductForm(forms.ModelForm):
	predefinedProduct = forms.ModelChoiceField(queryset=PredefinedProduct.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label=None)
	unit = forms.ModelChoiceField(queryset=Unit.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label=None)
	def __init__(self, *args, **kwargs):
		super(ProductForm, self).__init__(*args, **kwargs)
		self.fields['quantity'].label = "Product quantity"
		self.fields['predefinedProduct'].label = "Product name"
		self.fields['unit'].label = "Product meassurement unit"
	class Meta:
		model = Product
		fields = ('predefinedProduct', 'quantity', 'unit')
		widgets = {
			'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity', 'value': MODEL_PRODUCT_MIN_QUANTITY,'min': MODEL_PRODUCT_MIN_QUANTITY, 'max': MODEL_PRODUCT_MAX_QUANTITY})
		}
class CategoryForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CategoryForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = "Category name"
	class Meta:
		model = Category
		fields = ('name',)
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name', 'min': 3, 'max': MODEL_CATEGORY_NAME_LENGTH})
		}
class ProductTypeForm(forms.ModelForm):
	name = forms.ModelChoiceField(queryset=PredefinedProduct.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label=None)
	unit = forms.ModelChoiceField(queryset=Unit.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label=None)
	def __init__(self, *args, **kwargs):
		super(ProductTypeForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = "Product name"
		self.fields['category'].label = "Product category"
	class Meta:
		model = Product
		fields = ('name', 'quantity', 'unit')
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name', 'min': 3, 'max': 80})
		}