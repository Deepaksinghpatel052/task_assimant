# Generated by Django 3.1.5 on 2021-01-30 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_webpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='Created_date',
            field=models.DateField(),
        ),
    ]
