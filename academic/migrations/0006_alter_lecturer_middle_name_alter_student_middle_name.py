# Generated by Django 4.1 on 2022-09-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0005_alter_lecturer_middle_name_alter_student_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='middle_name',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]
