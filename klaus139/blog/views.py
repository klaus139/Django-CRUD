from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import UpdateView
from .models import Post
from django.urls import reverse, reverse_lazy
# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"


class PostCreateView(CreateView):
    model = Post 
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = PostCreateViewfields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
