from django.db import models
from django.utils import timezone


class ExchangeProgram(models.Model):
    university = models.CharField(max_length=256, verbose_name="Університет")
    languages = models.CharField(max_length=256, verbose_name="Мови навчання")
    deadline = models.DateField(verbose_name="Дедлайн подачі")
    description = models.TextField(verbose_name="Опис")
    country = models.CharField(max_length=128, verbose_name="Країна", default="")
    seats = models.IntegerField(verbose_name="Кількість місць", null=True)

    class Meta:
        verbose_name = "Програма обміну"
        verbose_name_plural = "Програми обміну"

    def __str__(self):
        return self.university

    @property
    def is_closed(self):
        return self.deadline < timezone.localdate()
