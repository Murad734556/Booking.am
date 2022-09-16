from distutils.command.upload import upload
from django.db import models
from apps.users.models import User

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название сайта")
    description = models.TextField(verbose_name="Описание сайта")
    logo = models.ImageField(upload_to = 'logo/', verbose_name="Логотип сайта")
    second_logo= models.ImageField(upload_to= 'second_logo/', verbose_name="second logo")
    phone = models.CharField(max_length=255, verbose_name="Телефонный номер")
    email = models.EmailField(max_length=150, verbose_name="Электронная почта сайта")
    facebook = models.URLField(blank = True, null=True, verbose_name="Ссылка на facebook")
    youtube = models.URLField(blank = True, null=True, verbose_name="Ссылка на youtube")
    instagram = models.URLField(blank = True, null=True, verbose_name="Ссылка на instagram")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_message")
    email=models.EmailField(max_length=100, verbose_name="Почта")
    title =models.CharField(max_length=255, verbose_name="Заголовок")
    phone =models.CharField(max_length=100, verbose_name="Номер телефона")
    problem=models.TextField(verbose_name="Проблема")
    CHOICE_STATUS=(
        ('В ожидании', 'В ожидании'),
        ('Решена', 'Решена'),
        ('Не решена', 'Не решена'),
    )       
    status = models.CharField(choices=CHOICE_STATUS, max_length=30, verbose_name="Статус обращения", default="В ожидании")

    def __str__(self):
        return f"{self.user} {self.title[0:30]}... {self.status}"

    class Meta:
        verbose_name="Сообщение Админу"
        verbose_name_plural="Сообщения Админу"