from django.conf import settings
from django.contrib import messages
from django.contrib import auth
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
from lms.models import *
from registration.forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
import requests
import json
# Create your views here.

from lms.forms1 import *


@login_required
def thanks(request):
	#Instamojo stuff

	requesting_user = request.user
	request_status = request.GET.get('status')
	request_payment = request.GET.get('payment_id')
	# request_purpose = request.GET.get('purpose')
	# new_customer_payment_and_date = customer_payment_and_date(user_name = requesting_user, payment_id = request_payment, payment_status = request_status)
	# new_Customer_Payments = Customer_Payments(user_name = requesting_user, payment_id = request_payment, payment_status = request_status)
	# new_Customer_Payments.save()
	# new_customer_payment_and_date.save()
	# New stuff

	base_url = str("https://www.instamojo.com/api/1.1/payments/") + str(request_payment) + str("/?api_key=3c66e1a544a1d7b7c1d20e32a830557e&auth_token=f0d6a7756ae4115e4af7f7caecc4e0fe")
	#data = requests.get("https://www.instamojo.com/api/1.1/payments/?api_key=3c66e1a544a1d7b7c1d20e32a830557e&auth_token=f0d6a7756ae4115e4af7f7caecc4e0fe")
	data = requests.get(base_url)
	# info = json.loads(data)
	info = data.json()
	phone_number = info["payment"]["buyer_phone"]
	name = info["payment"]["buyer_name"]
	status = info["payment"]["status"]
	email = info["payment"]["buyer_email"]
	purpose = str(info["payment"]["link_title"])
	amount = info["payment"]["amount"]
	state = info["success"]
	# subscribed_course = Course.objects.get(course_name=purpose)
	subscribed_course = purpose
	#result = table.objects.filter(string__contains='pattern')
	new_Payment_details = Payment_detail(user = requesting_user, instamojo_name = name, payment_id = request_payment, payment_status = status, success = state, instamojo_email_id = email, instamojo_contact_no = phone_number, course_selected = subscribed_course, course_fees = amount, query_url = base_url)
	new_Payment_details.save()
	if state:
		try:
			mc = My_Course.objects.get(user = requesting_user)
		except:
			mc = My_Course(user = requesting_user)
			mc.save()
		if purpose == "Github":
			c = Course.objects.get(course_name = "Github")
			content_type = ContentType.objects.get_for_model(Github)
			permission = Permission.objects.get(content_type=content_type, codename='add_github')
		elif purpose == "Python":
			c = Course.objects.get(course_name = "Python")
			content_type = ContentType.objects.get_for_model(Python)
			permission = Permission.objects.get(content_type=content_type, codename='add_python')
		elif purpose == "Java":
			c = Course.objects.get(course_name = "Java")
			content_type = ContentType.objects.get_for_model(Java)
			permission = Permission.objects.get(content_type=content_type, codename='add_java')
		elif purpose == "Django":
			c = Course.objects.get(course_name = "Django")
			content_type = ContentType.objects.get_for_model(Django)
			permission = Permission.objects.get(content_type=content_type, codename='add_django')
		elif purpose == "Appium":
			c = Course.objects.get(course_name = "Appium")
			content_type = ContentType.objects.get_for_model(Appium)
			permission = Permission.objects.get(content_type=content_type, codename='add_appium')
		elif purpose == "Android":
			c = Course.objects.get(course_name = "Android")
			content_type = ContentType.objects.get_for_model(Android)
			permission = Permission.objects.get(content_type=content_type, codename='add_android')
		elif purpose == "R Programming":
			c = Course.objects.get(course_name = "R Programming")
			content_type = ContentType.objects.get_for_model(R_Programming)
			permission = Permission.objects.get(content_type=content_type, codename='add_r_programming')
		elif purpose == "Ruby On Rails":
			c = Course.objects.get(course_name = "Ruby On Rails")
			content_type = ContentType.objects.get_for_model(Ruby_on_Rails)
			permission = Permission.objects.get(content_type=content_type, codename='add_ruby_on_rails')
		elif purpose == "iOS":
			c = Course.objects.get(course_name = "iOS")
			content_type = ContentType.objects.get_for_model(IOS)
			permission = Permission.objects.get(content_type=content_type, codename='add_ios')
		elif purpose == "AngularJS":
			c = Course.objects.get(course_name = "AngularJS")
			content_type = ContentType.objects.get_for_model(AngularJS)
			permission = Permission.objects.get(content_type=content_type, codename='add_angularjs')
		elif purpose == "Data Science":
			c = Course.objects.get(course_name = "Data Science")
			content_type = ContentType.objects.get_for_model(Data_Science)
			permission = Permission.objects.get(content_type=content_type, codename='add_data_science')
		else:
			c = Course.objects.get(course_name = "Hadoop")
			content_type = ContentType.objects.get_for_model(Hadoop)
			permission = Permission.objects.get(content_type=content_type, codename='add_hadoop')

	# def Github():
	# 	content_type = ContentType.objects.get_for_model(Github)
	# 	permission = Permission.objects.get(content_type=content_type, codename='add_github')
	# def Python():
	# 	content_type = ContentType.objects.get_for_model(Python)
	# 	permission = Permission.objects.get(content_type=content_type, codename='add_python')
	# def f(x):
	# 	return {"Python": Python(), "Github": Github()}[x]
	# f(purpose)
	mc.courses_enrolled.add(c)
	requesting_user.user_permissions.add(permission)
	context = {
	 "requesting_user":requesting_user,
	 "request_payment":request_payment,
	 "request_status":request_status,
	 "request_purpose":purpose,
	 "base_url": base_url,
	 "info": info,
	 "data": data,
	 "base_url": base_url,
	 "phone_number": phone_number,
	 "name": name,
	 "state": state,
	 "status": status,
	 "email": email,
	 "purpose": purpose,
	 "amount": amount,
	 }
	return render(request, 'thanks.html', context)

def post_question(request):
	form = QuestionForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			question = form.cleaned_data.get("question")
			form.save()
			return HttpResponseRedirect("/")
	else:
		form = QuestionForm(request.POST or None)
	return render(request, "post_question.html", {"form":form})


def post_comment(request):
	quest = request.POST.get('question')
	comm = request.POST.get('comment')
	quest_save = Question.objects.get(question=quest)
	new_Comments_choice = Comments_choice(question=quest_save, comment=comm)
	new_Comments_choice.save()
	return HttpResponseRedirect("/")
	
def detail(request, question_id):
 	cc = request.GET.get("cc")
 	uid = request.GET.get("uid")
 	vote = request.GET.get("vote")
 	try:
 	    comment = Comments_choice.objects.get(pk=cc)
 	    likes = comment.up_vote
 	    dislikes = comment.down_vote
 	    cve = comment.votes.exists(uid)
 	    if not cve:
 	 	    if vote=="True":
 	 	    	comment.up_vote = likes + 1
 	 	    	comment.total_vote += 1
 	 	    	comment.save()
 	 	    	comment.votes.up(uid)
 	 	    elif vote=="False":
 	 	    	comment.votes.up(uid)
 	 	    	comment.total_vote += 1
 	 	    	comment.down_vote = dislikes - 1
 	 	    	comment.save()
 	except:
 		comment = ""
 	question = Question.objects.get(pk=question_id)
 	return render(request, "detail.html", {"question":question, "cc":cc})	
	
def send_python_file(request):

    import os, tempfile, zipfile
    from django.core.servers.basehttp import FileWrapper
    from django.conf import settings
    import mimetypes

    filename = "/home/gktcs/public_html/GLMS/public/static/Python.pdf" # Select your file here.
    download_name ="Python.pdf"
    wrapper = FileWrapper(open(filename))
    content_type = mimetypes.guess_type(filename)[0]
    response = HttpResponse(wrapper,content_type=content_type)
    response['Content-Length']      = os.path.getsize(filename)    
    response['Content-Disposition'] = "attachment; filename=%s"%download_name
    return response
	
def send_hadoop_file(request):

    import os, tempfile, zipfile
    from django.core.servers.basehttp import FileWrapper
    from django.conf import settings
    import mimetypes

    filename = "/home/gktcs/public_html/GLMS/public/static/Hadoop.pdf" # Select your file here.
    download_name ="BigData&Hadoop.pdf"
    wrapper = FileWrapper(open(filename))
    content_type = mimetypes.guess_type(filename)[0]
    response = HttpResponse(wrapper,content_type=content_type)
    response['Content-Length']      = os.path.getsize(filename)    
    response['Content-Disposition'] = "attachment; filename=%s"%download_name
    return response	
	
def send_ruby_file(request):

    import os, tempfile, zipfile
    from django.core.servers.basehttp import FileWrapper
    from django.conf import settings
    import mimetypes

    filename = "/home/gktcs/public_html/GLMS/public/static/ruby.pdf" # Select your file here.
    download_name ="Ruby On Rails.pdf"
    wrapper = FileWrapper(open(filename))
    content_type = mimetypes.guess_type(filename)[0]
    response = HttpResponse(wrapper,content_type=content_type)
    response['Content-Length']      = os.path.getsize(filename)    
    response['Content-Disposition'] = "attachment; filename=%s"%download_name
    return response	

def send_angularjs_file(request):

    import os, tempfile, zipfile
    from django.core.servers.basehttp import FileWrapper
    from django.conf import settings
    import mimetypes

    filename = "/home/gktcs/public_html/GLMS/public/static/angularjs.pdf" # Select your file here.
    download_name ="AngularJS.pdf"
    wrapper = FileWrapper(open(filename))
    content_type = mimetypes.guess_type(filename)[0]
    response = HttpResponse(wrapper,content_type=content_type)
    response['Content-Length']      = os.path.getsize(filename)    
    response['Content-Disposition'] = "attachment; filename=%s"%download_name
    return response	
def send_android_file(request):

    import os, tempfile, zipfile
    from django.core.servers.basehttp import FileWrapper
    from django.conf import settings
    import mimetypes

    filename = "/home/gktcs/public_html/GLMS/public/static/android.pdf" # Select your file here.
    download_name ="Android.pdf"
    wrapper = FileWrapper(open(filename))
    content_type = mimetypes.guess_type(filename)[0]
    response = HttpResponse(wrapper,content_type=content_type)
    response['Content-Length']      = os.path.getsize(filename)    
    response['Content-Disposition'] = "attachment; filename=%s"%download_name
    return response	

def send_data_science_file(request):

    import os, tempfile, zipfile
    from django.core.servers.basehttp import FileWrapper
    from django.conf import settings
    import mimetypes

    filename = "/home/gktcs/public_html/GLMS/public/static/data_science.pdf" # Select your file here.
    download_name ="Data Science.pdf"
    wrapper = FileWrapper(open(filename))
    content_type = mimetypes.guess_type(filename)[0]
    response = HttpResponse(wrapper,content_type=content_type)
    response['Content-Length']      = os.path.getsize(filename)    
    response['Content-Disposition'] = "attachment; filename=%s"%download_name
    return response	
	
def send_r_prog_file(request):

    import os, tempfile, zipfile
    from django.core.servers.basehttp import FileWrapper
    from django.conf import settings
    import mimetypes

    filename = "/home/gktcs/public_html/GLMS/public/static/r_prog.pdf" # Select your file here.
    download_name ="R Programming.pdf"
    wrapper = FileWrapper(open(filename))
    content_type = mimetypes.guess_type(filename)[0]
    response = HttpResponse(wrapper,content_type=content_type)
    response['Content-Length']      = os.path.getsize(filename)    
    response['Content-Disposition'] = "attachment; filename=%s"%download_name
    return response		
	
def send_appium_file(request):

    import os, tempfile, zipfile
    from django.core.servers.basehttp import FileWrapper
    from django.conf import settings
    import mimetypes

    filename = "/home/gktcs/public_html/GLMS/public/static/appium.pdf" # Select your file here.
    download_name ="Appium.pdf"
    wrapper = FileWrapper(open(filename))
    content_type = mimetypes.guess_type(filename)[0]
    response = HttpResponse(wrapper,content_type=content_type)
    response['Content-Length']      = os.path.getsize(filename)    
    response['Content-Disposition'] = "attachment; filename=%s"%download_name
    return response			

@login_required
def myprofileview(request, user_id, template_name='myprofile.html'):
    u = userprofile.objects.all()
    try:
        if request.user.is_superuser:
            up = get_object_or_404(userprofile, user_id=user_id)
        else:
            up = get_object_or_404(userprofile, user_id=user_id, user=request.user)   
    except:
        up = userprofile(user=request.user)    
    form = userprofileForm(request.POST or None, instance=up)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.picture = request.FILES.get('picture', save_it.picture)
        save_it.save()
    return render(request, template_name, {'form':form})
	
def search_titles(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
    course = courses.objects.filter(course_name__contains=search_text.title())
    return render(request, "ajax_search.html", {"course": course})	
	
def courseview(request):
    course = courses.objects.all()
    return render(request, 'course.html', locals(), context_instance=RequestContext(request))

# def mycoursesview(request):
    # course = courses.objects.filter(id__in=[20, 25, 30, 40])
    # return render(request, 'mycourses.html', locals(), context_instance=RequestContext(request))

@login_required
def mycoursesview(request):
    user = request.user
    user_courses = My_Course.objects.filter(user=user)
    type_user_courses = str(type(user_courses))
    context = {"user_courses":user_courses, "type_user_courses":type_user_courses}
    return render(request, 'mycourses.html', context)	
#@login_required
#def mypythonview(request):
#    course = courses.objects.filter(id=20)
#    return render(request, 'mypython.html', locals(), context_instance=RequestContext(request))	
	
@login_required
def mydjangoview(request):
    course = courses.objects.filter(id=20)
    return render(request, 'mydjango.html', locals(), context_instance=RequestContext(request))	

# @login_required
# def myhadoopview(request):
    # return render(request, 'myhadoop.html', locals(), context_instance=RequestContext(request))

# @login_required
# def myrubyonrailsview(request):
    # return render(request, 'myrubyonrails.html', locals(), context_instance=RequestContext(request))
	

# def mydatascienceview(request):
    # return render(request, 'mydatascience.html', locals(), context_instance=RequestContext(request))	

# def myangularjsview(request):
    # return render(request, 'myangularjs.html', locals(), context_instance=RequestContext(request))

# def myjavaview(request):
    # return render(request, 'myjava.html', locals(), context_instance=RequestContext(request))

# def myiosview(request):
    # return render(request, 'myios.html', locals(), context_instance=RequestContext(request))

# def myandroidview(request):
    # return render(request, 'myandroid.html', locals(), context_instance=RequestContext(request))
	
# def myrprogrammingview(request):
    # return render(request, 'myrprogramming.html', locals(), context_instance=RequestContext(request))

# def myappiumview(request):
    # return render(request, 'myappium.html', locals(), context_instance=RequestContext(request))	
	
@login_required
@permission_required('lms.add_python')
def mypythonview(request):
	context = Python.objects.all()
	return render(request, 'mypython.html', {"context": context})

@login_required
@permission_required('lms.add_r_programming')
def myrprogrammingview(request):
	context = R_Programming.objects.all()
	return render(request, 'myrprogramming.html', {"context": context})


@login_required
@permission_required('lms.add_appium')
def myappiumview(request):
	context = Appium.objects.all()
	return render(request, 'myappium.html', {"context": context})


@login_required
@permission_required('lms.add_android', raise_exception=True)
def myandroidview(request):
	context = Android.objects.all()
	return render(request, 'myandroid.html', {"context": context})


@login_required
@permission_required('lms.add_ruby_on_rails')
def myrubyonrailsview(request):
	context = Ruby_on_Rails.objects.all()
	return render(request, 'myrubyonrails.html', {"context": context})


@login_required
@permission_required('lms.add_ios')
def myiosview(request):
	context = IOS.objects.all()
	return render(request, 'myios.html', {"context": context})


@login_required
@permission_required('lms.add_java', login_url='/java/')
def myjavaview(request):
	context = Java.objects.all()
	return render(request, 'myjava.html', {"context": context})


@login_required
@permission_required('lms.add_data_science')
def mydatascienceview(request):
	context = Data_Science.objects.all()
	return render(request, 'mydatascience.html', {"context": context})


@login_required
@permission_required('lms.add_angularjs')
def myangularjsview(request):
	context = AngularJS.objects.all()
	return render(request, 'myangularjs.html', {"context": context})


@login_required
@permission_required('lms.add_hadoop')
def myhadoopview(request):
	context = Hadoop.objects.all()
	return render(request, 'myhadoop.html', {"context": context})	

def baseview(request):
    template = "base.html"
    if request.method == "POST":
        form = Enquiryform(request.POST or None)
        if form.is_valid():
            save_it=form.save(commit=False)
            save_it.save()
            name = form.cleaned_data.get("Name")
            email = form.cleaned_data.get("Email")
            contact = form.cleaned_data.get("Contact")
            message = form.cleaned_data.get("Message")

            subject = 'enquiry'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,email]
            contact_message = " Name: %s Message: %s via Contact No.: %d Email Id: %s"%(name,message,contact,email)
            send_mail(subject,contact_message,from_email,to_email,fail_silently=True)
        else:
            form = Enquiryform(request.POST or None)
    else:
        form = Enquiryform(request.POST or None)

        #send mail
        #subject = 'thanku you'
        #Message = 'welcome to gktcs'
        #from_email = save_it.Email
        #to_list = [settings.EMAIL_HOST_USER]
        #send_mail(subject, message, from_email, to_list, fail_silently = True)

    #return render_to_response("home2.html",
    #                          locals(),
    #                          context_instance=RequestContext(request))


    if request.method == "POST":
        form1 = login_form(request.POST or None)
        if form1.is_valid():
            instance = form1
            username = instance.cleaned_data.get("username")
            password = instance.cleaned_data.get("password")

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.info(request, "Logged in Successfully!!")
                return HttpResponseRedirect('/home')
            else:
                messages.info(request, "Logged in Fail!!")			
                return HttpResponseRedirect('/home')
    else:
        form1 = login_form(request.POST or None)


    form2 = Custom_registeration_form(request.POST or None)
    if form2.is_valid():
        form2.save(commit=True)
        messages.info(request, "Registered Successfully!!")

    context = {"form": form, "form1": form1, "form2": form2}
    return render(request, template, context)


def instructor_addview(request):
    form = trainerform(request.POST or None)
    form.fields['linkedin_profile'].required = False
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.info(request, "Thank You. We will get back to you shortly")
    return render_to_response("instructor_add.html",
                              locals(),
                              context_instance=RequestContext(request))

def htmlcourse(request):
    batch = Batches.objects.all()
    return render_to_response('HTML5Courses.html',locals())


def Aboutusview(request):
    return render(request, 'Aboutus.html', locals(), context_instance=RequestContext(request))	

def Corporateview(request):
    form = trainerform(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    return render_to_response("Corporate.html",
                              locals(),
                              context_instance=RequestContext(request))

def enrollview(request):
    form = enrollform(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        subject = "Thank You for Registration"
        message = "Welcome to Gktcs Lms"
        from_email = settings.EMAIL_HOST_USER
        to_list = [save_it.email,settings.EMAIL_HOST_USER]
        send_mail(subject,message,from_email,to_list,fail_silently = True)
        messages.success(request,'Thank u for Enrollment, we will get back to you shortly' )

    return render_to_response("enroll.html",
                              locals(),
                              context_instance=RequestContext(request))



def html5view(request):
    batch = Batches.objects.all()
    return render_to_response('HTML5Courses.html',locals())

def css3view(request):
    batch = Batches.objects.all()
    return render_to_response('CSS3Courses.html',locals())

def javascriptview(request):
    batch = Batches.objects.all()
    return render_to_response('JavaScriptCourses.html',locals())

def jqueryview(request):
    batch = Batches.objects.all()
    return render_to_response('JQueryCourses.html',locals())

def angularjsview(request):
    batch = Batches.objects.all()
    return render(request, 'AngularJS.html', locals(), context_instance=RequestContext(request))	

def bootstrapview(request):
    batch = Batches.objects.all()
    return render_to_response('Bootstrap.html',locals())

def apacheview(request):
    batch = Batches.objects.all()
    return render_to_response('ApacheTomcat.html',locals())

def djangoview(request):
    batch = Batches.objects.all()
    return render_to_response('Django.html',locals())

def hadoopview(request):
    batch = Batches.objects.all()
    return render(request, 'Hadoop.html', locals(), context_instance=RequestContext(request))
	
def javaview(request):
    batch = Batches.objects.all()
    return render(request, 'Java.html', locals(), context_instance=RequestContext(request))	

def mongodbview(request):
    batch = Batches.objects.all()
    return render_to_response('Mongodb.html',locals())

def mysqlview(request):
    batch = Batches.objects.all()
    return render_to_response('Mysql.html',locals())

def redhatview(request):
    batch = Batches.objects.all()
    return render_to_response('Redhat.html',locals())

def rubyonrailsview(request):
    batch = Batches.objects.all()
    return render(request, 'Rubyonrails.html', locals(), context_instance=RequestContext(request))	

def wordpressview(request):
    batch = Batches.objects.all()
    return render_to_response('Wordpress.html',locals())

def androidview(request):
    batch = Batches.objects.all()
    return render(request, 'Android.html', locals(), context_instance=RequestContext(request))	

def iosview(request):
    batch = Batches.objects.all()
    return render(request, 'Ios.html', locals(), context_instance=RequestContext(request))	

def phonegapview(request):
    batch = Batches.objects.all()
    return render_to_response('phonegap.html',locals())

def jqmobview(request):
    batch = Batches.objects.all()
    return render_to_response('jqmob.html',locals())

def mdotnetview(request):
    batch = Batches.objects.all()
    return render_to_response('Mdotnet.html',locals())

def csharpview(request):
    batch = Batches.objects.all()
    return render_to_response('Csharp.html',locals())

def mvcview(request):
    batch = Batches.objects.all()
    return render_to_response('Mvc.html',locals())



def Blogsview(request):
    b = blogs.objects.all()
    return render(request, 'blogs.html', locals(), context_instance=RequestContext(request))	

def contactview(request):
    return render(request, 'contactus.html', locals(), context_instance=RequestContext(request))	

def index(request):
    return render_to_response("index2.html")


def helo(request):
    return HttpResponse("helloe world")


def homeview(request):
    template = "home2.html"
    if request.method == "POST":
        form = Enquiryform(request.POST or None)
        if form.is_valid():
            save_it=form.save(commit=False)
            save_it.save()
            name = form.cleaned_data.get("Name")
            email = form.cleaned_data.get("Email")
            contact = form.cleaned_data.get("Contact")
            message = form.cleaned_data.get("Message")

            subject = 'enquiry'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,email]
            contact_message = " Name: %s Message: %s via Contact No.: %d Email Id: %s"%(name,message,contact,email)
            send_mail(subject,contact_message,from_email,to_email,fail_silently=True)
        else:
            form = Enquiryform(request.POST or None)
    else:
        form = Enquiryform(request.POST or None)

        #send mail
        #subject = 'thanku you'
        #Message = 'welcome to gktcs'
        #from_email = save_it.Email
        #to_list = [settings.EMAIL_HOST_USER]
        #send_mail(subject, message, from_email, to_list, fail_silently = True)

    #return render_to_response("home2.html",
    #                          locals(),
    #                          context_instance=RequestContext(request))


    if request.method == "POST":
        form1 = login_form(request.POST or None)
        if form1.is_valid():
            instance = form1
            username = instance.cleaned_data.get("username")
            password = instance.cleaned_data.get("password")

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.info(request, "Logged in Successfully!!")
                return HttpResponseRedirect('/home')
            else:
                messages.info(request, "Login and Password does not match")			
                return HttpResponseRedirect('/home')
    else:
        form1 = login_form(request.POST or None)


    form2 = Custom_registeration_form(request.POST or None)
    if form2.is_valid():
        form2.save(commit=True)
        messages.info(request, "Registered Successfully!!")

    context = {"form": form, "form1": form1, "form2": form2}
    return render(request, template, context)



def hireview(request): # to insert the data
    form =  hireform(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    return render_to_response("hire.html",
                              locals(),
                              context_instance=RequestContext(request))


def batchview(request): # to fetch the data frm database
    batch=Batches.objects.all()
    return render_to_response('Batches.html',locals())




def searchfrmview(request):
    return render_to_response("searchfrm.html")

def searchview(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
	r = q.title()
        course = courses.objects.filter(course_name__contains=r)
    return render(request, 'search.html', locals(), context_instance=RequestContext(request))

def pythonview(request):
    return render(request, 'python.html', locals(), context_instance=RequestContext(request))	

def datascienceview(request):
    return render(request, 'datascience.html', locals(), context_instance=RequestContext(request))	

def webdevelopview(request):
    return render_to_response('webdevelop.html',locals())

def privacyview(request):
    return render(request, 'privacy.html', locals(), context_instance=RequestContext(request))	

def termsview(request):
    return render(request, 'terms.html', locals(), context_instance=RequestContext(request))	

def tempview(request):
    return render_to_response("temp.html")

#def loginview(request):
#    form = loginform(request.POST or None)
#    if form.is_valid():
#        save_it = form.save(commit=False)
#        save_it.save()
#    return render_to_response("login.html",
#                              locals(),
#                              context_instance=RequestContext(request))

def loginview(request):
    template = "login.html"
    if request.method == "POST":
        form = login_form(request.POST or None)
        context = {"form": form}
        if form.is_valid():
            instance = form
            username = instance.cleaned_data.get("username")
            password = instance.cleaned_data.get("password")

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/home')
            else:
                return HttpResponseRedirect('/invalid')
    else:
        form = login_form(request.POST or None)
        context = {"form": form}
    return render(request, template, context)

def registerview(request):
    return render_to_response("register.html")

#def registerview(request):
#    form = registerform(request.POST or None)
#    if form.is_valid():
#        save_it = form.save(commit=False)
#        save_it.save()
#    return render_to_response("register.html",
#                              locals(),
#                              context_instance=RequestContext(request))

def forgotview(request):
    form = forgotform(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    return render_to_response("forgot.html",
                              locals(),
                              context_instance=RequestContext(request))


def test_formView(request):
    form1 = LoginForm(request.POST or None)
    form2 = Custom_registeration_form(request.POST or None)
    context = {"form1": form1, "form2": form2}
    return render(request, 'test_form.html', context)
