from django.db import models
from datetime import date


class Author(models.Model):
    MSK_SKLAD = 'МСК СКЛАД'
    MSK_OFFICE = 'МСК ОФИС'
    PROISVODSTVO = 'ПРОИЗВОДСТВО'
    SKLAD = 'СПБ СКЛАД'
    OFFICE = 'СПБ ОФИС'
    BUH = 'БУХГАЛТЕРИЯ'
    SVETON = 'СВЕТОН'
    EP = 'ЭЛЕКТРОПРОЕКТ'
    INOL = 'ИНОЛ'
    SHOP1 = 'МАГАЗИН БЕЛОВОДСКИЙ'
    SHOP2 = 'МАГАЗИН ВАРШАВКА'

    DEPART_CHOICES = [
        (MSK_SKLAD, 'МСК СКЛАД'),
        (MSK_OFFICE, 'МСК ОФИС'),
        (PROISVODSTVO, 'ПРОИЗВОДСТВО'),
        (SKLAD, 'СПБ СКЛАД'),
        (OFFICE, 'СПБ ОФИС'),
        (BUH, 'БУХГАЛТЕРИЯ'),
        (SVETON, 'СВЕТОН'),
        (EP, 'ЭЛЕКТРОПРОЕКТ'),
        (INOL, 'ИНОЛ'),
        (SHOP1, 'МАГАЗИН БЕЛОВОДСКИЙ'),
        (SHOP2, 'МАГАЗИН ВАРШАВКА'),
    ]
    depart = models.CharField("Департамент", max_length=50, choices=DEPART_CHOICES)
    surname = models.CharField("Фамилия", max_length=50)

    def __str__(self):
        return self.surname


class Listy(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField("Картридж", max_length=50)
    numbers = models.PositiveIntegerField("Количество", default=1)
    date = models.DateField("Дата", default=date.today, blank=True)

    def __str__(self):
        return self.title

