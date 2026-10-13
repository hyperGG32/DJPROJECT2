from django.db import models


class ExchangeProgram(models.Model):
    university = models.CharField(max_length=256, verbose_name="Університет")
    languages = models.CharField(max_length=256, verbose_name="Мови навчання")
    slots = models.CharField(max_length=10, verbose_name="Кількість місць")
    deadline = models.DateField(verbose_name="Дедлайн подачі")
    description = models.TextField(verbose_name="Опис")

    class Meta:
        verbose_name = "Програма обміну"
        verbose_name_plural = "Програми обміну"

    def __str__(self):
        return self.university
