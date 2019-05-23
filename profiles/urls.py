from django.urls import path, include, re_path
from . import views


app_name = "profiles"


urlpatterns = [
    path('',views.dashboard, name='profile_dashboard'),
    path('create/', views.CreateProfileView.as_view(), name="profile_create"),
    path('<int:pk>/edit/', views.UpdateProfileView.as_view(), name="profile_edit"),
    path('delete/<int:pk>/', views.DeleteProfileView.as_view(), name="profile_delete"),
    path('delete/success/', views.delete_success, name="delete_success"),
]


