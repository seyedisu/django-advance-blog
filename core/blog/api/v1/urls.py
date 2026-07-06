from django.urls import path
from . import views

urlpatterns = [
    # path("post/", views.PostList.as_view(), name="post-list"),
    # path("post/<int:pk>", views.PostDetail.as_view(), name="post-detail"),
    path("post/", views.PostViewSet.as_view({"get":"list"}), name="post-list")
]