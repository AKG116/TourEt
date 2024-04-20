from django import forms
from django.contrib.auth.forms import UserCreationForm
from TourETAPP.models import *

class Visitor_Login(forms.Form):
    email = forms.EmailField(
        max_length=25,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter email',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control floating',
            'placeholder': 'Enter Password',
            'required': 'true'
        })
    )


class SiteRegistrationForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=25, 
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter First name', 'class': 'form-control'}))
    
    last_name = forms.CharField(
        max_length=25, 
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Last name',
                'class': 'form-control'
            }
        ))
    username = forms.CharField(
        max_length=25, 
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Username',
                'class': 'form-control'
            }
        ))
    email = forms.EmailField(
        max_length=25,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter email',
                'class': 'form-control'
            }
        )
    )
    password1 = forms.CharField(max_length=40, label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Password',
        'autocomplete': 'off'
    }))
    password2 = forms.CharField(max_length=40, label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
        'autocomplete': 'off'
    }))

    photo = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Add Photo(Optional)',
   
    }))


    class Meta:
        model = CustomUser
        fields = 'username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'photo'


class BookATourForm(forms.Form):
    name = forms.CharField(
        label='Your Name',
        widget=forms.TextInput(attrs={'class': 'form-control bg-transparent', 'placeholder': 'Your Name'})
    )
    email = forms.EmailField(
        label='Your Email',
        widget=forms.EmailInput(attrs={'class': 'form-control bg-transparent', 'placeholder': 'Your Email', 'Value': '{{amount}}'})
    )
    date = forms.DateField(
        label='Date & Time',
        widget=forms.DateInput(
            attrs={'class': 'form-control bg-transparent datetimepicker-input', 'placeholder': 'Date & Time'}
        )
    )
    destination = forms.ChoiceField(
        label='Destination',
        choices=[(1, 'Destination 1'), (2, 'Destination 2'), (3, 'Destination 3')],
        widget=forms.Select(attrs={'class': 'form-select bg-transparent'})
    )
    person = forms.ChoiceField(
        label='Person',
        choices=[(1, '1'), (2, '2'), (3, '3')],
        widget=forms.Select(attrs={'class': 'form-select bg-transparent'})
    )
    special_request = forms.CharField(
        label='Special Request',
        widget=forms.Textarea(attrs={'class': 'form-control bg-transparent', 'placeholder': 'Special Request', 'rows': 3})
    )



class PackageForm(forms.ModelForm):

    class Meta:
        model = Package
        fields = ['name', 'person', 'days', 'price', 'description', 'package_pic']
        widgets = {
           'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
           
           'person': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Person'}),
         
           'days': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Days'}), 
           
           'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price'}),
         
           'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description'}),
         
          'package_pic': forms.ClearableFileInput(attrs={'class': 'form-control'}),
}


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class ContactForm(forms.Form):
  name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
  message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'phone', 'address', 'twitter', 'instagram', 'facebook']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control'}),
        }