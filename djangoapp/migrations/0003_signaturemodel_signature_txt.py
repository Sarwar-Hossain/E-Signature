# Generated by Django 4.1 on 2022-08-18 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_jsignaturemodel_signaturemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='signaturemodel',
            name='signature_txt',
            field=models.TextField(blank=True, null=True),
        ),
    ]