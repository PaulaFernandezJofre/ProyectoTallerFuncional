from datetime import timezone
from django.db import models

# Create your models here.
class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True, serialize=False)
    nombre_empresa = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    rut_empresa = models.CharField(max_length=20)
    correo_empresa = models.EmailField()
    telefono_contacto = models.CharField(max_length=15)
    direccion_empresa = models.CharField(max_length=255)
    tipo_industria = models.CharField(max_length=255)
    password = models.CharField(max_length=128, default=1)

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=255)

class Ofertas_emp(models.Model):
    id_oferta_emp = models.AutoField(primary_key=True)
    nombre_puesto = models.CharField(max_length=255)
    nombre_emp = models.CharField(max_length=255, default="Empresa")
    descripcion = models.TextField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    cupos = models.PositiveIntegerField()
    fecha_limite = models.DateField()
    fecha_creacion = models.DateField()
    discapacidad_enfoque = models.CharField(max_length=100)
    id_of_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fono_empre = models.CharField(max_length=15)
    correo_empre = models.EmailField()

class Postulantes(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_postulante = models.CharField(max_length=255)
    apellido_post = models.CharField(max_length=255)
    telefono_postulante = models.CharField(max_length=15)
    correo_postulante = models.EmailField(null=True, blank=True)
    rut_postu = models.CharField(max_length=12, unique=True)
    curriculum_postu = models.FileField(upload_to='curriculums/', default=1)
    contraseña = models.CharField(max_length=128, default=1)


class Postulaciones(models.Model):
    id_postulacion = models.AutoField(primary_key=True)
    id_oferta_empl = models.ForeignKey(Ofertas_emp, on_delete=models.CASCADE)
    id_postulante = models.ForeignKey(Postulantes, on_delete=models.CASCADE, default=1)
    mensaje_postu = models.TextField(null=True)
    fecha_creacion_postu = models.DateField(auto_now_add=True)
    

