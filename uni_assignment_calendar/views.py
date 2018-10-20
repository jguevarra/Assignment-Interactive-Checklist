from django.http import HttpResponse
from .models import Post
from django.template import loader

def index(request):
    latest_post_list = Post.objects.order_by('-post_date')[:5]
    template = loader.get_template('uni_assignment_calendar/index.html')
    context = {
        'latest_post_list': latest_post_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, post_id):
    return HttpResponse("You're looking at post # %s." % post_id)
