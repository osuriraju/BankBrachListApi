from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class BanksList(models.Model):
    ifsc = models.CharField(_("ifsc"),max_length=50)
    bank_id = models.CharField(_("bank_id"),max_length=250)
    branch = models.CharField(_("branch"),max_length=250)
    address = models.CharField(_("address"),max_length=350)
    city = models.CharField(_("city"),max_length=350)
    district = models.CharField(_("district"),max_length=450)
    state = models.CharField(_("state"),max_length=350)
    bank_name = models.CharField(_("bank_name"),max_length=450)
