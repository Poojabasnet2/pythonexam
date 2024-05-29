from django.urls import path
from django.contrib import admin
from .import views
from django.conf import settings
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog'), 
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),  
    path('add-blog/', views.AddBlog.as_view(), name='add_blog')
    path('update-blog/<int:pk>/', views.UpdateBlog.as_view(), name='update_blog'),
]