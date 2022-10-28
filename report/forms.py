from django import forms

class ReportForm(forms.Form):
    name = forms.CharField(label="Nama Anak", max_length=255, required=True)
    age = forms.CharField(label="Umur Anak", max_length=15, required=True)
    height = forms.CharField(label="Tinggi Badan Anak", max_length=15, required=True)
    weight = forms.CharField(label="Berat Badan Anak", max_length=15, required=True)
    eat = forms.Select(choices=["Tidak baik, Kurang baik, Cukup baik, Sangat baik"])
    drink = forms.Select(choices=["Tidak baik, Kurang baik, Cukup baik, Sangat baik"])    
    progress = forms.CharField(label="Permasalahan Pada Anak", widget=forms.Textarea())