from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import (
    Doctor,
    Notes,
    Patient,
    ForumPost,
    BlogPost,
    JournalPost,
    Comment,
    Consultation,
    ConsultationComment)
from django.urls import reverse_lazy
from .forms import JournalPostForm, ConsultationForm, EditProfileForm, ConsultationCommentForm



# Create your views here.


class UserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect("unauthorized")


def unauthorized(request):
    return render(request, "unauthorized.html")


def index(request):
    return render(request, "index.html")


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = self.model.objects.all().order_by("-date_added")
        return queryset


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog_detail.html"

    def get_queryset(self):
        queryset = self.model.objects.all().order_by("-date_added")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = self.get_object()
        return context


class ForumListView(ListView):
    model = ForumPost
    template_name = "forum_list.html"
    context_object_name = "forums"

    def get_queryset(self):
        queryset = self.model.objects.all().order_by("-date_added")
        return queryset


class ForumDetailView(DetailView):
    model = ForumPost
    template_name = "forum_detail.html"
    context_object_name = "forums"

    def get_queryset(self):
        queryset = self.model.objects.all().order_by("-date_added")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = self.get_object()
        return context


class JournalListView(ListView):
    model = JournalPost
    template_name = "journal_list.html"
    context_object_name = "journal"


class JournalDetailView(DetailView):
    model = JournalPost
    template_name = "journal_detail.html"
    context_object_name = "post"


class AddJournal(CreateView):
    model = JournalPost
    template_name = "add_journal.html"
    form_class = JournalPostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditJournal(UpdateView):
    model = JournalPost
    template_name = "edit_journal.html"
    form_class = JournalPostForm


class DeleteJournal(DeleteView):
    model = JournalPost
    template_name = "delete_journal.html"
    success_url = reverse_lazy("journal_list")


# user interaction


class ProfileView(DetailView):
    model = User
    template_name = "registration/profile.html"


class EditProfileView(UpdateView):
    model = User
    template_name = "registration/edit_profile.html"
    form_class = EditProfileForm
    success_url = reverse_lazy("index")
    







class PatientProfileView(ListView):
    model = Patient
    template_name = "registration/patient_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patients"] = patients
        return context


class PatientProfileView(DetailView):
    model = Patient
    template_name = "registration/patient_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patients"] = patients
        return context


class Professional(UserMixin, ListView):
    model = Consultation
    template_name = "professional_list.html"
    context_object_name = "consultations"


class ProfessionalDetail(UserMixin, DetailView):
    model = Consultation
    template_name = 'professional_detail.html'
    context_object_name = 'consultation'
    form_class = ConsultationCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = self.object.notes_set.all() #or consultation.notes.all()
        context['comments'] = self.object.comments.all()
        return context

class AddConsultation(UserMixin, CreateView):
    model = Consultation
    template_name = "add_consultation.html"
    form_class = ConsultationForm
    success_url = reverse_lazy("professional_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs
