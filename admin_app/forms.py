from django import forms
from admin_app.models import product_item

class product_form(forms.ModelForm):
    class Meta:
        model=product_item
        fields="__all__"