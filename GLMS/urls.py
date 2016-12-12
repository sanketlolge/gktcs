from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from lms.views import *



urlpatterns = [
    # Examples:
    # url(r'^$', 'GLMS.views.home', name='home'),

            url(r'^admin/', include(admin.site.urls)),
            url(r'^About/',Aboutusview,name="Aboutus"),
			url(r'^base/',baseview,name="base"),
			url(r'^question/(?P<question_id>[0-9]+)$', detail, name='detail'),
			url(r'^post_question/$', post_question, name='post_question'),
			url(r'^post_comment/$', post_comment, name='post_comment'),
            url(r'^courses/',courseview,name="Courses"),
			url(r'^myprofile/(?P<user_id>\d+)$', myprofileview, name="myprofile"),
			url(r'^mycourses/',mycoursesview,name="mycourses"),
			url(r'^mypython/',mypythonview,name="mypython"),
			url(r'^mydjango111/',mydjangoview,name="mydjango"),
			url(r'^myhadoop/',myhadoopview,name="myhadoop"),
			url(r'^myrubyonrails/',myrubyonrailsview,name="myrubyonrails"),
			url(r'^mydatascience/',mydatascienceview,name="mydatascience"),
			url(r'^myangularjs/',myangularjsview,name="myangularjs"),
			url(r'^myjava/',myjavaview,name="myjava"),
			url(r'^myios/',myiosview,name="myios"),
			url(r'^myandroid/',myandroidview,name="myandroid"),
			url(r'^myrprogramming/',myrprogrammingview,name="myrprogramming"),
			url(r'^myappium/',myappiumview,name="myappium"),
            url(r'^html5/',htmlcourse),
            url(r'^trainer/',Corporateview,name="CT"),
			url(r'^instructor/add/',instructor_addview,name="instructor_add"),
            url(r'^contact/',contactview,name="contact"),
            url(r'^hire/',hireview,name="hire"),
            url(r'^terms/',termsview,name="terms"),
            url(r'^blogs/',Blogsview,name="blog"),
            url(r'^html5/',html5view,name="html5"),
            url(r'^css3/',css3view,name="css3"),
            url(r'^javascript/',javascriptview,name="javascript"),
            url(r'^jquery/',jqueryview,name="jquery"),
            url(r'^angularjs/',angularjsview,name="angularjs"),
            url(r'^bootstrap/',bootstrapview,name="bootstrap"),
            url(r'^apachetomcat/',apacheview,name="apachetomcat"),
            url(r'^django/',djangoview,name="django"),
            url(r'^hadoop/',hadoopview,name="hadoop"),
            url(r'^java/',javaview,name="java"),
            url(r'^mongodb/',mongodbview,name="mongodb"),
            url(r'^mysql/',mysqlview,name="mysql"),
            url(r'^redhat/',redhatview,name="redhat"),
            url(r'^rubyonrails/',rubyonrailsview,name="rubyonrails"),
            url(r'^wordpress/',wordpressview,name="wordpress"),
            url(r'^android/',androidview,name="android"),
			url(r'^datascience/',datascienceview,name="datascience"),
			url(r'^webdevelop/',webdevelopview,name="webdevelop"),
            url(r'^ios/',iosview,name="ios"),
            url(r'^jqmob/',jqmobview,name="jqmob"),
            url(r'^phonegap/',phonegapview,name="phonegap"),
            url(r'^mdotnet/',mdotnetview,name="mdotnet"),
            url(r'^csharp/',csharpview,name="csharp"),
            url(r'^mvc/',mvcview,name="mvc"),
            url(r'^searchfrm/',searchfrmview,name="search2"),
            url(r'^search2/',searchview,name="search2"),
            url(r'^Index/',index,name="index1"),
            url(r'^Enroll/',enrollview,name="enroll"),
            url(r'^python/',pythonview,name="python"),
            url(r'^privacy/',privacyview,name="privacy"),
            url(r'^login/',loginview,name="login"),
			url(r'^temp/',tempview),
            url(r'^register/',registerview,name="register"),
            url(r'^forgot/',forgotview,name="forgot"),
            url(r'^test_form/',test_formView,name="test_form"),
			url(r'^python.pdf', send_python_file),
			url(r'^hadoop.pdf', send_hadoop_file),
			url(r'^ruby.pdf', send_ruby_file),
			url(r'^angularjs.pdf', send_angularjs_file),
			url(r'^android.pdf', send_android_file),
			url(r'^data_science.pdf', send_data_science_file),
			url(r'^r_prog.pdf', send_r_prog_file),
			url(r'^appium.pdf', send_appium_file),
			url(r'^search/', search_titles,name="search"),
			url(r'^thanks/$', 'lms.views.thanks', name='thanks'),


            #redux
            url(r'^accounts/', include('registration.backends.default.urls')),
			url(r'^home2/',homeview,name="home2"),
			url(r'',homeview,name="home"),
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
