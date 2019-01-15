from django.contrib import admin
from maps.models import *
#from valuenetwork.valueaccounting.actions import export_as_csv
#from django_mptt_admin.admin import DjangoMpttAdmin

#admin.site.add_action(export_as_csv, 'export_selected objects')

class UseFaircoinAdmin(admin.ModelAdmin):
    list_display = ('title', 'tagline', 'lat', 'lng', 'faircoin_address', )

admin.site.register(UseFaircoin, UseFaircoinAdmin)
