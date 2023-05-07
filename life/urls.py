from django.urls import path
from . import views
from .views import BlogListView,ForumListView,BlogDetailView,ForumDetailView,JournalListView, JournalDetailView, ProfileView, Professional, ProfessionalDetail


urlpatterns = [
    path("", views.index, name="index"),
    path("404/", views.errorpage,),
    path("blog_list/", BlogListView.as_view(), name="blog_list"),
    path("blog_detail/<int:pk>", BlogDetailView.as_view(), name="blog_detail"),
    
    path("forum_list/", ForumListView.as_view(), name="forum_list"),
    path("forum_detail/<str:pk>", ForumDetailView.as_view(), name="forum_detail"),
    
    path("journal_list/", JournalListView.as_view(), name="journal_list"),
    path("journal_detail/<str:pk>", JournalDetailView.as_view(), name="journal_detail"),
    
    path("profile/<str:pk>", ProfileView.as_view(), name="profile"),
    path("professional_list/", Professional.as_view(), name="professional_list"),
    path("<str:pk>/professional_detail/", ProfessionalDetail.as_view(), name="professional_details"),


]

