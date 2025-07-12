from django import forms
from .models import UserProfile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'bio', 'phone', 'address']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }