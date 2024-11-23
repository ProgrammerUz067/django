from django import forms
from django.core.exceptions import ValidationError

from .models import CustomUser



class SignupForm(forms.ModelForm):
    password1=forms.CharField(label='Parolni kiriting',widget=forms.PasswordInput)
    password2=forms.CharField(label='Parolni qayta kiriting',widget=forms.PasswordInput)
    class Meta:
        model=CustomUser
        fields=('username','first_name','last_name','email','photo_user','password1','password2')


    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Kiritilgan parollar bir biriga teng bo'lishi kerak")
        return password1






