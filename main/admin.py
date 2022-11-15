from django.contrib import admin
from .models import Author, Listy
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field


class ListyInLineAdmin(admin.TabularInline):
    model = Listy


class AuthorAdmin(admin.ModelAdmin):
    inlines = [ListyInLineAdmin]


class UserResource(resources.ModelResource):
    surname = Field(attribute='author__surname', column_name='Фамилия')
    depart = Field(attribute='author__depart', column_name='Департамент')
    title = Field(attribute='title', column_name='Картридж')
    numbers = Field(attribute='numbers', column_name='Количество')
    date = Field(attribute='author__date', column_name='Дата заявки')


class ListyAdmin(ImportExportModelAdmin):
    resource_class = UserResource


admin.site.register(Author, AuthorAdmin)

