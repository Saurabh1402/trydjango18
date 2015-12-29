from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model=SignUp
		fields=["email","full_name"]
	def clean_email(self):
		email = self.cleaned_data.get("email")
		address,dns=email.split('@')
		dns_name,dns_ext=dns.split('.')
		if not  dns_ext == "edu":
			raise forms.ValidationError("Please use a valid .EDU email address")
		return email	

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email=forms.EmailField()
	to_email=forms.EmailField()
	password =  forms.CharField()
	message= forms.CharField(required=False)
