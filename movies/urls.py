from django.urls import path
from . import views

urlpatterns = [
    path('', views.WikipediaView.as_view()),
]
