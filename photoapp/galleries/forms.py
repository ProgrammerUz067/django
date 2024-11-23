from django.forms import ModelForm
from .models import Photo,Category


class Add(ModelForm):
    class Meta:
        model=Photo
        fields="__all__"


class Addcat(ModelForm):
    class Meta:
        model:Category
        fields="__all__"




