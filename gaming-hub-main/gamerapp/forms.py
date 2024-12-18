from django import forms
from .models import *
from django.forms import widgets
   
     
class ProfileForm(forms.ModelForm):
    email = forms.EmailField(widget=widgets.EmailInput(attrs={'id': 'user-email', 'name': 'user-email' , 'placeholder' : 'Enter User\'s Email... ' , 'type' : 'email'}) , required=False)
    username = forms.CharField(widget=widgets.TextInput(attrs={'placeholder': 'Enter Username...' , 'id' : 'username    '}) , required=False)
    password = forms.CharField(widget=widgets.TextInput(attrs={'placeholder': 'Enter Password...' , 'id' : 'password    ',  'type' : 'password'}) , required=False)
    class Meta:
        model = User
        fields = ['username' , 'email' ,'password']