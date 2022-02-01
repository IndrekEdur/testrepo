from . models import Product
from django.contrib import admin
from . models import Project
from . models import Comment


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hours', 'is_published', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('hours',)
    list_editable = ('is_published',)
    search_fields = ('name', 'hours')
    ordering = ('hours',)



admin.site.register(Product, ProductAdmin)
admin.site.register(Project)
admin.site.register(Comment)