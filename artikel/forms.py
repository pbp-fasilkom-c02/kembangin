from django import forms

class ReplyThread(forms.Form):
    comment = forms.CharField(label='comment', max_length=150,widget=forms.Textarea(attrs={"rows":"5"}))