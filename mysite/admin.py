from django.contrib import admin
from mysite.models import Post, Post2

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','date','img')
    list_filter=('booking',)

admin.site.register(Post,PostAdmin)
admin.site.register(Post2,PostAdmin)