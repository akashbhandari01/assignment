from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection
from .models import User

# Create your views here.

def home(request):
    return render(request, "index.html")
def hello(request):
    return render(request, "hello.html", {"message": "Hello World!"})

def users_list(request):
    users = User.objects.all()
    return render(request, "users.html", {"users": users})

def user_detail(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return render(request, "404.html", status=404)
    return render(request, "user_details.html", {"user": user})

def new_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        role = request.POST.get("role")

        if not (name and email and role):
            return render(request, "new_user.html", {"error": "All fields are required."})

        User.objects.create(name=name, email=email, role=role)
        return redirect("/users")

    return render(request, "new_user.html")
