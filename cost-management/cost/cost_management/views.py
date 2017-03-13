from django.shortcuts import render

# Create your views here.
from .models import Expense
def ListExpense(request):
	listexpense=Expense.objects.all()
	return render (request, 'all_list.html', {'listexpense':listexpense})
	
