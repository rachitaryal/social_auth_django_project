"""Account URL Configuration"""
from django.urls import path, include

from account.views import UserAuthTestAPIView, UserNormalRegisterAPIView

app_name = 'account'

urlpatterns = [
    path('api/', include([
        path('v1/', include([
            path('user/', include([
                path('auth/test/', UserAuthTestAPIView.as_view(), name='user_auth_test'),
                path('register/', UserNormalRegisterAPIView.as_view(), name='user_normal_register'),
            ]))
        ])),
    ])),
]
