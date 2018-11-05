from .models import Events, Choice
from django.template import loader, RequestContext
from calendar import monthrange
from datetime import datetime, date
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from .forms import IndexForm, UserForm
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# generic views
class IndexView(generic.ListView):
    template_name = 'uni_assignment_calendar/index.html'
    context_object_name = "latest_events_list"

    def get_queryset(self):
        """Return the last five published assignments
        (not including those set to be published in the future)"""
        return Events.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
    model = Events
    template_name = 'uni_assignment_calendar/detail.html'


def results(request, events_id):
    events = get_object_or_404(Events, pk=events_id)
    return render(request, 'uni_assignment_calendar/detail.html', {'events': events})


def vote(request, events_id):
    events = get_object_or_404(Events, pk=events_id)
    try:
        selected_choice = events.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'events': events,
            # 'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(events.id,)))


def create_assignment(request):
    form = IndexForm()

    if request.method == "POST":
        form = IndexForm(request.POST)

        if form.is_valid():          
            form.save(commit=True)
            return HttpResponseRedirect('../')
        else:
            return HttpResponse("Form Not Valid")

    return render(request, 'uni_assignment_calendar/create.html', {'form':form})


def signup(request):
    registered = False

    if request.method == "POST":
        form = UserForm(data=request.POST)

        if form.is_valid():          
            user = form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            return HttpResponse("Form Not Valid")
    else:
        form = UserForm()
    return render(request,'uni_assignment_calendar/signup.html',{'form':form, 'registered':registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                messages.success(request, "Log in successfully")
                return HttpResponseRedirect('../')
            else:
                return HttpResponse("accounts not active")
        else:
            return HttpResponse("invalid login")
    
    else:
        return render(request,'uni_assignment_calendar/login.html',{})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Log out successfully")
    return HttpResponseRedirect('../')