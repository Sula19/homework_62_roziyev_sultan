from django.urls import path
from accounts.views import LoginView, logout_view, RegisterView
from webapp.views.users import DeleteUser

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('project/delete/user/<int:pk>', DeleteUser.as_view(), name='delete_user'),
]