# Generated by Django 3.2.12 on 2022-02-20 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220215_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password_quiz',
            field=models.CharField(choices=[('내 보물 1호는?', '내 보물 1호는?'), ('처음 키운 반려동물 이름은?', '처음 키운 반려동물 이름은?'), ('어머니 성함은?', '어머니 성함은?'), ('아버지 성함은?', '아버지 성함은?'), ('좋아하는 음식은?', '좋아하는 음식은?')], default='내 보물 1호는?', max_length=100),
        ),
    ]