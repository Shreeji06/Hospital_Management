# Generated by Django 4.0.5 on 2022-07-04 11:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_alter_patient_admitdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='admitDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 4, 16, 46, 59, 231394)),
        ),
    ]