from django.urls import path, include
from . import views


app_name = "blog"

urlpatterns = [
    path('create/', views.UpoadFileCreateView.as_view(), name='upload_create'),
]