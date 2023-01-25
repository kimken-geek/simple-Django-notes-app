from django.contrib import admin
from .models import BlogPost
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published')
    list_filter = ('author', 'date_published')
    search_fields = ('title', 'content')

admin.site.register(BlogPost, BlogPostAdmin)
