# Generated by Django 4.2.4 on 2023-08-30 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0012_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='members',
            field=models.ManyToManyField(to='API.profile'),
        ),
    ]
