from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import * 
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
 

@login_required
def index(request):
    name = request.user.username
    blogdata = Blogs.objects.all().values("name","title","image","id")
    return render(request,'index.html',{'name':name, "data":blogdata}) 
 
def userlogout(request):
    logout(request)
    return redirect('loginpage')
 
def dashboard(request):
    name = request.user.username
    return render(request , 'pages/dashboard.html' ,{'name':name})

def home(request):
    reg_form = Registerform(request.POST or None)
    if reg_form.is_valid():
        user = reg_form.save(commit=False)
        user.set_password(reg_form.cleaned_data['password'])
        user.save()
    user_data = User.objects.all()
    reg_form  = Registerform()
    return render(request,'home.html',context={'data':user_data,'reg_form':reg_form})

def login_route(request):
    if request.POST:
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = authenticate(request,username= username,password=password)
        if user is not None:
            login(request,user)
            return redirect('indexpage')
        else:
            return render(request,'login.html',context={'message':'user is invalid'})
    return render(request,'login.html')
            
def edituser(request):
    name = request.user.username
    firstname = request.user.first_name
    lastname = request.user.last_name
    password = request.user.password
    id = request.user.id
    print(id , "hhhhhhhhhhh")
    user_data = User.objects.all()
    print(user_data[id - 1] , "XXXXXXXX")

    # form = Userform(request.POST,request.FILES, instance= user_data)
    # if form.is_valid():
    #     form.save()
    #     return HttpResponseRedirect('/')
    # else:
    #     user_data = Owner.objects.get(id=id)
    #     form = Userform(instance= user_data)
    return render(request , "edituser.html",context={'name':name, "firstname" :firstname,"lastname":lastname,"password":password,"data": user_data})
# Create your views here.


def addblog(request):
    form = Blogsform(request.POST,request.FILES or None)
    if form.is_valid():
        form.save()
    form = Blogsform()
    return render(request,"blog.html",{"form":form })


def Blog_delete(request ,id):
    Mng = Blogs.objects.get(id=id)
    Mng.delete()
    return HttpResponseRedirect('/blog')

def Blog_update(request, id):
    emp = Blogs.objects.get(id=id)
    form = Blogsform(request.POST,request.FILES, instance= emp)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/blog')
    else:
        emp = Blogs.objects.get(id=id)
        form = Blogsform(instance= emp)
    return render(request,'EmpUpdate.html',{'form':form})