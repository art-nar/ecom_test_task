import random
import requests


def run():

    fields = ["user_name", "lead_email", "order_date", "phone_number"]

    emails = [
        # Правильные имейлы
        "john.doe@example.com",
        "jane-doe_123@sub.example.org",
        "user.name+alias@company.co.uk",
        "test_email123@domain.com",
        "info@web-site.io",
        "support@sub.domain.edu",
        "hello_world@domain-name.net",
        "admin@local-server.local",
        "feedback@shop.online",
        "mailer.daemon@server.com",
        # Неправильные имейлы
        "plainaddress",
        "@missingusername.com",
        "user@@example.com",
        "username@.com",
        "username@domain,com",
        "username@domain..com",
        ".username@example.com",
        "username@domain@another.com",
        "user space@domain.com",
        "username@domain!com",
    ]

    dates = [
        # Правильные даты
        "2023-12-10",
        "1999-01-01",
        "2024-02-29",
        "2022-06-15",
        "2000-12-31",
        "31.12.2023",
        "01.01.2000",
        "29.02.2024",
        "15.06.2022",
        "10.10.2010",
        # Неправильные даты
        "2023/12/10",  # Неверный разделитель
        "10-12-2023",  # Неправильный порядок
        "31.02.2023",  # Некорректная дата
        "2023.12.10",  # Неправильный формат
        "99.99.9999",  # Некорректная дата
        "2023-13-01",  # Месяц больше 12
        "2023-00-10",  # Нулевой месяц
        "2023-12-32",  # День больше 31
        "31-12-23",  # Неполный год
        "2023-2-9",  # Неполный формат
    ]

    phones = [
        "+7 999 123 45 67",
        "+7 888 234 56 78",
        "+7 777 345 67 89",
        "+7 666 456 78 90",
        "+7 555 567 89 01",
        "+7 444 678 90 12",
        "+7 333 789 01 23",
        "+7 222 890 12 34",
        "+7 111 901 23 45",
        "+7 000 012 34 56",
        # Неправильные номера
        "+7 999 123-45-67",
        "+7 888 234 56 78-90",
        "+7 777 345 67 89-01",
        "+7 666 456-78-90",
        "+7 555 567 89 01-23",
        "+7444 678 90 12 34",
        "+9 333 789 01 23 45",
        "+77 222 890 12 34 56",
    ]

    usernames = [
        "john_doe",
        "janeDoe123",
        "cool_user",
        "user.name",
        "pro_gamer99",
        "hello_world",
        "alpha_beta",
        "sunshine_2024",
        "nightowl",
        "tech_guru",
        "space_explorer",
        "happy_coder",
        "the_real_deal",
        "fast_runner",
        "lazy_cat",
        "bookworm",
        "star_gazer",
        "mountain_hiker",
        "coffee_lover",
        "pythonista",
    ]

    print("Выберите поля из корректных указанных или введите своё:", fields)
    selected_keys = []
    while len(selected_keys) < 2:
        key = input(f"Выберите поле {len(selected_keys) + 1}: ").strip()
        selected_keys.append(key)

    endpoint = "http://127.0.0.1:8000/get_form/"

    for _ in range(int(input("Введите количество запросов: "))):
        data = {}
        for key in selected_keys:
            if key == "lead_email":
                data[key] = random.choice(emails)
            elif key == "order_date":
                data[key] = random.choice(dates)
            elif key == "phone_number":
                data[key] = random.choice(phones)
            elif key == "user_name":
                data[key] = random.choice(usernames)
            else:
                data[key] = random.choice(phones)
        try:
            get_response = requests.post(endpoint, data=data, timeout=5)
            print(data, "\n", get_response.text, "\n\n")
        except requests.exceptions.Timeout:
            print("Время ответа истекло. Сервер не отвечает.")
        except requests.exceptions.RequestException as e:
            print(f"Возникла ошибка: {e}")
