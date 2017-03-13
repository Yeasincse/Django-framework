from django.db import models

# Create your models here.
class Expense(models.Model):
	purpose=models.CharField(max_length=100)
	amount=models.IntegerField()
	date=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.purpose
	def __unique__(self):
		return self.amount
		