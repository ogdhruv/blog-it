from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class BlogView(ListView):
    model = Post
    template_name: str = "blog/bloglist.html"
    paginate_by: int = 3
    context_object_name = "all_blogs"


class BlogDetailView(DetailView):
    model = Post
    template_name: str = "blog/blog_page.html"


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name: str = "blog/createblog.html"
    fields = ["title", "author", "body"]
    success_url = reverse_lazy("blog")


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name: str = "blog/updateblog.html"
    fields = ["title", "body"]
    success_url = reverse_lazy("blog")


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name: str = "blog/deleteblog.html"
    success_url = reverse_lazy("blog")
