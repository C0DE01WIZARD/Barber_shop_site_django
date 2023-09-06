from django.db import models

# Create your models here.


class Hairstyles(models.Model):  # создаем модели для причесок
    type = models.TextField("Тип прически", max_length=20, blank=True)
    price = models.CharField('Цена прически', max_length=4)
    description = models.TextField("Описание прически", max_length=255, default='default title')
    image_hairs = models.ImageField('Фотография прически', upload_to='Hairstyles/', default='default title')

    def __str__(self):
        return self.type


class Barber(models.Model):  # создаем модель для Барберов
    name = models.CharField(max_length=20, blank=False)
    types_hairstyle = models.ForeignKey(Hairstyles, on_delete=models.CASCADE)

    def __str__(self):
        return f" ID:{self.id} {self.name}"

