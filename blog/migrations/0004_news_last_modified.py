# Generated by Django 4.1 on 2022-09-06 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_news_published_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
