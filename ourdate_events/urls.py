from django.urls import path
from .views import CalendarView, edit_event, event

app_name = 'ourdate_events'
urlpatterns = [
    path('', CalendarView.as_view(), name='index'),
    path('event/<int:event_id>/', event, name='event'),
    path('event/<int:event_id>/edit/', edit_event, name='edit_event'),
]
