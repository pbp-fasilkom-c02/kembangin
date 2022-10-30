from django import forms

class ChangeProfile(forms.Form):
    bio = forms.CharField(label="bio",widget=forms.Textarea(attrs={"rows":"5"}))

ratings = (
    (1, "1 Worst"),
    (2, "2 Bad"),
    (3, "3 Good"),
    (4, "4 Great"),
    (5, "5 Amazing")
)

class RatingForm(forms.Form):
    rating = forms.ChoiceField(choices= ratings)
    comment = forms.CharField(label="comment",widget=forms.Textarea(attrs={"rows":"4"}))