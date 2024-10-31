from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Project 
from . serializers import ProjectSerializer
from django.http import JsonResponse
# Create your views here.


@api_view(['GET'])
def dashboard(request):
  return JsonResponse({"dashboard":"Welcome you are in dashbord"})

@api_view(['POST'])
def create_project(request):
  if request.method == 'POST':
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      print("-----------------------------")
      print(Response(serializer.data, status=status.HTTP_201_CREATED))
      print("-------------------------------")
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_project(request, pk):
  try:
    project = Project.objects.get(pk=pk)
  except Project.DoesNotExist:
    return Response({"error": "Project not found."}, status=status.HTTP_404_NOT_FOUND)
  serializer = ProjectSerializer(project)
  return Response(serializer.data)



@api_view(['PUT'])
def update_project(request, pk):
  try:
    project = Project.objects.get(pk=pk)
  except Project.DoesNotExist:
    return Response({"error": "Project not found."}, status=status.HTTP_404_NOT_FOUND)
  
  serializer = ProjectSerializer(project, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_project(request, pk):
  try:
    project = Project.objects.get(pk=pk)
  except Project.DoesNotExist:
    return Response({"error": "Project not found."}, status=status.HTTP_404_NOT_FOUND)
  project.delete()
  return Response({"message": "Project deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_project_list(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)