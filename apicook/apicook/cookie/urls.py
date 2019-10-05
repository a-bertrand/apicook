from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from .views import ArticleViewSet, IngredientViewSet, RecipeViewSet, ListShopRecipe

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'recipes', RecipeViewSet,  basename='recipes')
router.register(r'ingredients', IngredientViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/', include(router.urls)),
    path('api/shop-recipes/', ListShopRecipe.as_view()),
    path('api/shop-recipes/<int:id_shop>', ListShopRecipe.as_view())
]