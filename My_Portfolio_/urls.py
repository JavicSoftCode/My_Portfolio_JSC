import hashlib

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# @JavicSoftCode
from .views import HomeTemplateView


def generate_slug(text):
  return hashlib.md5(text.encode()).hexdigest()[:64]  # Un hash corto


urlpatterns = [
                path("admin/", admin.site.urls),
                path('', HomeTemplateView.as_view(), name='home'),
                path(f'b/{generate_slug("blog")}/', include('Apps.My_Blogs.urls', namespace='blog')),
                path(f'p/{generate_slug("portfolio")}/', include('Apps.My_Portfolio.urls', namespace='portfolio')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
