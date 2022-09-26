from django.urls import path
from .views import (
    BlogCreateView,
    BlogDetailView,
    BlogUpdateView,
    BlogView,
    BlogDeleteView,
)

urlpatterns = [
    path("", BlogView.as_view(), name="blog"),
    path("<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("newpost/", BlogCreateView.as_view(), name="newpost"),
    path("<int:pk>/updatepost/", BlogUpdateView.as_view(), name="updatepost"),
    path("<int:pk>/deletepost/", BlogDeleteView.as_view(), name="deletepost"),
]
