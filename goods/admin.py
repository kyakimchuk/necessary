from django.contrib import admin
from .models import Category1, Category2, Category3, CategoryHierarchy, Thing


admin.site.register(Category1)
admin.site.register(Category2)
admin.site.register(Category3)

class CategoryHierarchyAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'cat1', 'cat2', 'cat3')

admin.site.register(CategoryHierarchy, CategoryHierarchyAdmin)

class ThingAdmin(admin.ModelAdmin):
    list_display = ('name', 'cat_hierar', 'description', 'price', 'size', 'show_image')

admin.site.register(Thing, ThingAdmin)