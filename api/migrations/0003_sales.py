# Generated by Django 4.0.3 on 2022-03-23 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('month', models.CharField(max_length=3)),
                ('district_name', models.CharField(max_length=16)),
                ('sales', models.IntegerField()),
            ],
        ),
    ]