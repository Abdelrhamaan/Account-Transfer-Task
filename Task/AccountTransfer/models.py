from decimal import Decimal
from django.db import models


class Accounts(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"{self.name} : {self.balance}"
