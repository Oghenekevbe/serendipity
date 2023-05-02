from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

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
    

    