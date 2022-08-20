from django.db import models
from jsignature.fields import JSignatureField
from jsignature.mixins import JSignatureFieldsMixin


# Create your models here.

class DigitalSignature(models.Model):
    name = models.CharField(max_length=200, blank=None, null=True)
    signature = models.ImageField(upload_to='uploads/', )


class SignatureModel(models.Model):
    signature_txt = models.TextField(null=True, blank=True)
    signature = JSignatureField(max_length=1000)


class JSignatureModel(JSignatureFieldsMixin):
    name = models.CharField(max_length=1000)
