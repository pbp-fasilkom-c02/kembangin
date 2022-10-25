from django import forms

class ForumForm(forms.Form):
    question = forms.CharField(label='Question', max_length=250)
    description = forms.CharField(label='Description',widget=forms.Textarea(attrs={"rows":"5"}))