from django.http import HttpResponse
from .models import Event
from django.template import loader
from calendar import monthrange
from datetime import datetime, date
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render

from .forms import IndexForm


def index(request):
    latest_event_list = Event.objects.order_by('-day')
    context = {
        'latest_event_list': latest_event_list,
    }

    return render(request, 'uni_assignment_calendar/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'uni_assignment_calendar/detail.html', {'event': event})


# # for the form
# def get(self, request):
#     form = IndexForm()
#     events = Event.objects.all().order_by('-created')
#
#     args = {
#         'form': form, "events": events
#     }
#     return render(request, 'uni_assignment_calendar/index.html', args)
#
# def post(self, request):
#     form = IndexForm(request.POST)
#     if form.is_valid():
#         post = form.save(commit=False)
#         post.save()
#
#         text = form.cleaned_data['post']
#         form = IndexForm()
#         return redirect('calendar:calendar')
#
#     args = {'form': form, 'text': text}
#     return render(request, 'uni_assignment_calendar/index.html', args)





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