from django import forms

class ChangeProfile(forms.Form):
    bio = forms.CharField(label="bio",widget=forms.Textarea(attrs={"rows":"5", "class": "bg-red-100 rounded px-4 pt-2 mt-1 w-full"}))

ratings = (
    (1, "1 Sangat Buruk"),
    (2, "2 Buruk"),
    (3, "3 Cukup"),
    (4, "4 Baik"),
    (5, "5 Sangat Baik")
)

class RatingForm(forms.Form):
    rating = forms.ChoiceField(choices= ratings, widget = forms.Select(attrs={"class": "bg-red-100 rounded h-10 px-4 mt-1"}))
    comment = forms.CharField(label="comment",widget=forms.Textarea(attrs={"rows":"4", "class": "bg-red-100 rounded px-4 pt-2 mt-1"}))