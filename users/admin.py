from django.contrib import admin

from .models import Profile


# admin.site.register(Post)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["image"]
