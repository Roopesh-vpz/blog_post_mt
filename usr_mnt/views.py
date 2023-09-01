from django.shortcuts import render,redirect
from django.contrib import auth
from blog_app.models import *

def index(request):
    return render(request,'login.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username , password=password)
        if user is not None:
            print(user)
            auth.login(request,user)
            return redirect('home')
        else:
            return render (request,'login.html',{"error":"You have entered the wrong credentials..."})
    return render(request,'login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return render(request,'login.html')
        
    return render(request,'login.html')

def homepage(request):

    first_name=request.user.first_name
    last_name=request.user.last_name
    name=first_name+" " +last_name
    
    post_details=UserPostMapper.objects.filter(user=request.user.id).select_related('post').all().order_by('-post__pbl_date')
    postList=[]
    for post in post_details:
        post_name=post.post.title
        post_content=post.post.content
        pbl_date=post.post.pbl_date.strftime("%d-%m-%Y")
        postList.append({"post_name":post_name,"post_cont":post_content,"pbl_date":pbl_date})
    context={"name":name,
             "post":postList
             }
    

    return render(request,'home.html',context)



# Create your views here.
