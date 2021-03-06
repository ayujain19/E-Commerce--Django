# Generated by Django 3.0.7 on 2020-07-01 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200630_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(max_length=501),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='', max_length=100),
        ),
    ]
