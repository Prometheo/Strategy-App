from django.db import models
from django.utils.translation import gettext_lazy as _
from tenant_schemas.models import TenantMixin
# Create your models here.

class Company(TenantMixin):
    name = models.CharField(_("company name"),max_length=250)
    created_on = models.DateField(auto_now_add=True)
    on_trial = models.BooleanField()
    paid_until = models.DateField()
    auto_create_schema = True
