from django.db import models


class WebURL(models.Model):
    """
    Model that represents a shortened URL
    """
    full_url = models.URLField(verbose_name='Full url')
    short_url = models.CharField(max_length=64)
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return F"URL: {self.full_url} Value:{self.short_url}"
