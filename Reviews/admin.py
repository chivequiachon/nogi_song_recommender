from django.contrib import admin
from .models import NogizakaSong, SongReview

class SongReviewAdmin(admin.ModelAdmin):
    model = SongReview
    list_display = ('song', 'rating', 'user_name', 'comment', 'publish_date')
    list_filter = ['publish_date', 'user_name']
    search_fields = ['comment']

admin.site.register(NogizakaSong)
admin.site.register(SongReview, SongReviewAdmin)