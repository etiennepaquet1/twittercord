# Generated by Django 4.2.4 on 2023-08-29 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_chat_message_dms'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DMs',
        ),
    ]
