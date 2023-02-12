# Generated by Django 4.1.6 on 2023-02-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialty',
            name='url',
        ),
        migrations.AlterField(
            model_name='inst',
            name='properties',
            field=models.ManyToManyField(blank=True, null=True, to='main.property', verbose_name='Признаки'),
        ),
        migrations.AlterField(
            model_name='inst',
            name='specialities',
            field=models.ManyToManyField(blank=True, null=True, to='main.specialty', verbose_name='Направления'),
        ),
        migrations.AlterField(
            model_name='property',
            name='typ',
            field=models.IntegerField(choices=[(0, 'Тип Да/Нет'), (1, 'Тип число')], unique=True, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Код направления'),
        ),
    ]