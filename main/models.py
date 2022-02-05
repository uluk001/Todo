from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=55, verbose_name="Заголовок")
    discription = models.CharField(max_length=255, verbose_name="Описание")
    sent_at = models.DateTimeField (auto_now_add=True, verbose_name="Дата и время публикации")

# class Comments(models.Model):
    
# class My_skill(models.Model):
#     discription2 = models.TextField(verbose_name='Навыки')
#     sent_at2 = models.DateTimeField(auto_now_add=True,verbose_name="Дата и время публикации")
