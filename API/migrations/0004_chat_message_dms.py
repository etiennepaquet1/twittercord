# Generated by Django 4.2.4 on 2023-08-29 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_alter_friend_friend_profile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senderId', models.CharField(default='', max_length=16)),
                ('content', models.CharField(default='', max_length=1048576)),
                ('timedate', models.DateTimeField(auto_now_add=True)),
                ('edited', models.BooleanField(default=False)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='messages', to='API.chat')),
            ],
        ),
        migrations.CreateModel(
            name='DMs',
            fields=[
                ('chat_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='API.chat')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='DMs', to='API.friend')),
            ],
            bases=('API.chat',),
        ),
    ]
