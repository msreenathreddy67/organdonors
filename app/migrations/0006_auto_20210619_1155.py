# Generated by Django 3.1.7 on 2021-06-19 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_delete_patientrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hopitals',
            name='Hospital_Loc',
            field=models.CharField(max_length=20),
        ),
    ]
