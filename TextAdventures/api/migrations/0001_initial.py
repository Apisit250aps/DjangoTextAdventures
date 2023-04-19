# Generated by Django 4.1.7 on 2023-04-19 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('attack', models.IntegerField(blank=True, default=10)),
                ('health', models.IntegerField(blank=True, default=100)),
                ('defense', models.IntegerField(blank=True, default=100)),
                ('levels', models.IntegerField(blank=True, default=1)),
                ('gold', models.IntegerField(blank=True, default=0)),
                ('status_points', models.IntegerField(blank=True, default=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('damage', models.IntegerField(default=0)),
                ('defense', models.IntegerField(default=0)),
                ('category', models.IntegerField(choices=[(1, 'weapon'), (2, 'armor')])),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('levels', models.IntegerField()),
                ('health', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('exp_drop', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('detail', models.TextField(max_length=128)),
                ('target', models.CharField(max_length=64)),
                ('unit', models.IntegerField()),
                ('reward_type', models.IntegerField(choices=[(1, 'exp'), (2, 'gold')])),
                ('reward_unit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StatusPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str', models.IntegerField(default=1)),
                ('vit', models.IntegerField(default=1)),
                ('agi', models.IntegerField(default=1)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.character')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_id', models.IntegerField(blank=True)),
                ('unit', models.IntegerField(default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.character')),
            ],
        ),
    ]
