# Generated by Django 3.1.1 on 2020-09-20 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bills', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.DecimalField(decimal_places=3, max_digits=16)),
                ('fee', models.DecimalField(decimal_places=3, max_digits=16)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.bill')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
