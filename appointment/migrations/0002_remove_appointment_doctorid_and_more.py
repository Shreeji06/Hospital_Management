# Generated by Django 4.0.5 on 2022-06-30 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='doctorId',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patientId',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctorName',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patientName',
            field=models.CharField(max_length=20),
        ),
    ]
