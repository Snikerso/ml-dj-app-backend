# Generated by Django 3.0.3 on 2020-06-14 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regression', '0003_auto_20200614_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='picture1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='picture2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='picture3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='picture4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='picture5',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='picture6',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='picture_predicted',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='picture_target',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
