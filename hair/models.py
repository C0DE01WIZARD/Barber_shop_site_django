from django.db import models


class Hairstyles(models.Model):  # создаем модели для причесок
    type = models.TextField("Тип прически", max_length=20, blank=True)
    price = models.CharField('Цена прически', max_length=4)
    image_hairs = models.ImageField(upload_to='Hairstyles/', default='default title')

    def __str__(self):
        return self.type


class Barber(models.Model):  # создаем модель для Барберов
    name = models.CharField('Ими барбера', max_length=20, blank=False)
    types_hairstyle = models.ForeignKey(Hairstyles, verbose_name='Тип прически', on_delete=models.CASCADE)
    image = models.ImageField('Выберите изображение', upload_to='images/')

    def __str__(self):

        return f" ID:{self.id} {self.name}"


class Records(models.Model):
    name = models.CharField("Ваше имя", max_length=24, default='title')
    barbres = models.ForeignKey(Barber, on_delete=models.CASCADE)
    datetime = models.DateTimeField('Время и дата записи')

    def __str__(self):
        return f'Время: {self.datetime} | Имя: {self.name}| Барбер: {self.barbres}'
