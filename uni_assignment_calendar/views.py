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
    context = {}
    template = 'uni_assignment_calendar/about_page.html'
    return render(request, template, context)

def GoalsView(request):
    context = {}
    template = 'uni_assignment_calendar/goals_page.html'
    return render(request, template, context)

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
# def events_detail(request, pk):
#     events = get_object_or_404(Events, pk=pk)
#     courses = events.course
#     return render(request, 'uni_assignment_calendar/detail.html', {'events':events, 'courses':courses})



# If GET request, displays the course detail
# If POST request, enroll user in this class  
def course_detail(request, class_id):
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

#handle ajax request to hide deleted assignments for active users
def hideAssgn(request):
    if request.is_ajax():
        url = request.GET.get('data')
        mystring = str(url)
        temp = ''
        i = -2
        while mystring[i] != '/':
            temp += mystring[i]
            i -= 1     
        hide = temp[::-1]
        enroll = Enrollment.objects.filter(username=request.user.username)
        enroll.exclude.add(int(hide))
        message = 'Assignment deleted'
    else:
        message = 'Something went wrong!'
    return HttpResponse(message)

# Form for creating an assignment
def create_assignment(request):
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
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect("/home")
            else:
                messages.warning(request, "Warning: Account Not Active")
        else:
            return render(request,'uni_assignment_calendar/login_page.html',{})
    
    else:
        return render(request,'uni_assignment_calendar/login_page.html',{})

# Logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

