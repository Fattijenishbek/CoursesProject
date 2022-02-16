from unicodedata import category
from .models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields='__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'

class CourseSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(many=False, read_only= True)
    contact = ContactSerializer(many=True, read_only= True)
    category = CategorySerializer(many=False, read_only= True)
    class Meta:
        model=Course
        fields='__all__'