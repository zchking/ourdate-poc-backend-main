# users/forms.py
from django.contrib.auth.models import User
from .models import AlcoholUsage, DateActivities, Diet, Education, FamilyPlans, Genders, Hobbies, Interests, LookingFor, \
    OtherDrugUsage, Profile, RelationshipStatus, TobaccoUsage, WeedUsage
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Profile


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(required=True, max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")


class LogInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class UpdateProfileForm(forms.ModelForm):
    alcohol_usage_choices = AlcoholUsage.objects.all().values_list()
    alcohol_usage_selection = Profile.objects.filter(
    ).values_list('alcohol_usage', flat=True)
    date_activities_choices = DateActivities.objects.all().values_list()
    date_activities_selection = Profile.objects.filter(
    ).values_list('date_activities', flat=True)
    diet_choices = Diet.objects.all().values_list()
    diet_selection = Profile.objects.filter().values_list('diet', flat=True)
    education_choices = [(e.id, e.school) for e in Education.objects.all()]
    # we'd better write the choice like this.As many model have more than one fields
    # it will big bug if there are >2 fields for choices.
    education_selection = Profile.objects.filter().values_list('education', flat=True)
    family_plans_choices = FamilyPlans.objects.all().values_list()
    family_plans_selection = Profile.objects.filter(
    ).values_list('family_plans', flat=True)
    gender_choices = Genders.objects.all().values_list()
    gender_selection = Profile.objects.filter().values_list('gender', flat=True)
    hobbies_choices = Hobbies.objects.all().values_list()
    hobbies_selection = Profile.objects.filter().values_list('hobbies', flat=True)
    interests_choices = Interests.objects.all().values_list()
    interests_selection = Profile.objects.filter().values_list('interests', flat=True)
    looking_for_choices = LookingFor.objects.all().values_list()
    looking_for_selection = Profile.objects.filter().values_list('looking_for', flat=True)
    other_drug_usage_choices = OtherDrugUsage.objects.all().values_list()
    other_drug_usage_selection = Profile.objects.filter(
    ).values_list('other_drug_usage', flat=True)
    relationship_status_choices = RelationshipStatus.objects.all().values_list()
    relationship_status_selection = Profile.objects.filter(
    ).values_list('relationship_status', flat=True)
    tobacco_usage_choices = TobaccoUsage.objects.all().values_list()
    tobacco_usage_selection = Profile.objects.filter(
    ).values_list('tobacco_usage', flat=True)
    weed_usage_choices = WeedUsage.objects.all().values_list()
    weed_usage_selection = Profile.objects.filter().values_list('weed_usage', flat=True)

    alcohol_usage = forms.MultipleChoiceField(
        choices=alcohol_usage_choices,
        initial=alcohol_usage_selection,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}))
    avatar = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={'class': 'form-control'}))
    bio = forms.Textarea(attrs={'class': 'form-control'})
    birthday = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control'}))
    date_activities = forms.MultipleChoiceField(
        choices=date_activities_choices,
        initial=date_activities_selection,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}))
    diet = forms.MultipleChoiceField(
        choices=diet_choices,
        initial=diet_selection,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}))
    education = forms.MultipleChoiceField(
        choices=education_choices,
        initial=education_selection,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}))
    family_plans = forms.MultipleChoiceField(
        choices=family_plans_choices,
        initial=family_plans_selection,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}))
    gender = forms.MultipleChoiceField(
        choices=gender_choices,
        initial=gender_selection,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}))
    hobbies = forms.MultipleChoiceField(
        choices=hobbies_choices,
        initial=hobbies_selection,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}))
    interests = forms.MultipleChoiceField(
        choices=interests_choices,
        initial=interests_selection,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}))
    looking_for = forms.MultipleChoiceField(
        choices=looking_for_choices,
        initial=looking_for_selection,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}))
    occupation = forms.TextInput(attrs={'class': 'form-control'})
    other_drug_usage = forms.MultipleChoiceField(
        choices=other_drug_usage_choices,
        initial=other_drug_usage_selection,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}))
    phone_number = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    relationship_status = forms.MultipleChoiceField(
        choices=relationship_status_choices,
        initial=relationship_status_selection,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}))
    tobacco_usage = forms.MultipleChoiceField(
        choices=tobacco_usage_choices,
        initial=tobacco_usage_selection,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}))
    weed_usage = forms.MultipleChoiceField(
        choices=weed_usage_choices,
        initial=weed_usage_selection,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}))

    class Meta:
        model = Profile
        fields = [
            'alcohol_usage',
            'avatar',
            'bio',
            'birthday',
            'date_activities',
            'diet',
            'education',
            'family_plans',
            'gender',
            'hobbies',
            'interests',
            'looking_for',
            'occupation',
            'other_drug_usage',
            'phone_number',
            'relationship_status',
            'tobacco_usage',
            'weed_usage',
        ]
