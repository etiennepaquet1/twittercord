# Generated by Django 4.2.4 on 2023-08-29 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0009_delete_bungo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bungo',
            fields=[
                ('code', models.CharField(default='', max_length=16, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('description', models.CharField(default='', max_length=4096)),
                ('stranger_can_see', models.BooleanField(default=False)),
                ('stranger_can_mssg', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
