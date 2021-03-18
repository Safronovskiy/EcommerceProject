from django import forms
from .models import *


class AddCategoryProductForm(forms.ModelForm):
    class Meta:
        model = CategoryProductModel
        fields = "__all__"
























