from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path("members/", view=views.members, name="members"),
    path("members/details/<int:id>", view=views.details, name="details")
]
