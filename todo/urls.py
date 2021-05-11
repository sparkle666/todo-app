from django.urls import path
from .views import index, addTodo, complete, deletecompleted, delete_all

urlpatterns = [
    path('', index, name = 'index'),
    path('add/', addTodo, name = 'add' ),
    path('todo/<todo_id>', complete, name = 'mark-completed'),
    path('delete/item/', deletecompleted, name = 'delete-completed'),
    path('delete/all/', delete_all, name='delete-all'),
]
