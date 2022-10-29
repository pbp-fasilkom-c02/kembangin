from django import forms

class ReportForm(forms.Form):
    name = forms.CharField(label="Nama Anak", max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Contoh: Yasmin', 'class': 'form-control bg-red-100 rounded-lg h-10 pl-4 w-full', 'id': 'report-name'}))
    age = forms.CharField(label="Umur Anak", max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Contoh: 3 Tahun', 'class': 'form-control bg-red-100 rounded-lg h-10 pl-4 w-full', 'id': 'report-age'}))
    height = forms.CharField(label="Tinggi Badan Anak", max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Contoh: 130 cm', 'class': 'form-control bg-red-100 rounded-lg h-10 pl-4 w-full', 'id': 'report-height'}))
    weight = forms.CharField(label="Berat Badan Anak", max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Contoh: 30 kg', 'class': 'form-control bg-red-100 rounded-lg h-10 pl-4 w-full', 'id': 'report-weight'}))
    CHOICES = (("Tidak Baik", "Tidak baik"), ("Kurang Baik", "Kurang baik"), ("Cukup Baik", "Cukup baik"), ("Sangat Baik", "Sangat baik"))
    eat = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'bg-red-100 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full p-2', 'id': 'report-eat'}), choices=CHOICES)
    drink = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'bg-red-100 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full p-2', 'id': 'report-drink'}), choices=CHOICES)    
    progress = forms.CharField(label="Permasalahan Pada Anak", widget=forms.Textarea(attrs={'rows': '3', 'placeholder': 'Contoh: Belajar sepeda, Sudah bisa membaca', 'class':'form-control bg-red-100 rounded-lg w-full', 'id': 'report-progress'}))