# Generated by Django 4.2.1 on 2023-11-13 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_record_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='created_at',
            field=models.DateTimeField(max_length=50),
        ),
    ]