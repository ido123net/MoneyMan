from django.db import models

# Create your models here.

class Expense(models.Model):
    title = models.CharField(max_length=128)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    date = models.DateField()
