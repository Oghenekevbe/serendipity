from django.urls import path
from . import views
from .views import BlogListView,ForumListView,BlogDetailView,ForumDetailView,JournalListView, JournalDetailView, AddJournal, EditJournal, DeleteJournal, ProfileView, Professional, ProfessionalDetail, AddConsultation, EditProfileView, AddConsultationNotes, PatientProfileList, PatientProfileDetail


urlpatterns = [
    path("", views.index, name="index"),
    path("unauthorized/", views.unauthorized, name='unauthorized'),
    path("blog_list/", BlogListView.as_view(), name="blog_list"),
    path("blog_detail/<int:pk>", BlogDetailView.as_view(), name="blog_detail"),
    
    path("forum_list/", ForumListView.as_view(), name="forum_list"),
    path("forum_detail/<str:pk>", ForumDetailView.as_view(), name="forum_detail"),
    
    path("journal_list/", JournalListView.as_view(), name="journal_list"),
    path("journal_detail/<str:pk>", JournalDetailView.as_view(), name="journal_detail"),
    path("add_journal/", AddJournal.as_view(), name="add_journal"),
    path("edit_journal/<str:pk>", EditJournal.as_view(), name="edit_journal"),
    path("delete_journal/<str:pk>", DeleteJournal.as_view(), name="delete_journal"),
    
    path("profile/<str:pk>", ProfileView.as_view(), name="profile"),
    path("edit_profile/<str:pk>", EditProfileView.as_view(), name="edit_profile"),
    path("professional_list/", Professional.as_view(), name="professional_list"),
    path("professional_detail/<str:pk>", ProfessionalDetail.as_view(), name="professional_detail"),
    path("add_consultation", AddConsultation.as_view(), name="add_consultation"),
    path("add_notes/<str:pk>", AddConsultationNotes.as_view(), name="add_notes"),
    path("patient_list/", PatientProfileList.as_view(), name="patient_list"),
    path("patient_detail/<str:pk>", PatientProfileDetail.as_view(), name="patient_detail"),

        # USER CREDENTIALS
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('forgot_password/', views.forgot_password, name= 'forgot_password'),
    path('reset_password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path('reset_password_email/', views.reset_password_email, name='reset_password_email'),
    path('change-password/', views.change_password, name='change_password'),            



]

