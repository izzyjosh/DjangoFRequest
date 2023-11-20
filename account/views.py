from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import auth
from django.contrib import messages

'''def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(
                username=username,
                password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("main:home")
        else:
            messages.error(request,"incorrect username or password")
            return redirect("account:signin")

    return render(request,"signin.html")
'''

def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("account:login")
    else:
        form = UserRegistrationForm()

    return render(request,"signup.html",{"form":form})

"""def logout(request):
    auth.logout(request)
    return redirect("account:login")
    """
