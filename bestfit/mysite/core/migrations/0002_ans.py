# Generated by Django 2.2.7 on 2019-12-05 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(default=False)),
                ('anskey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Test')),
            ],
        ),
    ]
