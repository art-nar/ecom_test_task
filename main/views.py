# from django.shortcuts import render
from tinydb import TinyDB
from rest_framework.decorators import api_view
from rest_framework.response import Response
from form_check import settings

from .utils import determine_field_type

db = TinyDB(settings.TINYDB_PATH)


@api_view(["GET", "POST"])
def get_form_template_name_or_post_data(request):
    form_templates = db.all()  # Получаем все шаблоны
    if request.method == "POST":
        data = request.data  # Данные из POST-запроса
        if len(data) != 2:
            return Response("Неправильный запрос. Ожидается 2 параметра.")
        for template in form_templates:  # Сверяем данные парами "ключ":"тип данных" с каждым шаблоном по паре "ключ":"значение"
            if all(
                determine_field_type(value) == template.get(key)
                for key, value in data.items()
            ):
                return Response(template["name"])  # Имя шаблона при совпадении

        return Response(
            {key: determine_field_type(value) for key, value in data.items()}
        )
    return Response(form_templates)
