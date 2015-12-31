from django.shortcuts import render

def about(request):
	about="""
	This is about us. This is about us. This is about us. This is about us. This is about us. 
	This is about us. This is about us. This is about us. This is about us. This is about us. 
	This is about us. This is about us. This is about us. This is about us. This is about us. 
	This is about us. This is about us. This is about us. This is about us. This is about us. 
	This is about us. This is about us. This is about us. This is about us. This is about us. 
	This is about us. This is about us. This is about us. This is about us. This is about us. 
	This is about us. This is about us. This is about us. This is about us. This is about us. 
	"""
 	context = {
 		"about":about,
 	}
	return render(request,"about.html",context)

