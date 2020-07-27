from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.db.models import Sum



class SummaryAPIView(APIView):
    """
    返回统计信息
    """
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        获取统计信息
        """
        user = request.user
        user_info = {
            'username': user.username,
            'role':  '管理员' if user.is_superuser else '普通用户',
        }

        return Response(data={
            'user': user_info,
            'statistics': 0
        })
