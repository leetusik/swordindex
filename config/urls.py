"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("emails/", include("emails.urls")),
    path("asks/", include("asks.urls")),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("test-static/", views.test_static, name="test_static"),
    path("direct-image/", views.direct_image, name="direct_image"),
    path("search/api/", views.search_api, name="search_api"),
    path("test/", views.test, name="test"),
    path("robots.txt", views.robots_txt, name="robots_txt"),
    path("sitemap.xml", views.sitemap_xml, name="sitemap_xml"),
    path("sitemap/", views.sitemap_html, name="sitemap_html"),
    path("naver4483f8bee1728b2ccd7fe7f648565f14.html/", views.naver, name="naver"),
]
