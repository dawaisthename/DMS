# Generated by Django 4.0.6 on 2022-08-17 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0007_alter_document_allowed_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='allowed_users',
        ),
        migrations.AddField(
            model_name='document',
            name='doctype',
            field=models.CharField(choices=[('confidential', 'confidential'), ('visible', 'visible')], default='visible', max_length=255),
        ),
    ]
