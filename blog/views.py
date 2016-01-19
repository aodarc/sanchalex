from django.shortcuts import render
from blog.form import *

# Create your views here.


def slider_image(request):
    return render(request, 'main.html')


def test_form(request):
    if request.method == 'GET':
        form = CommentForm(request.GET)
        if form.is_valid():
            text = form.cleaned_data['text']
            print(text)
        else:
            form = CommentForm()
    return render(request, 'add-comment.html', {'form': form})
