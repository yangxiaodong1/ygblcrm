from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout

# Create your views here.

def acc_login(request):
    errors = {}
    if request.method == "POST":
        _email = request.POST.get("email")
        _password = request.POST.get("password")
        #认证成功就返回这个对象，不成功就返回none
        user = authenticate(username = _email,password = _password)
        if user:
            # 怎么直接创建一个session呢，下次不用登陆了
            login(request,user) #login 就会在数据库中创建session
            # 在登陆不成功的时候后面会加上url
            next_url = request.GET.get("next","/")
            return redirect(next_url)
        else:
            errors['error'] = "Wrong username or password"
    return render(request,"login.html",{"errors":errors})

def acc_logout(request):

    logout(request)
    return redirect('/account/login/')


def index(request):

    return render(request,'index.html')