# Generated by Django 2.2.7 on 2019-11-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=256, unique=True),
        ),
    ]
