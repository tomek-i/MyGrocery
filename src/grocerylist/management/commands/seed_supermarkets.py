from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from grocerylist.models import Supermarket


class Command(BaseCommand):
    help = 'TODO: new command'

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        print('   deleting previous data')

        Supermarket.objects.all().delete()

        print('   creating data')

        Supermarket.objects.bulk_create([
            Supermarket(
                name='Woolworth - Main',
                address='Bonegilla Rd, Griffith NSW 2680'),
            Supermarket(
                name='Woolworth - Small',
                address='Burrell Pl, Griffith NSW 2680'),
            Supermarket(
                name='Aldi',
                address='4/6 Oakes Rd, Griffith NSW 2680'),
            Supermarket(
                name='Coles',
                address='Yambil St & Crossing St Griffin Plaza, Griffith NSW 2680'),
        ])

        print('   completed\n')
        pass
