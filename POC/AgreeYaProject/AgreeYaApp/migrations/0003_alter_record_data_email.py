# Generated by Django 3.2 on 2023-04-27 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgreeYaApp', '0002_alter_record_data_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record_data',
            name='Email',
            field=models.EmailField(blank=True, max_length=70, null=True),
        ),
    ]