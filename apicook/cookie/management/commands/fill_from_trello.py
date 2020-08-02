import requests
import tempfile
from django.core.management.base import BaseCommand
from apicook.cookie.models import Recipe, Article, Ingredient, Category, MatchKeywords
import urllib
from django.core import files
import re

class Command(BaseCommand):

    keyword_list = {}

    def handle(self, *args, **options):

        print('------ START IMPORT ')
        id_one = '5e47c58622b9bf4074b82faf'
        key = '0cdf547b55d2500b0ff411de2c5278ba'
        token = '4f902678282fe58f81bc7b4a0709f38ca92694ebe887727a6d098fdbdf36c443'


        base_url = 'https://api.trello.com/1/'
        board_id = 'DpFpOnQ6'
        attachment_endpoint_name = 'attachments' # apres cards
        checklist_endpoint_name = 'checklists' # solo ou pas
        cards_endpoint_name = 'cards'

        self.keyword_list = self._get_measure_type_keywords()

        url_cards_on_board = f'{base_url}boards/{board_id}/{cards_endpoint_name}/?key={key}&token={token}'
        #url_one_cards_on_board = f'{base_url}boards/{board_id}/{cards_endpoint_name}/{id_one}/?key={key}&token={token}'

        #print('--- Import payloads')
        payloads = requests.get(
           url_cards_on_board
        )

        trello_recipes = payloads.json()

        # for ONE recipe trello

        Article.objects.all().delete()
        
        for recipe_trello in trello_recipes:
            trello_card_id = recipe_trello.get('id')
            base_card_url = f'{base_url}/{cards_endpoint_name}/{trello_card_id}'
        
            new_recipe = Recipe()
            new_recipe.title = recipe_trello.get('name')
            new_recipe.text = recipe_trello.get('desc')
            
            #print('--')
            print(f'import recette {new_recipe.title}')
            
            attachements_url = (
                f'{base_card_url}/{attachment_endpoint_name}/?key={key}&token={token}'
            )
            attachements = requests.get(attachements_url)

            extensions_img = ('.jpg', '.JPG', '.PNG', '.png', '.jpeg', '.JPEG')
            for attachement in attachements.json():
                if attachement:
                    if attachement.get('name').endswith(extensions_img):
                        image_url = attachement.get('url')
                        image = request = requests.get(image_url, stream=True)
                        if request.status_code == requests.codes.ok:
                            file_name = image_url.split('/')[-1]
                            lf = tempfile.NamedTemporaryFile()
                            for block in request.iter_content(1024 * 8):
                                # If no more file then stop
                                if not block:
                                    break
                                # Write image block to temporary file
                                lf.write(block)

                            # Save the temporary image to the model#
                            # This saves the model so be sure that is it valid
                            new_recipe.image.save(file_name, files.File(lf))
                        
            new_recipe.save()
            try :
                categories = recipe_trello.get('labels')
                #print(categories)
                for trello_category in categories:
                    category_name = trello_category.get('name')
                    category = self._get_or_update_category(category_name)
                    new_recipe.categories.add(category)
                    
                #print('end category')
                id_checklist = recipe_trello.get('idChecklists')[0]
                #print(id_checklist)
                checklist_url = (
                    f'{base_url}/{checklist_endpoint_name}/{id_checklist}/?key={key}&token={token}'
                )
                checklists = requests.get(checklist_url).json()
                for item in checklists.get('checkItems'):
                    #print(item)
                    article_name = self._clean_article_name(item.get('name'), new_recipe)
                    #print('save item')
                print('--- Fin dimport perfect')   
            except Exception as e:
                print('erreur sur : ')
                print(e)
                new_recipe.delete()

    def _get_or_update_category(self, category_name):
        #print('check get or update category')
        finded_category = Category.objects.filter(name=category_name).first()
        if finded_category:
            #print('found')
            return finded_category
        else:
            #print('create')
            new_category = Category(name=category_name)
            new_category.save()
            return new_category


    def _clean_article_name(self, name, recipe):
        #print(name)
        key_words_list = [
            'cuil.', 'c.', 'à', '**', 'cuillere', 
            'cuilleres', 'à café', 'à soupe', 'gouttes', 
            'ou', 'boite'
        ]

        between_paranthese_REGEX = '\(([^\)]+)\)' 
        quantity_REGEX = '\d+'
        quanitty_found = re.findall(quantity_REGEX, name)
        quantity = '0'
        if quanitty_found:
            quantity =  quanitty_found[0]
        #print(quantity)
        name_number_quantity_cleaned =  re.sub(quantity_REGEX, '', name)
        name_number_cleaned =  re.sub(between_paranthese_REGEX, '', name_number_quantity_cleaned)
        
        #print(name_number_cleaned)
        array_name = name_number_cleaned.split()
        #clean in keyword list
        
        resultwords  = [word for word in array_name if word.lower() not in key_words_list]
        #print(resultwords)
        result_name = ' '.join(resultwords)
        #print(result_name)
        measure_type = None
        if int(quantity) > 0:
            # 0 key, 1 word
            results = self._get_measure_type_in_str(name_number_quantity_cleaned)
            if results is not None:
                measure_type = results[0]
                result_name = result_name.replace(results[1],"",1)

        article = self._get_or_update_article_name(result_name)

        try:
            ingredient = Ingredient(article=article, quantity=quantity)
            ingredient.recipes = recipe
            if measure_type is not None:
                ingredient.measure_type = measure_type

            ingredient.save()

        except Exception as e:
            print('ingredient err')
            print(ingredient)
            print(e)
            ingredient.delete()

    def _get_or_update_article_name(self, name):
        #print('article')
        finded_article = Article.objects.filter(name=name).first()
        if finded_article:
            finded_article.how_many_found_in_recipes = finded_article.how_many_found_in_recipes + 1
            finded_article.save()
            return finded_article
        else:
            #print('create article')
            new_article = Article(name=name)
            new_article.save()
            return new_article
    
    def _get_measure_type_keywords(self):
        keywords = MatchKeywords.objects.order_by('order').all()
        keywordsDict = {}
        for keyword in keywords:
            keywordsDict[keyword.measure_type] = keyword.keywords.split(',')
        return keywordsDict

    def _get_measure_type_in_str(self, text):
        for key in self.keyword_list:
            for word in self.keyword_list[key]:
                result = text.find(word)
                # 5 is to prevent to find G after 5 letter
                
                if result != -1 and result < 3: 
                    return [key, word]
        return None

            
            