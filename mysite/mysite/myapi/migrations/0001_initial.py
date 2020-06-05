# Generated by Django 2.1.2 on 2020-06-05 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=60)),
                ('tz', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='activityperiod',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activityperiods', to='myapi.User'),
        ),
        migrations.AlterUniqueTogether(
            name='activityperiod',
            unique_together={('user', 'id')},
        ),
    ]
