"""article URL Configuration

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

from myarticle.views import signup_get, signup_post, article_dashboard, login_post, base_get, login_get, \
    add_article_get, add_article_post, del_article, edit_article_get, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',base_get),
    url(r'^signup_get/$',signup_get),
    url(r'^login_get/$',login_get),
    url(r'^signup_post/',signup_post),
    url(r'^article_dashboard/$', article_dashboard),
    url(r'^login/$', login_post),
    url(r'^add_article_post/$', add_article_post),
    url(r'^add_article/$', add_article_get),
    url(r'^del_article/$', del_article),
    url(r'^edit_article_get/$', edit_article_get),
    url(r'^logout_get/$', logout)

]
from django.conf import settings
from django.conf.urls.static import static
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
