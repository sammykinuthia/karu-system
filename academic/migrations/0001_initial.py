# Generated by Django 4.1 on 2022-09-05 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
                ('duration', models.IntegerField(max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academic.department')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('SPAS', 'School Of Pure And Applied Sciences'), ('SAB', 'School of Agriculture and Biotechnology'), ('SOB', 'School of Business'), ('SESS', 'School of Education and Social Sciences'), ('SNRE', 'School of Natural Resources and Environmental Studies'), ('SN', 'School of Natural Resources and Environmental Studies')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200)),
                ('adm_number', models.CharField(max_length=20, unique=True)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('adm_date', models.DateTimeField(auto_now_add=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academic.program')),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredUnits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_code', models.CharField(choices=[('y1s1', 'y1s1'), ('y1s2', 'y1s2'), ('y1s3', 'y1s3'), ('y2s1', 'y2s1'), ('y2s2', 'y2s2'), ('y2s3', 'y2s3'), ('y3s1', 'y3s1'), ('y3s2', 'y3s2'), ('y3s3', 'y3s3'), ('y4s1', 'y4s1'), ('y4s2', 'y4s2'), ('y4s3', 'y4s3')], max_length=4)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.student')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academic.unit')),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Dr', 'Dr'), ('Prof', 'Prof')], max_length=4)),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('adm_date', models.DateTimeField(auto_now_add=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academic.school')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='academic.school'),
        ),
    ]