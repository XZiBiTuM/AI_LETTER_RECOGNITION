from django import forms
from .models import *


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя')
    email = forms.EmailField(label='Эл. почта')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'first_name', 'last_name', 'email')
        error_messages = {
            'avatar': {
                'invalid_image': 'Изображение должно быть квадратом.',
            },
        }