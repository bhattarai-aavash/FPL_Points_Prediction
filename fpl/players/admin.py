from django.contrib import admin
from .models import Players, Team
# Register your models here.
admin.site.register(Team)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'club', 'type')
    search_fields = ['name']


admin.site.register(Players, PlayerAdmin)
