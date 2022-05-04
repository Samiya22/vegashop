from email.policy import default
from django.apps import AppConfig


class LeadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoFiled'
    name = 'leads'
