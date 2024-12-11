from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('', lambda request: redirect('/get_form/', permanent=True)),
    path("get_form/", views.get_form_template_name_or_post_data, name="get_form"),
]
