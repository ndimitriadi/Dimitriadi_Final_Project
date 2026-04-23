from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.HiddenInput(attrs={'id': 'hidden_rating'}),
            'comment': forms.Textarea(attrs={'class': 'review-textarea', 'rows': 4, 'placeholder': 'Share your experience...'}),
        }