# Generated by Django 4.0.4 on 2022-04-27 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.BigIntegerField(unique=True, verbose_name='UserID')),
                ('name', models.CharField(max_length=255, verbose_name='UserName')),
                ('second_name', models.CharField(default='', max_length=255, verbose_name='SirName')),
                ('username', models.CharField(default='', max_length=255, verbose_name='username')),
                ('user_role', models.CharField(max_length=255, verbose_name='Роль')),
                ('chat_id', models.BigIntegerField(default=0, verbose_name='Чат пользователя')),
                ('chanel_id', models.BigIntegerField(default=0, verbose_name='Канал пользователя')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='UserDiscussion',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('history', models.CharField(max_length=1000000, null=True, verbose_name='История вопроса')),
                ('mes_id', models.CharField(default='', max_length=20000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersupport.telegramuser', verbose_name='Пользователь')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
