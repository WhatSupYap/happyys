# forms.py
from django import forms
from samples.models import Document

class filetestForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'uploaded_file',)
