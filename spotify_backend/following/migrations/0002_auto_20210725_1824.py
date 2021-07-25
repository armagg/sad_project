# Generated by Django 3.2.5 on 2021-07-25 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210725_0534'),
        ('playlists', '0001_initial'),
        ('following', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='followplaylist',
            name='playlist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='playlists.playlist'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='followplaylist',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.listener'),
            preserve_default=False,
        ),
    ]
