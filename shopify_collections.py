import requests
import pprint
import json
import sqlite3
from typing import TypedDict
from collections import ChainMap

from requests.api import get

# url = 'https://061d17e754a926fcec4ffd6c5f9fb808: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@ashdevstore.myshopify.com/admin/api/2021-07/'

###Get products
#Get collection
def get_collection(url, id, fields = ''):
    if fields:
        query = 'collections' + "/" + str(id) + '.json?=' + fields
    else:
        query = 'collections' + "/" + str(id) + '.json'
    r = requests.get(url + query).json()
    
    return r

#Get all smart collections
def get_smart_collections(url, fields=''):
    endpoint = 'smart_collections.json'
    r = requests.get(url + endpoint + fields).json()
    return r

#Get all products in a collection
def get_collection_products(url, collection_id,fields=''):
    endpoint = 'products.json'
    r = requests.get(url+ "collections/" + str(collection_id) + "/" + endpoint + fields).json()
    return r

#Get all variants of a product
def get_variants(url, product_id, fields =''):
    endpoint = 'variants.json'
    r = requests.get(url + "/products/" + str(product_id) + "/" + endpoint + fields).json()
    return r

#Get all products
def get_all_products(url, fields = ''):
    print("Getting all products...")
    endpoint = 'products.json'
    r = requests.get(url + endpoint + fields).json()
    print("Done")
    return r
#Save response.json() to file
def save_request(data, filename = ''):
    if not filename:
        filename = str(input("Enter json filename: "))
    with open(filename,'w') as f:
        json.dump(data, f, indent=2)
        print(f'{filename} saved')

def generate_sku(products):
    for product in get_all_products[products]:
        print(product.get('title'))
        sku_vendor = brands.get(product.get('vendor').lower())
        
        variants_list = product.get('variants')
        for variant in variants_list:
            print(variant.get('title'))
            pos =  variants_list.index(variant)
            if pos < 10:
                sku_pos = str(pos).zfill(2)
            else:
                sku_pos = str(pos)
            opt2 = variant.get('option2')
            opt1 = variant.get('option1')
            # print(sku_vendor)
            print(f"{sku_vendor} {sku_pos} {opt2} {opt1}")
            
            sku = str(sku_vendor + sku_pos + opt2 + opt1)
            print(sku)

def flatten_json(y):
    out = {}
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
    flatten(y)
    return out

def get_variants(variants):    
    # print(type(variants))
    
    for variant in variants:
        sku_comps = [] 
        pos = variants.index(variant) + 1
        if pos < 10:
            sku_pos = str(pos).zfill(2)
        else:
            sku_pos = str(pos)
        sku_comps.append('sku_pos')
        for variant in variants:
            sku_comps.append(variant.get('option2'))
            sku_comps.append(variant.get('option1'))
        return sku_comps
    






# smart_collections = get_smart_collections()
# print(type(smart_collections))
# pprint.pprint(smart_collections)
# save_request(all_collections)

# multi_rules = get_collection(273262706894)
# save_request(multi_rules)

# skate = get_collection(273262706894)
# pprint.pprint(skate)
###Save

# for collection in smart_collections['smart_collections']:
#     collection_title = collection.get('title').lower()
#     collection_id = collection.get('id')
#     collection_products = get_collection_products(collection_id)
    
#     for values in collection_products.values():
#         for val in values:
#             print(val.get('handle'))
            # for v in val:
            #     print(f"{v}\n")
    
    # save_request(collection_products,collection_title)

# Gets collection id and title, unpacks rules list into dict
# with open("db/all-collections") as f:
#     data = json.load(f)

brands = dict({"adidas": "AD",    "nike": "NK",    "flex fit": "FF",    "vans": "VN",    "converse": "C",    "dr martens": "DM", "herschel": "H",   "timberland": "TM",    "vans": "VN",    "supra": "SU",    "puma": "PM",    "asics tiger": "As-Ti","palladium": "PAL"})
# rules_max = 1
# for collections in smart_collections["smart_collections"]:
#     #extract column, relation, condition dldddf
#     collection_name = collections.get('title')
#     rule_id = collections.get("id")
#     # print(collections.get('rules'))
#     # print(rule_id, collection_name)
#     print(f"{collection_name}")
#     rule_list = len(collections.get('rules'))
#     print(len(collections.get('rules')))
#     if rule_list > rules_max:
#         rules_max = rule_list
# print(rules_max)

# with open("db//allproducts.json") as f:
#     allproducts = json.load(f)


    # collection_rules = dict(ChainMap(*rule_string[::-1]))
    # collection_rules["collection_id"] = rule_id
    # print(collection_rules)
# Mao ni final

# with open("db/all-collections") as f:
#     data = json.load(f)

# flat_collections = []
# for collections in data["smart_collections"]:
#     flat_collections.append(flatten_json(collections))
#     # print(type((flatten_json(collections))))
# save_request(flat_collections)

#insert to db
# https://stackoverflow.com/questions/55699090/how-to-create-a-sqlite3-table-from-a-dictionary/55699244
#########END SAVE




# with open("db/all-collections") as f:
#     data = json.load(f)
#     print("type(data)")
# for collections in data["smart_collections"]:

# extract column, relation, condition dldddf
#     collection_name = collections.get('title')
#     rule_id = collections.get("id")
#     print(type(rule_id))
#     rule_string = collections.get("rules")
#     print(type(rule_string))
    
#     collection_rules = flatten_json()
#     collection_rules["collection_id"] = rule_id
#     print(collection_rules))


# print(type(brands.get('nike')))
