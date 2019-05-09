from django.urls import path, include
from . import views

app_name = "feedback"
urlpatterns = [
    path('', views.FeedBackCreateView.as_view(), name="feedback"),
    path('thanks/', views.success_feedback_view, name="success_message")
]
