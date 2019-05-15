from .datas_manager import DatasManager
from answer.models import Categories

from django.core.management.base import BaseCommand, CommandError
import urllib
import json


class Command(BaseCommand):
    # Creation of the instances
    categories_list = DatasManager()

    def handle(self, *args, **options):
        categories_json = urllib.request.urlopen('https://fr.openfoodfacts.org/categories.json')
        categories_read = categories_json.read()
        categories_data = json.loads(categories_read.decode("utf-8"))

        categories_list = []
        for value in categories_data["tags"]:
            if value["products"] >= 4017:
                categories_values = value["name"]
                categories_list.append(categories_values)
                for element in categories_list:
                    category_name = Categories(name=element)
                    category_name.save()
