# Generated by Django 4.2.2 on 2023-07-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_alter_product_p_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='P_img',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
