# Generated by Django 5.0 on 2023-12-13 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioteca', '0014_alter_cantant_imatge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cantant',
            name='imatge',
            field=models.ImageField(null=True, upload_to='audioteca/static/imatge/'),
        ),
    ]
