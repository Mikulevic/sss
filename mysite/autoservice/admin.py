from django.contrib import admin

from .models import (Automobilis,
                     Automobilio_modelis,
                     Paslauga,
                     Uzsakymas,
                     UzsakymoEilute)

admin.site.register(Automobilis)
admin.site.register(Automobilio_modelis)
admin.site.register(Paslauga)
admin.site.register(Uzsakymas)
admin.site.register(UzsakymoEilute)
