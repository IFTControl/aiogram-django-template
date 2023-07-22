from django.contrib import admin
from django.contrib.admin import ModelAdmin

from app.apps.cryptotransaction.models import ExampleCryptotransactionModel


@admin.register(ExampleCryptotransactionModel)
class CryptotransactionAdmin(ModelAdmin[ExampleCryptotransactionModel]):
    pass
