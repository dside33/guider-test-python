# Generated by Django 5.0.7 on 2024-07-20 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='street',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
