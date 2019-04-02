from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","content","updated","timestamp"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated","timestamp"]
    search_fields = ["title","content"]

admin.site.register(Post, PostModelAdmin)



