from ..services.local import save_products_local
import os


def test_save_products_local():
    filename = "products.test.json"

    save_products_local(filename)
    assert os.path.exists(f"../db/{filename}")


def test_save_waiter_local():
    filename = "waiters.test.json"
    test_save_waiter_local(filename)
    assert os.path.exists(f"../db/{filename}")
