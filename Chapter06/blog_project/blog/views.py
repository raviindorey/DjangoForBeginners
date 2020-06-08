from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Post


class BlogListView(ListView):
    model = Post
    context_object_name = 'all_posts_list'
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']
