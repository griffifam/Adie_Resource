# Generated by Django 2.1.5 on 2019-01-21 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adie_app', '0003_auto_20190109_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adie',
            name='orientation',
            field=models.CharField(choices=[('straight', 'straight'), ('queer-lesbian', 'lesbian'), ('queer-gay', 'gay'), ('queer-bisexual', 'bisexual'), ('asexual', 'asexual')], max_length=20),
        ),
    ]
