# Generated by Django 4.1.3 on 2022-11-28 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_resume_id_resume_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='likes',
            fields=[
                ('resume_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.resume')),
                ('like', models.IntegerField()),
            ],
            bases=('myapp.resume',),
        ),
    ]
