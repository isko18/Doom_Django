from django.db import models

# Create your models here.


class Socialnetworks(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Тел.номер"
    )
    email = models.EmailField(
        verbose_name="Почта",
        null=True,blank=True
    )
    locate = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    message = models.TextField(
        max_length=255,
        verbose_name="Введите ваше сообщение"
    )
    subject = models.CharField(
        max_length=255,
        verbose_name="Тема сообщения"
    
    )
    twitter = models.URLField(
        verbose_name="Ссылка на twiter"
    )
    facebook = models.URLField(
        verbose_name="Ссылка на Facebook"
    )
    linkedin = models.URLField(
        verbose_name="Ссылка на linkedin"
    )
    youtube = models.URLField(
        verbose_name="Ссылка на Youtube"
    )
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Настройки контактов"
        verbose_name_plural = "Настройка контактов"