# Generated by Django 3.2.14 on 2022-10-14 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_author_depart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='depart',
            field=models.CharField(choices=[('МСК СКЛАД', 'МСК СКЛАД'), ('МСК ОФИС', 'МСК ОФИС'), ('ПРОИЗВОДСТВО', 'ПРОИЗВОДСТВО'), ('СПБ СКЛАД', 'СПБ СКЛАД'), ('СПБ ОФИС', 'СПБ ОФИС'), ('БУХГАЛТЕРИЯ', 'БУХГАЛТЕРИЯ'), ('СВЕТОН', 'СВЕТОН'), ('ЭЛЕКТРОПРОЕКТ', 'ЭЛЕКТРОПРОЕКТ'), ('ИНОЛ', 'ИНОЛ'), ('МАГАЗИН БЕЛОВОДСКИЙ', 'МАГАЗИН БЕЛОВОДСКИЙ'), ('МАГАЗИН ВАРШАВКА', 'МАГАЗИН ВАРШАВКА')], max_length=50, verbose_name='Департамент'),
        ),
    ]
