import binascii
import os

from django.db import models
from django.contrib.auth.models import User


class Device(models.Model):
    """
    Requests for iot device Gateway
    """
    name = models.CharField(('Device Name'), max_length=60, help_text=('Device Name'))
    owner = models.ForeignKey(User, verbose_name=("Owner"), on_delete=models.CASCADE)
    api_key = models.CharField(('Api key'), max_length=200, null=True, blank=True)  # api key
    description = models.TextField(('Description'), blank=True, max_length=255)
    enable = models.BooleanField(('Enable'), default=True)
    remote_address = models.GenericIPAddressField(("Ip Address"), protocol="both", unpack_ipv4=False)
    pub_date = models.DateTimeField(('Publish Date'), auto_now=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.api_key:
            self.api_key = self.generate_key()

        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(12)).decode()

