from django import forms
from django.forms import Select, Textarea
from .models import *

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order 
        fields = ['address','description']
        widgets = {
			'address':Select(attrs={
				'style': 'width:80%; height:50px; color:black; background:transparent; border: 0px; border-bottom:1px solid black;'
			}),
            'description':Textarea(attrs={
				'style': 'width:100%; color:black; border-bottom:1px solid black;'
			}),
            
		}
