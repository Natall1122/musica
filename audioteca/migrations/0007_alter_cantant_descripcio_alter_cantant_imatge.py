# Generated by Django 5.0 on 2023-12-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioteca', '0006_cantant_imatge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cantant',
            name='descripcio',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cantant',
            name='imatge',
            field=models.ImageField(null=True, upload_to='audioteca/static/imatge'),
        ),
    ]
