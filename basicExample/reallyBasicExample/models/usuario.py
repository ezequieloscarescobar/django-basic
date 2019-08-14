from django.db import models

class Usuario(models.Model):
    class Meta:
            db_table = 'usuario'

    nombre = models.TextField(null = True, blank = True)
    apellido = models.TextField(null = True, blank = True)