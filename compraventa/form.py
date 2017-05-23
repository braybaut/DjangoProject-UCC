from django import forms

class compraventa(forms.Form):
    Articulos = (
        ('oro', 'Valor tipo Oro'),
        ('plata', 'Valor tipo Plata'),
        ('Chatarra','Valor tipo Chatarra'),
    )
    
    Tarticulo   = forms.ChoiceField(choices=Articulos,required=True)
    documento = forms.CharField(max_length=15,widget = forms.TextInput(attrs={'required' : 'True' ,'placeholder' : 'Documento', 'type' : 'number', 'min' : '0', 'data-error' : 'Documento invalido'}))
    nombre = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder' : 'nombre',  'class' : 'form-control' , 'data-error' : 'Bruh, that email address is invalid' , 'type' : 'text'}))
    apellido = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder' : 'Apellido',  'class' : 'form-control' , 'data-error' : 'Bruh, that email address is invalid' , 'type' : 'text'}))
    NArticulo = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder' : 'Nombre Articulo',  'class' : 'form-control' , 'data-error' : 'Bruh, that email address is invalid' , 'type' : 'text'}))
    precio = forms.IntegerField(max_length=15, widget=forms.TextInput(attrs={'placeholder' : 'Nombre Articulo',  'class' : 'form-control' , 'data-error' : 'Bruh, that email address is invalid' , 'type' : 'number'}))
    email = forms.EmailField(widget = forms.TextInput(attrs={'placeholder' : 'email' , 'class' : 'form-control' , 'data-error' : 'Bruh, that email address is invalid' , 'type' : 'email' }))

    FVencimiento = forms.DateField(widget = forms.TextInput(attrs={"placeholder" : "MM/DD/YYYY","type" : "text", "name" : "date"}))
