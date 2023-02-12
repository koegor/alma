from django.db import models

# Create your models here.


class Specialty(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Название направления')
    code = models.CharField(max_length=10, verbose_name='Код направления')
    url = models.URLField(verbose_name="Адрес сайта")

    class Meta:
        ordering = ['name']
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return f"{self.name}"


TYPES = (
    (0, "Тип Да/Нет"),
    (1, "Тип число")
)


class Property(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Название признака')
    quest = models.CharField(max_length=200, verbose_name='Вопрос')
    typ = models.IntegerField(choices=TYPES, unique=True, verbose_name='Вопрос')

    class Meta:
        ordering = ['name']
        verbose_name = 'Признак'
        verbose_name_plural = 'Признаки'

    def __str__(self):
        return f"{self.name}"


class Inst(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Институт')
    short_name = models.CharField(max_length=10)
    url = models.URLField(verbose_name="Адрес сайта")
    specialities = models.ManyToManyField(Specialty)
    properties = models.ManyToManyField(Property)

    class Meta:
        ordering = ['short_name']
        verbose_name = 'Институт'
        verbose_name_plural = 'Институты'

    def __str__(self):
        return f"{self.short_name}"
