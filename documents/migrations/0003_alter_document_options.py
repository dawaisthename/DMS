# Generated by Django 4.0.6 on 2022-08-14 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_rename_uploaded_time_document_uploaded_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['-uploaded_date']},
        ),
    ]
