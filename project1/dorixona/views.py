from django.shortcuts import render
from .models import Dori

def dorilar_list(request):
    dorilar = Dori.objects.all()
    return render(request, "dorilar_list.html", context={"dorilar": dorilar})


