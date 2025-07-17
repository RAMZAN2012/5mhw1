from django.urls import path
from apps.api.views import PostListAPView

urlpatterns = [
    path("api/posts/", PostListAPView.as_view()),
]
