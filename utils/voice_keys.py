from utils.get_json import get_json


products = get_json("products.json")

tables = [
    "m uno",
    "m dos",
    "m tres",
    "m cuatro",
    "m cinco",
    "m seis",
    "m siete",
    "m ocho",
    "m nueve",
    "m diez",
    "m once",
    "m doce",
]

waiters = [
    "david",
    "ramon",
    "daniel",
]

products_names = [product["name"].lower() for product in products]

voice_keys = ["m"]
# , *products_names, *[f"set {waiter}" for waiter in waiters]

print(voice_keys)
