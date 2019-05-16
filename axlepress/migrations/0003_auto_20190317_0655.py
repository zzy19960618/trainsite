# Generated by Django 2.1.7 on 2019-03-17 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axlepress', '0002_auto_20190316_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caraxle',
            name='axleNo',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='carriage',
            name='carriageNo',
            field=models.SmallIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pressure',
            name='axle1_pressure',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='pressure',
            name='axle2_pressure',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='pressure',
            name='axle3_pressure',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='pressure',
            name='axle4_pressure',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='rawdata',
            name='num1',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='rawdata',
            name='num2',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='rawdata',
            name='num3',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='rawdata',
            name='num4',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='rawdata',
            name='num5',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='rawdata',
            name='num6',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='rawdata',
            name='num7',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='rawdata',
            name='num8',
            field=models.SmallIntegerField(),
        ),
    ]