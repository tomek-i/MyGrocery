from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from grocerylist.models import Item
from classification.models import Category


class Command(BaseCommand):
    help = 'TODO: new command'

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        print('   deleting previous data')

        Item.objects.all().delete()

        print('   creating data')

        Item.objects.bulk_create([
            Item(name='Milk', category=Category.objects.get(slug='dairy-and-milk')),
            Item(name='Ice Cream', category=Category.objects.get(
                slug='dairy-and-milk')),
            Item(name='Eggs', category=Category.objects.get(
                slug='protein-and-meat')),
            Item(name='Water', category=Category.objects.get(
                slug='other')),
            Item(name='Chicken Breast', category=Category.objects.get(
                 slug='chicken')),

        ])

        print('   completed\n')
        pass
