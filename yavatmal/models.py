from django.db import models
#from fluent_contents.models import *
#from fluent_contents.models import ContentItem
#from fluent_contents.models.fields import PlaceholderField, PlaceholderRelation, ContentItemRelation

# Create your models here.

class T_Subject(models.Model):
	SubjectID = models.AutoField(primary_key=True)
	SubjectName = models.CharField(max_length=200)
	CreateDate = models.DateField()
	StatusID = models.CharField(max_length=20,choices=[('Active', 'Active'), ('In-Active', 'In-active')])
	class Meta:
		db_table = u't_subject'
		verbose_name_plural = "Subject"
	def __str__(self):
		return self.SubjectName



class T_Exam(models.Model):
	ExamID = models.AutoField(primary_key=True)
	ExamName = models.CharField(max_length=200)
	CreateDate = models.DateField()
	SubjectID = models.ForeignKey(T_Subject)
	Status = models.CharField(max_length=20,choices=[('Active', 'Active'), ('In-Active', 'In-active')])
	TimePeriod = models.IntegerField()

	class Meta:
	    db_table = u't_exam'
	    verbose_name_plural = "Exam Papers"
	def __str__(self):
		return self.ExamName


class User(models.Model):
	UserName = models.CharField(max_length=200)
	FirstName = models.CharField(max_length=200)
	LastName = models.CharField(max_length=200)
	MobNo = models.IntegerField(max_length=10)
	EmailID = models.CharField(max_length=200)
	Password = models.CharField(max_length=200)
	DateOfBirth = models.DateField(max_length=200)
	def __str__(self):
		return self.FirstName + " " + self.LastName

class T_Status(models.Model):
	StatusID = models.AutoField(primary_key=True)
	Status = models.CharField(max_length=200)
	Description = models.CharField(max_length=200)
	CreateDate = models.DateField()

	class Meta:
		db_table = u't_status'
		verbose_name_plural = "Status"
	def __str__(self):
		return self.Status



class T_QuestionsSet(models.Model):
	QueID = models.AutoField(primary_key=True)
	Question = models.CharField(max_length=200)
	A = models.CharField(max_length=200)
	B = models.CharField(max_length=200)
	C = models.CharField(max_length=200)
	D = models.CharField(max_length=200)
	Tip = models.CharField(max_length=200)
	Answer = models.CharField(max_length=10,choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
	CreateDate = models.DateField()
	Status = models.CharField(max_length=20,choices=[('Active', 'Active'), ('In-Active', 'In-active')])
	SubjectID = models.ForeignKey(T_Subject)
	ExamID = models.ForeignKey(T_Exam)
	marks = models.CharField(max_length=100)

	class Meta:
		db_table = u't_questionsset'
		verbose_name_plural = "Question Bank"
	def __str__(self):
		return self.Question

class T_UserResult(models.Model):
	ResultID = models.AutoField(primary_key=True)
	UserName = models.CharField(max_length=200)
	CheckAnswer = models.CharField(max_length=20)
	Status = models.CharField(max_length=20,choices=[('Active', 'Active'), ('In-Active', 'In-active')])
	SubjectID = models.ForeignKey(T_Subject, related_name='t_subject_t_userresult', blank=True, null=True)
	ExamID = models.ForeignKey(T_Exam, related_name='t_exam_t_userresult', blank=True, null=True)
	QueID = models.ForeignKey(T_QuestionsSet, related_name='t_questionsset_t_userresult', blank=True, null=True)
	CreateDate = models.DateField()
	Question = models.CharField(max_length=200)
	A = models.CharField(max_length=200)
	B = models.CharField(max_length=200)
	C = models.CharField(max_length=200)
	D = models.CharField(max_length=200)
	CorrAnswer = models.CharField(max_length=200)

	class Meta:
		db_table = u't_userresult'
		verbose_name_plural = "Students Exam Detail"
	def __str__(self):
		return self.UserName



class T_Notifications(models.Model):
	Notification = models.CharField(max_length=200)
	Description = models.CharField(max_length=200)
	Status = models.CharField(max_length=20,choices=[('Active', 'Active'), ('In-Active', 'In-active')])
	CreateDate = models.DateField()
	class Meta:
	    db_table = u't_notifications'
	    verbose_name_plural = "Notification For Students"

	def __str__(self):
	    return self.Notification

class T_ResultDetail(models.Model):
	ResultDetailID = models.AutoField(primary_key=True)
	UserName = models.CharField(max_length=200)
	Status = models.CharField(max_length=20,choices=[('Active', 'Active'), ('In-Active', 'In-active')])
	ExamID = models.ForeignKey(T_Exam, related_name='t_exam_T_ResultDetail', blank=True, null=True)
	Attempted = models.CharField(max_length=200)
	TotalQue = models.CharField(max_length=200)
	MarksObtain = models.CharField(max_length=200)
	TotalMarks = models.CharField(max_length=200)
	FinalResults = models.CharField(max_length=200)
	Percentage = models.CharField(max_length=200)
	CreateDate = models.DateField()
	Subject = models.CharField(max_length=200)
	class Meta:
	    db_table = u'T_ResultDetail'
	    verbose_name_plural = "Result"

	def __str__(self):
	    return self.UserName

class T_Articles(models.Model):
	ArticleID = models.AutoField(primary_key=True)
	Heading = models.CharField(max_length=200)
	Comments = models.CharField(max_length=20000)
	#Comments = models.PlaceholderField("t_articles_Comments")
	Status = models.CharField(max_length=20,choices=[('Active', 'Active'), ('In-Active', 'In-active')])
	CreateDate = models.DateField()
	class Meta:
	    db_table = u'T_Articles'
	    verbose_name_plural = "Articles"

	def __str__(self):
	    return self.Heading





