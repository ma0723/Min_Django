from django.contrib import admin
from .models import Review, Comment

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment)