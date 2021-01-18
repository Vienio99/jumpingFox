from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.


class BlogListView(generic.ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts'
    

class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class BlogCreateView(generic.CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['author', 'title', 'body']