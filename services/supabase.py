from utils.supabase import client
from utils.console import log, error, success
from utils.json_helpers import get_json
from utils.similarity import similarity


def save_order(data, waiter):
    log("Uploading to database")
    table = data["table"]
    products = data["products"]

    waiters = get_json("waiters.json")

    for db_waiter in waiters:
        ratio = similarity(waiter, db_waiter["name"])
        if ratio > 0.5:
            waiter_id = db_waiter["id"]
            break

    try:
        client.table("orders").insert(
            {"table": table, "products": products, "waiter": waiter_id}
        ).execute()
        success("Data uploaded to database successfully")
        return True
    except Exception as e:
        error(e)
        return False
