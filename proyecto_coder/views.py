import email
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.shortcuts import redirect, render
from proyecto_coder.forms import UserEditForm, UserRegisterForm

# LogIn/LogOut


def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username = usuario, password = contra)
            
            if user is not None:
                login(request, user)
                return redirect('Inicio')
            else:
                return render(request, "login.html",
                    {'form': form,
                     'error': 'Los datos ingresados no son válidos'})
            
        else:
                return render(request, "login.html", {'form': form})
    
    form = AuthenticationForm()
    
    return render(request, "login.html", {'form': form})


def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return HttpResponse(f'Usuario {username} fue creado correctamente')
            
    else:
        form = UserRegisterForm()
        
    return render(request, 'registro.html', {'form': form})
        

# edit perf

def editar_perfil(request):
    usuario = request.user 
    
    if request.method == 'POST':
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.email = data['email']
            usuario.password1 = data['password1']
            usuario.password2 = data['password2']
            usuario.save()
            return redirect('Inicio')
    else:
        formulario = UserEditForm({'email':usuario.email})
        
    return render(request, 'registro.html', {'form': formulario})
        