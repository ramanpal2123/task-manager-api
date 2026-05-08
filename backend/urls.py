from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager API",
        default_version='v1',
    ),
    public=True,
)

def home(request):
    return render(request, 'index.html')

urlpatterns = [
    path('', home),  # Frontend
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('swagger/', schema_view.with_ui('swagger')),
]