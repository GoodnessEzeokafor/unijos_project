from django.urls import path, include
from . import views


app_name = "profiles"


urlpatterns = [
    path('',views.dashboard, name='profile_dashboard'),
    # path('create/', views.CreateProfileView.as_view(), name="profile_create")
    # path('create/', views.create_profile_view, name="profile_create")
    path('create/', views.CreateProfileView.as_view(), name="profile_create"),
    path('<int:pk>/edit/', views.UpdateProfileView.as_view(), name="profile_edit")
]

