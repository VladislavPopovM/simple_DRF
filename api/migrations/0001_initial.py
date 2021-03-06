# Generated by Django 3.1 on 2020-11-09 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('second_name', models.CharField(max_length=32)),
                ('middle_name', models.CharField(max_length=32)),
                ('numb_pass', models.PositiveBigIntegerField()),
                ('born_date', models.DateField()),
                ('place_born', models.CharField(max_length=128)),
                ('get_pass_date', models.DateField()),
                ('department_code', models.PositiveIntegerField()),
                ('issued_by', models.CharField(max_length=128)),
                ('reg_address', models.CharField(max_length=128)),
                ('photo', models.ImageField(upload_to='users/')),
                ('investor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.investor')),
            ],
        ),
    ]
