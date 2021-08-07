# Generated by Django 3.2.6 on 2021-08-05 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('file_id', models.IntegerField()),
                ('file_type', models.CharField(choices=[('podcast', 'podcast'), ('music', 'music')], max_length=7)),
                ('lenght', models.IntegerField(verbose_name='time in seconds')),
                ('release_date', models.DateField()),
                ('cover', models.ImageField(upload_to='', verbose_name='cover')),
                ('played_count', models.IntegerField(default=0)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.provider')),
                ('singers', models.ManyToManyField(to='accounts.Singer')),
            ],
        ),
        migrations.CreateModel(
            name='MusicGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.SmallIntegerField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.genre')),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.music')),
            ],
        ),
    ]
