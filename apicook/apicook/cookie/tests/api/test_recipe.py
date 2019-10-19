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

    def get_request(self):
        url = reverse("recipes-list")
        return Client().get(url)

    def test_get_recipes_OK(self):
        response = self.get_request()
        assert response.status_code == HTTPStatus.OK

    def test_get_recipes_valid_JSON(self):
        response = self.get_request()
        assert len(response.json()) == 1
        assert response.json() == [
            {
                "id": self.recipe.id,
                "ingredients": [
                    {
                        "id": self.ingredient.id,
                        "article": {
                            "id": self.article.id,
                            "name": "tomate"
                        },
                        "quantity": 1,
                        "weight": None
                    }
                ],
                "title": "tomate mozza",
                "text": None,
                "categories": []
            },
        ]
    
