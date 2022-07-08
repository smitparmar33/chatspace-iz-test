from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from django.http import Http404
from django.http import JsonResponse


class ViewMessages(generics.GenericAPIView):
    serializer_class = ViewMessageSerializer

    # @verify_token
    def get(self, request, room_name):
        try:
            item = ChatModel.objects.filter(room_name=room_name)
            serializer = ViewMessageSerializer(item, many=True)
            return JsonResponse({"status": "success", "message": serializer.data}, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
