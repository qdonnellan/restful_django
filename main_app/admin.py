from django.contrib import admin
from main_app.models import Thing

class ThingAdmin(admin.ModelAdmin):
    list_display=('title', 'body', 'created')

admin.site.register(Thing, ThingAdmin)
