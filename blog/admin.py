from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *

class BlogPostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogImages)

# Register your models here.
