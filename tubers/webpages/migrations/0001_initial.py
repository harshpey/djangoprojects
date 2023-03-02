# Generated by Django 4.1.3 on 2022-12-07 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('button_text', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='media/slider/%Y/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
