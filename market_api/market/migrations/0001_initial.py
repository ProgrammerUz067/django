# Generated by Django 5.0 on 2024-02-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OziqOvqat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ishlab_chiqaruvchi', models.TextField()),
                ('narxi', models.IntegerField()),
                ('yaroqlilik_mudati', models.IntegerField()),
                ('rangi', models.CharField(max_length=250)),
            ],
        ),
    ]