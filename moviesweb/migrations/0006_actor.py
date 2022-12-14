# Generated by Django 4.1.1 on 2022-09-21 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesweb', '0005_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('movies', models.ManyToManyField(related_name='actors', to='moviesweb.movie')),
            ],
        ),
    ]
