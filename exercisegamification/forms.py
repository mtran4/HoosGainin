from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, Field
from .models import Profile, Goal, MyWorkout, Workout
from datetime import date
from bootstrap_datepicker_plus import DatePickerInput

class EditProfileForm(ModelForm):

    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    age = forms.IntegerField(max_value=None,min_value=0, label="Age")
    weight = forms.IntegerField(max_value=None, min_value=0, required=False, label='Weight*')
    bmi = forms.IntegerField(max_value=100, min_value=0, required=False, label='BMI*')
    fav_exercise = forms.CharField(max_length=500, required=True)
    profile_pic = forms.ImageField(required=False, label='Profile Picture', error_messages = {
                 'required':"Please Enter your Name"
                 })


    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'age',
            'weight',
            'bmi',
            'fav_exercise',
            'profile_pic'
        )

class AddGoalForm(ModelForm):
    title = forms.CharField(max_length=50, required=True)
    pub_date = forms.DateTimeField(required=True, label="Date Created")
    reach_date = forms.DateTimeField(required=True, label='Target Reach Date')
    pub_date = forms.DateField(widget=DatePickerInput(format='%m/%d/%Y'),initial=date.today, required=True, label="Date Created")
    reach_date = forms.DateField(widget=DatePickerInput(format='%m/%d/%Y'),required=True, label='Target Reach Date')
    goal_text = forms.CharField(required=True)
    accomplished = forms.BooleanField(required=True)
    accomplished = forms.BooleanField(required=False)

    class Meta:
        model = Goal
        fields = (
            'title',
            'pub_date',
            'reach_date',
            'goal_text',
            'accomplished'
        )

class EditGoalForm(ModelForm):
    title = forms.CharField(max_length=50, required=True)
    pub_date = forms.DateTimeField(required=True, label="Date Created")
    reach_date = forms.DateTimeField(required=True, label='Target Reach Date')
    pub_date = forms.DateField(widget=DatePickerInput(format='%m/%d/%Y'), required=True, label="Date Created")
    reach_date = forms.DateField(widget=DatePickerInput(format='%m/%d/%Y'), required=True, label='Target Reach Date')
    goal_text = forms.CharField(required=True)
    accomplished = forms.BooleanField(required=True)
    accomplished = forms.BooleanField(required=False)

    class Meta:
        model = Goal
        fields = (
            'title',
            'pub_date',
            'reach_date',
            'goal_text',
            'accomplished'
        )


class AddMyWorkoutForm(ModelForm):
    myworkout_title = forms.CharField(max_length=200, required=True)
    myworkout_description = forms.CharField(max_length=500, required = True)

    class Meta:
        model = MyWorkout
        fields = (
            'myworkout_title',
            'myworkout_description',
            )

class WorkoutDateForm(ModelForm):
    date = forms.DateField(widget=DatePickerInput(format='%m/%d/%Y'), initial=date.today, required=True,
                           label="Date Completed")

    class Meta:
        model = Workout
        fields = {
            'date'
        }





#class AddGoalForm(forms.ModelForm):
#    class Meta:
#        model = Goal
#        fields = ('author', 'title', 'pub_date', 'reach_date', 'goal_text', 'accomplished')

#        widgets = {
#            'author': forms.Select(attrs={'class':'form-control'}),
#            'title': forms.TextInput(attrs={'class':'form-control'}),
#            'pub_date': forms.SelectDateWidget(attrs={'class':'form-control'}),
#            'reach_date': forms.SelectDateWidget(attrs={'class':'form-control'}),
#            'goal_text': forms.Textarea(attrs={'class':'form-control'}),
#            'accomplished': forms.BooleanField(),
#        }