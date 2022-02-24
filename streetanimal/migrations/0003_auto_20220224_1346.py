# Generated by Django 3.2.12 on 2022-02-24 13:46

from django.db import migrations, models
import streetanimal.models


class Migration(migrations.Migration):

    dependencies = [
        ('streetanimal', '0002_auto_20220215_2236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='physical_condition',
            new_name='info',
        ),
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.ImageField(blank=True, upload_to='', validators=[streetanimal.models.validate_image]),
        ),
    ]
