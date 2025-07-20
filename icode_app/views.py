from django.shortcuts import render
from django.views.generic import TemplateView
from icode_app.forms import *
# Create your views here.
class Homeview(TemplateView):
    template_name="Feast.html"

def home(request):
    return render(request, 'Feast.html')

def order(request):
    return render(request, 'order.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def table(request):
    return render(request, 'table.html')

def menu(request):
    return render(request, 'menu.html')

def Privacy_Policy(request):
    return render(request, 'Privacy_Policy.html')



def insertcontact(request):
      if request.method=='POST':
           form=contactform(request.POST)
           if form.is_valid():
                 form.save()
           return render(request,"contact.html")
      
def insertreservation(request):
    if request.method=='POST':
           form=reservationform(request.POST)
           if form.is_valid():
                 form.save()
           return render(request,"table.html")