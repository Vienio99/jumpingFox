from django.shortcuts import render
from django.views import generic
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.


class BlogListView(generic.ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts'
    
class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(BlogCreateView, self).form_valid(form)

class BlogUpdateView(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


