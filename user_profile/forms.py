from django import forms

class ChangeProfile(forms.Form):
    bio = forms.CharField(label="bio",widget=forms.Textarea(attrs={"rows":"5"}))

ratings = (
    (1, "1 Sangat Buruk"),
    (2, "2 Buruk"),
    (3, "3 Cukup"),
    (4, "4 Baik"),
    (5, "5 Sangat Baik")
)

class RatingForm(forms.Form):
    rating = forms.ChoiceField(choices= ratings)
    comment = forms.CharField(label="comment",widget=forms.Textarea(attrs={"rows":"4"}))