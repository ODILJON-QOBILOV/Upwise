from django.urls import path

from apps.students.views.auth import RegisterAPIView, LoginAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("login/", LoginAPIView.as_view()),
]