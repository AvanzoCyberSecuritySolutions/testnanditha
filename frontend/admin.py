from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AdminUser, Post, GalleryImage

admin.site.register(AdminUser)
admin.site.register(Post)
admin.site.register(GalleryImage)