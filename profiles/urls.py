from django.urls import path, include, re_path
from . import views


app_name = "profiles"


urlpatterns = [
    path('',views.dashboard, name='profile_dashboard'),
    path('create/', views.CreateProfileView.as_view(), name="profile_create"),
    re_path('edit/(?P<pk>[\w-]+)/', views.UpdateProfileView.as_view(), name="profile_edit"),
    re_path('delete/(?P<pk>[\w-]+)/', views.DeleteProfileView.as_view(), name="profile_delete"),
    re_path('delete/success/', views.delete_success, name="delete_success"),
]

