# Generated by Django 3.1.7 on 2021-06-10 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DonorReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Donor_Name', models.CharField(max_length=20)),
                ('Donor_Age', models.PositiveIntegerField()),
                ('Donor_Bloodgroup', models.CharField(max_length=20)),
                ('Donation_Item', models.CharField(max_length=20)),
                ('Donor_Phno', models.IntegerField()),
                ('Donor_Address', models.TextField()),
                ('Donor_HealthCertificate', models.ImageField(upload_to='Donor_HealthCertificate')),
            ],
        ),
    ]
