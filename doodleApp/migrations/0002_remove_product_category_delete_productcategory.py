# Generated by Django 5.2.2 on 2025-06-14 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doodleApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
    ]
