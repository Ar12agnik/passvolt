# Generated by Django 3.0.5 on 2024-02-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Url', models.URLField()),
                ('Username', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]