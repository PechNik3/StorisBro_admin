# Generated by Django 4.2.9 on 2024-02-10 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commission_rate', models.DecimalField(decimal_places=2, default=0.05, max_digits=5)),
                ('referral_earnings', models.DecimalField(decimal_places=2, default=1.0, max_digits=10)),
                ('advertising_cost', models.DecimalField(decimal_places=2, default=10.0, max_digits=6)),
            ],
        ),
    ]
