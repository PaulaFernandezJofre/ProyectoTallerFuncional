from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render, redirect
from ABEPD.models import Categoria,Ofertas_emp,Empresa, Postulantes, Postulaciones
from .forms import RegistroForm
from django.contrib.auth.hashers import make_password , check_password
from django.utils import timezone
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect

# AREA POSTULANTES.
def CerrarSesionPostu(request):
    logout(request)
    if 'id_usuario' in request.session:
        del request.session['id_usuario']
    return redirect('principal')

def RegistroPostu(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        telefono = request.POST['telefono']
        rut = request.POST['rut']
        curriculum = request.FILES['curriculum']
        contraseña = make_password(request.POST['contraseña'])

        postulacion = Postulantes(nombre_postulante=nombre, apellido_post=apellido, correo_postulante=email, telefono_postulante=telefono, rut_postu=rut, curriculum_postu=curriculum, contraseña=contrasena)
        postulacion.save()
        return redirect('LoginPostu')

    return render(request,'RegisPostu.html')

def MiPostu(request):
    id_usuario = request.session.get('id_usuario')
    postulaciones = Postulaciones.objects.filter(id_postulante=id_usuario)
    return render(request,'MisPostus.html', {'postulaciones': postulaciones})

def Loginpostu(request):
    if request.method == 'POST':
        nombre_postulante = request.POST.get('nombre')
        contraseña = request.POST.get('contraseña')
        
        postulante = Postulantes.objects.filter(nombre_postulante=nombre_postulante).first()
        
        if postulante is not None and check_password(contraseña, postulante.contraseña):
            request.session['id_usuario'] = postulante.id_usuario
            return redirect('categoria')
        else:
            error_message = "Credenciales inválidas, intenta de nuevo."
            return render(request, 'LoginPostu.html', {'error_message': error_message})
        
    return render(request,'LoginPostu.html')

def DatosPostu(request):
    postulante_id = request.session.get('id_usuario')
    postulante = Postulantes.objects.get(id_usuario=postulante_id)

    if request.method == 'POST':
        postulante.nombre_postulante = request.POST['nombre']
        postulante.apellido_post = request.POST['apellido']
        postulante.correo_postulante = request.POST['email']
        postulante.telefono_postulante = request.POST['telefono']
        postulante.rut_postu = request.POST['rut']
        nueva_contraseña = request.POST['contraseña']
        if nueva_contrasena:
            postulante.contraseña = make_password(request.POST['contraseña'])
        if 'curriculum' in request.FILES:
            postulante.curriculum_postu = request.FILES['curriculum']
        postulante.save()
        return redirect('datospostu')
    
    return render(request, 'AjusteDatosPostu.html', {'postulante': postulante})

def Pagppal(request):
    return render(request,'ppal.html')

def CategoryData(request):
    return render(request,'Home.html')

@csrf_exempt
def postular(request):
    if request.method == 'POST':
        postulante_id = request.POST['postulante_id']
        oferta_id = request.POST['oferta_id']
        if postulante_id and oferta_id:
            postulante = get_object_or_404(Postulantes, id_usuario=postulante_id)
            oferta = get_object_or_404(Ofertas_emp, id_oferta_emp=oferta_id)
            postulacion = Postulaciones(id_postulante=postulante, id_oferta_empl=oferta)
            postulacion.save()
            return redirect('categoria')
        else:
            return HttpResponseBadRequest("Falta postulante_id u oferta_id")
        
    else:
        return HttpResponseNotAllowed(['POST'])

def OfferData(request):
    ofertas_emp = Ofertas_emp.objects.filter(discapacidad_enfoque=1)
    return render(request, 'Listado.html', {'ofertas_emp': ofertas_emp})

def Categoria2(request):
    ofertas_emp = Ofertas_emp.objects.filter(discapacidad_enfoque=2)
    return render(request, 'Categoria2.html', {'ofertas_emp': ofertas_emp})

def Categoria3(request):
    ofertas_emp = Ofertas_emp.objects.filter(discapacidad_enfoque=3)
    return render(request, 'Categoria3.html', {'ofertas_emp': ofertas_emp})

def Categoria4(request):
    ofertas_emp = Ofertas_emp.objects.filter(discapacidad_enfoque=4)
    return render(request, 'Categoria4.html', {'ofertas_emp': ofertas_emp})



#AREA REGISTRO LOGIN EMPRESA

def LoginEmp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        empresa = Empresa.objects.filter(username=username).first()
        
        if empresa is not None and check_password(password, empresa.password):
            # Si las credenciales son válidas, iniciar sesión
            request.session['empresa_id'] = empresa.id_empresa
            # Redirigir a una página después del inicio de sesión
            return redirect('dashboard')
        else:
            # Manejar caso de credenciales inválidas o usuario no encontrado
            error_message = "Credenciales inválidas, intenta de nuevo."
            return render(request, 'loginemp.html', {'error_message': error_message})
        
    return render(request, 'loginemp.html')

def DashView(request):
    return render(request,'index.html')
   

def RegisEmp(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            empresa = form.save(commit=False)
            password = form.cleaned_data['password']
            hashed_password = make_password(password)
            empresa.password = hashed_password
            empresa.save()
            return redirect('loginemp') 
    else:
        form = RegistroForm()
    return render(request,'registroemp.html', {'form': form})

#AJUSTAR ESTO PARA EL DASHBOARD EMPRESA


def CreateView(request):
    if not request.session.get('empresa_id'):
        messages.error(request, 'Inicia sesión para ingresar una oferta.')
        return redirect('loginemp')
    
    if request.method == 'POST':
        nombre_puesto = request.POST.get('nombre_puesto')
        descripcion = request.POST.get('descripcion')
        sueldo = request.POST.get('sueldo')
        cupos = request.POST.get('cupos')
        fecha_limite = request.POST.get('fecha_limite')
        fono_empre = request.POST.get('fono_empre')
        correo_empre = request.POST.get('correo_empre')
        discapacidad_enfoque = request.POST.get('discapacidad_enfoque')

        fecha_creacion = datetime.now().date()
        id_of_empresa = request.session.get('empresa_id')

        if not all([nombre_puesto, descripcion, sueldo, cupos, fecha_limite, id_of_empresa, fono_empre, correo_empre, discapacidad_enfoque]):
            error_message = "Por favor, completa todos los campos."
            return render(request, 'creacion_of_emp.html', {'error_message': error_message})

        try:
            oferta = Ofertas_emp(
                nombre_puesto=nombre_puesto,
                descripcion=descripcion,
                sueldo=sueldo,
                cupos=cupos,
                fecha_limite=fecha_limite,
                fecha_creacion=fecha_creacion,
                id_of_empresa_id=id_of_empresa,
                fono_empre=fono_empre,
                correo_empre=correo_empre,
                discapacidad_enfoque=discapacidad_enfoque
            )
            oferta.save()

            return redirect('dashboard')

        except Exception as e:
            error_message = f"Error al guardar la oferta: {str(e)}"
            return render(request, 'creacion_of_emp.html', {'error_message': error_message})

    return render(request, 'creacion_of_emp.html')


def PostulationsView(request):
    id_empresa = request.session.get('empresa_id')

    ofertas_empresa = Ofertas_emp.objects.filter(id_of_empresa=id_empresa)

    postulaciones = Postulaciones.objects.filter(id_oferta_empl__in=ofertas_empresa)

    return render(request,'postulacion_ofemp.html', {'postulaciones': postulaciones})

def CheckView(request):
    if request.method == 'POST':
        oferta_id = request.POST.get('oferta_id')
        oferta = get_object_or_404(Ofertas_emp, id_oferta_emp=oferta_id)
        oferta.nombre_puesto = request.POST.get('jobTitle')
        oferta.descripcion = request.POST.get('jobDescription')
        oferta.sueldo = request.POST.get('salary')
        oferta.cupos = request.POST.get('availablePositions')
        oferta.fecha_limite = request.POST.get('deadline')
        oferta.discapacidad_enfoque = request.POST.get('disabilityArea')
        oferta.fono_empre = request.POST.get('fono_empre')
        oferta.correo_empre = request.POST.get('correo_empre')
        oferta.save()
        return redirect('dashboard')

    else:
        ofertas = Ofertas_emp.objects.filter(id_of_empresa=request.session.get('empresa_id'))
        return render(request, 'act_rev_ofemp.html', {'ofertas': ofertas})

def eliminar_oferta(request, oferta_id):
    if request.method == 'POST':
        oferta = get_object_or_404(Ofertas_emp, id_oferta_emp=oferta_id)
        oferta.delete()
        return redirect('dashboard')   
    
def CerrarSesionEMP(request):
    logout(request)
    if 'empresa_id' in request.session:
        del request.session['empresa_id']
    return redirect('principal')