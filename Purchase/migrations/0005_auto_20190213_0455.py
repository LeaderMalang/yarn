# Generated by Django 2.0.9 on 2019-02-13 04:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Purchase', '0004_auto_20190212_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('base64Image', models.BinaryField()),
            ],
        ),
        migrations.AlterField(
            model_name='contracts',
            name='dateOfEntry',
            field=models.DateField(default=datetime.datetime(2019, 2, 13, 4, 55, 39, 935357), editable=False),
        ),
    ]
