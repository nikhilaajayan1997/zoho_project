# Generated by Django 4.1.7 on 2023-05-10 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0020_mail_table1_doc_upload_table1_comments_table1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doc_upload_table',
            name='user',
        ),
        migrations.RemoveField(
            model_name='doc_upload_table',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='mail_table',
            name='user',
        ),
        migrations.RemoveField(
            model_name='mail_table',
            name='vendor',
        ),
        migrations.DeleteModel(
            name='comments_table',
        ),
        migrations.DeleteModel(
            name='doc_upload_table',
        ),
        migrations.DeleteModel(
            name='mail_table',
        ),
    ]
