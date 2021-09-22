from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    title = models.CharField(max_length=255, default='', blank=False)
    desc = models.TextField(default='', blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Article(BaseModel):
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ['-created']
