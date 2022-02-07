from django.forms import DateField, Form, IntegerField, DecimalField, CharField, EmailField

class atleta_create(Form):
    nombre = CharField()
    apellido = CharField()
    disciplina = CharField()
    fecha_de_nacimiento = DateField()
    ciudad_de_nacimiento = CharField()
    pais_de_nacimiento = CharField()
    altura = DecimalField()
    peso = DecimalField()
    email = EmailField()

class entrenador_create(Form):
    nombre = CharField()
    apellido = CharField()
    fecha_de_nacimiento = DateField()
    estudios = CharField()
    especialidad = CharField()
    email = EmailField()

class rutina_create(Form):

    nombre = CharField()
    fecha_inicio = DateField()
    intensidad = CharField()
    ejercicio_1 = CharField()
    ejercicio_2 = CharField()
    ejercicio_3 = CharField()
    ejercicio_4 = CharField()
    ejercicio_5 = CharField()
    ejercicio_6 = CharField()
    ejercicio_7 = CharField()
    duracionPorEjercicio = IntegerField()
    descansoEntreEjercicio = IntegerField()
    rondas = IntegerField()