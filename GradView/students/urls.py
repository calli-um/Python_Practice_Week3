from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import StudentViewSet


router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('',include(router.urls)),
     #path('login/', views.login_view, name='login'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
]