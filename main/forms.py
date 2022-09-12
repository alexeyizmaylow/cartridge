from django import forms
from django.forms.models import modelformset_factory, inlineformset_factory
from .models import Author, Listy


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('surname', 'depart')

        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов'}),
            'depart': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Производство'}),
        }


OrderFormset = inlineformset_factory(
    Author,
    Listy,
    fields=('title', 'numbers'),
    widgets={
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "TK-3160"}),
            'numbers': forms.NumberInput(attrs={'class': 'form-control'}),
        },
    min_num=1,
    extra=0,
    can_delete=False
)
