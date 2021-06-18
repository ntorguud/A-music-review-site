# Generated by Django 3.2.1 on 2021-05-16 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Club', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventtitle', models.CharField(max_length=255)),
                ('location', models.TextField(blank=True, null=True)),
                ('eventdate', models.DateField()),
                ('eventtime', models.DateTimeField()),
                ('description', models.TextField()),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetingtitle', models.CharField(max_length=255)),
                ('meetingdate', models.DateField()),
                ('meetingtime', models.DateTimeField()),
                ('location', models.TextField(blank=True, null=True)),
                ('agenda', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Meeting',
            },
        ),
        migrations.CreateModel(
            name='MeetingMinutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetingid', models.CharField(max_length=255)),
                ('minutestext', models.TextField()),
                ('attendance', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourcename', models.CharField(max_length=255)),
                ('resourceurl', models.URLField()),
                ('dateentered', models.DateField()),
                ('description', models.TextField()),
                ('resourcetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Club.meeting')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Resource',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='producttype',
        ),
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.DeleteModel(
            name='ClubType',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
