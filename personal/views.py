from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/contact.html')

def aboutme(request):
    return render(request, 'personal/aboutme.html')
	
def resume(request):
    return render(request, 'personal/resume.html')
	

	

