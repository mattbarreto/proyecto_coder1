from distutils.command.upload import upload
from tkinter import CASCADE
from django.db.models import Model, ForeignKey, CASCADE, ImageField
from django.utils import timezone
from django.db.models.fields import CharField, EmailField, DateField, DecimalField, IntegerField
from django.contrib.auth.models import User

class Atleta(Model):

    nombre = CharField(max_length=40)
    apellido = CharField(max_length=40)
    disciplina = CharField(max_length=40)
    fecha_de_nacimiento = DateField(default=timezone.now)
    ciudad_de_nacimiento = CharField(max_length=30)
    pais_de_nacimiento = CharField(max_length=30)
    altura = DecimalField(decimal_places=2, max_digits=3)
    peso = DecimalField(decimal_places=2, max_digits=5)
    email = EmailField()

    def __str__(self):
        return f'Atleta: {self.nombre} {self.apellido} Disciplina: {self.disciplina} Altura: {self.altura} Peso: {self.peso} Pais de origen: {self.pais_de_nacimiento} Email: {self.email}'
class Entrenador(Model):

    nombre = CharField(max_length=40)
    apellido = CharField(max_length=40)
    fecha_de_nacimiento = DateField(default=timezone.now)
    estudios = CharField(max_length=50)
    especialidad = CharField(max_length=40)
    email = EmailField()

    def __str__(self):
        return f'Entrenador: {self.nombre} {self.apellido} Estudios: {self.estudios} Especialidad: {self.especialidad} Email: {self.email}'

class Rutina(Model):

    nombre = CharField(max_length=40)
    fecha_inicio = DateField(auto_now_add=False, auto_now=False, blank=True)
    intensidad = CharField(max_length=10)
    ejercicio_1 = CharField(max_length=40)
    ejercicio_2 = CharField(max_length=40)
    ejercicio_3 = CharField(max_length=40)
    ejercicio_4 = CharField(max_length=40)
    ejercicio_5 = CharField(max_length=40)
    ejercicio_6 = CharField(max_length=40)
    ejercicio_7 = CharField(max_length=40)
    duracionPorEjercicio = IntegerField()
    descansoEntreEjercicio = IntegerField()
    rondas = IntegerField()

    def __str__(self):
        return f'Rutina: {self.nombre} Intensidad: {self.intensidad} Rondas: {self.rondas}'
    
    
class Avatar(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    imagen = ImageField(upload_to= 'avatares', null=True, blank= True)