from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model
from .models import Frequest
from django.contrib.auth.decorators import login_required

User=get_user_model()

@login_required
def home(request):
    suggestions = User.objects.all()
    friends = User.objects.get(username=request.user.username).friends.all()

    context = {
            "suggestions":suggestions,
            "friends":friends,
            }

    return render(request,"home.html",context)


def allrequest(request):
    friendrequests = Frequest.objects.filter(receiver=request.user)
    return render(request,"accept.html",{"friendrequests":friendrequests})


@login_required
def frequest(request,user_id):
    sender = request.user
    receiver = get_object_or_404(User,pk=user_id)

    #check if a friendrequest already exist

    check = Frequest.objects.filter(
            sender=sender,
            receiver=receiver)
    if not check.exists() and receiver != sender:
        Frequest.objects.create(sender=sender,receiver=receiver)

        return redirect("main:home")

@login_required
def acceptrequest(request,request_id):
    receiver = request.user
    frequest = get_object_or_404(
            Frequest,
            pk=request_id,
            receiver=receiver)

    frequest.status = True
    frequest.save()

    sender = User.objects.get(username=frequest.sender.username)

    receiver.friends.add(sender)
    sender.friends.add(receiver)



    return redirect("main:home")

@login_required
def rejectrequest(request,request_id):
    request = get_object_or_404(
            Frequest,
            pk=request_id,
            reciever=request.user)

    request.delete()
    return redirect("main:home")





