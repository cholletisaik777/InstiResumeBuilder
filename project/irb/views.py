from django.shortcuts import render
from django.shortcuts import render, render_to_response

# Create your views here.
def home(request):
	return render_to_response('home_page.html')

def resume_options_pd(request):
	return render_to_response('resume_options.html')
