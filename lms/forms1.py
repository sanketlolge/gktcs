from lms.models import *
from django.forms import ModelForm
from django import forms
from registration.forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
#from .models import models


class Enquiryform(ModelForm):
    class Meta:
        model = Enquiry
        fields=['Name','Email','Contact','Message']

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		exclude = []

class Comments_choiceForm(forms.ModelForm):
	class Meta:
		model = Comments_choice
		exclude = []

class trainerform(ModelForm):
    class Meta:
        model = add_instructor
        fields=['f_name', 'l_name', 'mobile', 'email', 'course_name', 'linkedin_profile', 'about_course', 'about_yourself']



class searchform(ModelForm):
    class Meta:
        model = search
        fields=['s']

class hireform(ModelForm):
    class Meta:
        model = hire
        fields=['job_title','vaccancies','job_description','Desired_profile', 'Experience','salary','location','company_name','person_name','mobile','Email','companyurl']

class coursesform(ModelForm):
    class Meta:
        model = courses
        fields = ['course_name']

class blogsform(ModelForm):
    class Meta:
        model = blogs
        fields = ['blog_writer' , 'blog_title', 'blog_content','blog_date']

#class loginform(ModelForm):
#    class Meta:
#        model = login
#        fields = ['username' , 'password']

class registerform(ModelForm):
    class Meta:
        model = register
        fields = ['name' , 'email', 'enter_password' ,'re_enter_password', 'contact']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'eg. Pravin Kumar'}),
            'email': forms.TextInput(attrs={'placeholder': 'eg. pravin@gmail.com'}),
        }

class forgotform(ModelForm):
    class Meta:
        model = forgot
        fields = ['email']


class Custom_registeration_form(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email',]


class LoginForm(AuthenticationForm):
    class Meta:
		model = User
		fields = ['username', 'password',]
		
class userprofileForm(ModelForm):
    class Meta:
        model = userprofile
        fields = ['mobile', 'linkedin_id', 'picture','city', 'des'] 
		
#class UserProfileForm(ModelForm):
#    class Meta:
#		model = UserProfile
#		fields = ['mobile', 'linkedin_id',]	


class login_form(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'id': 'custom_login_username'}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'id': 'custom_login_password'}))
