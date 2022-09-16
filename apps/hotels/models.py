from django.db import models
from apps.places.models import Places
from django.db.models.signals import pre_save
from apps.hotels.slug_generator import unique_slug_generators
# Create your models here.


class Hotel(models.Model): 
    title= models.CharField(max_length=255, verbose_name="Название отеля")
    place = models.ForeignKey(Places, on_delete=models.CASCADE, related_name="hotels_in_place")
    description= models.TextField(verbose_name="Описание", blank=True, null=True)
    image= models.ImageField(upload_to="hotel_image", verbose_name="Фото отеля")
    CHOICE_CURRENCY =(
        ('Хостел', 'Хостел'),
        ('Гостиница', 'Гостиница'),
        ('Отель', 'Отель'),
        ('Апартаменты', 'Апартаменты'),
        ('Аренда', 'Аренда')
    )
    hotel_type= models.CharField(max_length=100, choices=CHOICE_CURRENCY, default='Отель')
    phone= models.CharField(max_length=100, default='+996 708 89 03 08')
    RESTAURANT=(
        ('Да', 'Да'),
        ('Нет', 'Нет'),
    )
    restaurant= models.CharField(choices=RESTAURANT, max_length=10, default='Not')
    slug = models.SlugField(blank=True, null = True, unique = True, verbose_name="Автогенерация URL")
    valid= models.BooleanField(default=True, verbose_name="Работает") 
    price=models.PositiveIntegerField()


    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"


class HotelImage(models.Model):
    hotel= models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="restaurant_image")
    image= models.ImageField(upload_to= "second_restaurant_image/")

    class Meta:
        verbose_name= "Дополнительная фотография"
        verbose_name_plural= "Дополнительные фотографии"


def slag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generators(instance)


pre_save.connect(slag_pre_save_receiver, sender=Hotel)