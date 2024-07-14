from django.urls import path
from .views import UserRegistrationView, UserLoginView,UserDetailView,UserListView,UserRoleUpdateView,UserUpdateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('user/',UserDetailView.as_view(),name='user-detail'),
    path('users/',UserListView.as_view(),name='user-list'),
    path('<int:pk>/update-role/',UserRoleUpdateView.as_view(),name='user-role-update'),
    path('<int:pk>/',UserUpdateView.as_view(),name='user-update')
]
