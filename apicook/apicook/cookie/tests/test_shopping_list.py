from http import HTTPStatus
import pytest
from django.urls import reverse
from model_mommy import mommy
from django.test import Client, TestCase
from apicook.cookie.models import Recipe, Article

class TestShoppingList(TestCase):

    @classmethod
    def setUpTestData(cls):
        super(TestShoppingList, cls).setUpTestData()
        cls.article = mommy.make('Article', name="tomate")
        cls.article_mozza = mommy.make('Article', name="mozza")
        cls.recipe = mommy.make(Recipe, title='tomate mozza')
        cls.ingredient = mommy.make('Ingredient', quantity=1, article=cls.article, recipes=cls.recipe)
        cls.ingredient = mommy.make('Ingredient', quantity=1, article=cls.article_mozza, recipes=cls.recipe)

    def create_random_recipe(self):
        article = mommy.make('Article')
        recipe = mommy.make(Recipe)
        mommy.make('Ingredient', quantity=1, article=article, recipes=recipe)
        return recipe.id


    def get_request(self, shop_id):
        url = reverse("shopping-list", kwargs={'shop_id':shop_id})
        return Client().get(url)
    
    def get_request_generate(self, number_recipe = 1):
        url = reverse("generate-shop-recipes")
        return Client().get(url + '?generate=true&number_recipe=' + str(number_recipe))
    
    def test_get_list_of_ingredients_in_shop_list(self):
        recipe = mommy.make(Recipe, title='duo de tomate')
        ingredient = mommy.make('Ingredient', quantity=2, article=self.article, recipes=recipe)

        # add recipe to check this recipe is not in list

        generate_list = self.get_request_generate(2).json()

        self.create_random_recipe()

        shop_id = generate_list.get('id')
        generate_list = self.get_request(shop_id).json()

        response = self.get_request(shop_id)
        assert response.json() == [
            {
                'quantity': 3,
                'name': 'tomate',
                'weight': None,
            },
            {
                'quantity': 1,
                'name': 'mozza',
                'weight': None,
            } 
        ]

    def test_get_list_of_ingredients_in_shop_list_with_weight(self):
        recipe = mommy.make(Recipe, title='duo de tomate')
        ingredient = mommy.make('Ingredient', weight=2, article=self.article, recipes=recipe)

        # add recipe to check this recipe is not in list

        generate_list = self.get_request_generate(2).json()

        self.create_random_recipe()

        shop_id = generate_list.get('id')
        generate_list = self.get_request(shop_id).json()

        response = self.get_request(shop_id)
        assert response.json() == [
            {
                'quantity': 1,
                'name': 'tomate',
                'weight': 2,
            },
            {
                'quantity': 1,
                'name': 'mozza',
                'weight': None,
            } 
        ]
