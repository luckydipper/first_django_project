# Generated by Django 3.0.8 on 2020-07-28 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='create_data',
            new_name='create_date',
        ),
    ]
