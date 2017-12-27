from django.contrib import admin
from django import forms
from yavatmal.models import *
#from yavatmal.resources import T_QuestionsSetAdmin
from django.conf import settings
#from fluent_contents.models import *
#from fluent_contents.models.fields import PlaceholderField, PlaceholderRelation, ContentItemRelation
#from ckeditor.widgets import CKEditorWidget

# Register your models here.

class T_ExamAdmin(admin.ModelAdmin):
	list_display = ('ExamName', 'SubjectID', 'Status', 'CreateDate')
	#search_fields = ('ExamName', 't_subject__SubjectID', 'CreateDate')
	search_fields = ('ExamName','CreateDate')

class T_SubjectAdmin(admin.ModelAdmin):
    list_display = ('SubjectName', 'StatusID', 'CreateDate')
    search_fields = ('SubjectName', 'StatusID', 'CreateDate')


class UserAdmin(admin.ModelAdmin):
	list_display = ('UserName', 'FirstName', 'LastName', 'MobNo', 'EmailID', 'DateOfBirth')
	#search_fields = ('UserName', 'FirstName', 'LastName', 'MobNo', 'EmailID', 'DateOfBirth')



class T_ResultDetailAdmin(admin.ModelAdmin):
    list_display = ('UserName', 'ExamID', 'Subject', 'TotalQue', 'Attempted','TotalMarks', 'MarksObtain', 'Percentage', 'FinalResults', 'Status', 'CreateDate')
    #search_fields = ('UserName', 'ExamID', 'Subject', 'FinalResults', 'Status', 'CreateDate')
    search_fields = ('UserName', 'Subject', 'FinalResults', 'Status', 'CreateDate')

class T_UserResultAdmin(admin.ModelAdmin):
    list_display = ('UserName', 'ExamID', 'SubjectID', 'Question', 'CheckAnswer','CorrAnswer','Status', 'CreateDate')
    #search_fields = ('UserName', 'ExamID', 'SubjectID', 'Question', 'Status', 'CreateDate')
    search_fields = ('UserName', 'Question', 'Status', 'CreateDate')

class T_NotificationsAdmin(admin.ModelAdmin):
    list_display = ('Notification', 'Status', 'CreateDate')
    search_fields = ('Notification', 'Status', 'CreateDate')


#class T_ArticlesForm(forms.ModelForm):
#    #Heading = forms.CharField( widget=forms.Textarea(attrs={'rows': 15, 'cols': 200}))
#    Comments = forms.CharField(widget=CKEditorWidget())
#    #Comments = forms.PlaceholderField("T_Articles_Comments")
    #change_form_template = 'fun/admin/change_form.html'

#    class Meta:
#        model = T_Articles


#class T_ArticlesAdmin(admin.ModelAdmin):
#    form = T_ArticlesForm
#    list_display = ('ArticleID', 'Heading', 'Comments', 'Status', 'CreateDate')
#    search_fields = ('ArticleID', 'Heading', 'Comments', 'Status', 'CreateDate')



#admin.site.register(User)
admin.site.register(T_Subject, T_SubjectAdmin)
admin.site.register(T_Exam,T_ExamAdmin)
#admin.site.register(T_Status)
#admin.site.register(T_QuestionsSet, T_QuestionsSetAdmin)
admin.site.register(T_UserResult, T_UserResultAdmin)
admin.site.register(T_Notifications, T_NotificationsAdmin)
admin.site.register(T_ResultDetail, T_ResultDetailAdmin)
#admin.site.register(T_Articles, T_ArticlesAdmin)