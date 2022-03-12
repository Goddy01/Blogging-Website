from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (TemplateView, DetailView, ListView, View, CreateView, UpdateView, DeleteView)
from django.utils import timezone
from blog_app.models import Post, Comment, RegisterProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from blog_app.forms import CommentForm, RegisterForm, PostForm

# Create your views here.

class RegisterProfileView(CreateView):
    '''The view for users to register their profile.'''
    fields = ['author', 'title', ',image','text','date_created', 'date_published']
    model = RegisterProfile

class AboutView(TemplateView):
    '''The view for the about page'''
    template_name = 'about.html'

class PostListView(ListView):
    '''The view for the series of posts made'''
    model = Post

    # Formats how the list of posts should appear on the website in terms of date and order.
    def get_queryset(self):
        return Post.objects.filter(date_published__lte=timezone.now()).order_by('-date_published')

class PostDetailView(DetailView):
    '''The view that provides the details of a post'''
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    '''The view to create post'''
    login_url = '/login/' # The url the user is directed in case they are not logged in.
    fields  = ['author','title','image','text','date_created','date_published']
    redirect_field_name = 'blog_app/post_detail.html' # The url the user is redirected to after logging in.
    form_class =  PostForm
    model = Post

class UpdatePostView(LoginRequiredMixin, UpdateView):
    '''The view to update an existing post'''
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    form_class = PostForm
    model = Post

class DeletePostView(LoginRequiredMixin, DeleteView):
    '''Deletes a post from the website.'''
    model = Post
    success_url = reverse_lazy('blog_app:post_list')

    def get_query(self):
        return Post.objects.filter(date_published__is_null=True).order_by('-date_created')

class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    login_utl = 'login'
    redirect_field_name = reverse_lazy('blog_app:post_detail')

    def get_queryset(self):
        return Post.objects.filter(date_published___isnull=True).order_by('date_created')