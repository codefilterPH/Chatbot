# Generated by Django 4.1.7 on 2023-03-24 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0004_openaikey_max_tokens_openaikey_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openaikey',
            name='key',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='openaikey',
            name='model',
            field=models.CharField(default='text-davinci-003', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='openaikey',
            name='name',
            field=models.CharField(default='API KEY', max_length=50, null=True),
        ),
    ]
