from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from .models import School, Class, Teacher, StudentsList, Subject
from .serializers import SchoolSerializer, ClassSerializer, TeacherSerializer, StudentListSerializer, SubjectSerializer, TeachersSerializer, showProfileSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class SchoolAPIView(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        school = School.objects.all()
        serializer = SchoolSerializer(school, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SchoolSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassSearchAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    # filter_fields = ('ClassName', )
    search_fields = ('ClassName',)


class SearchAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('Class', 'TeacherName')


class ClassAPIView(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


    def get(self, request):
        Clas = Class.objects.all()
        serializer = ClassSerializer(Clas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherAPIView(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeachersSerializer(teacher, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeachersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentListAPIView(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        student = StudentsList.objects.all()
        serializer = StudentListSerializer(student, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubjectAPIView(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        subject = Subject.objects.all()
        serializer = SubjectSerializer(subject, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SchoolUpdateAPIView(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_object(self, id):
        try:
            return School.objects.get(id=id)

        except School.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        school = self.get_object(id)
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    def put(self, request, id):
        school = self.get_object(id)
        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        school = self.get_object(id)
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClassUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


    def get_object(self, id):
        try:
            return Class.objects.get(id=id)

        except Class.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        Clas = self.get_object(id)
        serializer = ClassSerializer(Clas)
        return Response(serializer.data)

    def put(self, request, id):
        Clas = self.get_object(id)
        serializer = ClassSerializer(Clas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        Class = self.get_object(id)
        Class.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeacherUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_object(self, id):
        try:
            return Teacher.objects.get(id=id)

        except Teacher.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        teacher = self.get_object(id)
        serializer = TeachersSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, id):
        teacher = self.get_object(id)
        serializer = TeachersSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        teacher = self.get_object(id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentListUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


    def get_object(self, id):
        try:
            return StudentsList.objects.get(id=id)

        except StudentsList.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        student = self.get_object(id)
        serializer = StudentListSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = self.get_object(id)
        serializer = StudentListSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = self.get_object(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SubjectUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_object(self, id):
        try:
            return Subject.objects.get(id=id)

        except Subject.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        teacher = self.get_object(id)
        serializer = SubjectSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, id):
        teacher = self.get_object(id)
        serializer = SubjectSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        teacher = self.get_object(id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ShowProfile(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        serializer = showProfileSerializer(request.user)
        return Response(serializer.data)
