from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class BlogListView(ListView):
    model = Post
    context_object_name = 'blogs'
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'bloginfo'
    template_name = 'blog_details.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'new_blog.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('home')