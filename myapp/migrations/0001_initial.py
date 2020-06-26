# Generated by Django 2.2.7 on 2020-06-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('phone', models.IntegerField(max_length=11)),
                ('gender', models.CharField(max_length=10)),
                ('job', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to='Profilepic/')),
            ],
        ),
    ]