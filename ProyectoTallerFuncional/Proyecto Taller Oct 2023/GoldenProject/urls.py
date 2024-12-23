"""
URL configuration for GoldenProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ABEPD.views import CategoryData,OfferData,LoginEmp,RegisEmp,DashView,CreateView,PostulationsView,CheckView,RegistroPostu,MiPostu,Loginpostu,DatosPostu,Pagppal,postular,CerrarSesionEMP,CerrarSesionPostu,eliminar_oferta,Categoria2,Categoria3,Categoria4
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Pagppal, name='principal'),
    path('registropostu/', RegistroPostu, name='RegisPostu'),
    path('mispostus/', MiPostu, name='MisPostus'),
    path('loginpostu/', Loginpostu, name='LoginPostu'),
    path('datospostu/', DatosPostu, name='datospostu'),
    path('home',CategoryData,name='categoria'),
    path('listado/',OfferData,name='ofertas'),
    path('login_emp/',LoginEmp,name='loginemp'),
    path('registro/',RegisEmp,name='registroemp'),
    path('dashboard/',DashView,name='dashboard'),
    path('create_offer/',CreateView,name='creation_view'),
    path('Postulaciones/',PostulationsView,name='postus'),
    path('ofertas_hechas/',CheckView,name='empview_ofertas'),
    path('postular/', postular, name='postular'),
    path('logoutemp/', CerrarSesionEMP, name='logoutemp'),
    path('logoutpost/', CerrarSesionPostu, name='logoupost'),
    path('eliminar_oferta/<int:oferta_id>/',eliminar_oferta, name='eliminar_oferta'),
    path('listado2/',Categoria2,name='ofertas2'),
    path('listado3/',Categoria3,name='ofertas3'),
    path('listado4/',Categoria4,name='ofertas4'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
