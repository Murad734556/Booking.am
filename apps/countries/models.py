from django.db import models
from django.db.models.signals import pre_save
from apps.countries.slug_generator import unique_slug_generators

# Create your models here.
class Country(models.Model):
    title = models.CharField(max_length=255,verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание',blank=True, null=True)
    slug = models.SlugField(blank=True, null = True, unique = True, verbose_name="Автогенерация URL")
    image = models.ImageField(upload_to='country_image',verbose_name='Фото страны')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ('-id',)


class CountryImage(models.Model):
    post= models.ForeignKey(Country, on_delete=models.CASCADE, related_name="image_post")
    image= models.ImageField(upload_to= "second_post_image/")

    class Meta:
        verbose_name= "Дополнительная фотография"
        verbose_name_plural= "Дополнительные фотографии"

def slag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generators(instance)


pre_save.connect(slag_pre_save_receiver, sender=Country)