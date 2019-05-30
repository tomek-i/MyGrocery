from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from classification.models import Tag
from classification.management.commands import seed_categories, seed_tags
from grocerylist.management.commands import seed_items, seed_products, seed_supermarkets


class Command(BaseCommand):
    help = "Seeds the database with default and commonly used tags."

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        User.objects.create_superuser(
            username='tomek',
            email='tomek.iwainski@gmail.com',
            password='tomek')

        seed_categories.Command.handle(args, options)
        seed_tags.Command.handle(args, options)

        seed_items.Command.handle(args, options)
        seed_products.Command.handle(args, options)
        seed_supermarkets.Command.handle(args, options)
