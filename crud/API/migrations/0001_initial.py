# Generated by Django 4.2.2 on 2023-07-02 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=200)),
                ('p_catagory', models.CharField(max_length=100)),
                ('p_disc', models.TextField()),
                ('p_price', models.IntegerField()),
            ],
        ),
    ]
