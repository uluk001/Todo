from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=55, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField (auto_now_add=True, verbose_name="Дата и время публикации")
    is_done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title}'