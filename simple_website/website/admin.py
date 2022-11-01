from django.contrib import admin
from .models import Gallery, Gallery360, Post

# Register your models here.

admin.site.register(Gallery)  # register gallery
admin.site.register(Gallery360)  # register gallery360


class PostAdmin(admin.ModelAdmin):  # post admin
    list_display = ('title', 'slug', 'status', 'created_on')  # list display
    list_filter = ("status",)  # list filter
    search_fields = ['title', 'content']  # search fields
    prepopulated_fields = {'slug': ('title',)}  # prepopulated fields


admin.site.register(Post, PostAdmin)  # register post
