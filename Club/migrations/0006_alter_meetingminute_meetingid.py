# Generated by Django 3.2.1 on 2021-06-11 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Club', '0005_alter_meetingminute_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingminute',
            name='meetingid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Club.meeting'),
        ),
    ]
