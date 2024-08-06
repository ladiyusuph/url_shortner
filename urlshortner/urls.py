from django.urls import path
from . import views

urlpatterns = [
    path("shorten/", views.UrlView.as_view(), name="shorten-url"),
    path("<slug:slug>/", views.redirect_to_url, name="redirect-to-url"),
]
