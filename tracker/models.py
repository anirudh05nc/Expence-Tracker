from django.db import models

# Create your models here.
class CurrentBalance(models.Model):
    current_balance = models.FloatField(default = 0)

class TrackingHistory(models.Model):
    current_balance = models.ForeignKey(CurrentBalance, on_delete=models.CASCADE)
    amount = models.FloatField()
    expense_type = models.CharField(choices=(('CREDIT', 'CREDIT'),('DEBIT','DEBIT')), max_length=10)
    description = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=True)