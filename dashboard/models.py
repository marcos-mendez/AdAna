from django.db import models
from django.contrib.auth.models import User

#This is the model for Companies that are going to be registered even thought they are not clients in the system
class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    usuarios = models.ManyToManyField(User)

    def __str__(self):
        return self.nombre

#This is the model for the competitors it is a relation of a Company to another.
class Competencia(models.Model):
    empresa = models.ForeignKey(Empresa, related_name='empresa', on_delete=models.CASCADE)
    competidor = models.ForeignKey(Empresa, related_name='competidor', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('empresa', 'competidor')

    def __str__(self):
        return f"{self.empresa.nombre} competidor: {self.competidor.nombre}"