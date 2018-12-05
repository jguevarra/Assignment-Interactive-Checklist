from .models import Events, Courses, Enrollment
from django.shortcuts import render, get_object_or_404
from .forms import IndexForm, UserForm
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def AboutView(request):
    """
    View for the about_page.html

    :param request:
    :return renders the request parameter, html template, and the context list:
    """
    context = {}
    template = 'uni_assignment_calendar/about_page.html'
    return render(request, template, context)

def GoalsView(request):
    """
    View for the goal_page.html

    :param request:
    :return renders the request parameter, html template, and the context list:
    """
    context = {}
    template = 'uni_assignment_calendar/goals_page.html'
    return render(request, template, context)

class IndexView(generic.ListView):
    """
    Generic view for index.html
    """
    template_name = 'uni_assignment_calendar/index.html'
    context_object_name = "latest_events_list"

    def get_queryset(self):
        """
        Sorts the query into the top 10 most recent postings

        :return max of 10 recent postings:
        """
        return Events.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:10]

class DetailView(generic.DetailView):
    """
    Generic view of detail.html
    """
    model = Events
    template_name = 'uni_assignment_calendar/detail.html'

def course_detail(request, class_id):
    """
    View for the course_detail.html

    if GET request, displays the course detail
    if POST request, enroll user in this class

    :param request:
    :param class_id:
    :return render of the request parammeter, the template url path, and a list of what will be used in
    the page content:
    """
    courses = get_object_or_404(Courses, class_id=class_id)
    status = ""
    username = request.user.username
    enrolled = Enrollment.objects.filter(username=username,class_id=class_id)
    
    if request.method == "POST":
        if enrolled.count() != 0:
            if request.POST.get('add') != None:
                status = "You have enrolled in this class"
            if request.POST.get('cancel') != None:
                enrolled.delete()
                status = "Course Successfully Deleted from Your Schedule!"

        else:
            if request.POST.get('add') != None:
                new_enroll = Enrollment(username=username,class_id=class_id)
                new_enroll.save()
                status = "Course Successfully Added!"        
            if request.POST.get('cancel') != None:   
                status = "You haven't Enrolled, why click remove?"

        return render(request, 'uni_assignment_calendar/course_detail.html', {'courses':courses,'status':status,'enrolled':enrolled})
    
    return render(request, 'uni_assignment_calendar/course_detail.html', {'courses':courses,'status':status,'enrolled':enrolled})


def ScheduleResults(request):
    """
    View for schedule.html -- For the course results after searching for a course using the search bar

    :param request:
    :return renders the request parameter, html url path, and the context list:
    """
    message = ""
    result = []

    if request.GET['search_id'] != "":
        message += 'search_id: ' + request.GET['search_id']
        result = Courses.objects.filter(class_id=request.GET['search_id'])

    if request.GET['search_abb'] != "":
        message += 'search_abb: ' + request.GET['search_abb']
        if result == []:
            result = Courses.objects.filter(class_abbrev=request.GET['search_abb'])
        else:
            result = result.filter(class_abbrev=request.GET['search_abb'])
        
    if request.GET['search_num'] != "":
        message += 'search_num: ' + request.GET['search_num']
        if result == []:
            result = Courses.objects.filter(class_num=request.GET['search_num'])
        else:
            result = result.filter(class_num=request.GET['search_num'])

    events_list = []
    course_list = []
    enrollments = Enrollment.objects.filter(username=request.user.username)
    
    for c in enrollments:
        #course = get_object_or_404(Courses,class_id=c.class_id)
        course = Courses.objects.get(class_id=c.class_id)
        events_list += Events.objects.filter(course=course).order_by('due_date','due_time')
        course_list.append(course)

    context = {'events_list':events_list,'enrollments':enrollments,'course_list':course_list,'result':result, 'message':message}

    return render(request,'uni_assignment_calendar/schedule.html',context)


def schedule(request):
    """
    View for schedule.html to view the user's schedule of enrolled classes

    :param request:
    :return renders the request parameter, html url path, and the context list:
    """
    events_list = []
    course_list = []
    enrollments = Enrollment.objects.filter(username=request.user.username)
    
    for c in enrollments:
        #course = get_object_or_404(Courses,class_id=c.class_id)
        course = Courses.objects.get(class_id=c.class_id)
        events_list += Events.objects.filter(course=course).order_by('due_date','due_time')
        course_list.append(course)
    context = {'events_list':events_list,'enrollments':enrollments,'course_list':course_list}

    
    return render(request,'uni_assignment_calendar/schedule.html',context)


# Form for creating an assignment
def create_assignment(request):
    """
    View for create.html
    Containe the form for creating a new assignment

    :param request:
    :return renders the request parameter, html url path, and the context list:
    """
    form = IndexForm()
    courses = set()
    enrollments = Enrollment.objects.filter(username=request.user.username)
    for c in enrollments:
        course = Courses.objects.get(class_id=c.class_id)
        courses.add(course)

    if request.method == "POST":
        form = IndexForm(request.POST)

        if form.is_valid():          
            obj = Events()
            obj.course = form.cleaned_data['course']
            obj.events_name = form.cleaned_data['events_name']
            obj.due_date = form.cleaned_data['due_date']
            obj.due_time = form.cleaned_data['due_time']
            obj.description = form.cleaned_data['description']
            obj.save()

            return HttpResponseRedirect("/home")
        else:
            return HttpResponseRedirect("/create")

    return render(request, 'uni_assignment_calendar/create.html', {'form':form,'courses':courses})


# Signup
def signup(request):
    """
    View for signup_page.html

    :param request:
    :return renders the request parameter, html url path, and the context list:
    """
    registered = False

    if request.method == "POST":
        form = UserForm(data=request.POST)

        if form.is_valid():

            if request.POST.get('password') != request.POST.get('password2'):
                messages.error(request, "Password Not Equal")
                return render(request,'uni_assignment_calendar/signup_page.html',{})            

            user = form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            return HttpResponse("Form Not Valid")
    else:
        form = UserForm()
    return render(request,'uni_assignment_calendar/signup_page.html',{'form':form, 'registered':registered})

# Login
def user_login(request):
    """
    View for login_page.html

    :param request:
    :return renders the request parameter, html url path, and the context list:
    """
    login_status = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect("/home")
            else:
                # messages.warning(request, "Warning: Account Not Active")
                login_status = "Warning: Account not active"
        else:
            return render(request,'uni_assignment_calendar/login_page.html',{})
    
    else:
        # messages.warning(request, "Login invalid, Try again!")
        login_status = "Login invalid. Try Again!"
        return render(request,'uni_assignment_calendar/login_page.html', {"login_status": login_status})

# Logout
@login_required
def user_logout(request):
    """
    View for logout.html

    :param request:
    :return renders the request parameter, html url path, and the context list:
    """
    logout(request)
    return HttpResponseRedirect("/")

