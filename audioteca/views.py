from django.shortcuts import render
from django.views import generic
from .models import Cantant, Album, Canço, Genere

def index(request):
    num_albums=Album.objects.all().count()
    num_cançons=Canço.objects.all().count()
    num_cantants=Cantant.objects.count() 
    num_generes=Genere.objects.count()
    return render(
        request,
        'index.html',
        context={'num_albums':num_albums,'num_cançons':num_cançons,'num_cantants':num_cantants, 'num_generes':num_generes},
    )

class CantantListView(generic.ListView):
    model = Cantant

class CantantDetailView(generic.DetailView):
    model = Cantant

class AlbumListView(generic.ListView):
    model = Album

class AlbumDetailView(generic.DetailView):
    model = Album

class CançoDetailView(generic.DetailView):
    model = Canço

class GenereListView(generic.ListView):
    model = Genere

class GenereDetailView(generic.DetailView):
    model = Genere



