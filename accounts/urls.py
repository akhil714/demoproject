from django.urls import path,include
from .views import Inputcsv

urlpatterns = [
    path('csv/', Inputcsv.as_view()),
]