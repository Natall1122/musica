# Generated by Django 5.0 on 2023-12-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioteca', '0009_alter_cantant_imatge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cantant',
            name='imatge',
            field=models.ImageField(height_field=300, null=True, upload_to='imatge/', width_field=300),
        ),
    ]
