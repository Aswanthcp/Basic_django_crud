from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import Members
# Create your views here.


def index(request):
    mymembers = Members.objects.all().values()
    content = {
        'mymembers': mymembers
    }
    return render(request, 'myfirst.html', content)


def add(request):
    return render(request, 'add_member.html')


def addrecord(request):
    first_name = request.POST['first']
    last_name = request.POST['last']
    member = Members(first_name=first_name, last_name=last_name)
    member.save()
    return redirect(index)


def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return redirect(index)


def update(request, id):
    mymember = Members.objects.get(id=id)
    content = {
        'mymember': mymember
    }
    return render(request, 'update_member.html', content) 

def updaterecord(request, id):
    first_name = request.POST['first']
    last_name = request.POST['last']
    mymember = Members.objects.get(id=id)
    mymember.first_name = first_name
    mymember.last_name=last_name
    mymember.save()
    return redirect(index)
    