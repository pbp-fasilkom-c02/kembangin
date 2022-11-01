import imp
from django import forms

class BmiCalculatorForm(forms.Form):
    height = forms.FloatField(label='Height (cm)', min_value=0, max_value=300)
    weight = forms.FloatField(label='Weight (kg)', min_value=0, max_value=300)
    