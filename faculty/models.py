from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")
    boss = models.CharField(max_length=100, verbose_name="Завідувач")

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедри"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Specialty(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")
    code = models.CharField(max_length=3, verbose_name="Код")
    desc = models.TextField(verbose_name="Опис")
    coord_name = models.CharField(max_length=100, verbose_name="Ім'я координатора")
    coord_contact = models.CharField(max_length=100, verbose_name="Контакт "
                                                                  "координатора")
    department = models.ForeignKey(Department, on_delete=models.PROTECT,
                                   related_name="specialties", verbose_name="Кафедра")
    list_of_subjects = models.TextField(verbose_name="Перелік предметів")

    class Meta:
        verbose_name = "Спеціальність"
        verbose_name_plural = "Спеціальності"
        ordering = ["code"]

    def __str__(self):
        return f"{self.name}"


class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    position = models.CharField(max_length=100, verbose_name="Посада")
    degree = models.CharField(max_length=100, verbose_name="Ступінь")
    department = models.ForeignKey(Department, on_delete=models.PROTECT,
                                   related_name="teachers", verbose_name="Кафедра")

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"

