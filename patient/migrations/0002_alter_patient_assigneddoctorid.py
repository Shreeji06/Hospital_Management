# Generated by Django 4.0.5 on 2022-06-29 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_alter_doctor_profile_pic'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='assignedDoctorId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor'),
        ),
    ]