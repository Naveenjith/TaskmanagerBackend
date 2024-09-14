from django.urls import path
from taskapp.views import Listcreateview,Taskdetails,Register
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/reg/',Register.as_view(),name='register'),
    path('api/tasks/',Listcreateview.as_view(),name='list-create'),
    path('api/tasks/<int:pk>/',Taskdetails.as_view(),name='task-details'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
