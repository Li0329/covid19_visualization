from django.shortcuts import render
from data_show.models import World


# Create your views here.
def show(request):
    return render(request, 'data_show/index.html')


