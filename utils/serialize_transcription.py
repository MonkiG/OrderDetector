from utils.console import log, success, error, warn
import re


def transcription_to_json(transcription: str, type: str):
    log("Serialiazing data to json")
    if type == "order":
        transcription_serialized = get_order(transcription.lower())
        return transcription_serialized
    if type == "waiter":
        waiter = get_waiter(transcription)
        return waiter


def get_waiter(data: str):
    data = data.lower()
    waiter_regex = r"(?<=mesero)\s(.+)"
    log("Retrieving waiter")

    waiter_match = re.search(waiter_regex, data)

    if waiter_match:
        waiter = waiter_match.group(1)
        success("Waiter retrieved successfully")
        return waiter
    else:
        error("Error retrieving waiter")
        print(data)


def get_order(data: str):

    table_regex = r"t(\d)"
    products_regex = r"(?<=productos)\s(.+)"

    log("Retrieving table and products")

    table_match = re.search(table_regex, data)
    products_match = re.search(products_regex, data)

    if table_match and products_match:
        table = table_match.group(1)
        success("Table retrieved")
        products = products_match.group(1)
        success("Products retrieved!")
        products = parse_products(products)
        serialized = {"table": table, "products": products}

        success("Order serialized correctly")
        return serialized
    else:
        error("Error retrieving data")


def parse_products(products):
    count_dictionary = {
        "un": "1",
        "dos": "2",
        "tres": "3",
        "cuatro": "4",
        "cinco": "5",
        "seis": "6",
        "siete": "7",
        "ocho": "8",
        "nueve": "9",
        "diez": "10",
    }

    products_splited = list(
        filter(
            lambda x: x != "" and x != "y" and x != " ",
            re.split(
                r"(un|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez)", products
            ),
        )
    )

    products_list = []

    for i in range(0, len(products_splited), 2):
        amount = products_splited[i].strip()
        product = products_splited[i + 1].strip()
        products_list.append({"name": product, "amount": count_dictionary[amount]})
    return products_list
