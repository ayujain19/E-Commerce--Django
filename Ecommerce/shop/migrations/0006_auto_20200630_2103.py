# Generated by Django 3.0.7 on 2020-06-30 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='city',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='state',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(max_length=111),
        ),
    ]
