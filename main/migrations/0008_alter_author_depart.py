# Generated by Django 3.2.14 on 2022-10-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_author_depart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='depart',
            field=models.CharField(choices=[('МСК СКЛАД', 'МСК СКЛАД'), ('МСК ОФИС', 'МСК ОФИС'), ('ПРОИЗВОДСТВО', 'ПРОИЗВОДСТВО'), ('СКЛАД', 'СКЛАД'), ('ОФИС', 'ОФИС'), ('БУХГАЛТЕРИЯ', 'БУХГАЛТЕРИЯ'), ('СВЕТОН', 'СВЕТОН'), ('ЭЛЕКТРОПРОЕКТ', 'ЭЛЕКТРОПРОЕКТ'), ('МАГАЗИН БЕЛОВОДСКИЙ', 'МАГАЗИН БЕЛОВОДСКИЙ'), ('МАГАЗИН ВАРШАВКА', 'МАГАЗИН ВАРШАВКА')], max_length=50, verbose_name='Департамент'),
        ),
    ]