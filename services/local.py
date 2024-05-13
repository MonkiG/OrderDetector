from utils.supabase import client
from utils.json_helpers import save_json_local
from utils.console import log, success


def save_products_local(filename="products.json"):
    log("Retrieving products to local")
    response = client.table("products").select("id, name").execute()
    data, count = response
    success("Products retrieved successfully!")
    products = data[1]

    if len(products) > 0:
        log("Saving products into local database!")
        save_json_local(products, filename)
        success("Products saved successfully!")


def save_waiters_local(filename="waiters.json"):
    response = client.table("products").select("id, name").execute()
    data, count = response

    products = data[1]
    if len(products) > 0:
        save_json_local(products, filename)
