# forms.py
from django import forms
from samples.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'uploaded_file',)
