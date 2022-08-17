
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import FileResponse
import os

# Create your views here.


def home(request):    
    if request.user.groups.all()== 'admin':
        qs = Document.objects.all()
    else:
        qs = Document.objects.filter(doctype='visible')
    
    
    count = qs.count()       
    return render(request, 'documents/home.html', {'qs':qs, 'count':count})

@login_required
def upload(request, pk=None):
    if request.method == 'POST':
        user  = User.objects.get(id=pk)
        form = DocumentForm(initial={'author':user})
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('home')

    else:
        form = DocumentForm()

    return render(request, 'documents/upload.html', {'form' : form})
def search(request):
    if request.method == 'POST':
        search =request.POST['search']
        qs=Document.objects.filter(name__icontains=search) | Document.objects.filter(author__username__icontains=search) | Document.objects.filter(notes__icontains=search)
    count = qs.count()
    return render(request, 'documents/search.html', {'qs':qs, 'count':count})
# @login_required
# def read_doc(request):
    
#     with open('media/files', 'rb') as pdf:
#         response = HttpResponse(pdf.read(),content_type='application/pdf')
#         response['Content-Disposition'] = 'inline;filename=MasonLongWalkPJCV.pdf'
#         return response

@login_required
def delete_doc(request, pk):
        doc = Document.objects.get(pk=pk)
        message =''
        if request.user == doc.author:
            doc = Document.objects.get(id=pk)
            doc.delete()
        else:
            messages.info(request,"not allowed")
        return redirect('home')
class DocUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Document
    success_url = '/'
    template_name = 'documents/upload.html'
    fields = ['notes', 'name', 'file']

    def test_func(self):
        Document = self.get_object()
        if self.request.user == Document.author:
            return True
    
        return False