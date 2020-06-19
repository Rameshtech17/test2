from django.urls import path
from .views import SchoolAPIView, ClassAPIView, SubjectAPIView, TeacherAPIView, StudentListAPIView, ClassSearchAPIView, SubjectUpdateAPIView, SchoolUpdateAPIView, ClassUpdateAPIView, StudentListUpdateAPIView, TeacherUpdateAPIView, SearchAPIView, ShowProfile

urlpatterns = [
    path('school/', SchoolAPIView.as_view()),
    path('school/<int:id>', SchoolUpdateAPIView.as_view()),

    path('class/', ClassAPIView.as_view()),
    path('class/<int:id>', ClassUpdateAPIView.as_view()),

    path('student/', StudentListAPIView.as_view()),
    path('student/<int:id>', StudentListUpdateAPIView.as_view()),

    path('subject/', SubjectAPIView.as_view()),
    path('subject/<int:id>', SubjectUpdateAPIView.as_view()),

    path('teacher/', TeacherAPIView.as_view()),
    path('teacher/<int:id>', TeacherUpdateAPIView.as_view()),

    path('classsearch/', ClassSearchAPIView.as_view()),
    path('search/', SearchAPIView.as_view()),

    path('profile/', ShowProfile.as_view()),
]
