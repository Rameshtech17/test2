from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from .models import School, Class, Teacher, StudentsList, Subject
from .serializers import SchoolSerializer, ClassSerializer, TeacherSerializer, StudentListSerializer, SubjectSerializer, TeachersSerializer, showProfileSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated



# @api_view(['GET', 'POST'])
# @permission_classes((IsAuthenticated,))
# def SchoolAPIView(request):
#     if request.method == 'GET':
#         school = School.objects.all()
#         serializer = SchoolSerializer(school, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = SchoolSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_2001_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# def School_details(request, id):
#     try:
#         article = School.objects.get(id=id)
#
#     except School.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     user = School.SchoolName
#     if article.SchoolName != 'BCA':
#         return Response({'Response': 'Access Not given '})
#
#     if request.method == 'GET':
#         serializer = SchoolSerializer(article)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = SchoolSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




class SchoolAPIView(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
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
    # search_fields = ('id'.'Class', 'TeacherName')


class ClassAPIView(APIView):

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

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

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

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

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
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

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

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


# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# def Subject_details(request, id):
#     try:
#         article = Subject.objects.get(id=id)
#
#     except School.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     user = School.SchoolName
#     if article.SchoolName != 'BCA':
#         return Response({'Response': 'Access Not given '})
#
#     if request.method == 'GET':
#         serializer = SubjectSerializer(article)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = SubjectSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


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

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = showProfileSerializer(request.user)
        return Response(serializer.data)


# @api_view(['GET', 'POST'])
# @permission_classes((IsAuthenticated,))
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_2001_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# def article_details(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#
#     except Article.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     user = Article.author
#     if article.author != "user1":
#         return Response({'Response': 'Access Not given '})
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
