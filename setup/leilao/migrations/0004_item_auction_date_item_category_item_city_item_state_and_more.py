# Generated by Django 4.2.13 on 2024-06-06 18:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leilao', '0003_item_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='auction_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Real Estate', 'Real Estate'), ('Vehicle', 'Vehicle')], default='vehicle', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='city',
            field=models.CharField(default='tte', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='state',
            field=models.CharField(default='sp', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='street',
            field=models.CharField(default='rua', max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='leilao.item')),
            ],
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='real_estates', to='leilao.item')),
            ],
        ),
    ]
