# Generated by Django 4.0.5 on 2022-07-01 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_auto_20211016_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmodel',
            name='receiver',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='chatmodel',
            name='sender',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
