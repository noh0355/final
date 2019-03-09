from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Fina

def home(request):
    finas = Fina.objects
    return render(request, 'home.html', {'finas': finas})

def detail(request, fina_id):
    fina_detail = get_object_or_404(Fina, pk=fina_id)
    return render(request, 'detail.html', {'fina': fina_detail}) 

def modify(request, fina_id):
    fina = Fina.objects.get(id = fina_id)
    fina.title = request.GET['title']
    fina.body = request.GET['body']
    fina.pub_date = timezone.datetime.now()
    fina.save()
    return redirect('/')

def writes(request):
    return render(request, 'writes.html')

def create(request):
    fina = Fina()
    fina.title = request.GET['title']
    fina.body = request.GET['body']
    fina.pub_date = timezone.datetime.now()
    fina.save()
    return redirect('/')

def delete(request, fina_id):
    fina = Fina.objects.get(id = fina_id)
    fina.delete()
    return redirect('/')

def pictur(request):
    return render(request, 'pictur.html')

def login(request):
    return render(request, 'login.html')

def lecture(request):
    return render(request, 'lecture.html')
    
def board(request):
    return render(request, 'board.html')



# Create your views here.
