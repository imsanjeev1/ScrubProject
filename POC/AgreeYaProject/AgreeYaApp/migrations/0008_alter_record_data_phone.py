# Generated by Django 3.2 on 2023-04-30 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgreeYaApp', '0007_alter_record_data_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record_data',
            name='Phone',
            field=models.CharField(max_length=500),
        ),
    ]