# Generated by Django 4.0.4 on 2022-05-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_game_message_room_alter_customuser_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_avatar',
            field=models.ImageField(default='user_avatars/profimg/DEFAULT_6.png', upload_to='user_avatars'),
        ),
    ]