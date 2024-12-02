# Generated by Django 5.1.3 on 2024-12-01 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='read',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('para1', models.TextField()),
                ('para2', models.TextField()),
                ('para3', models.TextField()),
                ('img1', models.URLField()),
                ('para4', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.card')),
            ],
        ),
    ]
