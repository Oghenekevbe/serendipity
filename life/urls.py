from django.urls import path
from . import views
from .views import BlogListView,ForumListView,BlogDetailView,ForumDetailView

urlpatterns = [
    path("", views.index, name="index"),
    path("blog_list/", BlogListView.as_view(), name="blog_list"),
    path("blog_detail/<int:pk>", BlogDetailView.as_view(), name="blog_detail"),
    path("forum_list/", ForumListView.as_view(), name="forum_list"),
    path("forum_detail/<str:pk>", ForumDetailView.as_view(), name="forum_detail"),

]
