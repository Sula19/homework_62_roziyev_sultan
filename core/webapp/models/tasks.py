from django.db import models


class Task(models.Model):
    summary = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Краткое описание'
    )
    description = models.TextField(
        max_length=2500,
        null=True,
        blank=False,
        verbose_name='Описание'
    )
    project = models.ForeignKey(
        to='webapp.Project',
        related_name='tasks',
        on_delete=models.PROTECT
    )
    status = models.ForeignKey(
        to='webapp.Status',
        related_name='status',
        on_delete=models.PROTECT
    )
    type = models.ManyToManyField(
        to='webapp.Type',
        related_name='type',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата и время обновления'
    )

    def __str__(self):
        return f'{self.summary}, {self.status}'