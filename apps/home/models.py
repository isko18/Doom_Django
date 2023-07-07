from django.db import models

# Create your models here.
class Settings(models.Model):
    name_site = models.CharField(
        max_length=150,
        verbose_name="Название сайта"
    )
    logo_site = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип сайта"
    )
    info_site = models.CharField(
        max_length=255,
        verbose_name="Дополнительная информация о сайте"
    )

    def __str__(self):
        return self.name_site
    
    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройка сайта"
    

class Socialnetworks(models.Model):
    phone = models.CharField(
    max_length=255,
    verbose_name="Тел.номер"
    )
    google = models.EmailField(
        verbose_name="Почта"
    )
    locate = models.CharField(
        max_length=255,
        verbose_name="Адрес"
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
        return self.phone
    
    class Meta:
        verbose_name = "Настройки соц.сетей"
        verbose_name_plural = "Настройка соц.сетей"

class Doom(models.Model):
    name_doom = models.CharField(
        max_length=50,
        verbose_name="Слайд №1"
    )
    name_doom2 = models.CharField(
        max_length=50,
       verbose_name="Слайд №2"
    )
    name_doom3 = models.CharField(
        max_length=50,
        verbose_name="Слайд №3"
    )

    def __str__(self):
        return self.name_doom
    
    class Meta:
        verbose_name = "Настройка домой"
        verbose_name_plural = "Настройки домой"



