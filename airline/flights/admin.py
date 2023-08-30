from django.contrib import admin
from .models import Flight, Airport, Passanger
# Register your models here.


class FlightAdmin(admin.ModelAdmin):
    list_display = ("origin", "destination", "duration")
    
class PassangerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)
    
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passanger, PassangerAdmin)