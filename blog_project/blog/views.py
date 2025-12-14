from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.text import slugify
from .models import Post

class PostListView(ListView):
    """View to display all published blog posts."""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(status='published')

class PostDetailView(DetailView):
    """View to display a single blog post."""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    """View to create a new blog post."""
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    """View to update an existing blog post."""
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'status']

    def get_queryset(self):
        # Only allow authors to edit their own posts
        return Post.objects.filter(author=self.request.user)

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    """View to delete a blog post."""
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        # Only allow authors to delete their own posts
        return Post.objects.filter(author=self.request.user)

def home(request):
    """Home page view."""
    posts = Post.objects.filter(status='published')[:5]
    return render(request, 'home.html', {'posts': posts})

