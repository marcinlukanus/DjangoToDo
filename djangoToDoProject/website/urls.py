from django.urls import path
from . import views
from .views import (
    ToDoCreateView,
    ToDoListView,
)


urlpatterns = [
    path('', ToDoListView.as_view(), name='website-home'),
    path('about/', views.about, name='website-about'),
    path('todo/create/', ToDoCreateView.as_view(), name='todo-create'),
]
