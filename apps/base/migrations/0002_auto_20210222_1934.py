# Generated by Django 3.1.3 on 2021-02-22 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemodel',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
