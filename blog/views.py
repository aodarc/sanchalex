from django.shortcuts import render
from django.views.decorators.gzip import gzip_page
from blog.form import *
from blog.models import *

# Create your views here.


def test_form(request):
    if request.method == 'GET':
        form = CommentForm(request.GET)
        if form.is_valid():
            text = form.cleaned_data['text']
            print(text)
        else:
            form = CommentForm()
    return render(request, 'blog/add-comment.html', {'form': form})


def show_articles(request):
    articles = Article.objects.all()
    content = {
        'articles': articles
    }
    return render(request, 'blog/articles.html', content)


@gzip_page
def custom404(request):
    return render(request, '404.html')
