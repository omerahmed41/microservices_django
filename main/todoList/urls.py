from django.urls import path
from todoList.domain import views as todo_views


urlpatterns = [
    # crud
    path('todo/', todo_views.TodoListView.as_view()),
    path('todo/<int:id>/', todo_views.TodoView.as_view()),
    # filtering
    path('today/', todo_views.TodayTodosView.as_view()),
    path('next7days/', todo_views.NextSevenDaysTodosView.as_view()),
]
