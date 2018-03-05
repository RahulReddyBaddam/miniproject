# Generated by Django 2.0.2 on 2018-02-17 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20180218_0327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='category',
        ),
        migrations.AddField(
            model_name='site',
            name='cat',
            field=models.CharField(choices=[('apartments', 'Apartments'), ('houses', 'Houses'), ('land', 'Land')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
