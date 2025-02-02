from django.urls import path
from .views import detailView

urlpatterns = [
    path("", detailView),
]
