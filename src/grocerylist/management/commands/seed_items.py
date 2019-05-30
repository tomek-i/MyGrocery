from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from grocerylist.models import Item


class Command(BaseCommand):
    help = 'TODO: new command'

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        print('deleting previous data')

        Item.objects.all().delete()

        print('creating data')

        Item.objects.bulk_create([
            Item(name='Milk'),
            Item(name='Eggs'),
            Item(name='Cat Food'),
            Item(name='Onion'),
            Item(name='Garlic'),
            Item(name='Coriander'),
            Item(name='Chips'),
            Item(name='Water'),

        ])

        print('completed')
        pass
