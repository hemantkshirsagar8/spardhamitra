from django.shortcuts import render
from yavatmal.models import *
from yavatmal.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from django.views.generic.list import ListView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

#from django.utils import simplejson
import socket
from django.http import *
import json
import datetime







from django.views.decorators.cache import never_cache

# Create your views here.
def index(request):
	items = User.objects.order_by("-FirstName")
	#now = datetime.datetime.now()
	#return render(request, 'portfolio/index.html', {"items": items})Commented on 21/03/2015
	return render(request,'site/index.html',{"items": items})

#def home(request):
#	#items = User.objects.order_by("-FirstName")
#	#now = datetime.datetime.now()
#	#return render(request, 'portfolio/index.html', {"items": items})Commented on 21/03/2015
#	return render(request,'site/home.html')

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],

            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email'],
            first_name=form.cleaned_data['UserName'],
            last_name=form.cleaned_data['LastName']
            #date_of_birth=form.cleaned_data['dateofbirth']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'registration/register.html',
    variables,
    )

def register_success(request):
    return render_to_response(
    'registration/success.html',
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def Applogout_page(request):
    logout(request)
    return HttpResponseRedirect('/signin')

@login_required
def home(request):
    return HttpResponseRedirect('http://www.hemantkshirsagar.in/Dashboard/')
    #return render_to_response(
    #'home.html',Commented on 21/03/2015
	#'site/Dashboard.html',
    #{ 'user': request.user }
    #)
@login_required
def myprofile(request):
    return render_to_response(
    'myprofile.html',
    { 'user': request.user}
    )
@login_required
def dashboard(request):

    context = RequestContext(request)


    notification_list = T_Notifications.objects.filter(Status__iexact = 'Active').order_by('-id')[:5]
    user_list = User.objects.get(username__iexact=request.user.username)
    exam_list = T_Exam.objects.filter(Status__iexact = 'Active').order_by('-ExamID')[:5]
    result_list = T_ResultDetail.objects.filter(UserName__iexact=request.user.username, Status__iexact = 'Active')
    context_dict = {'notifications': notification_list, 'userdata': user_list, 'examdata': exam_list, 'resultdata':result_list }




    return render_to_response(
    'site/Dashboard.html',context_dict, context
    )

@login_required
def appear_exam(request, T_Exam_ExamID_url):

    context = RequestContext(request)

    ExamID = T_Exam_ExamID_url.replace('_', ' ')
    examdata  = T_Exam.objects.filter(ExamID__iexact=ExamID, Status__iexact = 'Active')

    request.session['ExamID'] = ExamID

    questionset = T_QuestionsSet.objects.filter(ExamID=ExamID, Status__iexact = 'Active')

    context_dict ={'examdata': examdata, 'questionset': questionset}

    return render_to_response(
    'appear_exam.html', context_dict, context )

@login_required
def Appappear_exam(request, T_Exam_ExamID_url):

    context = RequestContext(request)

    ExamID = T_Exam_ExamID_url.replace('_', ' ')
    examdata  = T_Exam.objects.filter(ExamID__iexact=ExamID, Status__iexact = 'Active')

    request.session['ExamID'] = ExamID

    questionset = T_QuestionsSet.objects.filter(ExamID=ExamID, Status__iexact = 'Active')

    context_dict ={'examdata': examdata, 'questionset': questionset}

    return render_to_response(
    'site/App/appear_exam.html', context_dict, context )

@login_required
def start_exam(request, T_Exam_ExamID_url):

    context = RequestContext(request)

    ExamID = T_Exam_ExamID_url.replace('_', ' ')
    if T_ResultDetail.objects.filter(ExamID = ExamID, UserName__iexact=request.user.username, Status__iexact = 'Active').count() > 0:
        ResultData = T_ResultDetail.objects.filter(ExamID = ExamID, UserName__iexact=request.user.username, Status__iexact = 'Active')
        context_dict ={'ResultData': ResultData}
    else:
        examdata  = T_Exam.objects.filter(ExamID__iexact=ExamID, Status__iexact = 'Active')
        request.session['ExamID'] = ExamID
        questionset = T_QuestionsSet.objects.filter(ExamID=ExamID, Status__iexact = 'Active')
        context_dict ={'examdata': examdata, 'questionset': questionset}

    return render_to_response(
    'site/start_exam.html', context_dict, context )

@login_required
def Appstart_exam(request, T_Exam_ExamID_url):

    context = RequestContext(request)

    ExamID = T_Exam_ExamID_url.replace('_', ' ')
    if T_ResultDetail.objects.filter(ExamID = ExamID, UserName__iexact=request.user.username, Status__iexact = 'Active').count() > 0:
        ResultData = T_ResultDetail.objects.filter(ExamID = ExamID, UserName__iexact=request.user.username, Status__iexact = 'Active')
        context_dict ={'ResultData': ResultData}
    else:
        examdata  = T_Exam.objects.filter(ExamID__iexact=ExamID, Status__iexact = 'Active')
        request.session['ExamID'] = ExamID
        questionset = T_QuestionsSet.objects.filter(ExamID=ExamID, Status__iexact = 'Active')
        context_dict ={'examdata': examdata, 'questionset': questionset}

    return render_to_response(
    'site/App/start_exam.html', context_dict, context )


@login_required
def print_paper(request, T_Exam_ExamID_url):

    context = RequestContext(request)
    ExamID = T_Exam_ExamID_url.replace('_', ' ')

    examdata  = T_Exam.objects.filter(ExamID__iexact=ExamID, Status__iexact = 'Active')

    request.session['ExamID'] = ExamID

    questionset = T_QuestionsSet.objects.filter(ExamID=ExamID, Status__iexact = 'Active')

    context_dict ={'examdata': examdata, 'questionset': questionset}

    return render_to_response(
    'site/print.html', context_dict, context )

@login_required
def exam_answers(request, T_Exam_ExamID_url):

    context = RequestContext(request)

    ResultDetailID = T_Exam_ExamID_url

    result_list = T_ResultDetail.objects.filter(ResultDetailID__iexact=ResultDetailID, UserName__iexact=request.user.username, Status__iexact = 'Active')

    for rs in result_list:
        ExamName = rs.ExamID

    examdata  = T_Exam.objects.filter(ExamName__iexact=ExamName, Status__iexact = 'Active')
    userresult_list = T_UserResult.objects.filter(ExamID=ExamName, UserName__iexact=request.user.username, Status__iexact = 'Active')

    for Ex in examdata:
        questionset = T_QuestionsSet.objects.filter(ExamID=Ex.ExamID, Status__iexact = 'Active')

    context_dict ={'examdata': examdata, 'questionset': questionset, 'userresult': userresult_list }

    return render_to_response(
    'site/exam_answers.html', context_dict, context )

@login_required
def Appexam_answers(request, T_Exam_ExamID_url):

    context = RequestContext(request)

    ResultDetailID = T_Exam_ExamID_url

    result_list = T_ResultDetail.objects.filter(ResultDetailID__iexact=ResultDetailID, UserName__iexact=request.user.username, Status__iexact = 'Active')

    for rs in result_list:
        ExamName = rs.ExamID

    examdata  = T_Exam.objects.filter(ExamName__iexact=ExamName, Status__iexact = 'Active')
    userresult_list = T_UserResult.objects.filter(ExamID=ExamName, UserName__iexact=request.user.username, Status__iexact = 'Active')

    for Ex in examdata:
        questionset = T_QuestionsSet.objects.filter(ExamID=Ex.ExamID, Status__iexact = 'Active')

    context_dict ={'examdata': examdata, 'questionset': questionset, 'userresult': userresult_list }

    return render_to_response(
    'site/App/exam_answers.html', context_dict, context )

def Admissions(request):
    return render_to_response(
    'site/Admissions.html',
    { 'user': request.user}
    )
def Contacts(request):
    return render_to_response(
    'site/Contacts.html',
    { 'user': request.user}
    )
def Courses(request):
    return render_to_response(
    'site/Courses.html',
    { 'user': request.user}
    )
def Programs(request):

    context = RequestContext(request)

    Article_list = T_Articles.objects.filter(Status__iexact = 'Active').order_by('-ArticleID')

    context_dict ={'Articles': Article_list}

    return render_to_response('site/Programs.html', { 'user': request.user, 'Articles': Article_list } )

def Teachers(request):
    return render_to_response(
    'site/Teachers.html',
    { 'user': request.user}
    )

def percentage(part, whole):
    return 100 * float(part)/float(whole)


def SubmitPaper(request):
   if request.POST['client_response']:
        objs = json.loads(request.POST['client_response'])

        #y=objs['1']

        UserName = request.user.username
        #ExamID = objs['ExamID']
        #SubjectID = objs['SubjectID']

        if 'ExamID' in request.session:
            ExamID = request.session['ExamID']




        ExamID = T_Exam.objects.get(ExamID = ExamID, Status__iexact = 'Active')

        SubjectName = "MPSC"

        SubjectID = T_Subject.objects.get(SubjectName = SubjectName)

        marksperQues = 0
        totalmarksforQue = 0

        for key, value in objs.items():
            QueID = T_QuestionsSet.objects.get(QueID = str(key))
            QU = T_QuestionsSet.objects.filter(QueID = str(key), Status__iexact = 'Active')
            for Que in QU:
                Question = Que.Question
                A = Que.A
                B = Que.B
                C = Que.C
                D = Que.D
                Answer = Que.Answer
            #for Ques in QueID:
            U = T_UserResult.objects.create(UserName=UserName, CheckAnswer=str(value) , Status='Active', SubjectID=SubjectID, ExamID=ExamID, QueID=QueID, CreateDate=datetime.datetime.now(), Question=Question, A=A, B=B, C=C, D=D, CorrAnswer=Answer)
            U.save()
            if T_QuestionsSet.objects.filter(QueID = str(key), Answer = str(value), Status__iexact = 'Active').count() > 0:
                w = T_QuestionsSet.objects.filter(QueID = str(key), Answer = str(value), Status__iexact = 'Active')
                for w in w:
                    marksperQues = marksperQues + int(w.marks)

            #y=objs['1']
        x = T_QuestionsSet.objects.filter(ExamID=ExamID, Status__iexact = 'Active')
        for x in x:
            totalmarksforQue = totalmarksforQue + int(x.marks)
        QuesCount = str(T_QuestionsSet.objects.filter(ExamID=ExamID, SubjectID=SubjectID, Status__iexact = 'Active').count())
        QuesAttended = str(len(objs))
        TotalMarks = str(totalmarksforQue)
        MarksObtained = str(marksperQues)

        if (marksperQues > 0) and (totalmarksforQue > 0):
            Percentage = round(percentage(marksperQues, totalmarksforQue), 2)
        else:
            Percentage = 00.00

        if Percentage >= 50.00:
            FinalResults = "PASS"
        if Percentage < 50.00:
            FinalResults = "FAIL"

        Percentage = str(Percentage)

        M = T_ResultDetail.objects.create(UserName=UserName, Status='Active', ExamID=ExamID, Attempted=QuesAttended, TotalQue=QuesCount, MarksObtain=MarksObtained, TotalMarks=TotalMarks, FinalResults=FinalResults, Percentage=Percentage, CreateDate=datetime.datetime.now(),Subject = SubjectName)
        M.save()

        y = "Exam submitted successfully. Please check result in your Dashboard. "
        response_dict = {}
        response_dict.update({'server_response': y })
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
   else:
        return render_to_response(
            'appear_exam.html', context_instance = RequestContext(request))



#View-start
#import urlparse
#import six.moves.urllib.parse

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.http import base36_to_int, is_safe_url
from django.utils.translation import ugettext as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import get_current_site
#View-End

def root(request):
    return render_to_response(
    'site/Hindex.html',
    { 'user': request.user}
    )

@csrf_protect
@never_cache
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        form = authentication_form(data=request.POST)
        if form.is_valid():
            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = settings.LOGIN_REDIRECT_URL

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)

    request.session.set_test_cookie()

    current_site = get_current_site(request)


    notification_list = T_Notifications.objects.order_by('-id')[:1]

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
        'notifications': notification_list,
    }
    context.update(extra_context or {})
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request, current_app=current_app))

def articles(request, T_Exam_ExamID_url):

    ArticleID = T_Exam_ExamID_url

    Article_list = T_Articles.objects.filter(ArticleID__iexact=ArticleID, Status__iexact = 'Active')

    context_dict ={'Articles': Article_list}

    return render_to_response('site/Articles.html', {'Articles': Article_list } )

@csrf_protect
@never_cache
def signin(request, template_name='registration/App/signin.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        form = authentication_form(data=request.POST)
        if form.is_valid():
            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = 'http://www.hemantkshirsagar.in/AppDashboard/'

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)

    request.session.set_test_cookie()

    current_site = get_current_site(request)


    notification_list = T_Notifications.objects.order_by('-id')[:1]

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
        'notifications': notification_list,
    }
    context.update(extra_context or {})
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request, current_app=current_app))

def AppPrograms(request):

    context = RequestContext(request)

    Article_list = T_Articles.objects.filter(Status__iexact = 'Active').order_by('-ArticleID')

    context_dict ={'Articles': Article_list}

    return render_to_response('site/App/Programs.html', { 'user': request.user, 'Articles': Article_list } )

@login_required
def Appdashboard(request):

    context = RequestContext(request)


    notification_list = T_Notifications.objects.filter(Status__iexact = 'Active').order_by('-id')[:5]
    user_list = User.objects.get(username__iexact=request.user.username)
    exam_list = T_Exam.objects.filter(Status__iexact = 'Active').order_by('-ExamID')[:5]
    result_list = T_ResultDetail.objects.filter(UserName__iexact=request.user.username, Status__iexact = 'Active')
    context_dict = {'notifications': notification_list, 'userdata': user_list, 'examdata': exam_list, 'resultdata':result_list }




    return render_to_response(
    'site/App/Dashboard.html',context_dict, context
    )

