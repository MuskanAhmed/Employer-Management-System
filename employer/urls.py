from django.urls import path,include
from .views import SignupAPIView,CustomLoginView,LoginAPIView, UserProfileView,EmployerListCreateView, EmployerRetrieveUpdateDestroyView,LogoutView


urlpatterns = [
    path('auth/signup/', SignupAPIView.as_view(), name='signup_api'),
    path('auth/login/', CustomLoginView.as_view(), name='token_obtain_pair'),
    path('auth/login/', LoginAPIView, name='api_login'),
    path('auth/profile/', UserProfileView.as_view(), name='api_profile'),
    path('auth/employers/', EmployerListCreateView.as_view(), name='employer_list_create'),
    path('auth/employers/<int:id>/', EmployerRetrieveUpdateDestroyView.as_view(), name='employer_detail'),
    path('auth/profile/', UserProfileView.as_view(), name='user_profile'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
  
]

