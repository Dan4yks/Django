# Generated by Django 2.2.3 on 2019-08-07 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20190806_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, verbose_name='Имя пользователя')),
                ('review', models.TextField(verbose_name='Отзыв')),
            ],
        ),
    ]
