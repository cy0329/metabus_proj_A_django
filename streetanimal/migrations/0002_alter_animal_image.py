# Generated by Django 3.2.12 on 2022-02-11 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streetanimal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
