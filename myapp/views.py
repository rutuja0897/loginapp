from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class HelloView(APIView):
    permission_classes=(IsAuthenticated,)

    def get(self,request):
        content={'message':'Hello World!'}
        return Response(content)
def login(request):
    form = UserForm
    return render(request,"login.html",{'form':form})

def signup(request):
    # form=UserForm(request.POST)
    # form.save()
    # return redirect('/show')
    form=UserForm
    return render(request,"signup.html",{'form':form})

def add(request):
    form=UserForm(request.POST)
    form.save()
    return redirect('/show')

def show(request):
    user=User.objects.all
    return render(request,'show.html',{'user':user})


def edit(request,id):
    user=User.objects.get(id=id)
    return render(request,'edit.html',{'user':user})

def update(request,id):
    user=User.objects.get(id=id)
    form=UserForm(request.POST,instance=user)
    form.save()
    return redirect('/show')


def delete(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/show')


def logout(request):
    auth.logout(request)
    return render(request,'logout.html')