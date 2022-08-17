import os
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

# Create your models here.

class Document(models.Model): 
    DOC_TYPE_CHOICES = [
        ('confidential', 'confidential'),
        ('visible', 'visible'),
    ]

        
        
    doctype = models.CharField(max_length=255,choices=DOC_TYPE_CHOICES, default='visible')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255, null=True)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now = True)
    file = models.FileField(null=True,blank=True,upload_to='Files')

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-uploaded_date']

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)
        
    @property
    def extension(self):
        filename, file_extension = os.path.splitext(self.file.url)
        return file_extension


