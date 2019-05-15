import urllib.request
import json


class DatasManager:
    """ Class for the management of the datas """
    def __init__(self):
        pass

    def categories_extract(self):
        """ Extracting JSON categories values and converting into list """

        categories_json = urllib.request.urlopen('https://fr.openfoodfacts.org/categories.json')
        categories_read = categories_json.read()
        categories_data = json.loads(categories_read.decode("utf-8"))

        categories_list = []
        for value in categories_data["tags"]:
            if value["products"] >= 4017:
                categories_values = value["name"]
                categories_list.append(categories_values)
        return categories_list

    def convert_list_tuples(self, list_name):
        """ Convert list into list of tuples"""
        tuples_list = []
        for x in list_name:
            tuples_list.append((x,))
        return tuples_list

    def category_to_url(self, categories_name_list):
        """ Converting category name to url """
        category_name_url_list = []
        for category_name in categories_name_list:
            category_url_dict = {}
            category_name_url = category_name.lower()
            category_name_url = category_name_url.replace(' ', '-')
            category_name_url = category_name_url.replace('é', 'e')
            category_name_url = category_name_url.replace('è', 'e')
            category_name_url = category_name_url.replace('à', 'a')
            category_name_url = category_name_url.replace('ç', 'c')
            category_name_url = category_name_url.replace('ù', 'u')
            category_name_url = category_name_url.replace("'", '-')
            category_name_url = category_name_url.replace("â", 'a')
            category_url_dict[category_name] = category_name_url
            category_name_url_list.append(category_url_dict)
        return category_name_url_list

    def products_extract(self, category_name_url_list):
        """Extracting JSON products values and converting into list"""
        products_lists = []
        for element in category_name_url_list:
            for key_list, value_list in element.items():
                page = 1
                while page <= 5:
                    category_url = "https://fr.openfoodfacts.org/categorie/{0}/{1}.json".format(value_list, page)
                    products_json = urllib.request.urlopen(category_url)
                    products_read = products_json.read()
                    products_data = json.loads(products_read.decode("utf-8"))
                    products_in_category_list = DatasManager.products_shaping(self, products_data, key_list)
                    products_lists.append(products_in_category_list)
                    page += 1
        return products_lists

    def products_shaping(self, products_data, key_list):
        """ Creation of dictionnaries in list to exploit products datas """
        products_in_category_list = []
        for content in products_data["products"]:
            products_dict = {}
            for key, value in content.items():
                products_dict["nom_category"] = key_list
                if key == "product_name":
                    products_dict["name"] = value
                elif key == "url":
                    products_dict["link"] = value
                elif key == "stores_tags":
                    value_str = ', '.join(value)
                    products_dict["shops"] = value_str
                elif key == "ingredients_text_fr":
                    products_dict["ingredients"] = value
                elif key == "nutrition_grades":
                    products_dict["nutriscore"] = value
                elif key == "image_url":
                    products_dict["picture"] = value
            if len(products_dict) == 7:
                products_in_category_list.append(products_dict)
        return products_in_category_list

