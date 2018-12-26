from django.conf.urls import url, include
from rest_framework import routers
from  views import ArticleViewSet, IngredientViewSet, RecipeViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'ingredientss', IngredientViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/', include(router.urls))
]