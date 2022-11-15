from django import forms
from django.forms.models import modelformset_factory, inlineformset_factory
from .models import Author, Listy


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('surname', 'depart')

        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов'}),
            'depart': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Производство'}),
        }

CART_CHOICES = (
    ('TK-3160', 'TK-3160'),
    ('TK-1200', 'TK-1200'),
    ('TK-3100', 'TK-3100'),
    ('TK-1110', 'TK-1110'),
    ('TK-1120', 'TK-1120'),
    ('TK-2335', 'TK-2335'),
    ('TN-2275', 'TN-2275'),
    ('TN-1075', 'TN-1075'),
    ('TK-5230K', 'TK-5230 Черный'),
    ('TK-5230C', 'TK-5230 Синий'),
    ('TK-5230M', 'TK-5230 Красный'),
    ('TK-5230Y', 'TK-5230 Желтый'),
    ('TK-5140K', 'TK-5140 Черный'),
    ('TK-5140C', 'TK-5140 Синий'),
    ('TK-5140M', 'TK-5140 Красный'),
    ('TK-5140Y', 'TK-5140 Желтый'),
    ('CF330X', 'CF330X Черный'),
    ('CF331A', 'CF331A Синий'),
    ('CF332A', 'CF332A Желтый'),
    ('CF333A', 'CF333A Красный'),
    ('TK-6305', 'TK-6305'),
    ('106R01413', '106R01413'),
    ('Чернила черные hp8210', 'Чернила черные hp8210'),
    ('Чернила синие hp8210', 'Чернила синие hp8210'),
    ('Чернила красные hp8210', 'Чернила красные hp8210'),
    ('Чернила желтые hp8210', 'Чернила желтые hp8210'),
    ('Чернила черные пигметные ix6840', 'Чернила черные пигментые ix6840'),
    ('Чернила черные ix6840', 'Чернила черные ix6840'),
    ('Чернила синие ix6840', 'Чернила синие ix6840'),
    ('Чернила красные ix6840', 'Чернила красные ix6840'),
    ('Чернила желтые ix6840', 'Чернила желтые ix6840'),
    ('Чернила черные mb5140', 'Чернила черные mb5140'),
    ('Чернила синие mb5140', 'Чернила синие mb5140'),
    ('Чернила красные mb5140', 'Чернила красные mb5140'),
    ('Чернила желтые mb5140', 'Чернила желтые mb5140'),
    ('CLI 450PGBK', 'CLI 450PGBK Пигментный черный'),
    ('CLI 451BK', 'CLI 451BK Черный'),
    ('CLI 451C', 'CLI 451C Синий'),
    ('CLI 451M', 'CLI 451M Красный'),
    ('CLI 451Y', 'CLI 451Y Желтый'),
    ('PFI 102 MBK', 'PFI 102 MBK Пигментный черный'),
    ('PFI 102 BK', 'PFI 102 BK Черный'),
    ('PFI 102 C', 'PFI 102 C Синий'),
    ('PFI 102 M', 'PFI 102 M Красный'),
    ('PFI 102 Y', 'PFI 102 Y Желтый'),
)

OrderFormset = inlineformset_factory(
    Author,
    Listy,
    fields=('title', 'numbers'),
    widgets={
            'title': forms.Select(attrs={'class': 'form-control', 'placeholder': "TK-3160"}, choices=CART_CHOICES),
            'numbers': forms.NumberInput(attrs={'class': 'form-control'}),
        },
    min_num=1,
    extra=0,
    can_delete=False
)
