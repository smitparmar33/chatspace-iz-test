# Generated by Django 4.0.5 on 2022-07-01 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_chatmodel_receiver_alter_chatmodel_sender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatmodel',
            old_name='thread_name',
            new_name='room_name',
        ),
        migrations.AddField(
            model_name='chatmodel',
            name='platform_name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]