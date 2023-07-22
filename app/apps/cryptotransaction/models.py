from django.db import models


class ExampleCryptotransactionModel(models.Model):
    """Example model for cryptotransaction app"""

    objects: models.manager.BaseManager["ExampleCryptotransactionModel"]
