from django.urls import path
from .views import home


app_name = "randnum"
urlpatterns = [
    path('',home,name="home"),
]
