# Generated by Django 4.1 on 2022-09-05 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_alter_program_duration_alter_school_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(choices=[('SPAS', 'School of Pure and Applied Sciences'), ('SAB', 'School of Agriculture and Biotechnology'), ('SOB', 'School of Business'), ('SESS', 'School of Education and Social Sciences'), ('SNRE', 'School of Natural Resources and Environmental Studies'), ('SN', 'School of Business')], max_length=4),
        ),
    ]
