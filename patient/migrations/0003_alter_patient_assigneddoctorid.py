# Generated by Django 4.0.5 on 2022-06-29 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_patient_assigneddoctorid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='assignedDoctorId',
            field=models.IntegerField(null=True),
        ),
    ]
