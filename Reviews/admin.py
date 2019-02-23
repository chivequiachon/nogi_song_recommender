from django.contrib import admin
from .models import NogizakaSong, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('song', 'rating', 'user_name', 'comment', 'published_date')
    list_filter = ['published_date', 'user_name']
    search_fields = ['comment']

admin.site.register(NogizakaSong)
admin.site.register(Review, ReviewAdmin)