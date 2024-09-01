from django.contrib import admin
from .models import Image, Post, Tag, Category

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'created_at']

admin.site.register(Post, PostAdmin)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Category)