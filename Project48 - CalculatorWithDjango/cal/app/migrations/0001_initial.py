# Generated by Django 5.1.3 on 2024-11-21 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name1', models.CharField(max_length=100)),
                ('s_name2', models.CharField(max_length=100)),
                ('s_out', models.CharField(max_length=100)),
            ],
        ),
    ]
