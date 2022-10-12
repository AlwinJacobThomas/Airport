from django.contrib import admin

from core.models import Airport, Flight,User,Trip

# Register your models here.

admin.site.register(Airport)
admin.site.register(User)
admin.site.register(Trip)
admin.site.register(Flight)

