from django.shortcuts import render

# Create your views here.
# location of template folde is in myapp/example.html

def  example_view(request):
    return  render(request,'myapp/example.html')

def variable_view(request):
    # Dictionary Variable should be taken out 
    # Passing data to the template using context
    # Building template tag https://docs.djangoproject.com/en/4.0/ref/templates/builtins/ references
    
    my_variable={'first_name':'john', 'second_name':'lemar',
                 'somelist':[90,30,20], 'my_dic':{'inside_key':'inside_value'}
                 
                 }
    
    return render(request,'myapp/variables.html', context=my_variable)