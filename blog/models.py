from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    tag_name = models.CharField(max_length=20, unique=True, verbose_name=u'Тег')
    result = models.IntegerField(default=1, verbose_name=u'Кількість елементів з тегом')


class Article(models.Model):
    title = models.CharField(max_length=90, blank=False, null=False, verbose_name=u'Заголовок')
    text = models.TextField(max_length=2000, blank=False, null=False, verbose_name=u'Текст')
    # image = models.ImageField(blank=True, null=True)  # Need Install Numpy+PIL
    cheated = models.DateTimeField(auto_now_add=True, blank=False, null=False, verbose_name=u'Дата створення')
    modified = models.DateTimeField(auto_now=True, blank=True, null=False, verbose_name=u'Дата зміни')
    author_post = models.ForeignKey(User, verbose_name=u'Автор')
    tag = models.ManyToManyField(Tag, blank=True)
    like = models.IntegerField(default=0, null=False, verbose_name=u'Вподобання')
    is_posted = models.BooleanField(default=0, verbose_name=u'Опублікована?')

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=300, verbose_name=u'Коментак')
    author = models.ForeignKey(User, blank=False, null=True, verbose_name=u'Автор')
    created = models.DateTimeField(auto_now_add=True, auto_created=True, verbose_name=u'Дата')

    def __str__(self):
        return self.text[:200]