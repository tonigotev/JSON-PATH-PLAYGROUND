from django.urls import path
from .views import playground_view

urlpatterns = [
    path("", playground_view, name="playground"),
]
