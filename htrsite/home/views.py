from django.shortcuts import render

import os
import json

# Create your views here.
def main(request):
	template_name = "home/index.html"
	return render(request, template_name, {})

def progess(request):
	template_name = "home/progess.html"
	filename = "files/progress.txt"

	progess = []
	context = {}
	with open(filename, 'r') as file:
		for line in file:
			line = line.split(',')
			line = [each.strip() for each in line]
			progess.append(line)

	context['scripts'] = progess

	return render(request, template_name, context) 

def faq(request):
	template_name = "home/faq.html"
	filename = "files/faq.json"

	context = {}
	with open(filename, 'r') as file:
		data = json.load(file)	 
		
	context['data'] = data
	return render(request, template_name, context)

