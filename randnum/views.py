from django.shortcuts import render
import random

# Create your views here.

def home(request):
    a = random.randint(0,99999999999)
    context = {
    'randnum':a,
    }
    return render(request,'randnum/index.html',context)
