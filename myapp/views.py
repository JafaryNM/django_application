from django.shortcuts import render

# Create your views here.
# location of template folde is in myapp/example.html

def  example_view(request):
    return  render(request,'myapp/example.html')