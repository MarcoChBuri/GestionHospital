from django.db import models
from enum import Enum

class Especialidad(Enum):
    CARDIOLOGIA = "Cardiología"
    DERMATOLOGIA = "Dermatología"
    GASTROENTEROLOGIA = "Gastroenterología"
    GERIATRIA = "Geriatría"
    INMUNOLOGIA = "Inmunología"
    PEDIATRIA = "Pediatría"

class Estado(Enum):
    PROGRAMADA = "Programada"
    REALIZADA = "Realizada"
    CANCELADA = "Cancelada"

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre

# Modelo Paciente
class Paciente(Persona):
    grado = models.CharField(max_length=10)
    identificacion = models.CharField(max_length=10)

# Modelo Doctor
class Doctor(Persona):
    especialidad = models.CharField(
        max_length=50,
        choices=[(tag.name, tag.value) for tag in Especialidad]
    )


# Modelo Enfermero
class Enfermero(Persona):
    horario = models.CharField(max_length=10)

# Modelo CitaMedica
class CitaMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(
        max_length=50,
        choices=[(estado.name, estado.value) for estado in Estado],
        default=Estado.PROGRAMADA.name,
    )

    class Meta:
        verbose_name = "Cita Médica"
        verbose_name_plural = "Citas Médicas"

    def __str__(self):
        return f"{self.paciente} - {self.doctor} - {self.fecha} - {self.hora} - {self.estado}"