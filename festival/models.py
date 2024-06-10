from django.db import models




class Festival(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    foto_poster = models.ImageField(upload_to='festival_photos/', blank=True, null=True)

    def __str__(self):
        return self.nome

class Localizacao(models.Model):
    nome = models.CharField(max_length=100)
    Festival = models.ForeignKey(Festival, on_delete=models.CASCADE, related_name="localizacao")


    def __str__(self):
        return self.nome


class Banda(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE, related_name="bandas")

    def __str__(self):
        return self.nome
