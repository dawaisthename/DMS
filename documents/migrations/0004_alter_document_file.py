# Generated by Django 4.0.6 on 2022-08-14 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_alter_document_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='Files'),
        ),
    ]
