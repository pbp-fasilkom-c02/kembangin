from django import forms
from artikel.models import Artikel, Comment

class CreateArtikel(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = {"title", "description", "photo"}
    
class ShareExp(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {"comment"}