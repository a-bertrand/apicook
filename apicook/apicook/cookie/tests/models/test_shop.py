from http import HTTPStatus
import pytest
from django.urls import reverse
from model_mommy import mommy
from django.test import Client, TestCase
from apicook.cookie.models import Recipe, Article, ShopList


class TestListRecipe(TestCase):

    @classmethod
    def setUpTestData(cls):
        super(TestListRecipe, cls).setUpTestData()
        cls.article = mommy.make('Article', name="tomate")
        cls.recipe = mommy.make(Recipe, title='tomate mozza')
        cls.ingredient_1 = mommy.make('Ingredient', quantity=1, article=cls.article, recipes=cls.recipe)
        cls.ingredient_2 = mommy.make('Ingredient', quantity=2, article=cls.article, recipes=cls.recipe)
        cls.ingredient_3 = mommy.make('Ingredient', weight=2, article=cls.article, recipes=cls.recipe)
        cls.shop = mommy.make('Shop', recipes=[cls.recipe])
        cls.shop.generate_shopping_list()

    def test_check_list(self):
        shop_list = self.shop.list_content.all()

        assert len(shop_list) == 2
        assert shop_list[0].total_quantity == 3 
        assert shop_list[0].article.name == 'tomate'

        assert shop_list[1].total_weight == 2
        assert shop_list[1].article.name == 'tomate'

    def test_update_check_list_bought_status(self):
        shop_list = self.shop.list_content.all()

        ingredient_1 = shop_list[0]
        ingredient_2 = shop_list[1]

        assert ingredient_1.bought_status == ShopList.NOTTOUCH

        ingredient_1.bought_value = 2
        ingredient_1.save()

        assert ingredient_1.bought_status == ShopList.PARTIAL

        ingredient_1.bought_value = 3
        ingredient_1.save()

        assert ingredient_1.bought_status == ShopList.COMPLETE

        ingredient_1.bought_value = 2
        ingredient_1.save()

        assert ingredient_1.bought_status == ShopList.PARTIAL

        ingredient_1.bought_value = 0
        ingredient_1.save()

        assert ingredient_1.bought_status == ShopList.NOTTOUCH