import requests
from django.core.management.base import BaseCommand
from apicook.cookie.models import Recipe


class Command(BaseCommand):

    def handle(self, *args, **options):

        print('------ START IMPORT ')
        id_one = '5de2b428e004e71260b1d499'

        base_url = 'https://api.trello.com/1/'
        board_id = 'zZ5uRDAD'
        attachment_endpoint_name = 'attachments' # apres cards
        checklist_endpoint_name = 'checklists' # solo ou pas
        cards_endpoint_name = 'cards'

        #url_cards_on_board = f'{base_url}boards/{board_id}/{cards_endpoint_name}/?key={key}&token={token}'
        url_one_cards_on_board = f'{base_url}boards/{board_id}/{cards_endpoint_name}/{id_one}/?key={key}&token={token}'

        payloads = requests.get(
           url_one_cards_on_board
        )

        recipe_trello = payloads.json()
        new_recipe = Recipe()
        new_recipe.title = recipe_trello.get('name')
        new_recipe.text = recipe_trello.get('desc')
        
        trello_id = recipe_trello.get('id')
        attachements_url = (
            f'{base_url}/boards/{board_id}/{cards_endpoint_name}/{trello_id}/{attachment_endpoint_name}/?key={key}&token={token}'
        )
        attachements = requests.get(attachements_url)

        for attachement in attachements:
            pass

        categories = recipe_trello.get('labels')
        for trello_category in categories:
            category_name = trello_category.name
            category = self._get_or_update_category(category_name)
            new_recipe.categories.add(trello_category)
        new_recipe.save()
    
    def _get_or_update_category(self, category_name):
        finded_category = Category.objects.filter(name=category_name).first()
        if finded_category:
            return finded_category
        else:
            new_category = Category(name=category_name)
            new_category.save()
            return new_category
