from django.urls import path
from . import views

app_name = "MarianaEHugo"

urlpatterns = [
    path('', views.home_page_view, name='home'),
]
