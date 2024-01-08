from django.contrib import admin

from .models import Cantant, Genere, Album, Canço

#admin.site.register(Cantant)
#admin.site.register(Album)
#admin.site.register(Genere)
#admin.site.register(Canço)


# Define the admin class
class CantantAdmin(admin.ModelAdmin):
    list_display = ('cognom', 'nom', 'naixement', 'mort', 'premis')

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titol', 'cantant', 'duració', 'preu', 'display_genere')
    list_filter = ('cantant', 'generes')




class GenereAdmin(admin.ModelAdmin):
    pass

class CançoAdmin(admin.ModelAdmin):
    list_filter = ('cantant', 'album')

# Register the admin class with the associated model
admin.site.register(Album, AlbumAdmin)
admin.site.register(Genere, GenereAdmin)
admin.site.register(Canço, CançoAdmin)
admin.site.register(Cantant, CantantAdmin)

