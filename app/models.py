"""
Здесь пишутся модели для приложения (через ооп созадются таблицы с которыми можно потом будет работать на сайте)
"""

from django.db import models
class News(models.Model):
    name = models.CharField(max_length=50,verbose_name='Заголовок')
    short_description = models.CharField(max_length=200,verbose_name='Краткое описание',blank=True)
    description=models.TextField(verbose_name='Описание',blank=True)
    preview = models.ImageField('Фотография', upload_to="app/photos", default='',blank=True)
    photo = models.ImageField('Фотография', upload_to="app/photos", default='',blank=True)
    #Мета данные чтобы названия таблиц в панели администратора были на русском
    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'
        ordering=['id']
    def __str__ (self):
        return self.name