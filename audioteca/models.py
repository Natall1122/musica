from django.db import models
from django.urls import reverse

class Genere(models.Model):
    nom = models.CharField(max_length=200, help_text="Escriu el gènere de música (Ex: Pop, K-pop, Rock...)")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.nom
    def get_absolute_url(self):
        return reverse('genere-detail', args=[str(self.id)])


class Album(models.Model):
    titol = models.CharField(max_length=200)

    cantant = models.ForeignKey('Cantant', on_delete=models.SET_NULL, null=True)

    duració = models.IntegerField(help_text="Escriu la duració total del àlbum")

    preu = models.IntegerField(help_text='Escriu el preu de l\'àlbum')

    generes = models.ManyToManyField(Genere, help_text="Selecciona un gènere per a aquest àlbum.")
    portada = models.ImageField(null=True)


    def __str__(self):
        return self.titol


    def get_absolute_url(self):
        return reverse('album-detail', args=[str(self.id)])
    
    def display_genere(self):
        return ', '.join([ generes.nom for generes in self.generes.all()[:3] ])
    
    display_genere.short_description = 'Genere'

    
class Cantant(models.Model):
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    naixement = models.DateField(null=True, blank=True)
    mort = models.DateField('mort', null=True, blank=True)
    descripcio = models.TextField(null = True, max_length=1000)
    premis = models.IntegerField(help_text="Escriu el número de premis que ha guanyat.")
    imatge = models.ImageField(null=True)

    def get_absolute_url(self):

        return reverse('cantant-detail', args=[str(self.id)])


    def __str__(self):
        return '%s, %s' % (self.cognom, self.nom)


class Canço(models.Model):
    titol = models.CharField(max_length=200)

    cantant = models.ForeignKey('Cantant', on_delete=models.SET_NULL, null=True)
    lletra = models.TextField(null = True)

    duració = models.IntegerField(help_text="Escriu la duració de al cançó")

    album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True)
    video = models.CharField(max_length=100000, null=True)


    def __str__(self):
        return self.titol

    def get_absolute_url(self):
        return reverse('canço-detail', args=[str(self.id)])


