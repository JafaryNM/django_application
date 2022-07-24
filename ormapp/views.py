from django.shortcuts import render
from ormapp.models import Student
from django.db.models import Q
# Create your views here.



def index(request):
    ########################### Part 1 ###################33
    # Return students  in database

    #students=Student.objects.all()
    
    # Query Students OR Query
    
    #students=Student.objects.filter(surname__startswith='N') | Student.objects.filter(surname__startswith='V')

    # Option using Q objects

    students = Student.objects.filter(Q(surname__startswith='S') | Q(surname__startswith='V'))


    return render( request, 'index.html',  {'students' : students})

##################### Part 2 ###########################

def student_list(request):
    
    
    students=Student.objects.filter(classroom=3)& Student.objects.filter(first_name__startswith=("P"))
    
    

    return render(request, 'index2or.html', {'students':students })



_




