from django.shortcuts import render

from django.http import Http404
from django.template import loader
from .models import Post


def index(request):
    # displays the latest 5 poll questions in the system according to the post date
    latest_post_list = Post.objects.order_by('-post_date')[:5]
    context = {
        'latest_post_list': latest_post_list
    }
    return render(request, 'home/index.html', context)

# additional views
def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'home/detail.html', {'post': post})
