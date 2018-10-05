from django.shortcuts import render

# Create your views here.
def main(request):
	template_name = "home/index.html"
	return render(request, template_name, {'test': 'test'})