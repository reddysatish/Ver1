from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.template import RequestContext, loader
from .models import article
import random
from sqlite3 import Date
def list(request):
    startD='1991-01-01'
    endD=Date.today()

    obj = article.objects.filter( public_date__range=[startD,endD]).order_by('public_date')
    ran_art=random.choice(obj)
#for random articles
    context={'obj':obj}
    context['ran_art']=ran_art



    previeve_list =  article.objects.filter(public_date__range = [startD, endD])
    id_list = previeve_list.values_list('id', flat = True)
    id1 = random.choice(id_list)
    random_article = article.objects.get(id = id1)

    day = random_article.public_date.strftime("%A")
    context['day'] = day

    context['random_article'] = random_article


    #random.shuffle(obj)
    return render(request, 'demo1/list.html', context)
# Create your views here.

# Create your views here.
def desc(request,id):
    obj1=article.objects.get(pk=id)
    return render(request, 'demo1/disc.html', {'obj1' : obj1})
