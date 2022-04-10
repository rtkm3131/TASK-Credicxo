from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from accountinfo.models import *

# Create your views here.

# Main View function, prepares the context and filters user
# by their role, and then serves them the REST state accordigngly.
def returnData(request):
    if request.user.id is None:
        return HttpResponse("<p> Invalid </p>")
    user = MyUser.objects.get(id=request.user.id)
    admins = MyUser.objects.filter(groups__name='super-admin')
    students = Students.objects.all().select_related()
    teachers = Teachers.objects.all().select_related()
    context = {
        'students': students,
        'teachers': teachers,
        'admins': admins
    }
    print(user)
    if(user in admins):
        return render(request, 'accountinfo/admins.html', context)
    if user in MyUser.objects.filter(groups__name='Student'):
        return students_view(request, context)
    if user in MyUser.objects.filter(groups__name='Teacher'):
        return render(request, 'accountinfo/teach.html', context)

    return HttpResponse("You are nobody")

#View file for the student role, shows them only their own data
def students_view(request, context):
    me = MyUser.objects.filter(id=request.user.id)[0]
    print(me.first_name, me.date_of_birth)
    email = me.id
    name = me.first_name
    dob = me.date_of_birth
    return HttpResponse(f'Your details are \n Email-ID: {email} \n Name: {name} \n DOB: {dob}')

#View function to be used by the admin role only, to add new teachers
def add_teacher(request):
    if request is None:
        return None
    new_t_email = request.POST["teacheremail"]
    new_t_name = request.POST["newname"]
    if len(list(Teachers.objects.filter(email=new_t_email))) > 0:
        return  HttpResponseRedirect(reverse('accountinfo:returnData'))
    new_t = Teachers.objects.create(email=new_t_email, name=new_t_name)
    new_t.save()

    return HttpResponseRedirect(reverse('accountinfo:returnData'))

#View function to be used by a teacher or an admin, to add new students
def add_student(request):
    print("Here")
    if request is None:
        return None
    new_st_email = request.POST["studentemail"]
    new_st_name = request.POST["newname"]
    if len(list(Students.objects.filter(email=new_st_email))) > 0:
        return  HttpResponseRedirect(reverse('accountinfo:returnData'))
    new_st = Students.objects.create(email=new_st_email, name=new_st_name)
    new_st.save()
    print(new_st.id)
    
    return HttpResponseRedirect(reverse('accountinfo:returnData'))
