# Generated by Django 4.2.6 on 2023-10-21 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TourETAPP', '0011_remove_userprofile_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='image',
            field=models.ImageField(default=1, upload_to='package_images/'),
            preserve_default=False,
        ),
    ]
