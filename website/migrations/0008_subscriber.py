# Generated by Django 2.2.7 on 2019-11-10 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20191109_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=256)),
                ('last_emailed_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
