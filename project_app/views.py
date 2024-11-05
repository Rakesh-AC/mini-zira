from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import ProjectSerializer, UserSerializer
from .models import Project
from django.http import JsonResponse

# Register View
@api_view(['POST'])
def register(request):
  username = request.data.get("username")
  email = request.data.get("email")
  password = request.data.get("password")

  if User.objects.filter(username=username).exists():
    return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
  if User.objects.filter(email=email).exists():
    return Response({"error": "Email already registered"}, status=status.HTTP_400_BAD_REQUEST)

  user = User.objects.create_user(username=username, email=email, password=password)
  user.save()
  return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

# Login View
@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    
    user = authenticate(username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "username": user.username,
            "email": user.email,
        }, status=status.HTTP_200_OK)
    return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

# Logout View
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({"error": "Invalid token or token already blacklisted"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
  return JsonResponse({"dashboard":"Welcome you are in dashbord", "username":request.user.username})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        project = serializer.save(commit=False)  # Create a Project instance but don't save to the database yet
        project.project_owner = request.user     # Assign the logged-in user as the owner
        project.save()                           # Now save it to the database
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_project(request, pk):
  try:
    project = Project.objects.get(pk=pk)
  except Project.DoesNotExist:
    return Response({"error": "Project not found."}, status=status.HTTP_404_NOT_FOUND)
  serializer = ProjectSerializer(project)
  return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def delete_project(request, pk):
  try:
    project = Project.objects.get(pk=pk)
  except Project.DoesNotExist:
    return Response({"error": "Project not found."}, status=status.HTTP_404_NOT_FOUND)
  project.delete()
  return Response({"message": "Project deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_project_list(request):
    print("------")
    print("Request user:", request.user)
    projects = Project.objects.filter(project_owner=request.user)
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)