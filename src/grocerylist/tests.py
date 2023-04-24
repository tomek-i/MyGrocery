from django.test import TestCase

# Create your tests here.


class ShoppinglistTestCase(TestCase):

    def setUp(self):
        # TODO: need to create a few items, maybe can use the seed method for it?
        # TODO: need to create a shoppinglist and assign a few items to it
        pass

    def test_shoppinglist_missing_items(self):
        """ the shopping list can return an items which are not marked as completed """
        pass

    def test_shoppinglist_can_count_completed_items(self):
        """ the shopping list can return an items which are marked as completed """
        pass

    def test_shoppinglist_items(self):
        """ the shopping list can return all items """
        pass

    def test_shoppinglist_is_complete(self):
        """ the shopping list can determine if it has been completed when all items are completed """
        pass
