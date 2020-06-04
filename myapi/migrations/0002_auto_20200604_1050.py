# Generated by Django 2.1.2 on 2020-06-04 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=60)),
                ('tz', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
        migrations.AddField(
            model_name='activityperiod',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.User'),
        ),
    ]
