# Generated by Django 3.1.1 on 2020-10-11 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0007_auto_20201011_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='org_detail_page_header',
            field=models.CharField(default='Detail about what we do', max_length=80),
        ),
    ]
