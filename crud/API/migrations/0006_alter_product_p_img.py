# Generated by Django 4.2.2 on 2023-07-03 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_alter_product_p_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_img',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
