from django.contrib import admin

from main.models import Inst, Specialty, Property

# Register your models here.


# class SpecialityInline(admin.TabularInline):
#     model = Specialty
#
#
# class PropertyInline(admin.TabularInline):
#     model = Property
#
#
# class InstAdmin(admin.ModelAdmin):
#     inlines = [
#         SpecialityInline,
#         PropertyInline
#     ]


admin.site.register(Inst)
admin.site.register(Specialty)
admin.site.register(Property)
