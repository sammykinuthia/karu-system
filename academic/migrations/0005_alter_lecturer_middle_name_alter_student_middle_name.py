# Generated by Django 4.1 on 2022-09-05 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0004_alter_school_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='middle_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
