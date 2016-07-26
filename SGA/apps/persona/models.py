from __future__ import unicode_literals

from django.db import models

class persona(models.Model):
	nombre = models.CharField(max_length = 30)
	mail = models.EmailField(max_length=20)
	fecha_nacimiento = models.DateTimeField()
 