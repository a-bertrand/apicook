from http import HTTPStatus
import pytest
from django.urls import reverse
from model_mommy import mommy
from django.test import Client, TestCase
from apicook.cookie.models import Recipe, Article


class TestListRecipe(TestCase):

    @classmethod
    def setUpTestData(cls):
        super(TestListRecipe, cls).setUpTestData()
        cls.article = mommy.make('Article', name="tomate")
        cls.recipe = mommy.make(Recipe, title='tomate mozza')
        cls.ingredient = mommy.make('Ingredient', quantity=1, article=cls.article, recipes=cls.recipe)
    
    def create_random_recipe(self):
        article = mommy.make('Article')
        recipe = mommy.make(Recipe)
        mommy.make('Ingredient', quantity=1, article=article, recipes=recipe)
        return recipe.id

    def get_request_generate(self, number_recipe = 1):
        url = reverse("generate-shop-recipes")
        return Client().get(url + '?generate=true&number_recipe=' + str(number_recipe))
    
    def get_request_regenerate(self, id, generate = 'false', excluded_ids = ''):
        url = reverse("regenerate-shop-recipes", kwargs={'shop_id':str(id)})
        return Client().get(f"{url}?generate=true&excluded_recipe={excluded_ids}")

    def test_generate_shop_recipes_status_OK(self):
        response = self.get_request_generate()
        assert response.status_code == HTTPStatus.OK

    def test_generate_shop_recipes(self):
        mommy.make(Recipe)
        response = self.get_request_generate()
        assert len(response.json().get('recipes')) == 1

    def test_generate_shop_two_recipes_JSON(self):
        self.create_random_recipe()
        response = self.get_request_generate(2)
        assert len(response.json().get('recipes')) == 2

    def test_regenerate_get_shop_recipes_status_OK(self):
        first_response = self.get_request_generate().json()
        response = self.get_request_regenerate(first_response.get('id'))
        assert response.status_code == HTTPStatus.OK

    def test_regenerate_get_shop_recipes(self):
        first_response = self.get_request_generate().json()
        response = self.get_request_regenerate(first_response.get('id'))
        assert len(response.json().get('recipes')) == 1

    def test_regenerate_shop_recipes_an_exclude_the_only_one_recipe(self):
        first_response = self.get_request_generate().json()
        response = self.get_request_regenerate(
            first_response.get('id'), 
            generate = 'true', 
            excluded_ids = self.recipe.id
        )
        assert len(response.json().get('recipes')) == 0
