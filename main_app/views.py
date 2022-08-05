from django.shortcuts import render
from django.http import HttpResponse


class Finch:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Lolo', 'tabby', 'foul little demon', 3),
  Finch('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Finch('Raven', 'black tripod', '3 legged finch', 4)
]


# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
    return render(request,'finches/index.html', {
        'finches': finches
    })