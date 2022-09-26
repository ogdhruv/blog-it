from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpRequest


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200)
    # related_name allow us to access related objects easily from a user
    # object by using the user.blog_posts
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated"]

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return "{},' by ',{}".format(self.title, self.author)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
