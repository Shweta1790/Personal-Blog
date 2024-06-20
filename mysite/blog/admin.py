from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Tag, Author, Post

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "date", "tag")
    prepopulated_fields = {"slug":("title",)}
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
