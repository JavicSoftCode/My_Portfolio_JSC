import hashlib

from django.urls import path

# @JavicSoftCode
from .views import PortfolioListView

app_name = 'portfolio'


def generate_slug(text):
  return hashlib.md5(text.encode()).hexdigest()[:64]  # Un hash corto


urlpatterns = [
  path(f'p/{generate_slug("my_portfolio")}/', PortfolioListView.as_view(), name='my_portfolio'),
]
