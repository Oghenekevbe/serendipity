from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView
from .models import Doctor, Notes, Patient, ForumPost, BlogPost, JournalPost, Comment, Profile, Consultation, ConsultationComment
# from .forms import ProfessionalForm
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["journal"] = self.get_object()
        return context
    
def errorpage(request):
    return render(request, 'unauthorized.html')
    
    
    
# user interaction

class ProfileView(DetailView):
    model = Profile
    template_name = "registration/profile.html"


    # def get(self, request, *args, **kwargs):
    #     messages.success(request, 'Your action was successful!')
    #     return super().get(request, *args, **kwargs)
        
        
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
    
    