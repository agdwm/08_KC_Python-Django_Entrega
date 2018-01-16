"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from blogs.views import LatestPosts, BlogList, PostListByAuthor, PostDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/<str:autor>/<int:pk>', PostDetail.as_view(), name="post_detail_page"),
    path('blogs/<str:autor>/', PostListByAuthor.as_view(), name="list_posts_page"),
    path('blogs/', BlogList.as_view(), name="list_blogs_page"),
    path('', LatestPosts.as_view(), name="home_page")
]

