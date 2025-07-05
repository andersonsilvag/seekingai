import re
import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from rest_framework import viewsets
from rest_framework.response import Response

from django.db import connection

logger = logging.getLogger(__name__)

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class BaseAskViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def api_response(self,question):
        return answer

    def create(self, request):
        question = request.data.get('question')
        answer = self.api_response(question)
        response_data = {
            "question": question,
            "answer": answer
        }
        return Response(response_data, status=200)

