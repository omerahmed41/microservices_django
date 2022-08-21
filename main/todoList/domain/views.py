from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from todoList.models import TodoItem
from todoList.serializers import TodoSerializer
from datetime import datetime, timedelta
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from django.dispatch import receiver
import logging
import redis
from datetime import timedelta
import json
from my_microservice import settings

# AsyncTask class instance example
from django.core.exceptions import SuspiciousOperation
import math
import pika
from todoList.domain.domain_exception import ServiceUnavailable
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from todoList.serializers import TodoPostSerializer

# Connect to our Redis instance
redis_instance = redis.StrictRedis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0
)
logger = logging.getLogger(__name__)


class TodoListView(APIView):

    uthentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: TodoSerializer(many=True)})
    def get(self, request):
        # raise ServiceUnavailable
        cached_todo_items = redis_instance.get("todo_items")
        if cached_todo_items:
            logger.warning(f"Redis: {cached_todo_items}")
            data = json.loads(cached_todo_items)
            return Response(data)
        else:
            todo_items = TodoItem.objects.all()
            serializer = TodoSerializer(todo_items, many=True)
            redis_instance.set("todo_items", json.dumps(serializer.data), 10)
            # signals.some_task_done.send(sender='abc_task_done', task_id=123)

            return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="TodoSerializer", request_body=TodoPostSerializer
    )
    def post(self, request):
        serializer = TodoPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodayTodosView(APIView):
    def get(self, request):
        results = TodoItem.objects.filter(expireDate=datetime.now().date())
        serializer = TodoSerializer(results, many=True)
        return Response(serializer.data)


class NextSevenDaysTodosView(APIView):
    def get(self, request):
        today = datetime.now().date()
        results = TodoItem.objects.filter(
            expireDate__range=(today, today + timedelta(days=6))
        )
        serializer = TodoSerializer(results, many=True)
        return Response(serializer.data)


class TodoView(APIView):
    def get(self, request, id):
        cached_todo_item = redis_instance.get(f"todo_item_{id}")
        if cached_todo_item:
            logger.warning(f"Redis: {cached_todo_item}")
            data = json.loads(cached_todo_item)
            return Response(data)
        else:
            try:
                result = TodoItem.objects.get(id=id)
            except TodoItem.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = TodoSerializer(result)
            redis_instance.set(f"todo_item_{id}", json.dumps(serializer.data), 100)
            return Response(serializer.data)

    def put(self, request, id):
        try:
            result = TodoItem.objects.get(id=id)
        except TodoItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            result = TodoItem.objects.get(id=id)
        except TodoItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # serializer = TodoSerializer(result)
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
