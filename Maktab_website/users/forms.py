from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class SignupForm(forms.ModelForm):
    password1=forms.CharField(label="Parol Kiriting",widget=forms.PasswordInput)
    password2=forms.CharField(label="Parolni qayta tasdiqlang",widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','last_name','email','password1','password2')

    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Kiritilgan parollar bir birigi teng bo'lishi kerak")
        return password1
