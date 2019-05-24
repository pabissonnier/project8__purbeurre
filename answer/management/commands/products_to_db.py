# -*- coding: utf-8 -*-

from answer.models import Product
from .datas_manager import DatasManager
from .product_test_list import list
from django.db import IntegrityError

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        datas_from_api = DatasManager()

        categories_list = DatasManager.categories_extract(datas_from_api)
        categories_url_name = DatasManager.category_to_url(datas_from_api, categories_list)
        products_extract = DatasManager.products_extract(datas_from_api, categories_url_name)
        try:
            DatasManager.get_products_datas(datas_from_api, products_extract)
        except IntegrityError:
            pass
        finally:
            DatasManager.get_products_datas(datas_from_api, products_extract)
