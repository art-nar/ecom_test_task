import re
from datetime import datetime
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


DATE_REGEX_1 = r"^\d{2}\.\d{2}\.\d{4}$"
DATE_REGEX_2 = r"^\d{4}-\d{2}-\d{2}$"
PHONE_REGEX = r"^\+7 \d{3} \d{3} \d{2} \d{2}$"


def determine_field_type(value) -> str:
    """
    Определяет тип поля для заданного значения, проверяя его на соответствие шаблонам даты, телефона или email. Возвращает тип поля: "date", "phone", "email" или "text".
    """
    if re.match(DATE_REGEX_1, value) or re.match(DATE_REGEX_2, value):
        try:
            if re.match(DATE_REGEX_1, value):
                datetime.strptime(value, "%d.%m.%Y")
            else:
                datetime.strptime(value, "%Y-%m-%d")
            return "date"
        except ValueError:
            return "text"
    elif re.match(PHONE_REGEX, value):
        return "phone"
    else:
        validator = EmailValidator()
        try:
            validator(value)
            return "email"
        except ValidationError:
            return "text"
