from django.shortcuts import render
from django.shortcuts import render, render_to_response

# Create your views here.
def home(request):
	return render_to_response('home_page.html')

def options_pd(request):
	return render_to_response('options_pd.html')

def options_ed(request):
	return render_to_response('options_ed.html')

def options_qf(request):
	return render_to_response('options_qf.html')

def options_in(request):
	return render_to_response('options_in.html')

def options_pr(request):
	return render_to_response('options_pr.html')

def options_coxco(request):
	return render_to_response('options_coxco.html')

def options_inp(request):
	return render_to_response('options_inp.html')

def options_ref(request):
	return render_to_response('options_ref.html')

