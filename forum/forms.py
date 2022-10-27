from django import forms

class ForumForm(forms.Form):
    question = forms.CharField(label='Question', max_length=250)
    description = forms.CharField(label='Description',widget=forms.Textarea(attrs={"rows":"5"}))

class ReplyForm(forms.Form):
    comment = forms.CharField(label='Comment', max_length=150,widget=forms.Textarea(attrs={"rows":"5"}))