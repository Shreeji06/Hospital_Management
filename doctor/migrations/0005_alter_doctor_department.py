# Generated by Django 4.0.5 on 2022-06-30 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_alter_doctor_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons'), ('Pediatricians', 'Pediatricians'), ('Ophthalmologists', 'Ophthalmologists'), ('Endocrinologists', 'Endocrinologists'), ('Gastroenterologists', 'Gastroenterologists'), ('Nephrologists', 'Nephrologists'), ('Urologists', 'Urologists'), ('Pulmonologists', 'Pulmonologists'), ('Otolaryngologists', 'Otolaryngologists'), ('Neurologists', 'Neurologists'), ('Psychiatrists', 'Psychiatrists'), ('Oncologists', 'Oncologists'), ('Radiologists', 'Radiologists'), ('Rheumatologists', 'Rheumatologists')], default='Cardiologist', max_length=50),
        ),
    ]
