from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings

# Create your models here.
class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.BigIntegerField(blank=True, null=True)
    linkedin_id = models.CharField(max_length=60, blank=True)
    picture = models.ImageField(upload_to = 'placement', default= 'placement/default_pic.jpg', blank=True, null=True)
    city = models.CharField(max_length=15, blank=True) 	
    des = models.TextField(blank=True)
    
    def get_absolute_url(self):
        return reverse('myprofile', kwargs={'user_id': self.request.user.pk})
		
class courses(models.Model):
    course_name = models.CharField(max_length=50)
    course_desc = models.TextField()
    course_url = models.CharField(max_length=200)
    mycourse_url = models.CharField(max_length=200, null=True)    
    course_img_url = models.CharField(max_length=200)

    def __unicode__(self):
        return self.course_name	

class Question(models.Model):
	question = models.TextField()
	def __unicode__(self):
		return self.question

class Comments_choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	comment = models.CharField(max_length=200)
	up_vote = models.IntegerField(default=0)
	down_vote = models.IntegerField(default=0)
	total_vote = models.IntegerField(default=0)
	def __unicode__(self):
		return self.comment		

class Course(models.Model):
    course_name = models.CharField(max_length=30, primary_key = True)
    course_description = models.TextField(null=True, blank=True)
    course_url = models.CharField(max_length=200, null=True, blank=True)
    mycourse_url = models.CharField(max_length=200, null=True)
    course_img_url = models.CharField(max_length=200, null=True, blank=True)
    def __unicode__(self):
        return self.course_name

class My_Course(models.Model):
    user = models.ForeignKey(User)
    courses_enrolled = models.ManyToManyField(Course)
    def course_names(self):
        courses = ', '.join([c.course_name for c in self.courses_enrolled.all()])
        return courses
    def __unicode__(self):
        return str(self.user)
	

class Enquiry(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Message = models.TextField()
    Contact = models.BigIntegerField()

    def __unicode__(self):
        return self.Name


class Batches(models.Model):
    Start = models.CharField(max_length=200)
    Duration = models.CharField(max_length=30)
    Days = models.CharField(max_length=20)
    Time  = models.TimeField()
    Price = models.IntegerField()

    def __unicode__(self):
        return self.Start

class Trainer(models.Model):
    name = models.CharField(max_length=200)
    contactno = models.BigIntegerField()
    Email = models.EmailField()
    skills = models.CharField(max_length=20)
    aboutCourse = models.CharField(max_length=100)
    about_ourself = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class hire(models.Model):
    job_title = models.CharField(max_length=200)
    vaccancies = models.IntegerField(default=0)
    job_description = models.CharField(max_length=20)
    Desired_profile = models.CharField(max_length=20)
    Experience = models.IntegerField()
    salary = models.IntegerField()
    location = models.CharField(max_length=200)
    company_name = models.CharField(max_length=20)
    person_name = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    Email = models.EmailField()
    companyurl = models.CharField(max_length=200)


    def __unicode__(self):
        return self.job_title

class search(models.Model):
    s=models.CharField(max_length=20)




class blogs(models.Model):
    blog_writer = models.CharField(max_length=40)
    blog_title = models.CharField(max_length=150)
    blog_content = models.TextField()
    blog_date = models.DateTimeField()

    def __unicode__(self):
        return self.blog_title

class login(models.Model):
    username = models.EmailField()
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username

class register(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    enter_password = models.CharField(max_length=50)
    re_enter_password = models.CharField(max_length=50)
    contact = models.BigIntegerField()

    def __unicode__(self):
        return self.name

class forgot(models.Model):
    email =  models.EmailField()

    def __unicode__(self):
        return self.email


class add_instructor(models.Model):
    f_name = models.CharField(max_length = 50)
    l_name = models.CharField(max_length = 50)
    mobile = models.BigIntegerField()
    email = models.EmailField()
    course_name = models.CharField(max_length = 100)
    linkedin_profile = models.CharField(max_length = 100, blank=True, null=True)
    about_course = models.TextField(max_length = 150)
    about_yourself = models.TextField(max_length = 150)

    def __unicode__(self):
        return self.f_name
		
class Github(models.Model):
	topic = models.CharField(max_length=400)
	description = models.TextField()
	Difficulty = (("Easy","Easy"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced"))
	difficulty = models.CharField(max_length=12, choices=Difficulty, null=True)
	notes = models.FileField(upload_to="notes/", null=True, blank=True)
	video_link = models.URLField(null=True, blank=True)
	def __unicode__(self):
		return self.topic
	class Meta:
		permissions = (('is_subscribed', "is subscribed"),)

class Python(models.Model):
	topic = models.CharField(max_length=400)
	description = models.TextField()
	Difficulty = (("Easy","Easy"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced"))
	difficulty = models.CharField(max_length=12, choices=Difficulty, null=True)
	notes = models.FileField(upload_to="notes/", null=True, blank=True)
	video_link = models.URLField(null=True, blank=True)
	def __unicode__(self):
		return self.topic
	class Meta:
		permissions = (('is_subscribed', "is subscribed"),)

class Ruby_on_Rails(models.Model):
	topic = models.CharField(max_length=400)
	description = models.TextField()
	Difficulty = (("Easy","Easy"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced"))
	difficulty = models.CharField(max_length=12, choices=Difficulty, null=True)
	notes = models.FileField(upload_to="notes/", null=True, blank=True)
	video_link = models.URLField(null=True, blank=True)
	def __unicode__(self):
		return self.topic
	class Meta:
		permissions = (('is_subscribed', "is subscribed"),)


class Hadoop(models.Model):
	topic = models.CharField(max_length=400)
	description = models.TextField()
	Difficulty = (("Easy","Easy"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced"))
	difficulty = models.CharField(max_length=12, choices=Difficulty, null=True)
	notes = models.FileField(upload_to="notes/", null=True, blank=True)
	video_link = models.URLField(null=True, blank=True)
	def __unicode__(self):
		return self.topic
	class Meta:
		permissions = (('is_subscribed', "is subscribed"),)

class Data_Science(models.Model):
	topic = models.CharField(max_length=400)
	description = models.TextField()
	Difficulty = (("Easy","Easy"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced"))
	difficulty = models.CharField(max_length=12, choices=Difficulty, null=True)
	notes = models.FileField(upload_to="notes/", null=True, blank=True)
	video_link = models.URLField(null=True, blank=True)
	def __unicode__(self):
		return self.topic
	class Meta:
		permissions = (('is_subscribed', "is subscribed"),)


class AngularJS(models.Model):
	topic = models.CharField(max_length=400)
	description = models.TextField()
	Difficulty = (("Easy","Easy"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced"))
	difficulty = models.CharField(max_length=12, choices=Difficulty, null=True)
	notes = models.FileField(upload_to="notes/", null=True, blank=True)
	video_link = models.URLField(null=True, blank=True)
	def __unicode__(self):
		return self.topic
	class Meta:
		permissions = (('is_subscribed', "is subscribed"),)

class Java(models.Model):
	topic = models.CharField(max_length=400)
	description = models.TextField()
	Difficulty = (("Easy","Easy"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced"))
	difficulty = models.CharField(max_length=12, choices=Difficulty, null=True)
	notes = models.FileField(upload_to="notes/", null=True, blank=True)
	video_link = models.URLField(null=True, blank=True)
	def __unicode__(self):
		return self.topic
	class Meta:
		permissions = (('is_subscribed', "is subscribed"),)


class Android(models.Model):
	topic = models.CharField(max_length=400)
	description = models.TextField()
	Difficulty = (("Easy","Easy"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced"))
	difficulty = models.CharField(max_length=12, choices=Difficulty, null=True)
	notes = models.FileField(upload_to="notes/", null=True, blank=True)
	video_link = models.URLField(null=True, blank=True)
	def __unicode__(self):
		return self.topic
	class Meta:
		permissions = (('is_subscribed', "is subscribed"),)

class Appium(models.Model):
	topic = models.CharField(max_length=400)
	description = models.TextField()
	Difficulty = (("Easy","Easy"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced"))
	difficulty = models.CharField(max_length=12, choices=Difficulty, null=True)
	notes = models.FileField(upload_to="notes/", null=True, blank=True)
	video_link = models.URLField(null=True, blank=True)
	def __unicode__(self):
		return self.topic
	class Meta:
		permissions = (('is_subscribed', "is subscribed"),)


class R_Programming(models.Model):
	topic = models.CharField(max_length=400)
	description = models.TextField()
	Difficulty = (("Easy","Easy"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced"))
	difficulty = models.CharField(max_length=12, choices=Difficulty, null=True)
	notes = models.FileField(upload_to="notes/", null=True, blank=True)
	video_link = models.URLField(null=True, blank=True)
	def __unicode__(self):
		return self.topic
	class Meta:
		permissions = (('is_subscribed', "is subscribed"),)

class Django(models.Model):
	topic = models.CharField(max_length=400)
	description = models.TextField()
	Difficulty = (("Easy","Easy"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced"))
	difficulty = models.CharField(max_length=12, choices=Difficulty, null=True)
	notes = models.FileField(upload_to="notes/", null=True, blank=True)
	video_link = models.URLField(null=True, blank=True)
	def __unicode__(self):
		return self.topic
	class Meta:
		permissions = (('is_subscribed', "is subscribed"),)				
		
class IOS(models.Model):
	topic = models.CharField(max_length=400)
	description = models.TextField()
	Difficulty = (("Easy","Easy"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced"))
	difficulty = models.CharField(max_length=12, choices=Difficulty, null=True)
	notes = models.FileField(upload_to="notes/", null=True, blank=True)
	video_link = models.URLField(null=True, blank=True)
	def __unicode__(self):
		return self.topic
	class Meta:
		permissions = (('is_subscribed', "is subscribed"),)


class Payment_detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instamojo_name = models.CharField(max_length=50)
    payment_id = models.CharField(max_length=40, unique=True)
    date_of_payment = models.DateTimeField(auto_now_add = True, auto_now = False)
    payment_status = models.CharField(max_length=20, default="payable")
    success = models.BooleanField(default = False)
    instamojo_email_id = models.EmailField()
    instamojo_contact_no = models.BigIntegerField()
    # course_selected = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_selected = models.CharField(max_length=50)
    course_fees = models.CharField(max_length=50)
    query_url = models.URLField(default="https://www.instamojo.com/api/1.1/payments/")

    def __unicode__(self):
        return self.payment_id
	
