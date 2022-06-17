import shopify_collections as shp

url = 'https://061d17e754a926fcec4ffd6c5f9fb808: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@ashdevstore.myshopify.com/admin/api/2021-07/'

smart_collections = shp.get_smart_collections(url)

for collection in smart_collections['smart_collections']:
    collection_title = collection.get('title').lower()
    collection_id = collection.get('id')
    collection_products = shp.get_collection_products(url, collection_id)
    
    for values in collection_products.values():
        for val in values:
            print(f"{val.get('handle')}\n")
            # for v in val:
            #     print(f"{v}\n")