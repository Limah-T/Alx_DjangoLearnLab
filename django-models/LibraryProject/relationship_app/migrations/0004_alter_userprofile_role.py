# Generated by Django 5.1.6 on 2025-02-23 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0003_user_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('LIBRARIAN', 'Libarian'), ('MEMBER', 'Member')], default='Member', max_length=100),
        ),
    ]
