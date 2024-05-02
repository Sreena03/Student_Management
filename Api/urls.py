from django.urls import path
from Api.views import *
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns =[
    path("signup/",AdminRegistrationView.as_view(),name="reg"),
    path("signin/",AdminSigninView.as_view(),name="login"),
    path('login1/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("depart/",DepartmentAPIView.as_view(),name="dept"),
    path("student/",StudentAPIView.as_view(),name="stud"),
    path("stud_list/",StudentListApiView.as_view(),name="studlist"),
    path('students/<int:pk>/', StudentDetailApiView.as_view(), name='student-detail'),
]