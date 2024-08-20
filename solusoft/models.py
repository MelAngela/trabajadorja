from django.db import models

class Trabajador(models.Model):
    SEXO_CHOICES = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    ]
    ESTADO_CIVIL_CHOICES = [
        ('S', 'Soltero'),
        ('C', 'Casado'),
        ('V', 'Viudo'),
        ('D', 'Divorciado'),
    ]
    
    rut = models.CharField(max_length=9, default='12345678K')
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    nombres = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES)

    def __str__(self):
        return f"{self.rut} - {self.apellido_paterno} {self.apellido_materno} {self.nombres}"

class Cargas(models.Model):
    SEXO_CHOICES = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    ]
    PARENTESCO_CHOICES = [
        ('C', 'Cónyuge'),
        ('H', 'Hijo/a'),
    ]
    
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    parentesco = models.CharField(max_length=1, choices=PARENTESCO_CHOICES)

    def __str__(self):
        return f"{self.apellido_paterno} {self.apellido_materno} {self.nombre}"



