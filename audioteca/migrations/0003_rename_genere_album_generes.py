# Generated by Django 5.0 on 2023-12-12 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audioteca', '0002_cantant_descripcio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='genere',
            new_name='generes',
        ),
    ]