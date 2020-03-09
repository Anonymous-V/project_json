from django.urls import path
from .views import UserView, AlbumView


urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<uuid:api_key>/", UserView.as_view()),
    path("users/delete/<uuid:api_key>/", UserView.as_view()),
    path("albums/", AlbumView.as_view())
]