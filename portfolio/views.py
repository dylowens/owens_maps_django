from django.shortcuts import render
from .models import Work

def portfolio(request):
    works = Work.objects.all()
    return render(request, 'portfolio/portfolio.html', {'works': works})
