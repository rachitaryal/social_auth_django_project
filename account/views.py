# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import User
from account.serializer import UserInfoShowSerializer, UserRegisterSerializer


class UserAuthTestAPIView(APIView):
    """
        Authorized Test Endpoint
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            user_id = request.user.id
            user_instance = User.objects.get(id=user_id)
            user_info_show_serializer = UserInfoShowSerializer(user_instance)
            data = {
                'msg': 'Token Is Valid',
                'user': user_info_show_serializer.data
            }
            return Response(data=data, status=status.HTTP_200_OK)
        except Exception as e:
            info = {
                'msg': 'Something Went Wrong'
            }
            return Response(data=info, status=status.HTTP_400_BAD_REQUEST)


class UserNormalRegisterAPIView(APIView):
    """
        Endpoint to register user using normal method ie. not using social auth but basic django registration
    """

    def post(self, request, *args, **kwargs):
        user_data = request.data
        user_register_serializer = UserRegisterSerializer(data=user_data)
        user_register_serializer.is_valid(raise_exception=True)
        user_register_serializer.save()
        return Response(data=user_register_serializer.data, status=status.HTTP_201_CREATED)
