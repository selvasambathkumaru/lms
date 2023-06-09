# Generated by Django 4.2 on 2023-04-06 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsdetails', '0004_alter_empdetails_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=255)),
                ('leave_type', models.CharField(max_length=255)),
                ('leave_reason', models.CharField(max_length=255)),
                ('requesting_to', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
