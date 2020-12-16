# Generated by Django 3.0.7 on 2020-12-08 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userImage', models.ImageField(upload_to='static/')),
                ('bio', models.CharField(max_length=50)),
                ('connections', models.CharField(blank=True, max_length=50)),
                ('followers', models.IntegerField(default=0)),
                ('following', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captions', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='static/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userpage.Post')),
                ('user', models.ManyToManyField(related_name='likinguser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]