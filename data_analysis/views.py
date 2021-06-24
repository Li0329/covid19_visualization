from django.shortcuts import render
from data_show.models import China
from django.db.models import Sum


# Create your views here.
def show(request):
    data = China.objects.aggregate(Sum('confirmed'), Sum('cured'), Sum('curConfirmed'), Sum('died'),
                                   Sum('confirmedRelative'))
    mapdata = China.objects.all()
    return render(request, 'data_analysis/index.html', locals())
