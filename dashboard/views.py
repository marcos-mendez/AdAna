from django.shortcuts import render, redirect
from .models import Empresa
from django.contrib.auth.models import User

def asignar_usuarios(request, empresa_id):
    empresa = Empresa.objects.get(id=empresa_id)
    if request.method == 'POST':
        usuarios_id = request.POST.getlist('usuarios')
        usuarios = User.objects.filter(id__in=usuarios_id)
        empresa.usuarios.set(usuarios)

        # obtén la referencia al permiso de "view" para el modelo User
        permiso_ver_usuario = Permission.objects.get(codename='view_user')

        # para cada usuario de la empresa, agrega este permiso
        for usuario in empresa.usuarios.all():
            usuario.user_permissions.add(permiso_ver_usuario)

        return redirect('dashboard:empresa_detalle', empresa_id=empresa_id)
    else:
        usuarios = User.objects.all()
        return render(request, 'asignar_usuarios.html', {'empresa': empresa, 'usuarios': usuarios})

def inicio(request):
    return render(request, 'inicio.html')

