from django.shortcuts import render
from django.http import HttpResponse

from main_app.models import Finch


# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')


def finches_index(request):
  finches = Finch.objects.all()
  return render(request,'finches/index.html', {
        'finches': finches
    })