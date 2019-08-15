"""
Здесь пишутся модели для приложения (через ооп созадются таблицы с которыми можно потом будет работать на сайте)
"""

from django.db import models
class News(models.Model):
    name = models.CharField(max_length=50,verbose_name='Заголовок')
    short_description = models.CharField(max_length=200,verbose_name='Краткое описание',blank=True)
    description=models.TextField(verbose_name='Описание',blank=True)
    preview = models.ImageField('Превью', upload_to="app/photos", default='',blank=True)
    photo = models.ImageField('Первый слайд', upload_to="app/photos", default='',blank=True)
    photo2 = models.ImageField('Второй слайд', upload_to="app/photos", default='',blank=True)
    code = models.TextField(verbose_name='Пример кода',blank=True)
    code2 = models.TextField(verbose_name='Пример кода',blank=True)
    slaid_name1 = models.CharField(max_length=50,verbose_name='Название первого слайда/Название первого файла с примером кода',default='',blank=True )
    slaid_name2 = models.CharField(max_length=50,verbose_name='Название второго слайда/Название второго файла с примером кода',default='',blank=True)
    #Мета данные чтобы названия таблиц в панели администратора были на русском
    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'
        ordering=['id']
    def __str__ (self):
        return self.name

class Review(models.Model):
    user_name = models.CharField(max_length=50,verbose_name='Имя пользователя')
    review = models.TextField(verbose_name='Отзыв')
    def __str__ (self):
        return self.user_name
class Weather(models.Model):
    user_name = models.CharField(max_length=45,verbose_name='Имя пользователя',default='')
    name = models.CharField(max_length=45,verbose_name='Название города')
    class Meta:
        verbose_name='Город'
        verbose_name_plural='Погода'
    def __str__(self):
        return self.name