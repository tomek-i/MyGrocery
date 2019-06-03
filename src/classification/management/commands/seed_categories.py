from django.core.management.base import BaseCommand
from classification.models import Category


class Command(BaseCommand):
    help = "Seeds the database with the default food groups."

    # def add_arguments(self, parser):
    #   parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        print('   deleting previous data')
        Category.objects.all().delete()
        # grains
        # oils / fats
        # sugar
        categories = [

            {
                'name': 'Fruits',
                'desc': 'Various fruits like, pineapple, banana, melon etc.'
            },
            {
                'name': 'Vegetables',
                'desc': 'Various vegetables like, kidney beans, chickpeas, corn, tomato etc.'
            },
            {
                'name': 'Dairy & Milk',
                'desc': 'Milk, yoghurt, cheese and/or alternatives, mostly reduced fat'
            },
            {
                'name': 'Protein & Meat',
                'desc': 'Lean meats and poultry, fish, eggs,tofu, nuts and seeds and legumes/beans.',
            },
            {
                'name': 'Grains',
                'desc': 'Grain (cereal) foods, mostly wholegrain and/or high cereal fibre varieties.'
            },
            {
                'name': 'Other',
                'desc': 'Other which does not fall into any of the other categories.'
            },
        ]

        print('   creating data')
        for category in categories:
            Category.objects.create(**category)
        meat = Category.objects.get(slug='protein-and-meat')
        meat_subcategories = [
            {
                'name': 'Poultry',
                'desc': 'any pooultry.',
                'parent':  meat,
            },
            {
                'name': 'Beef',
                'desc': 'any beef.',
                'parent': meat,
            },
            {
                'name': 'Lamb',
                'desc': 'any lamb.',
                'parent':  meat,
            },
            {
                'name': 'Seafood',
                'desc': 'any Seafood.',
                'parent': meat,
            },
        ]
        for category in meat_subcategories:
            Category.objects.create(**category)

        poultry = Category.objects.get(slug='poultry')
        poultry_subcategories = [
            {
                'name': 'Chicken',
                'desc': 'any schick.',
                'parent':  poultry,
            },
            {
                'name': 'Duck',
                'desc': 'quack.',
                'parent': poultry,
            },
            {
                'name': 'Turkey',
                'desc': 'gulp.',
                'parent':  poultry,
            }
        ]
        for category in poultry_subcategories:
            Category.objects.create(**category)
        print('   completed\n')
