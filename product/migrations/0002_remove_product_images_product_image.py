# Generated by Django 4.1.7 on 2023-03-27 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(default='', upload_to='product_images'),
            preserve_default=False,
        ),
    ]
