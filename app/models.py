from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=50)

    def __str__(self):
        return str(self.amount)


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=50)

    def __str__(self):
        return str(self.amount)
