"""vietgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from images import views as image_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(
        regex = r'^$',
        view = user_views.index,
        name = 'index'
    ),

    url(
        regex = r'^login/$',
        view = user_views.login,
        name = 'login'
    ),

    url(
        regex = r'^explore$',
        view = user_views.explore,
        name = 'explore'
    ),
    
    url(
        regex = r'^images/(?P<image_id>[\d+])/like/$',
        view = image_views.like_image,
        name = 'like_image'
    ),

    url(
        regex = r'^images/(?P<image_id>[\d+])/comment/$',
        view = image_views.comment_image,
        name = 'comment_image'
    ),

    url(
        regex = r'^profile/(?P<username_from_url>.+)/$',
        view = user_views.profile,
        name = 'profile'
    )

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
