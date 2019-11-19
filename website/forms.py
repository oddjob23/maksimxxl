from django import forms
from .models import Subscriber, Message

class SubscriberFormModel(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Unesite vas Email...'}))
    class Meta:
        model = Subscriber
        fields = ('email',)

class ContactForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Unesite vas Email...'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Unesite vase ime i prezime'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Unesite vasu poruku...'}))

    class Meta:
        model = Message
        fields = ('name', 'email', 'message')