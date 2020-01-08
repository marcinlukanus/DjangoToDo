from django.urls import path
from . import views
from .views import (
    ToDoCreateView,
    ToDoListView,
    ToDoDeleteView
)


urlpatterns = [
    path('', ToDoListView.as_view(), name='website-home'),
    path('about/', views.about, name='website-about'),
    path('todo/create/', ToDoCreateView.as_view(), name='todo-create'),
    path('todo/delete/<int:pk>', ToDoDeleteView.as_view(), name='todo-delete')
]
