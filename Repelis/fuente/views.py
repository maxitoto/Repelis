from django.shortcuts import render

# Create your views here.

def viewnueva(request):
    return render(request, template_name='phtml.html')