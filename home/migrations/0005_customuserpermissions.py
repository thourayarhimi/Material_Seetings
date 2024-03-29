# Generated by Django 4.1.7 on 2023-09-02 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_customuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_create_equipe', models.BooleanField(default=False)),
                ('can_read_equipe', models.BooleanField(default=False)),
                ('can_update_equipe', models.BooleanField(default=False)),
                ('can_delete_equipe', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
