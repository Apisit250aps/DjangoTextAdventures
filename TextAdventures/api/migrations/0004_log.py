# Generated by Django 4.1.7 on 2023-05-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_inventory_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.TextField(max_length=255)),
            ],
        ),
    ]
