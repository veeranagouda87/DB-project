# Generated by Django 2.1 on 2019-04-14 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loginfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=64, null=True)),
                ('lname', models.CharField(blank=True, max_length=64, null=True)),
                ('email', models.CharField(blank=True, max_length=64, null=True)),
                ('passwd', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
    ]
