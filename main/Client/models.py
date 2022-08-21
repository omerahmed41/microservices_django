from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.utils import timezone, dateformat
import uuid


class Client(models.Model):
    B2C_TYPE = "B2C"
    B2B_CORPORATE_TYPE = "B2B CORPORATE"
    CLIENT_TYPE_CHOICES = [(B2C_TYPE, B2C_TYPE), (B2B_CORPORATE_TYPE, B2B_CORPORATE_TYPE)]

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name='client', null=True)
    client_id = models.UUIDField(default=uuid.uuid4, editable=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    client_type = models.CharField(max_length=200, choices=CLIENT_TYPE_CHOICES, blank=True, null=True, default=B2C_TYPE)
    client_type_detail = models.CharField(max_length=400, blank=True, null=True)
    first_name = models.CharField(max_length=400, blank=True, null=True)
    last_name = models.CharField(max_length=400, blank=True, null=True)

    referral_code = models.CharField(_('Referral Code'), max_length=200, blank=True, null=True, unique=True)
    referral_disabled = models.NullBooleanField(default=False)

    contact_preference = models.CharField(_('contact preference'), max_length=200, blank=True, null=True)

    def __str__(self):
        return "{} ({})".format(self.email, self.short_id)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    @property
    def email(self):
        return self.user and self.user.email

    # official first name and last are the ones provided in the KYC form

    @property
    def full_name(self):
        return '%s %s'%(self.first_name or '??', self.last_name or '??')