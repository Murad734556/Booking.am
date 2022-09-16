from django.db import models
from apps.countries.models import Country
from django.db.models.signals import pre_save
from apps.hotels.slug_generator import unique_slug_generators
# Create your models here.

class Places(models.Model):
    country =models.ForeignKey(Country, on_delete=models.CASCADE, related_name="place_from_country")
    title= models.CharField(max_length=255, verbose_name="Название места")
    image= models.ImageField(upload_to="place_image", verbose_name="Фото места")
    description= models.TextField(verbose_name="Описание", blank=True, null=True)
    slug  = models.SlugField(blank=True, null = True, unique = True, verbose_name="Автогенерация URL")


    def __str__(self):
        return self.title


    class Meta:
        verbose_name= "Место"
        verbose_name_plural= "Места"

class PlaceImage(models.Model):
    place= models.ForeignKey(Places, on_delete=models.CASCADE, related_name="image_place")
    image= models.ImageField(upload_to= "second_place_image/")

    class Meta:
        verbose_name= "Дополнительная фотография"
        verbose_name_plural= "Дополнительные фотографии"


def slag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generators(instance)


pre_save.connect(slag_pre_save_receiver, sender=Places)