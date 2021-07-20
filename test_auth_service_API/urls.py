from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from test_auth_service_API import views

urlpatterns = [
    path('api/users/', views.UserList.as_view(), name='account-create'),
    path('api/users/<int:pk>/', views.UserDetail.as_view()),
    path('api/permission/', views.PermList.as_view(), name='permission-create'),
    path('api/permission/<int:pk>/', views.PermDetail.as_view()),
    path('api/role/', views.RoleList.as_view(), name='role-create'),
    path('api/role/<int:pk>/', views.RoleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)