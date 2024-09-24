from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

# @JavicSoftCode
from .models import Blog


class BlogListView(ListView):
  model = Blog
  template_name = 'app_my_blogs/my_blogs.html'
  context_object_name = 'blogs'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['total_blogs'] = self.get_queryset().count()
    context['title'] = 'My Blogs JSC'
    return context


class BlogsDetailView(DetailView):
  model = Blog
  template_name = "app_my_blogs/blog_details.html"
  context_object_name = "blog"

  def get_object(self, **kwargs):
    blog_id = self.kwargs.get('blog_id')
    return get_object_or_404(Blog, pk=blog_id)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = self.object.title
    return context
