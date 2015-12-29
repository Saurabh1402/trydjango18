from django.db import models

STATUS_CHOICES = (
	('d','Draft'),
	('p','Published'),
	('w','Withdrawn'),
)
# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	status=models.CharField(max_length=1,default='d',choices=STATUS_CHOICES,blank=True,null=True)
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.email