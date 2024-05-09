from django.db import models


class Expense(models.Model):
    title = models.CharField(max_length=128)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    date = models.DateField()

    def __str__(self) -> str:
        return f'[#{self.id}] {self.title} @ {self.date} {self.amount}'
