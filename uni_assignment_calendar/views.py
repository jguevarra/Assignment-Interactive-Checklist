from django.http import HttpResponse
from .models import Events, Choice
from django.template import loader
from calendar import monthrange
from datetime import datetime, date
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render
from .forms import IndexForm
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


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






def named_month(month_number):
    """
    Return the name of the month, given the number.
    """
    return date(1900, month_number, 1).strftime("%B")

def this_month(request):
    """
    Show calendar of events this month.
    """
    today = datetime.now()
    return calendar(request, today.year, today.month)


def calendar(request, year, month, series_id=None):
    """
    Show calendar of events for a given month of a given year.
    ``series_id``
    The event series to show. None shows all event series.

    """

    my_year = int(year)
    my_month = int(month)
    my_calendar_from_month = datetime(my_year, my_month, 1)
    my_calendar_to_month = datetime(my_year, my_month, monthrange(my_year, my_month)[1])

    # my_events = Event.objects.filter(date_and_time__gte=my_calendar_from_month).filter(date_and_time__lte=my_calendar_to_month)
    # if series_id:
    #     my_events = my_events.filter(series=series_id)

    # Calculate values for the calendar controls. 1-indexed (Jan = 1)
    my_previous_year = my_year
    my_previous_month = my_month - 1
    if my_previous_month == 0:
        my_previous_year = my_year - 1
        my_previous_month = 12
    my_next_year = my_year
    my_next_month = my_month + 1
    if my_next_month == 13:
        my_next_year = my_year + 1
        my_next_month = 1
    my_year_after_this = my_year + 1
    my_year_before_this = my_year - 1
    # return render_to_response("templates/uni_assignment_calendar/home.html", { 'events_list': {},
    #                                                     'month': my_month,
    #                                                     'month_name': named_month(my_month),
    #                                                     'year': my_year,
    #                                                     'previous_month': my_previous_month,
    #                                                     'previous_month_name': named_month(my_previous_month),
    #                                                     'previous_year': my_previous_year,
    #                                                     'next_month': my_next_month,
    #                                                     'next_month_name': named_month(my_next_month),
    #                                                     'next_year': my_next_year,
    #                                                     'year_before_this': my_year_before_this,
    #                                                     'year_after_this': my_year_after_this,
    # }, context_instance=RequestContext(request))

    context = { 'events_list': {''},
                'month': my_month,
                'month_name': named_month(my_month),
                'year': my_year,
                'previous_month': my_previous_month,
                'previous_month_name': named_month(my_previous_month),
                'previous_year': my_previous_year,
                'next_month': my_next_month,
                'next_month_name': named_month(my_next_month),
                'next_year': my_next_year,
                'year_before_this': my_year_before_this,
                'year_after_this': my_year_after_this,
    }
    return render(request, "home.html", context)