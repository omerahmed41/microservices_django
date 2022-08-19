from django.urls import path
from todoList.views import *

urlpatterns = [
    # crud
    path('todo/', TodoListView.as_view()),
    path('todo/<int:id>/', TodoView.as_view()),
    # filtering
    path('today/', TodayTodosView.as_view()),
    path('next7days/', NextSevenDaysTodosView.as_view()),
]
