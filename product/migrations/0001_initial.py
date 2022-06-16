# Generated by Django 3.2.13 on 2022-06-14 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=30)),
                ('nameProduct', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='type.type')),
            ],
        ),
    ]
