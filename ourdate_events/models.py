import datetime

from author.decorators import with_author
from django.db import models
from django.urls import reverse
from location_field.models.plain import PlainLocationField

from users.models import CustomUser as User


@with_author
class Event(models.Model):
    title = models.CharField(max_length=200)
    hero_image = models.ImageField(upload_to="hero_images")
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    address = models.CharField(max_length=254, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    registration_limit = models.IntegerField(
        "Guest limit",
        default=0,
        choices=[(0, "No limit")] + list(zip(range(1, 1000), range(1, 1000))),
    )

    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse("ourdate_events:edit_event", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


def EventRegistration(request, event_id):
    event = models.ManyToOneRel(
        Event, blank=True, null=True, on_delete=models.CASCADE
    )
    user = models.ManyToOneRel(
        User, blank=True, null=True, on_delete=models.CASCADE
    )
    time_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name

    class Meta:
        ordering = ["time_registered"]
        verbose_name_plural = "Attendees"
        verbose_name = "Attendee"
        unique_together = ("event", "user")


def CancelledRegistrations(request, event_id):
    event = models.ManyToOneRel(
        Event, blank=True, null=True, on_delete=models.CASCADE
    )
    user = models.ManyToOneRel(
        User, blank=True, null=True, on_delete=models.CASCADE
    )
    time_cancelled = models.DateTimeField(auto_now_add=True)
    time_registered = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=200, blank=True, null=True)


def add_user_to_list_of_attendees(self, user):
    registration = EventRegistration.objects.create(
        user=user, event=self, time_registered=datetime.now()
    )


def remove_user_from_list_of_attendees(self, user):
    registration = EventRegistration.objects.get(user=user, event=self)
    registration.delete()
    cancelation = CancelledRegistrations.objects.create(
        user=user,
        event=self,
        time_cancelled=datetime.now(),
        reason="",
        time_registered=EventRegistration.objects.get(
            user=user, event=self
        ).time_registered,
    )
    cancelation.save()
