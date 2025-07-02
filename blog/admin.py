from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'pub_date')
    search_fields = ('title', 'author_name')
    list_filter = ('pub_date',)