from django.contrib import admin

from .models import Bicycle, BicyclePhoto

class PhotoInline(admin.StackedInline):
    model = BicyclePhoto


class BicyleAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Bicycle, BicyleAdmin)
admin.site.register(BicyclePhoto)