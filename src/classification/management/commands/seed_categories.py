from django.core.management.base import BaseCommand
from classification.models import Category


class Command(BaseCommand):
    help = "Seeds the database with the default food groups."

    # def add_arguments(self, parser):
    #   parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):

        # grains
        # oils / fats
        # sugar
        Category.objects.bulk_create(
            [
                Category(
                    name='Fruits', desc='Various fruits like, pineapple, banana, melon etc.'),
                Category(
                    name='Vegetables', desc='Various vegetables like, kidney beans, chickpeas, corn, tomato etc.'),
                Category(name='Dairy & Milk',
                         desc='Milk, yoghurt, cheese and/or alternatives, mostly reduced fat'),
                Category(name='Protein & Meat',
                         desc='Lean meats and poultry, fish, eggs,tofu, nuts and seeds and legumes/beans'),
                Category(name='Grains',
                         desc='Grain (cereal) foods, mostly wholegrain and/or high cereal fibre varieties'),
            ]
        )
