from django.shortcuts import render
from django.http import HttpResponseRedirect







def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profiles/')
    else:
        return HttpResponseRedirect('/accounts/login')