# Generated by Django 3.1.5 on 2021-01-31 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='product',
            name='url_source',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='product',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.groupproduct'),
        ),
    ]
