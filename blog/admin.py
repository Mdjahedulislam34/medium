from django.contrib import admin

from .models import Post


# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "content", "date_posted", "author"]
