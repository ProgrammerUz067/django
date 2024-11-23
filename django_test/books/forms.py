from .models import Book
from django.forms import ModelForm


class AddBookForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"




