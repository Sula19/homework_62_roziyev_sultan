from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    start_date = models.DateField(
        null=False,
        blank=False,
        verbose_name='Дата начала'
    )
    expiration_date = models.DateField(
        blank=True,
        verbose_name='Дата окончания'
    )
    name = models.CharField(
        max_length=40,
        null=False,
        blank=False,
        verbose_name='Название'
    )
    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False,
        verbose_name='Описание'
    )
    users = models.ManyToManyField(
        to=User,
        related_name='projects'
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        null=False,
        default=False)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def __str__(self):
        return f'{self.name} - {self.description}'
