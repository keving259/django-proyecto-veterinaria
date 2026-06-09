from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Tipo
from django.contrib.auth.hashers import make_password

User = get_user_model()

# Create your views here.
def vista_login(request):
    return render(request, 'login/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
            messages.error(request, 'Usuario no existe')
            
        if user:
            user_authenticated = authenticate(request, username=username, password=password)
            if user_authenticated is not None:
                if user.is_active:
                    auth_login(request, user_authenticated)
                    return redirect('home')
                else:
                    messages.error(request, 'Usuario inactivo')
            else:
                messages.error(request, 'Usuario no existe con esas credenciales')
        else:
            messages.error(request, 'Usuario o contraseña es incorrecto')
        
    return render(request, 'login/index.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'home/index.html', { 'usuario' : request.user })

@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    response = redirect('login')
    response['Cache-control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

@login_required(login_url='login')
def usuario(request):
    roles = Tipo.objects.exclude(nombre__in=['root'])
    return render(request, 'usuario/index.html', {'usuario':request.user, 'roles':roles})

@login_required(login_url='login')
def crear_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        username = request.POST['username']
        password = request.POST['password']
        tipo = request.POST['rol']
        
        if User.objects.filter(username=username).exists(): # Verificar si el username ya existe
            messages.error(request, f'El nombre de usuario "{username}" ya existe.')
            return redirect('usuario')
        
        if not nombre or not apellido or not username or not password or not tipo: # Verificar que ningún campo esté vacío
            messages.error(request, 'Todos los campos son obligatorios.')
            return redirect('usuario')
            
        try: # Verificar que el rol se válido
            tipo = Tipo.objects.get(id=tipo)
        except Tipo.DoesNotExist:
            messages.error(request, 'El rol seleccionado no es válido.')
            return redirect('usuario')
        
        user = User.objects.create(
            first_name = nombre, 
            last_name = apellido,
            username = username,
            password = make_password(password), # Encripta la contraseña antes de guardarla
            tipo = tipo
        )
        
        user.save()
        
        messages.success(request, 'Usuario creado exitosamente.')
        return redirect('usuario')
    
    usuarios = User.objects.all()
    roles = Tipo.objects.all()
    usuarios_con_rol = [(usuario, usuario.tipo.nombre if usuario.tipo else 'Sin rol') for usuario in usuarios]

    context = {
            'username' : request.user.username,
            'role_name' : request.user.tipo.nombre if request.user.tipo else 'Sin rol',
            'usuarios_con_rol' : usuarios_con_rol,
            'roles' : roles
        }
        
    return render(request, 'usuario/index.html', context)
