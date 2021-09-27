from django.db import models

from users.models import Users


class Projects(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    link = models.CharField(max_length=255, verbose_name='Ссылка', blank=True)
    users = models.ManyToManyField(Users, verbose_name='Пользователи')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class ProjectsTodo(models.Model):
    STATUS_NEW = 0
    STATUS_WORK = 1
    STATUS_CLOSE = 2

    STATUSES = (
        (STATUS_NEW, 'Новый'),
        (STATUS_WORK, 'В работе'),
        (STATUS_CLOSE, 'Закрыто'),
    )

    project = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name='Проект')
    description = models.TextField(blank=False, verbose_name='Описание')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Создатель')
    status = models.IntegerField(default=STATUS_NEW, choices=STATUSES, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return f'{self.project.title}'
