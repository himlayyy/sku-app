import json

with open("allproducts.json") as f:
    data = json.load(f)

print(type(data))

for product in data['products']:
    print(product.get('id'), product.get('title'))
    for variant in product['variants']:
        print(variant.get('id'), variant.get('title'))
