#from django.conf.urls import patterns, include, url


#from django.conf.urls.defaults import *
#from django.conf.urls import patterns, url, include
from yavatmal.views import *

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from spardhamitra import settings

from django.contrib import admin
from yavatmal import views
from yavatmal.models import *
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spardhamitra.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),

    # Examples:
    #url(r'^$', home),
    #url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^admintools/', include('admin_tools.urls')),
    #(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^$', root),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^index$', views.index, name='index'),
	url(r'^login/$', login),
	url(r'^signin/$', signin),
    url(r'^logout/$', logout_page),
    url(r'^Applogout/$', Applogout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^accounts/profile/$', home),
	url(r'^myprofile/$', myprofile),
    url(r'^Dashboard/$', dashboard),
    url(r'^AppDashboard/$', Appdashboard),
    #url(r'^appear_exam/(?P<id>\d+)/$', views.appear_exam),
    url(r'^appear_exam/(?P<T_Exam_ExamID_url>\w+)/$', views.appear_exam),
    url(r'^Appappear_exam/(?P<T_Exam_ExamID_url>\w+)/$', views.Appappear_exam),
    url(r'^start_exam/(?P<T_Exam_ExamID_url>\w+)/$', views.start_exam),
    url(r'^Appstart_exam/(?P<T_Exam_ExamID_url>\w+)/$', views.Appstart_exam),
    url(r'^print/admin/yavatmal/t_exam/(?P<T_Exam_ExamID_url>\w+)/history/$', views.print_paper),
    url(r'^exam_answers/(?P<T_Exam_ExamID_url>\w+)/$', views.exam_answers),
    url(r'^Appexam_answers/(?P<T_Exam_ExamID_url>\w+)/$', views.Appexam_answers),
	url(r'^Admissions/$', Admissions),
	url(r'^Contacts/$', Contacts),
	url(r'^Courses/$', Courses),
	url(r'^Programs/$', Programs),
	url(r'^AppPrograms/$', AppPrograms),
	url(r'^Teachers/$', Teachers),
	url(r'^submit_paper$', SubmitPaper),
	url(r'^Programs/(?P<T_Exam_ExamID_url>\w+)/$', views.articles),
	(r'^ckeditor/', include('ckeditor.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
