# Generated by Django 2.2 on 2019-10-24 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='images')),
                ('description', models.TextField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('bio', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Projects')),
            ],
        ),
    ]
