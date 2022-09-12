from django.db import models
from datetime import date


class Author(models.Model):
    surname = models.CharField("Фамилия", max_length=50)
    depart = models.CharField("Департамент", max_length=50)
    date = models.DateField("Дата", default=date.today, blank=True)

    def __str__(self):
        return self.surname


class Listy(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField("Картридж", max_length=50)
    numbers = models.PositiveIntegerField("Количество", default=1)

    def __str__(self):
        return self.title
