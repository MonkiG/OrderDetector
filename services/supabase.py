from utils.supabase import client
from utils.console import log, error, success


def save_order(data, waiter):
    log("Uploading to database")
    table = data["table"]
    products = data["products"]

    try:
        client.table("orders").insert(
            {"table": table, "products": products, "waiter": waiter}
        ).execute()
        success("Data uploaded to database successfully")
        return True
    except Exception as e:
        error(e)
        return False
