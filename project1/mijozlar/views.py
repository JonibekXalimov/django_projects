from django.shortcuts import render
from .models import Mijoz

def mijozlar_list(request):
    mijozlar = Mijoz.objects.all()
    return render(request,'mijozlar.html', {'mijozlar': mijozlar})


