# Generated by Django 3.2 on 2021-05-06 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoBanglaApp', '0002_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userprofile', models.FileField(upload_to='')),
            ],
        ),
    ]