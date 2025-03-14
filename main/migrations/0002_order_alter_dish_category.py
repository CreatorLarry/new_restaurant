# Generated by Django 5.1.6 on 2025-03-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('food_item', models.TextField()),
                ('quantity', models.PositiveIntegerField()),
                ('delivery_address', models.TextField()),
                ('message', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.CharField(choices=[('fast-food', 'Fast food'), ('appetizers', 'Appetizers'), ('main-course', 'Main Course'), ('desserts', 'Desserts'), ('drinks', 'Drinks')], max_length=50),
        ),
    ]
