# Generated by Django 2.2.3 on 2019-08-15 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_weather'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weather',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Погода'},
        ),
        migrations.AddField(
            model_name='weather',
            name='user_name',
            field=models.CharField(default='', max_length=45, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='name',
            field=models.CharField(max_length=45, verbose_name='Название города'),
        ),
    ]