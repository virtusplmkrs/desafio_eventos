# Generated by Django 4.2.3 on 2023-07-23 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_rename_contato_myeventouser_sobrenome_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myeventouser',
            name='sobrenome',
        ),
        migrations.AddField(
            model_name='myeventouser',
            name='fuso',
            field=models.CharField(default='1', max_length=6),
        ),
    ]
