from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import compraventa
from funtions	import articulo,client,empeno,empenoarticulo
# Create your views here.

def inicio(request):
    return render(request, 'index.html', {})
    
def test2(request):
    
    if request.method == 'POST':
        form = compraventa(request.POST)
        if form.is_valid():
            NOMBRE=form.cleaned_data['nombre']
            APELLIDO=form.cleaned_data['apellido']
            DOCUMENTO=form.cleaned_data['documento']
            NOMBREARTICULO=form.cleaned_data['NArticulo']
            PRECIO=form.cleaned_data['precio']
            FECHAVENCIMIENTO=form.cleaned_data['FVencimiento']
            TIPOARTICULO=form.cleaned_data['Tarticulo']
            USUARIO=1
            
            print NOMBRE, APELLIDO,DOCUMENTO,NOMBREARTICULO,PRECIO,FECHAVENCIMIENTO,TIPOARTICULO
            IDCLIENT=client(NOMBRE,APELLIDO,DOCUMENTO)
            IDEMPENO=empeno(FECHAVENCIMIENTO,IDCLIENT,USUARIO)
            IDARTICULO=articulo(NOMBREARTICULO,TIPOARTICULO)
            empenoarticulo(PRECIO,IDEMPENO,IDARTICULO)
            return HttpResponseRedirect('/test/')
    else :
        form = compraventa()
    return render(request, 'test2.html', {'form': form})
    
def test(request):
    
    form = compraventa()
    
    return render(request, 'test.html', {'form': form})
