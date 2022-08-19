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
from todoList import signals
from django.dispatch import receiver
import logging
import redis

from my_microservice import settings

# Connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)
logger = logging.getLogger(__name__)


class TodoListView(APIView):
    @swagger_auto_schema(responses={200: TodoSerializer(many=True)})
    def get(self, request):
        signals.some_task_done.send(sender='abc_task_done', task_id=123)
        redis_instance.set('key', 'value')
        results = TodoItem.objects.all()
        serializer = TodoSerializer(results, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_description="TodoSerializer", request_body=TodoSerializer)
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
        results = TodoItem.objects.filter(expireDate__range=(today, today + timedelta(days=6)))
        serializer = TodoSerializer(results, many=True)
        return Response(serializer.data)


class TodoView(APIView):
    def get(self, request, id):
        try:
            result = TodoItem.objects.get(id=id)
        except TodoItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(result)
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


@receiver(signals.some_task_done)
def my_task_done(sender, task_id, **kwargs):
    logger.warning('signal recived:' + sender)
    logger.warning(task_id)
    value = redis_instance.get('key')

    logger.warning(f"Redis: {value}")
    print(sender, task_id)
