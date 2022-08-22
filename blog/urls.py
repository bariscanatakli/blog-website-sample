from . import views
from django.urls import path,include
from .feeds import LatestPostsFeed
from .views import SignUpView,ProfileView
from django.contrib import admin
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    
    
]


