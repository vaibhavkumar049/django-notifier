from django.shortcuts import render

# Create your views here.

def notif(request):
    return render(request,'notifier/notifier.html',{})
