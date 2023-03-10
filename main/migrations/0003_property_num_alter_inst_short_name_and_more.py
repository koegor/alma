# Generated by Django 4.1.6 on 2023-02-13 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_specialty_url_alter_inst_properties_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='num',
            field=models.IntegerField(default=0, unique=True, verbose_name='Порядковый номер'),
        ),
        migrations.AlterField(
            model_name='inst',
            name='short_name',
            field=models.CharField(max_length=10, verbose_name='Краткое название'),
        ),
        migrations.AlterField(
            model_name='property',
            name='typ',
            field=models.IntegerField(choices=[(0, 'Тип Да/Нет'), (1, 'Тип число')], default=0, verbose_name='Тип'),
        ),
    ]
