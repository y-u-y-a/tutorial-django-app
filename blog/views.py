from django.shortcuts import render

def top(request):
    return render(request, "./blog/top.html")
