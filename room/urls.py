from django.urls import path
from . import views

urlpatterns = [
    path("room", views.room, name="room"),#get
    path("turmas", views.turmas, name="turmas"),#get
]
