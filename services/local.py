from ..utils.supabase import client
from ..utils.json_helpers import save_json_local


def save_products_local():
    response = client.table("products").select("id, name").execute()
    data, count = response

    products = data[1]
    if len(products) > 0:
        save_json_local(products, "products.json")


def save_waiters_local():
    response = client.table("products").select("id, name").execute()
    data, count = response

    products = data[1]
    if len(products) > 0:
        save_json_local(products, "waiters.json")
