from django.shortcuts import render
from .form import compraventa

# Create your views here.

def inicio(request):
    return render(request, 'index.html', {})
    
def test(request):
    
    form = compraventa()
    
    return render(request, 'test.html', {'form': form})
    
def test2(request):
    
    form = compraventa()
    
    return render(request, 'test2.html', {'form': form})
