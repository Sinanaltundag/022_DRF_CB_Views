from django.http import Http404
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
import rest_framework
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import messages

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

from rest_framework import status

from rest_framework import mixins, viewsets
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import action

# Create your views here.


def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>'
    )

# ! functional based views rest api
""" 
@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})


@api_view(['GET'])
def todoList(request):
    querset = Todo.objects.all()
    serializer = TodoSerializer(querset, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def todoCreate(request):

    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def todoListCreate(request):
    if request.method == "GET":
        querset = Todo.objects.all()
        serializer = TodoSerializer(querset, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todoUpdate(request, pk):

    querset = Todo.objects.get(id=pk)

    if request.method == "GET":
        serializer = TodoSerializer(querset)

        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = TodoSerializer(instance=querset,  data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

    elif request.method == "DELETE":

        querset.delete()
        return Response("Item Deleted")


@api_view(['DELETE'])
def todoDelete(request, pk):

    querset = Todo.objects.get(id=pk)
    querset.delete()
    return Response("Item Deleted") """

# ! class based views rest api

""" class TodoList(APIView):    
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetail(APIView):
    def get_object(self, pk):
        todo= get_object_or_404(Todo, pk=pk)
        return todo
        # try:
        #     return Todo.objects.get(pk=pk)
        # except Todo.DoesNotExist:
        #     raise Http404

    def get(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)

        return Response(serializer.data)

    def put(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoSerializer(instance=todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = self.get_object(pk)
        todo.delete()
        data = {
            "messa" : "Todo successfully deleted"
        }
        # messages.success(request, 'Todo item deleted successfully')

        return Response(data, status=status.HTTP_204_NO_CONTENT) """

""" class TodoList(mixins.ListModelMixin, mixins.CreateModelMixin,  GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) """
# 
""" class TodoListCreate(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    # def perform_create(self,serializer):
    #     serializer.save(user=self.request.user)

class TodoGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk' """

class TodoMVS(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(methods=["GET"], detail=False)
    def todo_count(self, request):
        todo_count = Todo.objects.filter(done=False).count()
        count = {
            'undo-todos': todo_count
        }
        return Response(count)