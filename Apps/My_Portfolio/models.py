from datetime import date

from django.db import models


class Portfolio(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=250)
  image = models.ImageField(upload_to='app_portfolio/images')
  url = models.URLField(blank=True)
  date = models.DateField(default=date.today)

  def __str__(self) -> str:
    return self.title
