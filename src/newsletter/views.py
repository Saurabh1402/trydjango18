from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm, SignUpForm

# Create your views here.
def home(request):
	title ="Welcome"
	form = SignUpForm(request.POST or None)
	context={
		"title":title,
		"form":form
	}
	
	# if request.method == "POST":
	# 	print request.POST
	if form.is_valid():
		instance=form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "unknown"
		instance.full_name=full_name
		instance.save()
		context = {
		"title":"Thank You"
		}
		# print instance.email
		# print instance.timestamp
		
	# if request.user.is_authenticated():
	# 	title = "My Title %s"%(request.user)

	#add  a form
	return render(request,"home.html",context)

def contact(request):
	title="Contact Us"
	form = ContactForm(request.POST or None)
	if form.is_valid():
	# 	for key, value in form.cleaned_data:
	# 		print key, value
		# 	print key, form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name= form.cleaned_data.get("full_name")
		form_to_email=form.cleaned_data.get("to_email")
		form_password= form.cleaned_data.get("password")
		
		settings.EMAIL_HOST_USER= form_email
		settings.EMAIL_HOST_PASSWORD = form_password
		
		from_email=settings.EMAIL_HOST_USER
		subject = 'Site contact Form'
		to_email = [form_to_email]
		contact_message="%s: %s via %s"%(form_full_name,form_message,form_email)
		print subject, contact_message, from_email,form_password, to_email
		send_mail(subject,
			contact_message,
			from_email,
			to_email,
			fail_silently=False)
		# print form_email, form_message, form_full_name

	context= {
		"form":form,
		"title":title,
	}
	return render(request,"forms.html",context)