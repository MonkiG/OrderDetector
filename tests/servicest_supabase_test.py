from ..services.supabase import save_order


def test_save_order():
    placeholder_obj = {
        "table": "table_placeholder",
        "products": [
            {
                "name": "product_placeholder",
                "amount": 0,
            }
        ],
    }

    saved = save_order(placeholder_obj)
    assert saved == True
