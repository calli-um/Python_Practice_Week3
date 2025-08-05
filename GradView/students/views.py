from rest_framework import viewsets
from .models import Student
from .serializer import StudentSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
@csrf_exempt
def api_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login successful", "role": user.role})
        else:
            return JsonResponse({"message": "Invalid credentials"}, status=401)

    return JsonResponse({"message": "Only POST allowed"}, status=405)

@login_required
def student_dashboard(request):
    return render(request, 'students/StudentDashboard.js')

@login_required
def admin_dashboard(request):
    return render(request, 'students/AdminDashboard.js')