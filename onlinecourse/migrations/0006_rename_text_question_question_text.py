# Generated by Django 4.0.5 on 2022-06-28 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0005_remove_question_course_question_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='text',
            new_name='question_text',
        ),
    ]
