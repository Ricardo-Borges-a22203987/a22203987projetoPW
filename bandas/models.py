from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    foto_banda = models.ImageField(upload_to='bandas/fotos', blank=True, null=True)

    def __str__(self):
        return self.nome

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name="albums")
    ano_lancamento = models.IntegerField()
    foto_Album = models.ImageField(upload_to='bandas/fotos', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, related_name="musicas")
    duracao = models.DurationField()
    biografia = models.TextField(default='', null=True, blank=True)
    letra = models.TextField(default='', null=True, blank=True)
    spotify = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.titulo

