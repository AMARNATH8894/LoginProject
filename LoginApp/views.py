from django.shortcuts import render

# Create your views here.
def getLoginPage(request):
    return render(request,'login.html')
def checkLogin(request):
    user=request.POST['un']
    password=request.POST['pw']
    if user=='amar' and password == 'amar':
        return render(request,'success.html',{'username':user})
    else:
        return render(request,'unsuccess.html',{'username':user})