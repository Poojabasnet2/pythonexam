from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView
from .models import Post
from django.views import View
from django.contrib.auth.views import LoginView
from myapp.forms import PostForm
# Create your views here.

class PostList(ListView):
    
    model=Post
    context_object_name='list'
    template_name="registration/blog.html"

class LoginView(LoginView):
    form_class=AuthenticationError
    authentication_form=None
    template_name="registration/login.html"
    redirect_authenticated_user=False
    extra_content=None

class AddBlog(CreateView):
    model=Post
    form_class=PostForm
    template_name='registration/add_blog.html'
    success_url=reverse_lazy('blog')

class UpdateBlog(UpdateView):
    model=Post
    form_class=PostForm
    template_name='registration/add_blog.html'
    success_url=reverse_lazy('blog')