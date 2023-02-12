import calendar
from datetime import date as dt
from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.safestring import mark_safe
from django.views import generic

from .forms import EventForm
from .models import Event as EventModel
from .models import *
from .utils import Calendar


@login_required
def index(request):
    return HttpResponse("hello")


@method_decorator(login_required, name="dispatch")
class CalendarView(generic.ListView):
    model = Event
    template_name = "events/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("month", None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context["calendar"] = mark_safe(html_cal)
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split("-"))
        return date(year, month, day=1)
    return dt.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = "month=" + str(prev_month.year) + "-" + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = "month=" + str(next_month.year) + "-" + str(next_month.month)
    return month


@login_required
def edit_event(request, event_id=None):
    try:
        event = EventModel.objects.get(pk=event_id)
    except EventModel.DoesNotExist:
        raise Http404("Event does not exist")

    if request.user.username != event.author.username:
        return HttpResponseRedirect(
            reverse("ourdate_events:event", args=(event.id,))
        )

    form = EventForm(request.POST or None, instance=event)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(
            reverse("ourdate_events:event", args=(event.id,))
        )
    return render(
        request, "events/event_edit.html", {"form": form, "event": event}
    )


@login_required
def event(request, event_id=None):
    try:
        event = EventModel.objects.get(pk=event_id)
    except EventModel.DoesNotExist:
        raise Http404("Event does not exist")
    return render(request, "events/event.html", {"event": event})
