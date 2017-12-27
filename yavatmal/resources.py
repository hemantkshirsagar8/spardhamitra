from import_export.admin import ImportExportModelAdmin,ImportExportMixin
from import_export import resources
from yavatmal.models import *
from django.contrib import admin

#class ExamResource(resources.ModelResource):
#    class Meta:
#        model = Exam
#class ExamAdmin(ImportExportModelAdmin):#
#	resource_class = ExamResource
#	pass
class T_QuestionsSetResource(resources.ModelResource):
    class Meta:
       model = T_QuestionsSet
       exclude = ('QueID',)
       import_id_fields = ['Question']
class T_QuestionsSetAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = T_QuestionsSetResource
    list_display = ('QueID', 'Question', 'SubjectID', 'ExamID', 'marks', 'Status', 'CreateDate')
    #search_fields = ('QueID', 'Question', 'SubjectID', 'ExamID', 'Status', 'CreateDate')
    search_fields = ('QueID', 'Question','Status', 'CreateDate')
    pass

#class T_QuestionsSetAdmin(admin.ModelAdmin):
#    list_display = ('QueID', 'Question', 'SubjectID', 'ExamID', 'marks', 'Status', 'CreateDate')
#    search_fields = ('QueID', 'Question', 'SubjectID', 'ExamID', 'Status', 'CreateDate')