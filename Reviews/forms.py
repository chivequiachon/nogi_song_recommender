from django.forms import ModelForm, Textarea
from .models import SongReview

class SongReviewForm(ModelForm):
    class Meta:
        model = SongReview
        fields = ['rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }