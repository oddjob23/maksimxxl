# Generated by Django 2.2.7 on 2019-11-09 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20191109_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discout',
            new_name='discount',
        ),
    ]
