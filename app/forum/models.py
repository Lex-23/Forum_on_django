from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.contrib.contenttypes.fields import GenericRelation
from likes.models import Like, Dislike

from users.models import User

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    """система постов"""
    title = models.CharField(max_length=300)
    text = models.TextField()
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               null=True)
    published = models.DateTimeField(auto_now=True)
    likes = GenericRelation(Like)
    dislikes = GenericRelation(Dislike)
    category = models.ForeignKey(Category,
                                 on_delete=models.DO_NOTHING,
                                 related_name='category_post')
    status = models.BooleanField(default=True,
                                 verbose_name='status')

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

    @property
    def total_comments(self):
        return self.comments_post.count()

    @property
    def author_name(self):
        return self.author.username

    @property
    def category_name(self):
        return self.category.title


class Comment(models.Model):
    """Система комментариев"""
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
    text = models.TextField(default=None,
                            verbose_name='add comment')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True,
                                 verbose_name='looking post')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.author_name} on post "{self.post}", id: {self.id}'

    def post_title(self):
        return self.post.title

    @property
    def total_replies(self):
        return self.replies_comment.count()

    @property
    def author_name(self):
        return self.author.username


class Reply(models.Model):
    """Система ответов на комментарии"""
    comment = models.ForeignKey(Comment,
                                on_delete=models.CASCADE,
                                related_name='replies_comment',
                                verbose_name='comment',
                                blank=True,
                                null=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               null=True,
                               verbose_name='author',
                               blank=True)
    text = models.TextField(default=None,
                            verbose_name='add reply')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True,
                                 verbose_name='looking comment')

    class Meta:
        ordering = ('created',)

    @property
    def author_name(self):
        return self.author.username

    def __str__(self):
        return f'Reply by {self.author_name} on post "{self.comment}", id: {self.id}'
