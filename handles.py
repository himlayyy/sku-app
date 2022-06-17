

# API SECRET
# f6969623459139e6498214b9e79948e6

import requests
from requests.api import get
import shopify

shop_url = "ashdevstore.myshopify.com/"
api_version = "2020-10"
private_app_password = "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"
api_key = "f6969623459139e6498214b9e79948e6"

url = f"https://{shop_url}.myshopify.com/admin/api/{api_version}"
shopify.ShopifyResource.set_site(shop_url)
shopify.ShopifyResource.set_user(api_key)
shopify.ShopifyResource.set_password(private_app_password)

with shopify.Session.temp(shop_url, api_version, private_app_password):
    collection = shopify.CollectionListing()
    collection.id= 272598630606
    # cur = shopify.Shop.current()
    product_ids = collection.product_ids()
    print(product_ids)
    # print(cur)
