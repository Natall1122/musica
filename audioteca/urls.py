from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('cantants/', views.CantantListView.as_view(), name='cantant'),
    path('cantants/<int:pk>', views.CantantDetailView.as_view(), name='cantant-detail'),

    path('albums/', views.AlbumListView.as_view(), name='album'),
    path('albums/<int:pk>', views.AlbumDetailView.as_view(), name='album-detail'),
    
    path('cançons/<int:pk>', views.CançoDetailView.as_view(), name='canço-detail'),

    path('generes/', views.GenereListView.as_view(), name='genere'),
    path('generes/<int:pk>', views.GenereDetailView.as_view(), name='genere-detail'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

