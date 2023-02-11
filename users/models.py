# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
try:
     import zoneinfo
except ImportError:
     from backports import zoneinfo
import pytz
from timezone_field import TimeZoneField


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must have is_staff=True.'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must have is_superuser=True.'
            )

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'username'  # make the user log in with the email
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

# Many to many models for choices


class AlcoholUsage(models.Model):
    usage = models.CharField(max_length=100)

    def __str__(self):
        return self.usage


class DateActivities(models.Model):
    activity = models.CharField(max_length=100)

    def __str__(self):
        return self.activity


class Diet(models.Model):
    diet = models.CharField(max_length=100)

    def __str__(self):
        return self.diet


class Education(models.Model):
    school = models.CharField(max_length=100, null=True)
    degree = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.degree


class FamilyPlans(models.Model):
    plan = models.CharField(max_length=100)

    def __str__(self):
        return self.plan


class Genders(models.Model):
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.gender


class Hobbies(models.Model):
    hobby = models.CharField(max_length=100)

    def __str__(self):
        return self.hobby


class Interests(models.Model):
    interest = models.CharField(max_length=100)

    def __str__(self):
        return self.interest


class LookingFor(models.Model):
    option = models.CharField(max_length=100)

    def __str__(self):
        return self.option


class OtherDrugUsage(models.Model):
    usage = models.CharField(max_length=100)

    def __str__(self):
        return self.usage


class RelationshipStatus(models.Model):
    relationship = models.CharField(max_length=100)

    def __str__(self):
        return self.relationship


class TobaccoUsage(models.Model):
    usage = models.CharField(max_length=100)

    def __str__(self):
        return self.usage


class WeedUsage(models.Model):
    usage = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.usage


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    alcohol_usage = models.ManyToManyField(AlcoholUsage, blank=True)
    avatar = models.ImageField(
        default='default.jpg', upload_to='profile_images')
    bio = models.TextField(default='')
    birthday = models.DateField('birthday', null=True)
    date_activities = models.ManyToManyField(DateActivities, blank=True)
    diet = models.ManyToManyField(Diet, blank=True)
    education = models.ManyToManyField(Education, blank=True)
    family_plans = models.ManyToManyField(FamilyPlans, blank=True)
    gender = models.ManyToManyField(Genders, blank=True)
    hobbies = models.ManyToManyField(Hobbies, blank=True)
    interests = models.ManyToManyField(Interests, blank=True)
    looking_for = models.ManyToManyField(LookingFor, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    other_drug_usage = models.ManyToManyField(OtherDrugUsage, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    relationship_status = models.ManyToManyField(
        RelationshipStatus, blank=True)
    time_zone = TimeZoneField(
        default='America/Los_Angeles')
    tobacco_usage = models.ManyToManyField(TobaccoUsage, blank=True)
    weed_usage = models.ManyToManyField(WeedUsage, blank=True)

    def __str__(self):
        return self.user.username
