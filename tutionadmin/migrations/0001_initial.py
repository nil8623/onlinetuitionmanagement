# Generated by Django 3.0.5 on 2020-07-10 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddCourse',
            fields=[
                ('courseid', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.CharField(max_length=60)),
                ('faculty', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=20)),
                ('fee', models.IntegerField()),
                ('duration', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MainAdminRegister',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=60)),
            ],
        ),
    ]