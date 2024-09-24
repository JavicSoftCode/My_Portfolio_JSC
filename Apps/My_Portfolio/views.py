from django.views.generic import ListView

# @JavicSoftCode
from .models import Portfolio


class PortfolioListView(ListView):
  model = Portfolio
  template_name = 'app_my_portfolio/my_portfolio.html'
  context_object_name = 'projects'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'My Portfolio JSC'
    return context
