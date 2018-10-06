from django.shortcuts import render

import os
import json

# Create your views here.
def main(request):
	template_name = "home/index.html"
	filename = "files/motivation.txt"
	context = {}
	with open(filename, 'r') as file:
		context['data'] = file.read()
	return render(request, template_name, context)

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

def people(request):
	template_name = "home/people.html"
	filename = "files/people.txt"

	context = {}
	with open(filename, 'r') as file:
		context['data'] = [line.strip() for line in file]

	return render(request, template_name, context)
	
def contact(request):
	template_name = "home/contact.html"
	context = {}
	return render(request, template_name, context)
	