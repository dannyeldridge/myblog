from django.db import models
from django.utils import timezone
from django.conf import settings
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
import datetime

class Post(models.Model):
    """docstring for Post."""

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = MarkdownxField(blank=True, null=True)
    created_date = models.DateField(default=datetime.date.today)
    published_date = models.DateField(blank=True, null=True)

    # Create a property that returns the markdown instead
    @property
    def formatted_markdown(self):
        return markdownify(self.text)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
