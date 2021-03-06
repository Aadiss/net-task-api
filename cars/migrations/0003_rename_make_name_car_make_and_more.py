# Generated by Django 4.0 on 2021-12-28 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='Make_Name',
            new_name='make',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='Model_Name',
            new_name='model',
        ),
        migrations.AlterUniqueTogether(
            name='car',
            unique_together={('make', 'model')},
        ),
    ]
