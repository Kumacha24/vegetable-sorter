# Generated by Django 2.2.24 on 2021-09-27 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='画像')),
            ],
        ),
    ]