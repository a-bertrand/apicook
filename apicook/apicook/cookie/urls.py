from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from .views import ArticleViewSet, IngredientViewSet, RecipeViewSet, GenerateListShopRecipe, ShoppingListRecipe, ShoppingListViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'recipes', RecipeViewSet,  basename='recipes')
router.register(r'ingredients', IngredientViewSet)
router.register(r'shopping-list', ShoppingListViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/', include(router.urls)),
    path('api/shop-recipes/', GenerateListShopRecipe.as_view(), name='generate-shop-recipes'),
    path('api/shop-recipes/<int:shop_id>', GenerateListShopRecipe.as_view(), name='regenerate-shop-recipes'),
    path(
        'api/shop-recipes/<int:shop_id>/shopping-list', 
        ShoppingListRecipe.as_view(), 
        name="shopping-recipe-list"
    ),
]