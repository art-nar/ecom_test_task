from itertools import combinations
from tinydb import TinyDB


def run():
    db = TinyDB("db.json")

    fields = {
        "user_name": "text",
        "lead_email": "email",
        "order_date": "date",
        "phone_number": "phone",
    }

    db.truncate()

    for field1, field2 in combinations(fields.items(), 2):
        field_key1, field_type1 = field1
        field_key2, field_type2 = field2

        record = {
            "name": f"form_{field_type1}_{field_type2}",
            field_key1: field_type1,
            field_key2: field_type2,
        }

        db.insert(record)

    print("База данных успешно заполнена.")
