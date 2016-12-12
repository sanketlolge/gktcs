from django.contrib import admin
from lms.models import *

# Register your models here.
class Payment_detailAdmin(admin.ModelAdmin):
	list_display = ["user", "instamojo_name", "payment_id", "date_of_payment", "payment_status", "success", "instamojo_email_id", "instamojo_contact_no", "course_selected", "course_fees", "query_url"]
	class Meta:
		model = Payment_detail
		
class userprofileAdmin(admin.ModelAdmin):
    list_display = ["user", "mobile","linkedin_id", "picture", "city", "des"]
    class Meta:
        model = userprofile	
		
class Comments_choiceInline(admin.TabularInline):
	model = Comments_choice
	extra = 1

class QuestionAdmin(admin.ModelAdmin):
	inlines = [Comments_choiceInline]		

admin.site.register(Payment_detail, Payment_detailAdmin)
admin.site.register(userprofile, userprofileAdmin)
#admin.site.register(temptest)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Comments_choice)
admin.site.register(Enquiry)
admin.site.register(Batches)
#admin.site.register(Trainer)
admin.site.register(hire)
admin.site.register(search)
admin.site.register(courses)
admin.site.register(blogs)
admin.site.register(login)
admin.site.register(register)
admin.site.register(forgot)
admin.site.register(add_instructor)
admin.site.register(Github)
admin.site.register(Python)
admin.site.register(Ruby_on_Rails)
admin.site.register(Hadoop)
admin.site.register(Data_Science)
admin.site.register(AngularJS)
admin.site.register(Java)
admin.site.register(Android)
admin.site.register(Appium)
admin.site.register(R_Programming)
admin.site.register(Django)
admin.site.register(Course)
admin.site.register(My_Course)
