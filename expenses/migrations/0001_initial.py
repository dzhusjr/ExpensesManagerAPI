# Generated by Django 4.2.16 on 2024-10-29 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.User')),
                ('title', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('category', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]