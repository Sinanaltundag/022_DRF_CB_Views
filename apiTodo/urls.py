from django.urls import path
from .views import (
    # TodoDetail, 
    # TodoGetUpdateDelete,
    # TodoListCreate,
    TodoMVS,
    home, 
# hello_world, 
# todoList, 
# todoCreate, 
# todoListCreate, 
# todoUpdate, 
# todoDelete
# TodoList,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todos', TodoMVS, )

urlpatterns = [
    # path('', home),
    # path('hello/', hello_world),
    # path('todoList/', todoList),
    # path('todoCreate/', todoCreate),
    # path('todoListCreate/', todoListCreate),
    # path('todoUpdate/<int:pk>/', todoUpdate),
    # path('todoDelete/<int:pk>/', todoDelete),
# ! class based urls rest api
    # path('todoList/', TodoList.as_view()),
    # path('todoDetail/<int:pk>/', TodoDetail.as_view()),

    # path('todoList/', TodoListCreate.as_view()),
    # path('todoDetail/<int:pk>/', TodoGetUpdateDelete.as_view()),


]
urlpatterns += router.urls
