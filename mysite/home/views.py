from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Post


def index(request):
    # displays the latest 5 poll questions in the system according to the post date
    latest_post_list = Post.objects.order_by('-post_date')[:5]
    # output = ', '.join([p.post_title for p in latest_post_list])
    template = loader.get_template('home/index.html')
    context = {
        'latest_post_list': latest_post_list
    }
    return HttpResponse(template.render(context, request))

# additional views
def detail(request, post_id):
    return HttpResponse("You're looking at question %s." % post_id)
