from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings
from classification.models import Tag
from classification.management.commands import seed_categories, seed_tags
from grocerylist.management.commands import seed_items, seed_products, seed_supermarkets


class Command(BaseCommand):
    help = "Seeds the database with default and commonly used tags."

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        if not User.objects.filter(username='tomek').count():
            User.objects.create_superuser(
                username='tomek',
                email='tomek.iwainski@gmail.com',
                password='tomek')

        print('CATEGORIES')
        seed_categories.Command.handle(args, options)
        print('TAGS')
        seed_tags.Command.handle(args, options)

        print('ITEMS')
        seed_items.Command.handle(args, options)
        print('SUPER MARKETS')
        seed_supermarkets.Command.handle(args, options)
        print('PRODUCTS')
        seed_products.Command.handle(args, options)
