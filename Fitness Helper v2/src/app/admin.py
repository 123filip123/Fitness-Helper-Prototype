from django.contrib import admin

from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'certified','highScore','dateAcquired')

# Register your models here.
admin.site.register(Split)
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Muscle)
admin.site.register(Profile,ProfileAdmin)