# Generated by Django 4.0.1 on 2022-01-11 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='student',
            constraint=models.CheckConstraint(check=models.Q(('age__gte', 10), ('age__lte', 20)), name='age10-20'),
        ),
    ]
