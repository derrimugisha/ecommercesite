# Generated by Django 2.2.14 on 2020-08-30 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=500)),
                ('colors', models.CharField(max_length=500)),
                ('product_description', models.TextField()),
                ('price', models.CharField(max_length=255)),
                ('quantit', models.CharField(max_length=255)),
                ('discount', models.CharField(default=0, max_length=255)),
                ('ranking', models.CharField(max_length=255)),
                ('picture', models.ImageField(upload_to='images')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
                ('type_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Type_category')),
            ],
        ),
    ]
