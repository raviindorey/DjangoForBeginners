from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'article_list.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'body']
    login_url = 'login'
    template_name = 'article_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'body']
    template_name = 'article_edit.html'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
