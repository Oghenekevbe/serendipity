from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Doctor, Notes, Patient, ForumPost, BlogPost, JournalPost, Comment, Profile, Consultation, ConsultationComment
from django.urls import reverse_lazy
from .forms import JournalPostForm


# Create your views here.

def index(request):
    return render(request, 'index.html')

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog_list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        queryset = self.model.objects.all().order_by('-date_added')
        return queryset
    
class BlogDetailView(DetailView): 
    model = BlogPost 
    template_name = 'blog_detail.html' 
     
    def get_queryset(self): 
        queryset = self.model.objects.all().order_by('-date_added') 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object()
        return context


    


class ForumListView(ListView):
    model = ForumPost
    template_name = 'forum_list.html'
    context_object_name = 'forums'
    
    def get_queryset(self):
        queryset = self.model.objects.all().order_by('-date_added')
        return queryset
    
class ForumDetailView(DetailView):
    model = ForumPost
    template_name = 'forum_detail.html'
    context_object_name = 'forums'
    
    def get_queryset(self):
        queryset = self.model.objects.all().order_by('-date_added')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object()
        return context



class JournalListView(ListView):
    model = JournalPost
    template_name = "journal_list.html"
    context_object_name = 'journal'
    

    
class JournalDetailView(DetailView):
    model = JournalPost
    template_name = "journal_detail.html"
    context_object_name = 'post'
    
def errorpage(request):
    return render(request, 'unauthorized.html')


class AddJournal(CreateView):
    model = JournalPost
    template_name = 'add_journal.html'
    form_class = JournalPostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class EditJournal(UpdateView):
    model = JournalPost
    template_name = 'edit_journal.html'
    form_class = JournalPostForm

class DeleteJournal(DeleteView):
    model = JournalPost
    template_name = 'delete_journal.html'
    success_url = reverse_lazy('journal_list')
    
# user interaction

class ProfileView(DetailView):
    model = Profile
    template_name = "registration/profile.html"


        
        
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
    
    
class Professional(ListView):
    model = Consultation
    template_name = "professional_list.html"   
    context_object_name = 'consultations'
    
class ProfessionalDetail(DetailView):
    model = Consultation
    template_name = "professional_detail.html"   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    