from dataclasses import field
from socket import fromshare
from django.forms import ModelForm
from .models import Document
from django import forms
from django.contrib.auth.models import User


class DocumentForm(forms.ModelForm):
   
    class Meta():
        model = Document        
        fields = ('author', 'name', 'notes', 'file','doctype')
# class allowed_users(DocumentForm)