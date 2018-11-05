from .models import Events, Courses
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

# Index (generic views) -- home page
class IndexView(generic.ListView):
    template_name = 'uni_assignment_calendar/index.html'
    context_object_name = "latest_events_list"

    def get_queryset(self):
        """Return the last five published assignments
        (not including those set to be published in the future)"""
        return Events.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:10]

# Detail (generic view)
class DetailView(generic.DetailView):
    model = Events
    template_name = 'uni_assignment_calendar/detail.html'

# Form for creating an assignment
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

# Signup
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

# Login
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

# Logout
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Log out successfully")
    return HttpResponseRedirect('../')