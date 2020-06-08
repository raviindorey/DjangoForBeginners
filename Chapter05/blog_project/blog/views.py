from django.views.generic import ListView
from .models import Post


class BlogListView(ListView):
    model = Post
    context_object_name = 'all_posts_list'
    template_name = 'home.html'


