# Generated by Django 2.1 on 2019-08-09 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20190804_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscription',
            old_name='sndGrade',
            new_name='finalExam',
        ),
        migrations.RenameField(
            model_name='inscription',
            old_name='trdGrade',
            new_name='finalGrade',
        ),
        migrations.RenameField(
            model_name='inscription',
            old_name='fstGrade',
            new_name='midTerm',
        ),
        migrations.RemoveField(
            model_name='inscription',
            name='fthGrade',
        ),
    ]
