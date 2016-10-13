from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Document

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Document)