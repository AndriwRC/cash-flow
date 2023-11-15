from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Transaction(models.Model):
    TRANSACTION_TYPES = (("income", "Income"), ("expense", "Expense"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)

    def is_income(self):
        return self.transaction_type == "income"

    def is_expense(self):
        return self.transaction_type == "expense"
