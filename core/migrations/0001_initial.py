# Generated by Django 4.1.2 on 2022-10-11 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City', models.CharField(max_length=30)),
                ('Code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Duration', models.IntegerField()),
                ('Passengers', models.ManyToManyField(to='core.user')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival', to='core.airport')),
                ('Origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure', to='core.airport')),
                ('Pilot', models.ManyToManyField(to='core.user')),
                ('Trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trip')),
            ],
        ),
    ]
