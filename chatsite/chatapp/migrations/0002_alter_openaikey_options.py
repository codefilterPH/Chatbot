# Generated by Django 4.1.7 on 2023-03-24 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='openaikey',
            options={'verbose_name': 'API KEY', 'verbose_name_plural': 'API KEY'},
        ),
    ]