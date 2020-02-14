import requests
from django.core.management.base import BaseCommand
from .models import Recipe


class Command(BaseCommand):

    def handle(self, *args, **options):

    
        base_url = 'https://api.trello.com/1/'
        board_id = 'zZ5uRDAD'
        attachment_endpoint_name = 'attachments' # apres cards
        checklist_endpoint_name = 'checklists' # solo ou pas
        cards_endpoint_name = 'cards'

        payload = requests.get(
           f'{base_url}/1/boards/{board_id}/{cards_endpoint_name}/?key={key}&token={token}
        )

        for recipe_trello in payload:
            new_recipe = Recipe
            recipe_name = recipe_trello.name
            recipe_text = recipe_trello.desc
            
            trello_id = recipe_trello.id
            attachements_url = (
                f'{base_url}/boards/{board_id}/{cards_endpoint_name}/{trello_id}/{attachment_endpoint_name}/?key={key}&token={token}'
            )
            attachements = requests.get(attachements_url)

            for attachement in attachements:
                pass

            categories = recipe_trello.labels
            for trello_category in categories:
                category_name = trello_category.name
                category = self._get_or_update_category(category_name)
                recipe.categories.add(trello_category)
    
    def _get_or_update_category(self, category_name):
        finded_category = Category.objects.filter(name=category_name).first()
        if finded_category:
            return finded_category
        else:
            new_category = Category(name=category_name)
            new_category.save()
            return new_category
