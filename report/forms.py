from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name', 'age', 'height', 'weight', 'eat', 'drink', 'progress']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Contoh: Yasmin', 'class': 'form-control bg-red-100 rounded-lg h-10 pl-4 w-full', 'id': 'report-name'}),
            'age': forms.TextInput(attrs={'placeholder': 'Contoh: 3 Tahun', 'class': 'form-control bg-red-100 rounded-lg h-10 pl-4 w-full', 'id': 'report-age'}),
            'height': forms.TextInput(attrs={'placeholder': 'Contoh: 145 cm', 'class': 'form-control bg-red-100 rounded-lg h-10 pl-4 w-full', 'id': 'report-height'}),
            'weight': forms.TextInput(attrs={'placeholder': 'Contoh: 50 kg', 'class': 'form-control bg-red-100 rounded-lg h-10 pl-4 w-full', 'id': 'report-weight'}),
            'eat': forms.Select(attrs={'class': 'bg-red-100 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full p-2', 'id': 'report-eat'}),
            'drink': forms.Select(attrs={'class': 'bg-red-100 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full p-2', 'id': 'report-drink'}),
            'progress': forms.Textarea(attrs={'rows': '3', 'placeholder': 'Contoh: Belajar sepeda, Sudah bisa membaca', 'class':'form-control bg-red-100 rounded-lg w-full', 'id': 'report-progress'})
        }