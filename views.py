from django.shortcuts import render,redirect
from .models import cricket
# from .forms import CricketForm

def home(request):
    return render(request,'home.html')
def register(request):
    # if request.method=='POST':
    #     morm=CricketForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('login')
    # else:
    #     form=cricket()
    return render(request,'register.html')

def ground(request):
    return render(request,'ground.html')
def gallery(request):
    return render(request,'gallery.html')

def about(request):
    return render(request,'about.html')
#
def contact(request):
    return render(request,'contact.html')

def search(request):
    return render(request,'search.html')

def login(request):
    return render(request,'login.html')


# Create your views here.
