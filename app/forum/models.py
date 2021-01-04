from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.contrib.contenttypes.fields import GenericRelation
from likes.models import Like, Dislike

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    published = models.DateTimeField(auto_now=True)
    likes = GenericRelation(Like)
    dislikes = GenericRelation(Dislike)
    category = models.ForeignKey(Category,
                                 on_delete=models.DO_NOTHING,
                                 related_name='category_post')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_edit', kwargs={'pk': self.pk})

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def total_dislikes(self):
        return self.dislikes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments_post',
                             verbose_name='post',
                             blank=True,
                             null=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               null=True,
                               verbose_name='author',
                               blank=True)
    text = models.TextField(default=None, verbose_name='add comment')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, verbose_name='looking post')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

    def post_title(self):
        return self.post.title
