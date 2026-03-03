from django.contrib import messages, auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from Dashboard.models import Student

# Create your views here.
@login_required
def dashboard(request):
    students = Student.objects.all()
    return render(request, 'dashboard.html', context={'students': students})
def add_student(request):
 if request.method == 'POST':
     if request.FILES.get('image'):
        image = request.FILES.get('image')
        name = request.POST.get('name')
        course = request.POST.get('course')
        age = request.POST.get('age')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        date = request.POST.get('date')


        Student.objects.create(
            image=image,
            name=name,
            course=course,
            age=age,
            email=email,
            gender=gender,
            date = date)
        return redirect( 'dashboard')

 return render(request, 'add_student.html')
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.course = request.POST.get('course')
        student.age = request.POST.get('age')
        student.email = request.POST.get('email')
        student.gender = request.POST.get('gender')
        student.date = request.POST.get('date')
        student.save()
        return redirect('dashboard')
    return render(request, 'update_student.html', {'student': student})
# delete
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('dashboard')


    return render('dashboard')

# *new sign up
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect('signup')
        user = User.objects.create_user(username=username, email=email, password=password)

        login(request, user)
        return redirect('dashboard')
    return render(request, 'sign_up.html')

# login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'login.html')
#logout
def logout_view(request):
    logout(request)
    return redirect('login')