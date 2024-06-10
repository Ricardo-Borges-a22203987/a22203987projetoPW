from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    foto_banda = models.ImageField(upload_to='imagesApp/fotos', blank=True, null=True)

    def __str__(self):
        return self.nome

