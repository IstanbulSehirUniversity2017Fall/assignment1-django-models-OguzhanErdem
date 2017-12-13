from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.


def index(request):
    return HttpResponse("<h1>Hey what's up!<h1>")

def details(request, student_id):
    student_id1 = Student.objects.all()
    html =""
    i = 0
    for id in student_id1:

        i=i+1
        if(int(student_id)==i):
            html += "<ul>%s</ul>" % id
            return HttpResponse(html)
            #break;

    #return HttpResponse(html)

    #return render(request,'Student/details.html', {'student_id':student_id1})
    #return #HttpResponse("<h2>This is student number %s<h2>"%str(student_id))
