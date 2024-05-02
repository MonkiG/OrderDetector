from utils.supabase import client
from utils.console import log, error, success


def save_order(data):
    log("Uploading to database")
    table = data["table"]
    products = data["products"]

    try:
        client.table("orders").insert({"table": table, "products": products}).execute()
        success("Data uploaded to database successfully")
    except Exception as e:
        error(e)
