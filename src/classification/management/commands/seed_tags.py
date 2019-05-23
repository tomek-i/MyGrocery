from django.core.management.base import BaseCommand
from classification.models import Tag


class Command(BaseCommand):
    help = "Seeds the database with default and commonly used tags."

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        Tag.objects.bulk_create(
            [
                Tag(name='fruit'),
                Tag(name='veggi'),
                Tag(name='protein'),
                Tag(name='carb'),
                Tag(name='healthy'),
                Tag(name='high'),
            ]
        )
