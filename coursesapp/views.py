from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySerializer, BranchSerializer, ContactSerializer, CourseSerializer
from .models import *
# Create your views here.


class CategoryListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ContactListView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

class BranchListView(generics.ListCreateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()

class CourseListView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

