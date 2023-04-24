# Generated by Django 2.2.1 on 2019-06-03 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grocerylist', '0006_add_shop_items_mm_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='item_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='grocerylist.Item', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='supermarket_product',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocerylist.Product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='supermarket_product',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocerylist.Supermarket', verbose_name='supermarket'),
        ),
    ]