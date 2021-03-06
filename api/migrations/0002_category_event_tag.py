# Generated by Django 3.0.3 on 2020-03-06 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('venue_name', models.CharField(max_length=100)),
                ('venue_address', models.CharField(max_length=150)),
                ('venue_link', models.URLField()),
                ('venue_map_link', models.URLField()),
                ('ticket_link', models.URLField()),
                ('image', models.ImageField(upload_to='uploads/images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Category')),
                ('tags', models.ManyToManyField(to='api.Tag', verbose_name='Tags')),
            ],
        ),
    ]
