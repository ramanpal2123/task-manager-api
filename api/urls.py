from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='task')

urlpatterns = [
    path('v1/auth/register/', views.register),
    path('v1/auth/login/', views.login),
    path('v1/auth/refresh/', TokenRefreshView.as_view()),
    path('v1/', include(router.urls)),
]