from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import SignUp


class SignUpAdmin(admin.ModelAdmin):
	list_display=["__unicode__","status","timestamp","updated"]
	actions=['make_published']
	form = SignUpForm

	def make_published(self,request,queryset):
		rows_updated=queryset.update(status='p')
		if rows_updated == 1:
			message_bit = "1 story was"
		else:
			message_bit = "%s stories were" %rows_updated
		self.message_user(request,"%s successfully marked as published." %message_bit)	
	make_published.short_description="Mark selected stories as published"
	

	#class Meta:
	#	model = SignUp
#admin.site.disable_action('delete_selected')
admin.site.register(SignUp,SignUpAdmin)

