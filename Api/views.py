from django.http import Http404
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework import status,generics
from Api.models import *
from Api.serializers import *
from rest_framework.response import Response
from rest_framework import authentication,permissions
from django.contrib.auth import login,authenticate
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class AdminRegistrationView(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_superuser(
                username = serializer.validated_data['username'],
                email = serializer.validated_data['email'],
                password = serializer.validated_data['password']
            )
            return Response({'message': ' Admin registration successfully completed '}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class AdminSigninView(APIView):
    serializer_class = SigninSerializer

    def post(self, request):
        serializer = SigninSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            user = authenticate(
                username = serializer.validated_data['username'],
                password = serializer.validated_data['password']
            )
            if user and user.is_superuser:
                login(request, user)
                return Response({'message': 'Admin logged successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class DepartmentAPIView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request,*args,**kwargs):
        serializer = DepartmentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data)
        else:
            return Response(data = serializer.errors)
        

class StudentAPIView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request,*args,**kwargs):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data)
        else:
            return Response(data = serializer.errors)


class StudentListApiView(APIView):
    permission_classes =[IsAuthenticated]

    def get(self,request,format=None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class StudentDetailApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)